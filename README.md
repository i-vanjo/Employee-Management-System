# Employee Management System

A Django-based Employee Management System developed during my internship at SoftLoom IT Solutions.

## Project Overview

This project is a web-based employee management application developed using Python and Django. It provides a structured platform for managing employee information through a simple and user-friendly interface.

The application includes employee management, user authentication, profile management, password management, and database integration.

## Features

- User registration and login
- User authentication
- Employee registration and management
- Add, view, update, and delete employee records
- Employee profile details
- Employee profile image support
- Employee listing
- Password change functionality
- Dashboard
- Database integration
- Responsive web interface

## Technologies Used

- Python
- Django
- HTML5
- CSS3
- Bootstrap
- SQLite
- Django Templates

## Project Structure

```text
Employee-Management-System/
├── mainapp/
├── mainproject/
├── media/
├── templates/
├── static/
├── manage.py
├── .gitignore
└── README.md
```

## How to Run the Project

Follow the steps below to run the Employee Management System on a local computer.

### 1. Download the Project

Open the GitHub repository:

https://github.com/i-vanjo/Employee-Management-System

Click the **Code** button and select **Download ZIP**.

Extract the downloaded ZIP file.

Alternatively, if Git is installed, clone the repository using:

```bash
git clone https://github.com/i-vanjo/Employee-Management-System.git
```

### 2. Install Python

Make sure Python 3.x is installed on the computer.

Check the installed version using:

```bash
python --version
```

### 3. Open the Project Folder

Open Command Prompt, PowerShell, or a terminal inside the project folder.

The folder should contain:

```text
manage.py
mainapp/
mainproject/
templates/
static/
```

### 4. Create a Virtual Environment

Create a virtual environment using:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 5. Install Django

Install Django using:

```bash
pip install django
```

### 6. Configure the Environment Variable

The Django project uses an environment variable for the secret key.

Create a file named:

```text
.env
```

in the same folder as `manage.py`.

Add the following:

```text
DJANGO_SECRET_KEY=your-secret-key-here
```

For local testing, replace `your-secret-key-here` with a newly generated Django secret key.

### 7. Apply Database Migrations

Run:

```bash
python manage.py migrate
```

This creates the required database tables.

### 8. Create an Administrator Account

To create an administrator account, run:

```bash
python manage.py createsuperuser
```

Enter the requested username, email address, and password.

### 9. Start the Development Server

Run:

```bash
python manage.py runserver
```

The terminal will display a local address similar to:

```text
http://127.0.0.1:8000/
```

Open this address in a web browser.

### 10. Use the Application

After starting the application, users can:

- Register an account
- Log in
- Access the dashboard
- Add employee records
- View employee information
- Update employee information
- Delete employee records
- Upload employee profile images
- Change passwords
- Manage employee information

## Project Requirements

- Python 3.x
- Django
- SQLite
- Web browser
- Internet connection for downloading the project and dependencies

## Learning Outcomes

Through this project, I gained practical experience in:

- Django web application development
- Python programming
- CRUD operations
- User authentication
- Database integration
- HTML and CSS
- Bootstrap-based interface development
- Git and GitHub for version control

## Internship

Developed during internship at SoftLoom IT Solutions, Kochi.

**Area:** Python and Web Development

## Important Note

This repository contains the source code of the Django application. The project is designed to be run locally after completing the setup steps above.

The `.env` file is not included in the repository for security reasons. A new secret key should be created for local use.

## Author

**Ivan Joseph**

BCA Student  
St. Thomas College Palai (Autonomous)

GitHub: https://github.com/i-vanjo
