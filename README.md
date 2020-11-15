# Dev-Ops
 Development Operations for CRUD app

This project illustrates the collaboration of development and operational stages of application development. 

- Creating an application that can create, read, update and delete to and from Mongodb database. 

Several routes are used to access points for each functionality. Flask library is used in this case.
We also import pytest and flasgger to implement testing and proper user interface further in the project.

Configuration file is created using a Config(object) and this could be called anywhere in the project to display configuration options. 

- Tests:
api_test : This is made out of importing 'myunitest' module and displays output like 'headers' for each access point url. 

connec_test : This checks if the connection to database is made on the correct port, if not prints error message.

unit_test: This verifies the return code of each route to check if the route is working as expected. It is made out of unittest and requests module. 

- CI/CD Pipeline

We use "circleci" to test and deploy our project.

Once the account is created on the website and github is linked, we are ready to write a YAML file that guides the pipeline 


