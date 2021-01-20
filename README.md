# Polling_tool_app_backend

This project contains files responsible for a backend of a web application that acts as a polling tool. User after oppening application can see two buttons, one is used to 
navigate to page where user can answer a question, second one allows to see responses of previous users of that application. When users answers to question, thank you
message appears. Database used here is mongoDB that runs on AWS cloud, therefore internet connection is required to run this application succesfuly.

Project was generated with Django 3.1.5 and Python 3.7.2


Running backend server:

  - Navigate to directory backendPollingApp
  - Open command line in this directory, type "myenv\Scripts\activate: and click enter in order to start virtual enviroment
  - Now change directory in command line by typing "cd recruitment_task" and click enter
  - Type in command line "python manage.py runserver". Backend server is now live, do not close the command line.
  
Test concluded using postman application:

   This backend uses methods "POST" and "GET" to retrieve and update data stored in database and correct implementation of those method is crucial for this app. 
  
   Running test for "GET" method:
        While backend server is live and it is running at http://127.0.0.1:8000 paste inside UI interface of postman to method "GET" this link http://127.0.0.1:8000/show-answers/
        The response from the server will be all files stored inside database.

   Running test for "POST" method
       While backend server is live and it is running at http://127.0.0.1:8000 paste inside UI interface of postman to method "POST" this link http://127.0.0.1:8000/add-answer/
        The input should be JSON format eg.
             {
                 "answer": "data you want to add"
             }
        After running this command the data will be added to the database, maximum lenght of the string is set to 150 characters. 

Running unitests:
    
   - While the virtual enviroment is activate and you are in "backendPollingApp\recruitment_task" folder, type in command line "python manage.py test" and press enter. 


Files responsible for frontend side of this application can be found here: https://github.com/Michalloo/Polling_tool_app_frontend/tree/master
