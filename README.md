# DjangoProject 
# Task 1
What I Did

step 1: i created  virtual env
python -m venv DjangoAssignment

Step 2: Activate the Virtual Environment
DjangoAssignment\Scripts\activate

Step 3: Install Django
pip install django

Step 4: Create a New Django Project: Login System
django-admin startproject LoginSystem
step 5:Navigate to the Project Directory:
cd LoginSystem
step 6:Create a New Django Application: Loginify
django-admin startproject LoginSystem

step 7:Register the Application:
Add "Loginify" to the INSTALLED_APPS list in settings.py

![image](https://github.com/user-attachments/assets/9b1114d7-cc31-4103-bb12-19cd55a843a4)



# Task 2


1) Create Views
   
![image](https://github.com/user-attachments/assets/9fb04693-5bb9-4ce7-a83f-4481705d9b69)


3) Define URL Patterns

   ![image](https://github.com/user-attachments/assets/e40e87ff-22bd-4411-8637-188c0bfe120a)

3)Create a view that returns an HTTP response with the text
"Hello, world!"
![image](https://github.com/user-attachments/assets/bcc5fbc6-512c-4c44-a54a-a98dbca265b0)



# Task  3

 1: Define Models
1.1 Define the UserDetails Model
In the models.py file of the Loginify app, we will create a UserDetails model. This model will store the user's username, email, and password

![image](https://github.com/user-attachments/assets/8b894515-9d5e-45db-8eac-51c77069a65f)

Make Migrations:
python manage.py makemigrations

Apply Migrations:
This command will apply the generated migrations and create the necessary tables in your database.
python manage.py migrate

![image](https://github.com/user-attachments/assets/b7aca513-dc18-4731-976a-2bb108dc5415)

2.Views:
Implement views for signup and login.

3.Templates:
Create HTML templates for signup and login forms.


Working:
if user is new user they will first sign up and create account 

![image](https://github.com/user-attachments/assets/fa425875-d3d2-4e76-834c-f453209faa0b)

once the signup is succesfull it will redirect the user to the login page

![image](https://github.com/user-attachments/assets/005fc72f-6798-4b62-875a-ccb42cf2c1c4)


![image](https://github.com/user-attachments/assets/6e452a09-431b-4d68-af07-eb8785d5dcf7)


# Task 4
1. Set Up Superuser Account
Django provides a command to create a superuser account that has full access to the Django admin interface.

Create the Superuser: Run the following command to create a superuser:python manage.py createsuperuser

![image](https://github.com/user-attachments/assets/266db50f-54a1-42dd-bace-230590aceb4a)


![image](https://github.com/user-attachments/assets/b63ff57f-e90c-4035-b3e9-8d15d0d3996c)



# Task 5
![image](https://github.com/user-attachments/assets/9e0e782d-f33a-42cc-8966-3b30468bdab1)



![image](https://github.com/user-attachments/assets/8dc08c35-7cef-4d26-88a6-5ff9de8f6df5)


![image](https://github.com/user-attachments/assets/1c32184c-b579-4aa8-a1fc-f4e0bdc98dda)
![image](https://github.com/user-attachments/assets/a3bba6c9-98b9-4984-9f68-2f066fe88586)

![image](https://github.com/user-attachments/assets/20147f32-9a99-4e31-90a5-23d41d6aea67)


![image](https://github.com/user-attachments/assets/6dac4903-e846-414d-91ed-bff05056e29a)


![image](https://github.com/user-attachments/assets/ca68b678-d2d0-4c09-8fa7-6ba63e2143f2)


![image](https://github.com/user-attachments/assets/95f5adee-9c31-4f8c-92b4-de0c9767e30c)



# POSTMAN
GET  Method:

![image](https://github.com/user-attachments/assets/a442a6a0-6c76-472d-94e9-cd5e6fdd1c07)

Get Single user data :

![image](https://github.com/user-attachments/assets/fa8bdb42-f3cf-4a42-9b29-313f41d66bdc)


Post Method:
![image](https://github.com/user-attachments/assets/b78d0eef-af0f-4757-b7a0-a660e0537167)



Put Method:
updating single user data
![image](https://github.com/user-attachments/assets/ec8e550c-7221-4945-a816-d3934a25b0ac)

![image](https://github.com/user-attachments/assets/1e1fd62a-b42b-4553-96fc-ad2133483bfa)


Delete:

![image](https://github.com/user-attachments/assets/30efd33b-9631-4c9f-bea1-1476de6404b2)














