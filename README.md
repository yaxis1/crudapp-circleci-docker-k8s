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

Once the account is created on the website and github is linked, we are ready to write a YAML file that guides the pipeline CI-CD pipeline

A .circleci folder is required to integrate this with the circleci web interface and build the pipeline.

Inside yml file:
 For first job, we run the application on docker after installing dependencies that was previously freezed from local environment.
 For second job, we run test files after installing dependencies. 
 The workflow runs these "Run app" and "test app" jobs parallely to reflect immediate changes in the workflow. 
 
- Infrastructure as Code
 Vagrant is used for building and maintaining portable virtual software development environments like virtualbox and dockers.
 After creating Vagrant file - we vim it to change it according to our application. Here we can change configuration, define the virtualbox name, attributes, also attach an ansible playbook to deploy applications.
 Ansible is one of the software provisioning, configuration management, and application-deployment tool. It is in yaml format and has inbuilt keywords for installation modules. In here, first we install python, mongodb, pip. Then create a virtual environment for our app. Install git and move src file to the virtual environment. Install dependencies from the previously freezed file "requirements.txt". Then, run the app using command module of ansible. We can also run tests using same module but it has to be a new job. 

- Building Docker image of application
 


