# **The happy Reader - Project Portfolio 4**

![The happy Reader]()

The Happy Reader is a Childrens Book Search and Review website, for users who would like to look up book reviews to help them decide the next book best suited for their child, and in turn to leave reviews on books to help others. Hopefully this well help your child grow a love for books that will last through out their life.

You can view the live site here - <a href="https://the-happy-reader.herokuapp.com/" target="_blank"> The happy reader </a>

# Objective

The aim of this site is to deliver an interactive website that users can engage with via a user log in system to acess a book database in which they can engage with to leave comments and search books for books is perfecrt for their child.

[Back to top](<#contents>)

# User Experience (UX)

## Site Aims

* To provide the user with a website that allows them to view book listings and reviews geared towards children
* To easily find books that may spark a love of books for their child.
* To allow the user the user to create, update and delete reviews
* To provide the admin user with the ability to approve, update and delete book reviews in the frontend
* To provide a clear and appropriate response to any user inputs or actions


## Agile Methodology

The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board which can be seen here -  <a href="https://github.com/users/LauraMayock/projects/3" target="_blank"> The happy reader Project </a>

Through the use of the Kanban board in the projects view in Github, the project was divived into a few different sections:
* No status
* Backlog
* Current Iteration
* In Progress
* Done

![Kanban board github](https://res.cloudinary.com/dyhess8yw/image/upload/v1670436094/Kamban_board_r9euxi.png)
Layout.

Github issues were used to create User Stories and any other Fixes or Updates for the project. This was where the project user was assigned, labels were added to show at a glance importance of tasks and help prioritise jobs. User story was added to the appropriate Iteration and the project. Each User Story, Fix or Update had a clear title, acceptance criteria and smaller tasks (if appropriate).

Milestones were used to create Iterations. There were 3 Iterations each dated appropriately. User Stories were completed based on the current Iteration that was in progress.

### User Stories

**Iteration 1**
* As a Site Admin I can create, read, update and delete posts so that I can manage my blog content.
* As a user I can easily see the purpose of the site from the landing page so that I can see if the site is relevant to my needs.
* As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments

**Iteration 2**
* As a User I can update and edit reviews so that I can amend errors or add extra information.
* As a user  I can save books so that I can easily see books of interest to me
* As a user I can create my own book reviews so that I can contribute to be blog
* As a user I can click into the book view i find interesting so that so that I can view the whole post on one page


**Iteration 3**
* As a user I can access all my reviews easily in one place so that I can easily update and delete
* As a user, I can view a list of books specific to a certain child's age group so I can see a list of books most relevant to the child I am researching for.
* As a user I can register an account so that I can save a list of books I live on the site

**Still in backlog for future features**
* As a user I can use a search bar to search for a specific book or author so I have quick and easy access to the information I need.
* As a user I can access my list of saved books and see the comments and likes I have left on Book reviews so that I can easily track my activity on the site and interacted with the blog owners' content
* As a user I can view a list of books genres/categories so that I can see a list of books relating to the child's specific interests or genres.
* As a user I can save books so that I have a list of books I approve of for my children for future reading.
* 

## Design Wireframes

<details> <summary> Low fidelity mobile wireframes</summary>

![Home Page](/the_happy_reader/Docs/Mobile/Mobile-landing%20page.png)

![Blog post](/the_happy_reader/Docs/Mobile/Mobile-%20Blog%20post%20when%20clicked.png)

![Signup Page](/the_happy_reader/Docs/Mobile/Mobile-%20Sign%20Up.png)

![Login Page](/the_happy_reader/Docs/Mobile/Mobile-%20Login%20page.png)


![My Books](/the_happy_reader/Docs/Mobile/Mobile-%20List%20of%20saved%20books.png)

![Contact Page](/the_happy_reader/Docs/Mobile/Mobile-%20Contact.png)

</details>

<details> <summary> Low fidelity tablet wireframes</summary>

![Home Page](/the_happy_reader/Docs/Tablet/Tablet-landing%20page.png)

![Signup Page](/the_happy_reader/Docs/Tablet/Tablet-%20Sign%20up.png)

![Login Page](/the_happy_reader/Docs/Tablet/Tablet%20-%20Log%20in%20page.png)

![Blog post](/the_happy_reader/Docs/Tablet/Tablet-%20Blog%20post%20when%20clicked.png)

![My Books](/the_happy_reader/Docs/Tablet/Tablet-%20List%20of%20saved%20books.png)


</details>

<details> <summary> Low fidelity Desktop wireframes</summary>

![Home Page](/the_happy_reader/Docs/Tablet/Tablet-landing%20page.png)

![Signup Page](/the_happy_reader/Docs/Tablet/Tablet-%20Sign%20up.png)

![Login Page](/the_happy_reader/Docs/Tablet/Tablet%20-%20Log%20in%20page.png)

![Blog post](/the_happy_reader/Docs/Tablet/Tablet-%20Blog%20post%20when%20clicked.png)

![My Books](/the_happy_reader/Docs/Tablet/Tablet-%20List%20of%20saved%20books.png)

</details>

## Database Schema
<details> <summary>Database layout using Lucidcharts</summary>

![Database Schema](/the_happy_reader/Docs/Org%20chart.png)

</details>

## Site Structure
On first view The Happy Reader website has 4 pages visible from the navigation bar, the Age group drop down filters the correct information onto the page which is only accessible from the home page. Sign in and log in are available on first landing as well as a contact us page. There are 2 other pages available on the nav bar when the user signs in. These are View reviews and Add a review. In the View Reviews page you can choose one of your reviews you previously created to either amend or Delete. This ensures that only authorised users can add or amend information from the database.

The Home page, Login, Signup Age group and Contact pages can be accessed by all users. Once a user logs in or signsup they have access to the Reviews dropdown that shows Add review or see reviews. The Signup page is removed from the navbar once the user logs in and the log in page is changed to a log out page.


## Design Choices

### Color Scheme

The color scheme chosen was a dark almost black colour with a stark white contrast and a bright green used as highlights. I chose colours that would allow the imagery stand out.

![Site colour scheme](/the_happy_reader/Docs/colours.png)

### Typography
One font was chosen for this website and that was Source Sans Pro from google fonts. It is clear and simple for reading. 

I also chose Kalam for the Logo on both the Navbar and Footer.

[Back to top](<#contents>)

# Features

## Navigation

* The site navigation is done through the navigation bar at the top of each page and this does not change in style throughout the user's navigation of the website.
* Tabs on the navigation bar change depending on whether the user is logged in or not.

    ![Navbar Admin Logged In](/the_happy_reader/Docs/nav-logged-in.png)

    * If the user logs in or signs up, those two tabs are removed to be replaced with a log out tab.

    ![Log out tab](/the_happy_reader/Docs/nav-logged-out.png)

    * Once the user logs in or signs up, a completely new tab appears called Reviews, which is essentially the users page

## Home Screen

 * The Home Page page of the website that's visible first when the site loads. It is designed that the purpose of the website easily determined.

 ![Homepage Desktop](/the_happy_reader/Docs/Main%20screen%20L.png)

 ![Homepage Tablet](/the_happy_reader/Docs/Main%20screen%20T.png)

 ![Homepage Mobile](/the_happy_reader/Docs/main%20screen%20S.png)


 * There is a large hero image to catch the user's eye, the site name, a call to action with a log in and signup button. If the user logs in, an alert appears to confirm login, and a welcome message addressing the user by username and two buttons which link to the user's reveiws or to creat a reveiw appears.

  ![Homepage Logged In](/the_happy_reader/Docs/Logged%20in.png)

  ![Homepage Logged Out](/the_happy_reader/Docs/logged%20out.png)

 * Below the hero image is a selection of book reviews clearly marked by age for the users easy. This secition draws from the entire database of approved books and those with uploaded book images, in random order. If the user clicks on a books image or title, the link brings the user to that book's page.
 
 ### Age Group Section

 * Filtering books by age range can be done by the user from the homepage using the navigation bar dropdown.

![Age group dropdown Desktop Page](/the_happy_reader/Docs/Age%20range.png)

 * When an age range is chosen by the user they are brought to a page showing only the books recommended for that age group.
 

 ![Age Range Desktop Page](/the_happy_reader/Docs/age%20range%20page.png)

## Log In Page

  ![Log In page desktop](/the_happy_reader/Docs/sign%20in%20desktop.png)

  ![Log In page tablet](/the_happy_reader/Docs/sign%20in%20tablet.png)

  

* The Log In page is accessed from either the navigation bar or a button on the homepage.
* The Log In page contains a link to the Sign Up page for the user who may have misclicked and needs to Sign Up rather than log in.
* It uses django-allauth to provide all the settings for user authentication.
* Styles are consistent with the rest of the website
* The page is fully responsive


## Sign Up Page

![Sign Up page desktop](/the_happy_reader/Docs/signup%20d.png)

* The Sign Up page is accessed from either the navigation bar or a button on the homepage.
* The Sign Up page contains a link to the Log In page for the user who may have misclicked and already has an account.
* It uses django-allauth to provide all the settings for user authentication.
    * Unique username
    * Strength of password
* Styles are consistent with the rest of the website
* The page is fully responsive

![Sign Up page mobile](/the_happy_reader/Docs/signup%20p.png)

## Log Out Page

![Log out page desktop](/the_happy_reader/Docs/logout%20d.png)

* The Log Out page can only be accessed from the navigation bar and only when the user is logged in.
* The Log Out page has a button for users to confirm they wish to log out.
* It uses django-allauth to provide all the settings for user authentication.
* Styles are consistent with the rest of the website
* The page is fully responsive

![Log out page phone](/the_happy_reader/Docs/logout%20p.png)


### Create a Review

* The user must be logged in to review a book

![Log in to review](/the_happy_reader/Docs/reveiw%20dropdown.png)

![Review page](/the_happy_reader/Docs/create%20a%20review.png)

* If the user isn't logged in, text informs the user to log in to review.

![Not logged in to review](/the_happy_reader/Docs/review%20warning.png)

* The review button at the top of the page brings the user to the review section at the bottom.
* Once the user reviews, they receive an alert that their review has been flagged for approval.

![Review added alert](/the_happy_reader/Docs/success%20alert.png)

* Once the review is approved it will appear with the other reviews.


### Veiw Reviews

* When the user is logged in they can view all the reviews they have created in the Your Reviews section in the dropdown or through the button on the homepage.

![Navbar Your reviews](/the_happy_reader/Docs/reveiw%20dropdown.png)

![Review page](/the_happy_reader/Docs/revie.png)

* From here the user can see all their reviews. One approved or not.
* The user can choose from here to either amend or delete a review.
* Clicking the update review button, brings the user to an edit review page where the user can change the content of their review.
* If the user decides to update their review it is sent for approval by an admin again.
* The user is brought back to their reveiws page and an alert notifies the user that they have updated their review and that it has been sent for approval.

## Delete a review 

* The user also has the ability to delete reviews that they have created in the 'Your reviews' page.

![Delete page](/the_happy_reader/Docs/delete%20page.png)
 
* If the user decides to delete their review, they are brought to a delete review page, where they are asked to confirm whether they wish to delete the review. If they decide to delete the review. If they choose the delete button they will get an alert stating that the review was deleted sucessfully if they choose to cancel it will revert them back to their reviews page.

## Contact

![Contact desktop page](/the_happy_reader/Docs/Contact%20us%20d.png)

![Contact mobile page](/the_happy_reader/Docs/contact%20us.png)

* The contact page can be accessed by all users, logged in or not.
* It uses django-allauth to ensure that it is fill out out correctly.
* It submits messages to the admin dashboard.
* It provides the user with an alert to say that it has been sent sucessfully.
* If the user doesn't fill all the fields, a pop up will ask the user to please fill out the required field.
* The email field requires a proper email address with the @ symbol to be able to field the field correctly.
* The page is fully responsive

[Back to top](<#contents>)

### Future Features

## Search Bar

In a future interger i would like to add

## Social Media Login

For ease of use, user's could use their social media credentials to log in, rather than creating another password to remember.

## 

## User Profile Page

 page could be expanded  to include the ability of the user to add their bookmarked books in categories to organise them; for example, Read Again, or Must Read or Read.

The page could also provide more user details that could also be added to the user profile in general. Such as a profile picture or avatar that could be utilised in their reviews, and the total number of books they have reviewed or bookmarked could be visible on their profile.


## Better Pagination

Pagination is implemented on some pages but it could definitely be expanded to more pages such as the My Books page or the Genre pages for better User Experience.

[Back to top](<#contents>)

# Technologies Used

* HTML - Used to structure all the templates on the site
* CSS - to provide extra styling to the site
* Python - To provide functionality to the site. Packages used in the project can be found in requirements.txt
* Django - Python framework used in the project
* Heroku - Used to deploy the site publicly
* Heroku ElephantSQL - Used for the database during development and deployment
* Javascript - Minimum javascript was used, to fade out alerts after a few seconds and and to  
  create a button up which would bring the user back to the top  of the screen.
* Bootstrap 4 -  used for providing layouts and styling the html in the templates
* Basimiq - Used to create wireframes for the progect
* Cloudinary - Used to host Static files for the site

[Back to top](<#contents>)

# Testing

## Validation

### Html Validation

Html validation was done with [https://validator.w3.org/nu/](https://validator.w3.org/nu/). The deployed link from the site was used the below errors were highlighted.

[HTML VALIDATION](/the_happy_reader/Docs/HTML%20error.png)

After researching the error message I learned on Slack that this issue was caused by a closing tag being in the wrong place. It needed to be placed after.



#### **Home Page**
![Home Page Html Validation](docs/images/validation/home-page.png)



[Back to top](<#contents>)

# Deployment

## Deployment to Heroku

### 1. Creating the Django Project
* If development if being done locally: Activate your virtual environment
* To ensure the virtual environment is not tracked by version control, add .venv to the .gitignore file.
* Install Django and gunicorn: `pip3 install django gunicorn`
* Install supporting database libraries dj_database_url and psycopg2 library: `pip install dj_database_url psycopg2`
* Install Cloudinary libraries to manage static files: `pip install dj-3-cloudinary-storage`
* Create file for requirements: `pip freeze --local > requirements.txt`
* Create project:`django-admin startproject project_name .`
* Create app: `python manage.py startapp app_name`
* Add app to list of `installed apps` in settings.py file: `'app_name'`
* Migrate changes: `python manage.py migrate`
* Test server works locally: `python manage.py runserver`

### 2. Create your Heroku app
* Navigate to the Heroku website
* Create a Heroku account by entering your email address and a password (or login if you have one already).
* Activate the account through the authentication email sent to your email account
* Click the **new button** on the top right corner of the screen and select create a new app from the dropdown menu.
* Enter a unique name for the application.
* Select the appropriate region for the application.
* Click create app
* In the Heroku dashboard click on the Resources tab
* Scroll down to Add-Ons, search for and select 'Heroku Postgres'
* In the Settings tab, scroll down to 'Reveal Config Vars' and copy the text in the box beside DATABASE_URL.

### 3. Set up Environment Variables
* In you IDE create a new env.py file in the top level directory
* Add env.py to the .gitignore file
* In env.py import the os library
* In env.py add `os.environ["DATABASE_URL"]` = "Paste in the text link copied above from Heroku DATABASE_URL"
* In env.py add `os.environ["SECRET_KEY"] = "Make up your own random secret key"`
* In Heroku Settings tab Config Vars enter the same secret key created in env.py by entering 'SECRET_KEY' in the box for 'KEY' and your randomly created secret key in the 'value' box.

### 4. Setting up settings.py

* In your Django 'settings.py' file type:

 ```
 from pathlib import Path
 import os
 import dj_database_url

 if os.path.isfile("env.py"):
  import env
 ```
* Remove the default insecure secret key in settings.py and replace with the link to the secret key variable in Heroku by typing: `SECRET_KEY = os.environ.get(SECRET_KEY)`
* Comment out the `DATABASES` section in settings.py and replace with:
```
DATABASES = {
  'default': 
  dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }`
```
* Create a Cloudinary account and from the 'Dashboard' in Cloudinary copy your url into the env.py file by typing: `os.environ["CLOUDINARY_URL"] = "cloudinary://<insert-your-url>"`
* In Heroku  add cloudinary url to 'config vars'
* In Heroku config vars add DISABLE_COLLECTSTATIC with value of '1' (note: this must be removed for final deployment)
* Add Cloudinary libraries to the installed apps section of settings.py file:
 ```
 'cloudinary_storage'
 'django.contrib.staticfiles''
 'cloudinary'
 ```
* Connect Cloudinary to the Django app in `settings.py`:
```
STATIC_URL = '/static'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'STATIC')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE =
'cloudinary_storage.storage.MediaCloudinaryStorage'
* Link file to the templates directory in Heroku 
* Place under the BASE_DIR: TEMPLATES_DIR = os.path.join(BASE_DIR,
'templates')
```
* Change the templates directory to TEMPLATES_DIR. Place within the TEMPLATES array: `'DIRS': [TEMPLATES_DIR]`
* Add Heroku Hostname to ALLOWED_HOSTS: ```ALLOWED_HOSTS =
['rhi-book-nook.herokuapp.com', 'localhost']```
*Create Procfile at the top level of the file structure and insert the following:
    ``` web: gunicorn PROJECT_NAME.wsgi ```

* Make an initial commit and push the code to the GitHub Repository.
    ```git add .```
    ```git commit -m "Initial deployment"```
    ```git push```

### 5. Heroku Deployment: 
* Click Deploy tab in Heroku
* In the 'Deployment method' section select 'Github' and click the 'connect to Github' button to confirm.
* In the 'search' box enter the Github repository name for the project
* Click search and then click connect to link the heroku app with the Github repository. The box will confirm that heroku is connected to the repository.

### 6. Final Deployment
In the IDE: 
* When development is complete change the debug setting to: `DEBUG = False` in `settings.py` 
* In Heroku settings config vars change the DISABLE_COLLECTSTATIC value to 0
* Because DEBUG must be switched to True for development and False for production it is recommended that only manual deployment is used in Heroku. 
* To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.

## To fork the repository on GitHub

A copy of the GitHub Repository can be made by forking the GitHub account. Changes can be made on this copy without affecting the original repository.

1. Log in to GitHub and locate the repository in question.
2. Locate the Fork button which can be found in the top corner, right-hand side of the page, inline with the repository name.
3. Click this button to create a copy of the original repository in your GitHub Account.

## To clone the repository on GitHub

1. Click on the code button which is underneath the main tab and repository name to the right.
2. In the 'Clone with HTTPS' section, click on the clipboard icon to copy the URL.
3. Open Git Bash in your IDE of choice.
4. Change the current working directory to where you want the cloned directory to be made.
5. Type git clone, and then paste the URL copied from GitHub.
6. Press enter and the clone of your repository will be created.

[Back to top](<#contents>)

# Credits

* [Crispy Forms Fix](https://stackoverflow.com/questions/65133364/django-crispy-forms-is-not-working-correctly)
* []()
* []()
* [Pexcel](https://www.pexels.com/)
* []()
* []()

[Back to top](<#contents>)

# Acknowledgements

This website was designed and developed in conjunction with the Full Stack Software Developer Diploma course (eccommerce) at the Code Institute. I would like to thank my family, my cohort facilitator, the members of our cohort, the Slack community and Code Institute for all their support.


[Back to top](<#contents>)
##bug

[](//the_happy_reader/Docs/Going%20back%20to%20old%20repo.png)

I tried to open a new workspace by and then deleted the old workspaces which caused my env.py not to appear on my new workspace. I created an new env.py and it fixed the issue but by fixing it i lost of the work i had done.

