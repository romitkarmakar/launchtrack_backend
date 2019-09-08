# LaunchTrack Backend API

## Installation

- Clone the repository.
- Open your Terminal enter into the folder.
```
pip install virtualenv
```
- Create a virtual environment.
```
python -m venv env
```
- Then activate the virtual environment.
```
.\env\Scripts\activate
```
- Install all the packages
```
pip install -r requirements.txt
```
- Migrate the database
```
python manage.py migrate
```
- Create admin username and password
```
python manage.py createsuperuser
```
- Run the development Server
```
python manage.py runserver
```