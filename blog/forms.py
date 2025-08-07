# blog/forms.py
'''
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md'}),
            'body': forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md', 'rows': 4}),
        }
'''
# blog/forms.py
from django import forms
from .models import Comment, Post # NEW: Import Post

# --- NEW: Form for Creating and Updating Posts ---
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md'}),
            'content': forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md', 'rows': 10}),
            'categories': forms.SelectMultiple(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md'}),
            'body': forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md', 'rows': 4}),
        }
