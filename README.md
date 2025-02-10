# Protirodh
## A Crime Reporting and Community Verification Platform By Team IIUC_Four-Stack Developers

A Django-based web application of a social media platform that enables users to report crimes in their area, attach multimedia evidence, and let the community verify the authenticity of these reports through voting and commenting. This project was built as a hackathon demo (NSU WebXtreme Hackathon 2025) within an 8-hour timeframe, featuring OTP-based user verification, dummy AI description generation, and robust community interactions.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration & Environment Variables](#configuration--environment-variables)
- [Known Issues & Improvements](#known-issues--improvements)
- [License](#license)

## Features

- **User Authentication & Authorization:**
  - User registration with email, phone number, and profile image upload.
  - OTP-based phone verification with a randomized, demo-friendly OTP.
  - Role management: verified, unverified, and banned users.
  
- **Crime Reporting:**
  - Verified users can submit crime reports with at least one image (video optional).
  - Auto-generated AI description for image uploads (dummy implementation for demo).
  - Selection of crime location via division and district.
  
- **Community Interaction:**
  - Upvote/downvote system for each crime report.
  - Commenting on crime reports with mandatory proof attachments (image/video).
  - Aggregated vote score displayed for each report.
  
- **Crime Feed:**
  - Paginated list of crime reports.
  - Filtering by division and district.
  - Sorting by date or by upvote score.
  
- **Admin Features:**
  - Built-in Django admin interface to manage users, ban users, and moderate reports/comments.

## Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite 
- **Frontend:** Django Templates, Tailwind CSS, JavaScript
- **AI Integration:** 
- **File Storage:** 

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package installer)
- Virtualenv (recommended)

### Setup Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Sayemahamed/Protirodh.git
   cd Protirodh
   ```
2. **Create a Virtual Environmen**t

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Node.js dependencies**

   ```bash
   npm install
   ```

5. **Run Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser (for admin access)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Collect Static Files**

   ```bash
   python manage.py collectstatic
   ```

8. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

7. **Access the Application**

   Production: http://127.0.0.1:8000/

## Usage
**1. User Registration & OTP Verification**

  - Register a new user at /users/register/.
  - Upon registration, a random OTP is generated and displayed.
  - Verify your phone number by entering the OTP .
  
**2. Reporting a Crime**

  - Log in and navigate to /reports/create/ to submit a crime report.
  - Upload an image (mandatory) or video (optional). For image-only submissions, a dummy AI-generated description is auto-filled.

**3. Community Interaction**

  - Browse crime reports on the feed at /reports/feed/ (or the home page).
  - Click on any report to view details, vote (upvote/downvote), and add comments with proof attachments.
    
**4. Filtering & Sorting the Feed**

  - Filter reports by adding URL query parameters (e.g., ?division=Dhaka&district=Dhaka).
  - Sort the feed by upvotes .

## Project Structure

```plaintext
Protirodh/
├── Protirodh/           # Main application directory
│   ├── __init__.py
│   ├── settings.py      # Django settings
│   ├── urls.py          # URL configurations
│   └── wsgi.py          # WSGI application
├── Report/              # Report application directory
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── User/                # User application directory
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── static/              # Static files (CSS, JavaScript, images)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/           # HTML templates
│   ├── base.html
│   └── [other templates]
├── .gitignore           # Git ignore file
├── db.sqlite3           # SQLite database file
├── manage.py            # Django management script
├── package.json         # Node.js dependencies
├── requirements.txt     # Python dependencies
└── tailwind.config.js   # Tailwind CSS configuration
```

## Configuration & Environment Variables

**Django Settings:**
The project uses a custom user model (users.CustomUser) and local file storage. Adjust Protirodh/settings.py for environment-specific configurations.

**Media Files:**
Uploaded images and videos are stored in the media/ directory. Ensure that the MEDIA_ROOT and MEDIA_URL settings are correctly configured.

---
This Repository is the official repository of Team IIUC_Four-Stack Developers for the NSU WebXtream Hackathon Co-powered by Programming Hero.

## Contact Us:

**IIUC_Four-Stack Developers**

Sayem Ahamed: [Email](mailto:c221020@ugrad.iiuc.ac.bd) [Linked In](https://www.linkedin.com/in/sayem-ahamed-47b890242/) <br>
Mir Tarhimul Quader: [Email](mailto:c221017@ugrad.iiuc.ac.bd) [Linked In](https://www.linkedin.com/in/tarhimul/) <br>
Mahamudul Hasan [Email](mailto:c221032@ugrad.iiuc.ac.bd) [Linked In](https://www.linkedin.com/in/mohammad-mahamudul-hasan-66931b223/) <br>
Turja Dutta [Email](mailto:c221026@ugrad.iiuc.ac.bd) [Linked In](https://www.linkedin.com/in/duttaturja/) <br>
