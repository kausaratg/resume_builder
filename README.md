# resume_builder
A webapp use to build a Resume
# Description
<ul>
<li>built with Python, Django, HTML, CSS, Bootstrap</li>
<li>The webapp allows the user to fill in their profile , and then render it in a cv template. It allows user all over the world to build their resume without going through any stress.</li>
<li>Technology Used: This webapp makes use of mostly Django. Django is a high-level Python web framework with pre-written composite codes for webdevelopment, thus easing the stress of coding on the developers. It is reassuringly secure and exceedingly scalable.</li>
</ul>
# Features
<li>Signup: Enables user to signup with Username and password</li>
<li>Login: Authenticate the user and allows the user to gain full access to the platform </li>
<li>Profile Form: Allows the user to fill in their basic information such as firstname, lastname, email, biography... inoder to render it in the cv template</li>
<li>Templates: The webapp allows the user to choose any of the template in the templates page. The Webapp consist of 5 different templates. </li>
### Special Feature
Resume Builder make use of django summernote which allows the user to costomize their information in the profile form. It has some of features such as 'bold', 'unordered list', 'ordered list', 'font size', 'font family' and also 'paragraph'.
## To install and run the project
<li>Create a django environment </li>
<li>clone the project              `git clone https://github.com/kausaratg/resume_builder.git`
</li>
<li>Enter into the directory</li>
```bash
cd portfolio_app
```
<li>Pull any recent change from main branch</li>
```bash
git pull origin main
```
<li> create a virtual env </li>
```bash
python -m venv env
```
<li>Activate the virtual env</li>
```bash
env/Scripts/activate
```
<li>Install dependencies</li>
```bash
pip install -r requirements.txt
```
<li>Make migration</li>
```bash
python manage.py makemigration
```
<li>Migrate the project</li>
```bash
python manage.py migrate
```
<li>Run local Server</li>
```bash
python manage.py runserver
```
# NOTE
There is also admin privilege for superuser. It can be accessed by only the superuser. Passwords are hashed wich makes it more secure against threat. Only superuser can make a post.
