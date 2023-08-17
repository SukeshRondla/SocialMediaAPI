# Social Media Clone API using FastAPI

This repository contains a FastAPI-based backend for a social media app resembling Instagram. The API offers four main routes for creating and managing posts, users, authentication, and voting/liking posts.

## Routes

### 1) Post Route


- **Endpoint**: `/posts`
- **Description**: This route handles creating, deleting, updating, and fetching posts.

### 2) Users Route

- **Endpoint**: `/users`
- **Description**: This route manages user creation and user search by ID.

### 3) Auth Route

- **Endpoint**: `/auth`
- **Description**: This route handles user authentication and login.

### 4) Vote Route

- **Endpoint**: `/votes`
- **Description**: This route manages the likes/votes system for posts. It currently includes the logic for upvoting but not downvoting.

## How to Run Locally

Follow these steps to run the FastAPI locally on your machine:

1. Clone the repository:

   ```bash
   git clone https://github.com/SukeshRondla/fastapi-SocialMediaAPI.git
   cd fastapi-SocialMediaAPI
   ```

2. Install FastAPI and required dependencies:

   ```bash
   pip install fastapi[all]
   ```

3. Run the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

4. Access the API documentation by opening the following link in your browser:

   ```
   http://127.0.0.1:8000/docs
   ```

## Database Setup

Ensure you have a PostgreSQL database created. Create a `.env` file in the project folder with the following configurations:

```dotenv
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=your_database_password
DATABASE_NAME=your_database_name
DATABASE_USERNAME=your_database_username
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

Replace the placeholders (`your_...`) with your actual database and secret key details. The secret key can be obtained from the FastAPI documentation.

**Note**: The provided `SECRET_KEY` in this example is a placeholder. You should generate a proper secret key for security purposes.
