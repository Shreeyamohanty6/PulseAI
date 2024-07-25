PulseAI
PulseAI is a seamless platform designed for patients and doctors to interact effortlessly. This hospital management system allows patients to register, book appointments, and engage in blog activities, while doctors can manage patient details and appointment statuses. The system supports two user roles: Patient (User) and Doctor (Admin).

Roles and Responsibilities
Admin (Doctor)
Login and Dashboard Access: Doctors log in to access their dedicated admin dashboard.
Appointment Management: Doctors can oversee and update patient appointments.
Blog Management: Doctors can create, publish, and manage blog posts.
Patient Interaction: Doctors can review patient test results, prescribe medications, and manage visit records using an inline stack.
User (Patient)
Registration and Login: Patients can register and log in to the platform.
Blog Interaction: Patients can read, comment on blogs, and post their own blogs.
Heart Disease Test: Patients can fill out a form for heart disease risk assessment.
AI-Based Prediction: An AI model predicts the patient's heart disease risk.
Appointment Scheduling: Patients can view their test results and schedule appointments based on the predictions.
Features
Admin (Doctor)
Access to an admin dashboard after logging in.
Management of appointments and patient interactions.
Publishing and management of blog posts.
Review and prescription based on patient test results.
Inline stack for managing patient visit records.
User (Patient)
Registration and login capabilities.
Ability to read, comment, and post blogs.
Heart disease test form submission.
AI model for heart disease risk prediction.
Viewing test results and scheduling appointments.
Tech Stack
Frontend: HTML, CSS, Bootstrap
Server: SQLite (db.sqlite3)
Backend: Django
Running Tests
To run tests, follow these steps:

Setting Up a Virtual Environment
Refer to this guide to set up a virtual environment.

Starting a New Project
bash
Copy code
django-admin startproject projectname
Creating a New App
bash
Copy code
python manage.py startapp appname
Building the Project
bash
Copy code
python manage.py -r requirements.txt
Running the Server
bash
Copy code
python manage.py runserver
Viewing Dependencies
bash
Copy code
pip freeze
Making Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
Creating a Superuser for Admin Registration
bash
Copy code
python manage.py createsuperuser
Enter email:
Enter password:
Re-enter password:
