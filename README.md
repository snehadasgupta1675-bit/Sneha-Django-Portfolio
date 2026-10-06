# Sneha Dasgupta — Django Portfolio

A responsive, blue-purple gradient portfolio website built with Django. It has seven main sections: Home, About Me, Education, Skills, Projects, Internships & Certificates, and Contact Me.

## Features

- Seven separate section pages and individual project detail pages
- Responsive navigation for desktop and mobile
- Animated hero text, floating design elements, and scroll reveal effects
- Django models and Admin management for education, skills, projects, internships, certificates, and contact messages
- Working contact form that saves messages to the database
- SQLite for local development and PostgreSQL via `DATABASE_URL` in deployment
- WhiteNoise static file serving, Gunicorn, and Render blueprint configuration
- Accessible labels, keyboard-friendly navigation, and reduced-motion support

## Requirements

- Python 3.11–3.13 recommended
- VS Code
- Internet connection for installing Python packages

## Run locally on Windows

1. Extract the ZIP file.
2. Open the extracted `Sneha_Django_Portfolio` folder in VS Code.
3. Open **Terminal → New Terminal**. Ensure the terminal is inside the folder containing `manage.py`.
4. Create a virtual environment:

   ```bat
   py -m venv .venv
   ```

5. Activate it in Command Prompt:

   ```bat
   .venv\Scripts\activate.bat
   ```

   If your terminal is PowerShell, use:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

6. Install dependencies:

   ```bat
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

7. Create the database tables:

   ```bat
   python manage.py makemigrations portfolio
   python manage.py migrate
   ```

8. Create your admin account:

   ```bat
   python manage.py createsuperuser
   ```

   Follow the prompts to create a username and password.

9. Start the development server:

   ```bat
   python manage.py runserver
   ```

10. Open `http://127.0.0.1:8000/` in your browser. Admin is at `http://127.0.0.1:8000/admin/`.

## Add your content

Use Django Admin to add and edit:
- **Education**: qualification, institution, period, details
- **Skills**: skill name and category
- **Projects**: title, slug, tagline, description, technologies, GitHub URL, live URL
- **Internships and certificates**: kind, title, organization, period, description, credential URL
- **Contact messages**: view messages submitted through the Contact Me page

The site has starter content as a fallback for several sections. Add database records to make the site fully editable. Confirm every date, credential, link, and description before publishing.

## Profile photo

Your uploaded profile photo is included at `static/images/sneha-profile.jpg` and displayed in the Home page profile card. The Home page wording, layout, colors, buttons, and animations have otherwise been kept unchanged.

## Contact form

The contact form saves messages to the Django database and makes them visible to the site administrator at `/admin/`. It does not send email by default. To receive email notifications, configure Django email settings and environment variables before launch. Protect the admin account and use spam protection/rate limiting before public production use.

## Deploy on Render

This repository includes `render.yaml` and `build.sh` as a starting point for Render Blueprint deployment.

1. Create a GitHub repository and upload the contents of this folder (not the ZIP itself).
2. On Render, choose **New → Blueprint** and connect your GitHub repository.
3. Review the resources and environment settings in `render.yaml`, then apply the Blueprint.
4. Wait for the build and deployment to finish, then open the generated `.onrender.com` URL.
5. Create an admin user for the hosted site. From Render's service Shell, run:

   ```bash
   python manage.py createsuperuser
   ```

6. Visit `/admin/` and add or update your portfolio records.
7. Test every page and submit a test contact form.

**Database note:** the sample `render.yaml` uses a small paid PostgreSQL database plan. Review current Render pricing and available plans before creating resources. Free web services may sleep and their local filesystem is ephemeral; do not rely on SQLite or local media files for persistent production data. Store uploaded media in a suitable object-storage service if you add media uploads later.

## Before publishing

- Add your own profile photo and professional email.
- Add verified LinkedIn and GitHub profile URLs.
- Verify education details, internship dates, certificates, and project URLs.
- Keep secrets in environment variables, never in GitHub.
- Consider a custom domain, email notifications, spam protection, and a privacy notice for contact form data.
