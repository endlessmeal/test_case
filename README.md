## Test case for fabrique (NOT all functionality as required)

API for surveys (Django 2.2.10, djangorestframework 3.10.2)

### API Endpoints

#### Admin's endpoints

* **api/surveys/create** (Endpoint for creating surveys)
* **api/surveys/update_delete/<int:pk>/** (Endpoint for update or delete survey)
* **api/surveys/question/create** (Endpoint for creating a question with parameter 'survey' with an id of survey)
* **api/surveys/question/update_delete/<int:pk>/** (Endpoint for update or delete question)

#### Users 

* **api/users/all_surveys** (Look at all surveys)
* **api/users/survey/questions/<int:pk>/** (All questions of current survey)
* **api/users/survey/questions/answer/<int:pk>/** (Create an answer to the question)

Notice that you need python 3.8 or higher

### Install (for UNIX/MAC OS)
    pip3 install virtualenv
    pip3 install django==2.2.10
    pip3 install djangorestframework
    python3 -m pip freeze
    python3 -m pip install -r requirements.txt
    
### Usage
    python3 -m venv your_name_to_env
    source your_name/bin/activate
    cd 'path/to/folder/with/manage.py'
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
