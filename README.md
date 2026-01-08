CS50 PROJECT 4 - NETWORK

OVERVIEW
--------
Network is a Twitter-like social network web application built with Django and Python. 
This project allows users to create posts, follow other users, like posts, and interact 
with a dynamic feed of content.

FEATURES
--------
- User Authentication: Register, login, and logout functionality
- Create Posts: Users can create text posts up to 280 characters
- Follow System: Follow and unfollow other users
- Like Posts: Like and unlike posts with real-time updates
- Edit Posts: Users can edit their own posts
- User Profiles: View user profiles with follower/following counts
- Following Feed: View posts only from users you follow
- Pagination: Browse posts with pagination (10 posts per page)

TECHNOLOGIES
------------
- Python (53. 5%)
- HTML (42.4%)
- CSS (4.1%)
- Django Web Framework
- Django ORM for database management
- JavaScript for dynamic interactions

PROJECT STRUCTURE
-----------------
network/
  - models.py: Database models (User, Post, Comment)
  - views.py: Application logic and view functions
  - urls.py: URL routing configuration
  - templates/:  HTML templates
  - static/: CSS and static files
  - migrations/: Database migrations

manage.py: Django management script
project4/:  Django project configuration

DATABASE MODELS
---------------
User:  Extended Django AbstractUser with following/followers relationship
Post: Stores user posts with author, text, timestamp, and likes
Comment: Stores comments on posts (model defined but not fully implemented)

INSTALLATION
------------
1. Install Python 3.x
2. Install Django:  pip install django
3. Navigate to project directory
4. Run migrations: python manage.py makemigrations && python manage.py migrate
5. Create superuser (optional): python manage.py createsuperuser
6. Start development server: python manage.py runserver

USAGE
-----
1. Navigate to http://localhost:8000
2. Register a new account or login
3. Create posts from the homepage
4. Visit user profiles to follow/unfollow users
5. Like posts by clicking the like button
6. Edit your own posts using the edit functionality
7. View posts from followed users in the "Following" page

URL ENDPOINTS
-------------
/ - Homepage with all posts\
/following - Posts from followed users only\
/login - User login page\
/logout - Logout user\
/register - New user registration\
/new_post - Create a new post\
/profile/<username> - View user profile\
/toggle_follow/<username> - Follow/unfollow user\
/toggle_like/<post_id> - Like/unlike post\
/edit_post/<post_id> - Edit post

NOTES
-----
- This is a CS50 Web Programming with Python and JavaScript project
- Posts are limited to 280 characters
- Only authenticated users can create posts, like, follow, and edit
- Users can only edit their own posts
- Pagination displays 10 posts per page
