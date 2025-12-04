# **Auth Demo: React + Flask + MongoDB**

A simple full-stack authentication system built with React (frontend), Flask (backend), and MongoDB (database).
This project demonstrates a clean, minimal, real-world authentication workflow using secure password hashing, JWT-based authentication, and protected routes.

## **Features**

### Authentication

* User Signup
* User Login
* Secure password hashing using bcrypt
* JWT token generation and verification
* Protected backend route (`/profile`)

### Frontend

* React user interface
* Signup page
* Login page
* Profile dashboard
* Token storage in localStorage
* Logout functionality

### Backend

* Flask API with CORS enabled
* Authentication endpoints (`/signup`, `/login`)
* Protected route (`/profile`)
* MongoDB user storage
* Token validation middleware

### Database

* MongoDB collection: `users`
* Stores hashed passwords and user metadata

## **Tech Stack**

### Frontend

* React
* React Router
* Fetch API
* CSS

### Backend

* Python 3
* Flask
* Flask-CORS
* PyJWT
* Bcrypt
* PyMongo

### Database

* MongoDB Community Edition (local installation)



# **Setup Instructions**

## Prerequisites

* Node.js (LTS recommended)
* Python 3.10 or later
* Pip
* MongoDB Community Server
* Git



# **Backend Setup (Flask)**

### 1. Navigate to the backend directory

```powershell
cd backend
```

### 2. Create and activate a virtual environment

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install backend dependencies

```powershell
pip install -r requirements.txt
```

### 4. Create a `.env` file inside `backend/`

```
MONGO_URI=mongodb://localhost:27017
JWT_SECRET=your_super_secret_key
```

### 5. Start MongoDB on Windows

If installed as a Windows service:

```powershell
net start MongoDB
```

### 6. Run the backend server

```powershell
python app.py
```

The backend will be available at:

```
http://127.0.0.1:5000
```



# **Frontend Setup (React)**

### 1. Navigate to the frontend directory

```powershell
cd ../frontend
```

### 2. Install frontend dependencies

```powershell
npm install
```

### 3. Create a `.env` file inside `frontend/`

```
REACT_APP_API_URL=http://localhost:5000
```

### 4. Start the React development server

```powershell
npm start
```

The frontend will be available at:

```
http://localhost:3000
```



# **Running the Full Application**

### Step 1 — Start MongoDB

```powershell
net start MongoDB
```

### Step 2 — Run the backend

```powershell
cd backend
venv\Scripts\activate
python app.py
```

### Step 3 — Run the frontend

Open a second terminal:

```powershell
cd frontend
npm start
```



# **Authentication Flow**

1. User submits the signup form.
2. Backend hashes the password and stores the user in MongoDB.
3. User logs in.
4. Backend verifies credentials and returns a JWT.
5. Frontend saves the token in `localStorage`.
6. Protected routes include the token in request headers.
7. Backend authorizes access using the provided token.



# **Environment Variables**

### Backend `.env`:

```
MONGO_URI=mongodb://localhost:27017
JWT_SECRET=your_secret
```

### Frontend `.env`:

```
REACT_APP_API_URL=http://localhost:5000
```



# **Useful Scripts**

### Backend

```powershell
python app.py
pip install -r requirements.txt
```

### Frontend

```powershell
npm start
npm run build
```



# **Future Improvements**

* Refresh token support
* Email verification
* Password reset workflow
* Improved UI
* Better error handling
* Deployment using Docker
* Role-based access control


# **Screenshots**


## Frontend (React)

The Login Page:
![Login Page](/screenshots/frontend/login.png)

The Registration Page:
![Registration Page](/screenshots/frontend/signup.png)

The Profile Page:
![Profile Page](/screenshots/frontend/profile_signed_in.png)

## Backend Endpoints (Flask)


The Registration Endpoint:
![Registration Endpoint](/screenshots/backend/register_endpoint.png)

The Login Endpoint:
![Login Endpoint](/screenshots/backend/login_endpoint.png)

The Refresh Endpoint:
![Refresh Endpoint 1/2](/screenshots/backend/refresh_endpoint_1_1.png)
![Refresh Endpoint 2/2](/screenshots/backend/refresh_endpoint_1_2.png)

The "Me" Endpoint:
![Me Endpoint](/screenshots/backend/me_endpoint.png)

The Logout Endpoint:
![Logout Endpoint](/screenshots/backend/logout_endpoint.png)


## Database Records (MongoDB)

Documents saved to the users database:
![Mongo Records](/screenshots/db/mongo_record.png)


# **Contributing**

Suggestions and pull requests are welcome.



# **License**

MIT License
