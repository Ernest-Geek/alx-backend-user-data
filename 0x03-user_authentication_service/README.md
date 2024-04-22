User Authentication Service
This project implements a user authentication service using Flask, a micro web framework for Python. The purpose of this project is to understand the mechanisms involved in user authentication by implementing them manually.

Learning Objectives
By completing this project, you will be able to:

Declare API routes in a Flask app to handle user authentication endpoints.
Understand how to work with cookies to maintain user sessions.
Retrieve and validate request form data for user authentication.
Return various HTTP status codes to provide appropriate responses.
Requirements
The project should be developed using Python 3.7 on Ubuntu 18.04 LTS.
The code should follow the PEP 8 style guide.
SQLAlchemy 1.3.x should be used for database interactions.
All modules, classes, and functions should be properly documented with descriptive comments.
The project should have executable permissions for all files.
A README.md file should be present at the root of the project folder, providing essential information about the project.
Project Structure
The project should consist of the following components:

API Routes: Declare API routes in the Flask app to handle user authentication endpoints, such as login, logout, registration, etc.
Cookie Management: Implement functionality to set, get, and manage cookies to maintain user sessions securely.
Request Handling: Retrieve and validate request form data for user authentication, ensuring data integrity and security.
HTTP Status Codes: Return appropriate HTTP status codes for various scenarios, such as successful authentication, invalid credentials, server errors, etc.
Auth and DB Interaction: The Flask app should interact only with the Auth class for user authentication and never directly with the database (DB). Only public methods of Auth and DB classes should be used outside these classes.
Usage
To use the authentication service:

Clone the project repository to your local machine.
Install the required dependencies using pip.
Run the Flask app by executing the main script.
Access the API endpoints using HTTP requests to perform user authentication operations.
Development Guidelines
Follow the PEP 8 style guide for writing clean, readable, and maintainable code.
Document all modules, classes, and functions with descriptive comments explaining their purpose, parameters, return values, etc.
Use type annotations for all functions to provide clear information about expected inputs and outputs.
Ensure that the Flask app interacts only with the Auth class for authentication and follows the principles of separation of concerns.
Credits
This project was created as part of a learning exercise to understand the fundamentals of user authentication in web applications using Flask. It draws inspiration from industry best practices and common authentication mechanisms used in modern web development.
