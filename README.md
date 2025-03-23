# Vue-Flask Web Application

This project is a web application built with Vue (frontend) and Python Flask (backend). The backend uses **Flask**, **pymongo**, and **flask-cors**. The instructions below will help you set up and run the complete application.


## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Backend Setup (Flask)](#backend-setup-flask)
  - [Frontend Setup (Vue)](#frontend-setup-vue)
- [Running the Application](#running-the-application)
- [Environment Variables](#environment-variables)
- [Troubleshooting](#troubleshooting)

## Prerequisites

- **Node.js** (v12 or later) and **npm** (or yarn)
- **Python 3.x** and **pip**
- **MongoDB** (local or remote)
- **Git** (for cloning the repository)

## Setup Instructions

# Backend Setup (Flask)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/anaGomide/CRUDify
   cd CRUDify

2. **Navigate to the server folder:**
   ```bash
   cd server

3. **Create a Python virtuall environment**
    ```bash
    python -m venv venv

4. **Activate the virtual environment:**
    ```bash
    //on Mac or Linux:
    source venv/bin/activate
    //On Windows:
    venv\Scripts\activate

5. **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt

## Configure Environment (Optional)
The current MongoDB connection string is hardcoded as:

          mongodb://localhost:27017/

and the database name is set to crudify. If you need to change the connection details, update the MongoClient initialization in your app.py.

If you prefer to use environment variables, you can modify app.py to load the connection string from an .env file using a package like python-dotenv.

## Running the Server

With the virtual environment activated and dependencies installed, run the server with:

      python app.py

The API will start in debug mode and be accessible at http://127.0.0.1:5000.

## API Endpoints
**GET/**
Returns a simple message indicating the API is running.

**GET/users/list**
Retrieves a list of all users.

**GET /users/view/<id>**
Retrieves details of a single user by their ID.

**POST /users/create**
Creates a new user. The request body should be JSON.

**PUT /users/update/<id>**
Updates an existing user by their ID. The request body should include the fields to update.

**DELETE /users/delete/<id>**
Deletes a user by their ID.

## Troubleshooting
Virtual Environment:
Ensure the virtual environment is activated when installing packages or running the server.

MongoDB Connection:
Confirm that MongoDB is running and accessible at the specified URI. Adjust the connection string in app.py if necessary.

CORS Issues:
The app uses flask-cors to handle CORS. If you experience cross-origin problems, verify that CORS is enabled correctly.

Following these steps should result in a working Flask API server. If you encounter any issues, please review the error messages or check your configuration.

# Frontend Setup (Vue)

**1. Navigate to the client folder:**

    cd ../client

**2. Install Node.js dependencies**

    npm install
    (or if you prefer yarn, run yarn install)

**3. Run the Vue development server:**

    npm run serve
    By default, the Vue app will be served at http://localhost:8080.

## Troubleshooting (Frontend)
Dependency Issues:
If you encounter errors during npm install or yarn install, verify that you have the correct version of Node.js installed.

API Connectivity:
If the frontend is not communicating with the backend, check that the VUE_APP_API_URL is correctly configured and that the Flask API server is running.

Port Conflicts:
Verify that no other application is using port 8080 (or the port specified by your Vue configuration).

## Running the Application
Once both servers are running:

  Backend (Flask): Accessible at http://127.0.0.1:5000

  Frontend (Vue): Accessible at http://localhost:8080

Ensure that the Vue frontend is configured to make API requests to the Flask backend. This may involve setting the API base URL in your Vue configuration or environment variables.

Environment Variables
Make sure you have correctly set the following environment variables in your backend’s .env file:

    FLASK_APP: The entry point of your Flask application (e.g., app.py).

    FLASK_ENV: Set to development during development for debug information.

    MONGO_URI: The MongoDB connection URI.

Following these instructions should result in a working application. If you encounter any issues, review the error messages and logs for further guidance.