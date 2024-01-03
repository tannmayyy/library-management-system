# library-management-system
Library Management System This project is a simple library management system implemented using FastAPI and SQLAlchemy. 
It allows you to perform CRUD operations (Create, Read, Update, Delete) on books in a library.

1) Clone the Repository:

git clone https://github.com/tannmayyy/library-management-system.git

2) Create Virtual Environment:

python -m venv venv

3) Install Dependencies:

pip install -r requirements.txt

4) Run the Application:

uvicorn app.main:app --reload

This will start the FastAPI application. You should see output indicating that the server is running.

5) Access the API Documentation:
Open your web browser and go to http://127.0.0.1:8000/docs. This is the Swagger-based API documentation where you can interact with the API and test the endpoints.

6) Create a Book:

I used postman to create books and check the proper flow of requests. 

Open Postman and create a new request.

Set Request Type to POST:

In the request tab, set the request type to POST.

Enter Request URL:

Set Headers:

Set Request Body:

Enter your JSON payload:

Send the Request:

7) Get All Books:

get on /books/ endpoint.


8) Click on the GET /books/{book_id} endpoint.
Replace {book_id} with the ID of an existing book.

Make sure to have SQLite installed on your machine as the project uses it as the database.