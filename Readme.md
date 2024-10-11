# FastAPI MongoDB CRUD Application

## Project Overview

This project is a FastAPI-based application that performs **CRUD** (Create, Read, Update, Delete) operations for two entities: **Items** and **User Clock-In Records**. The application interacts with a MongoDB database and follows FastAPI standards for API development, documentation, and error handling.

The application is deployed on a free hosting service and automatically generates API documentation using FastAPI's built-in **Swagger UI**.

## Features

- **CRUD Operations** for Items and User Clock-In Records
- **Filtering** of Items and Clock-In Records by various fields
- **MongoDB Aggregation** for counting items by email
- **Swagger UI** for easy API interaction
- Proper validation and error handling using **Pydantic models**

## Requirements

- **Python 3.8+**
- **MongoDB** (either local or MongoDB Atlas)
- **FastAPI**
- **Uvicorn**
- **Motor** (for async MongoDB operations)
- **Pydantic**

## Local Setup

Follow these instructions to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/satyajitsjs/FastAPI_Mongo_CRUD.git
cd FastAPI_Mongo_CRUD
```

### 2. Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Your `requirements.txt` file should include:

```
fastapi
uvicorn
motor
pydantic[email]
```

### 4. MongoDB Setup

Make sure you have MongoDB running either locally or on MongoDB Atlas. Update the `MONGO_DETAILS` in `app/database.py` to reflect your MongoDB connection string.

Example:
```python
MONGO_DETAILS = "mongodb://localhost:27017"  # Or your MongoDB Atlas connection string
```

### 5. Run the Application

```bash
uvicorn app.main:app --reload
```

This will start the FastAPI application on `http://127.0.0.1:8000`.

### 6. Access the Swagger Documentation

Once the app is running, you can access the automatically generated API documentation at:
```
http://127.0.0.1:8000/docs
```

## Endpoints

### Items API

- **POST /items**: Create a new item.
  - Request Body:
    ```json
    {
        "name": "Item Name",
        "email": "user@example.com",
        "item_name": "Laptop",
        "quantity": 10,
        "expiry_date": "2024-12-31"
    }
    ```
  
- **GET /items/{id}**: Retrieve an item by ID.

- **GET /items/filter**: Filter items based on email, expiry date, insert date, or quantity.
  - Query Parameters (optional):
    - `email`: exact match for email.
    - `expiry_date`: items expiring after this date.
    - `insert_date`: items inserted after this date.
    - `quantity`: items with a quantity greater than or equal to this number.

- **GET /items/aggregate**: Aggregate data to return the count of items grouped by email.

- **PUT /items/{id}**: Update an item by its ID (excluding `insert_date`).

- **DELETE /items/{id}**: Delete an item by its ID.

### User Clock-In Records API

- **POST /clock-in**: Create a new clock-in entry.
  - Request Body:
    ```json
    {
        "email": "user@example.com",
        "location": "Office"
    }
    ```

- **GET /clock-in**: Retrieve all clock-in records.

- **GET /clock-in/{id}**: Retrieve a clock-in record by ID.

- **GET /clock-in/filter**: Filter clock-in records based on email, location, or insert date.

- **PUT /clock-in/{id}**: Update a clock-in record by its ID (excluding `insert_date`).

- **DELETE /clock-in/{id}**: Delete a clock-in record by its ID.

## MongoDB Aggregation Example

The **GET /items/aggregate** endpoint uses MongoDB aggregation to count the number of items grouped by email.

Sample response:
```json
[
    {
        "_id": "user1@example.com",
        "count": 5
    },
    {
        "_id": "user2@example.com",
        "count": 2
    }
]
```

## Deployment

The application can be deployed to a free hosting service like **Koyeb**, **Heroku**, or any other service supporting FastAPI. Ensure you add the necessary environment variables for MongoDB connection in your hosting platform.

### Steps for Koyeb Deployment

1. Push your code to **GitHub**.
2. Connect your **Koyeb** account to your GitHub repository.
3. Set up the deployment with your MongoDB connection string as an environment variable.
4. Koyeb will automatically build and deploy your FastAPI app.

## Links

- **GitHub Repository**: [GitHub Link](https://github.com/satyajitsjs/FastAPI_Mongo_CRUD.git)

## Conclusion

This project demonstrates the use of FastAPI with MongoDB for performing CRUD operations, filtering, and aggregation. The application is easy to set up and provides a fully interactive API documentation interface via Swagger UI.
