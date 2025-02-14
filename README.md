# enLearning Blog

#### Description:
enLearning Blog is a simple website where people can write and read blogs. I used Python and JavaScript as programming languages to build it. For the backend, I used the Django Framework, and for styling, I used TailwindCSS, PostCSS and Vanilla JS. The database is SQLite3, and for writing blog posts, I added CKEditor5, which makes writing easier.

### Features:
1. **Signup**: New users can create an account.
2. **Login**: Registered users can log in to their account.
3. **Featured Blog**: Some blogs from each category are shown as featured on the homepage.
4. **Blog Categories**: Blogs are grouped into different categories.
5. **Post Approval**: Admin checks and approves blogs before showing them.
6. **Logout**: Users can log out of their account.
7. **Dashboard**: Django Built in admin panel page where users can manage their blogs. Need to be imporved..
8. **Social Media Links**: Icons for sharing or connecting on social platforms. added to Footer section. Dynamic.
9. **Post Detail Page**: Users can read full blogs on this page.
10. **Edit Blog**: Users can edit their blogs if needed.
11. **Delete Blog**: Users can delete their blogs.
12. **Pagingation**: Pagination system added to the Post By Category Page...

### Files and What They Do:
- **`manage.py`**: A tool for running commands like starting the server or managing the database.
- **`enLearning/`**: The main project folder. It has:
  - `settings.py`: All settings for the website like database and apps.
  - `urls.py`: Links pages with the functions that control them.
- **`blog/`**: The blog app folder. It has:
  - `models.py`: The structure for blog posts and categories.
  - `views.py`: The logic behind each page.
  - `urls.py`: The links for blog features.
  - `forms.py`: Handles forms like login or blog writing.
- **`account/`**: The account app folder. It has:
  - `forms.py`: Form fields for account management.
  - `views.py`: The logic behind each page.
  - `urls.py`: The links for account features.
- **`templates/`**: HTML files for how the website looks.
- **`static/`**: Files like CSS and JavaScript for design and interactivity.
- **`media/`**: Stores blog images uploaded by users.
- **`db.sqlite3`**: The database file where all information is saved.

### Why I Chose These Tools:
- **Django**: It makes backend development easy and fast.
- **TailwindCSS**: It helps design the website beautifully and quickly.
- **CKEditor5**: It is a good tool for writing blogs with text formatting options.
- **SQLite3**: A small database that works well for small projects.

---

Thank you for checking out enLearning Blog. I hope you find it useful and easy to use!
