# # blog/views.py
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Post, Category
# from .forms import CommentForm
#
#
# def post_list(request):
#     """
#     View to display a list of all blog posts.
#     """
#     posts = Post.objects.all().order_by('-created_on')
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'blog/post_list.html', context)
#
#
# def post_detail(request, pk):
#     """
#     View to display a single blog post and handle comment submission.
#     """
#     post = get_object_or_404(Post, pk=pk)
#     comments = post.comments.all().order_by('-created_on')
#
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.post = post
#             new_comment.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         comment_form = CommentForm()
#
#     context = {
#         'post': post,
#         'comments': comments,
#         'comment_form': comment_form,
#     }
#     return render(request, 'blog/post_detail.html', context)
#
#
# def posts_by_category(request, category_name):
#     """
#     View to display all posts belonging to a specific category.
#     """
#     category = get_object_or_404(Category, name=category_name)
#     posts = Post.objects.filter(categories=category).order_by('-created_on')
#     context = {
#         'category': category,
#         'posts': posts,
#     }
#     return render (request, 'blog/posts_by_category.html', context)


# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import CommentForm, PostForm # NEW: Import PostForm

# --- Function-Based Views (Unchanged) ---
def post_list(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_on')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    context = {'post': post, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'blog/post_detail.html', context)

def posts_by_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    posts = Post.objects.filter(categories=category).order_by('-created_on')
    context = {'category': category, 'posts': posts}
    return render(request, 'blog/post_by_category.html', context)

# --- NEW: Class-Based Views for Creating, Updating, and Deleting Posts ---

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    # Add this line to specify where to redirect after a successful form submission
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        # 1. Set the author of the post to the currently logged-in user
        form.instance.author = self.request.user
        # 2. Call the parent class's form_valid method.
        # This method saves the object to the database and then
        # returns an HttpResponseRedirect to the success_url.
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')


    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
