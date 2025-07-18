# Automatic Resume Builder

This project is an intelligent resume builder designed to automatically fetch employee details from a comprehensive database and generate professional PDF resumes in a company's standardized format. It streamlines the resume creation process by eliminating manual formatting and ensuring consistency across all employee resumes while maintaining professional presentation standards.

## File Structure

The project is organized into the following hierarchical structure:

```
project-2 pacewisdom/               # Root directory of the Django project
├── resume_builder_project/         # Main Django project settings
│   ├── asgi.py                     # ASGI configuration for async support
│   ├── settings.py                 # Project configurations (database, installed apps, templates, static files)
│   ├── urls.py                     # Main URL dispatcher, includes resume_app URLs
│   └── wsgi.py                     # WSGI configuration for web servers
├── resume_app/                     # Django application for resume management
│   ├── migrations/                 # Database schema migrations
│   │   └── 0001_initial.py         # Initial database migration
│   ├── templatetags/               # Custom template tags for Django templates
│   │   └── resume_filters.py       # Custom filters (e.g., for splitting lines)
│   ├── admin.py                    # Django Admin configurations for resume models
│   ├── apps.py                     # Application configuration
│   ├── models.py                   # Database models (Employee, TechnicalSkill, Project, EmployeeProject)
│   ├── tests.py                    # Placeholder for application tests
│   ├── urls.py                     # URLs for the resume application (e.g., search, generate)
│   ├── views.py                    # Views for rendering HTML and generating PDF resumes
│   └── templates/                  # HTML templates specific to the resume_app
│       └── resume_app/
│           ├── resume_template.html    # The HTML template used for PDF resume layout
│           └── search_resume.html      # Page for employee search and resume generation
├── manage.py                       # Django's command-line utility for administrative tasks
```

## Features

The Automatic Resume Builder offers the following core features:

  * **Database-Driven Data Storage**: Comprehensive storage for employee personal details, professional summaries, technical skills, and project information.
  * **Employee Selection**: Users can select an employee from a dropdown list to generate their resume.
  * **Automated Data Fetching**: Employee data, technical skills, and project details are automatically retrieved from the database based on the selected employee.
  * **PDF Resume Generation**: Generates professional resumes in PDF format.
  * **Standardized Format**: Ensures all generated resumes adhere to a consistent and professional company format.
  * **One-Click Download**: Provides a simple button for generating and downloading the resume PDF.

## Technical Stacks

The project is built using the following technologies:

  * **Backend Framework**: Django (Python)
  * **Database**: SQLite3
  * **Templating**: HTML/CSS with Django Template Language
  * **PDF Generation**: `xhtml2pdf` library
  * **Language**: Python

## Installation

To set up and run the project locally, follow these steps:

1.  **Clone the repository (or extract the provided files):**

    ```bash
    git clone <repository-url>
    cd project-2 pacewisdom
    ```

    *(Note: As the files are provided directly, you would typically place them in a directory named `project-2 pacewisdom`)*

2.  **Create and activate a virtual environment (recommended):**

    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install Django xhtml2pdf
    ```

4.  **Run database migrations:**

    ```bash
    python manage.py makemigrations resume_app
    python manage.py migrate
    ```

5.  **Create a superuser (for Django Admin access):**

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to set up a username, email, and password.

6.  **Add data (optional but recommended for testing):**
    You can manually add `Employee`, `TechnicalSkill`, and `Project` data through the Django admin interface (accessible at `/admin/`) after running the server.

## How to Run

1.  **Start the Django development server:**

    ```bash
    python manage.py runserver
    ```

    The server will typically run at `http://127.0.0.1:8000/`.

2.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:8000/` or `http://127.0.0.1:8000/resume/`.
    From here, you can select an employee and generate their resume.

3.  **Access Django Admin:**
    The Django admin interface is available at `http://127.0.0.1:8000/admin/`. Log in with the superuser credentials you created.

## Output File
   Sample output resume pdf is shared above. 
