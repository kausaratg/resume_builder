# resume_builder
A Django webapp use to build a Resume. It allows the user to fill in their information and then render it in the cv template.
# Description
<ul>
<li>Built with Python, Django, HTML, CSS, Bootstrap</li>
<li>The webapp allows the user to fill in their profile , and then render it in a cv template. It allows user all over the world to build their resume without going through any stress.</li>
<li>Technology Used: This webapp makes use of mostly Django. Django is a high-level Python web framework with pre-written composite codes for web development, thus easing the stress of coding on the developers. It is reassuringly secure and exceedingly scalable.</li>
</ul>

# Features
<li>Signup: Enables user to signup with Username and password</li>
<li>Login: Authenticate the user and allows the user to gain full access to the platform </li>
<li>Profile Form: Allows the user to fill in their basic information such as firstname, lastname, email, biography... in order to render it in the cv template</li>
<li>Templates: The webapp allows the user to choose any of the template in the templates page. The Webapp consist of 5 different templates. </li>

### Special Feature
Resume Builder make use of django summernote which allows the user to customize their information in the profile form. It has some of features such as 'bold', 'unordered list', 'ordered list', 'font size', 'font family' and also 'paragraph'.

## To install and run the project
1. Create a django environment 
2. clone the project             ```git clone https://github.com/kausaratg/resume_builder.git``` 
3.  Enter into the directory         ```cd portfolio_app```
4.  Pull any recent change from main branch     ```git pull origin main```
5.  create a virtual env   ```python -m venv env```
6. Activate the virtual env   ```env/Scripts/activate```
7. Install dependencies  ```pip install -r requirements.txt```
8. Make migration    ```python manage.py makemigration```
9. Migrate the project   ```python manage.py migrate```
10. Run local Server  ```python manage.py runserver```
# NOTE
There is also admin privilege for superuser. It can be accessed by only the superuser. Passwords are hashed wich makes it more secure against threat. Only superuser can make a post.
