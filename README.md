# Django Blog Platform

A full-featured, modern blog application built with Python and the Django Web Framework. This platform allows users to create accounts, publish posts, categorize their content, and interact with other posts through comments. It features a clean, responsive user interface and a powerful backend admin panel.

---

## 📚 Table of Contents

* [✨ Features](#-features)
* [🖼️ Project Demonstration](#️-project-demonstration)

  * [🏠 Homepage & Post Listings](#-homepage--post-listings)
  * [📄 Post Detail & Comments](#-post-detail--comments)
  * [✍️ Creating & Editing Posts](#️-creating--editing-posts)
  * [🗑️ Delete the Post](#delete-the-post)
  * [🆕 New Post](#new-post)
* [⚙️ Installation](#️-installation)
* [🚀 Usage](#-usage)
* [🛠 Technologies Used](#-technologies-used)
* [🤝 Contributing](#-contributing)

---

## ✨ Features

- **Full CRUD Functionality**: Authenticated users can Create, Read, Update, and Delete their own blog posts directly from the website's interface.
- **User Authentication**: Secure user registration, login, and logout system powered by Django's built-in authentication.
- **Post Categorization**: Organize posts with custom categories, allowing users to browse content by topic.
- **Interactive Commenting System**: Visitors can leave comments on posts to engage with the content and author.
- **Responsive Design**: The UI is built with Tailwind CSS for a seamless experience on desktops, tablets, and mobile devices.
- **Powerful Admin Panel**: Comes with the standard Django admin interface for advanced site management and content moderation.

---

## 🖼️ Project Demonstration

The application provides a clean and intuitive interface for both readers and authors.

### 🏠 Homepage & Post Listings

The homepage displays a list of all recent blog posts, showing the title, author, publication date, and a snippet of the content.

![Homepage Screenshot](https://github.com/bharathkukka/BlogApplication/blob/9f0f41f8912134423f207e41378f18dfbd94e75e/Data/Home.png)

---

### 📄 Post Detail & Comments

Clicking on a post leads to the full detail page. If you are the author of the post, "Edit" and "Delete" links will appear. Below the post, visitors can view existing comments and submit their own.

![Post Detail Screenshot](https://github.com/bharathkukka/BlogApplication/blob/9f0f41f8912134423f207e41378f18dfbd94e75e/Data/commentpost.png)

---

### ✍️ Creating & Editing Posts

Authenticated users can use a clean, web-based form to write new posts or edit their existing ones. The form includes fields for the title, content, and categories.

![Post Form Screenshot](https://github.com/bharathkukka/BlogApplication/blob/9f0f41f8912134423f207e41378f18dfbd94e75e/Data/editpost.png)

---  

## Django admin Page

![admin](https://github.com/bharathkukka/BlogApplication/blob/2f82ca7f9bc4fefd22b037897372ff715e19f7e0/Data/djangointerface.png)

---

### 🗑️ Delete the Post

![Post delete](https://github.com/bharathkukka/BlogApplication/blob/9f0f41f8912134423f207e41378f18dfbd94e75e/Data/deletepost.png)

---

### 🆕 New Post 

![new](https://github.com/bharathkukka/BlogApplication/blob/9f0f41f8912134423f207e41378f18dfbd94e75e/Data/newpost.png)

---  
## ⚙️ Installation

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://your-repository-url.git
cd BlogApplication
````

### 2. Create and Activate a Virtual Environment

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

Create a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

Then install:

```bash
pip install -r requirements.txt
```

> **Note:** Main dependency is Django.

### 4. Set Up the Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and a secure password.

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🚀 Usage

* **Viewing the Blog**: Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the list of posts.
* **Admin Panel**: Visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with your superuser credentials.
* **Creating a Post**:

  1. Log in using your credentials.
  2. Click on the "New Post" button in the navigation bar.
  3. Fill in the form and click "Save Post".

---

## 🛠 Technologies Used

* **Backend**: Python, Django
* **Frontend**: HTML, Tailwind CSS (via CDN)
* **Database**: SQLite 3 (default Django development DB)

---

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/your-feature-name
```

3. Make your changes and commit with a descriptive message.
4. Push to your forked repo:

```bash
git push origin feature/your-feature-name
```

5. Create a Pull Request to the `main` branch of the original repository.

---
