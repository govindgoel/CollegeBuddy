# CollegeBuddy

### Backend for CollegeBuddy

Python Commands <br>
-> Navigate to backend directory

0. Make sure that you have `Python 3`, `python-3-devel`, `gcc`, `virtualenv`, and `pip` installed.     

1. Create a python 3 virtualenv, and activate the environment.
    ```bash
        $ virtualenv -p python3 .
        $ source bin/activate
    ```   
2. Install the project dependencies from `requirements.txt`
    ```
        $ pip install -r requirements.txt
Then:
`python manage.py makemigrations` 

`python manage.py migrate` 

`python manage.py createsuperuser`

`python manage.py runserver`

Navigate to  `localhost:8000`
### Frontend for CollegeBuddy

NPM Commands


`npm install` - install all node modules (dependencies) to run the app

`npm run dev` - runs the app in development mode in port 3000

`npm run build` - builds the app for production


Tech Stack

Next / React / JSX / SASS

Linting & Quality: ESlint (ESlin Airbnb Config), Prettier

UI Library:  Ant Design

