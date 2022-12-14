# **The happy Reader - Project Portfolio 4**

<#contents>

![The happy Reader](/the_happy_reader/Docs/mockup.png)

The Happy Reader is a Children's Book Search and Review website for users who would like to look up book reviews to help them decide the next book best suited for their child and, in turn, to leave reviews on books to help others. Hopefully, this helps your child grow a love for books that will last through out their life.

You can view the live site here - <a href="https://the-happy-reader.herokuapp.com/" target="_blank"> The happy reader </a>

# Objective

This site aims to deliver an interactive website that users can engage with via a user log-in system to access a book database in which they can comment and search books for books that are perfect for their child.

[Back to top](<#contents>)

# User Experience (UX)

## Site Aims

* To provide the user with a website that allows them to view book listings and reviews geared toward children
* To easily find books that may spark a love of books for their child.
* To allow the user to create, update and delete reviews
* To provide the admin user with the ability to approve, update and delete book reviews in the frontend
* To provide a clear and appropriate response to any user inputs or actions


## Agile Methodology

The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board, which can be seen here -  <a href="https://github.com/users/LauraMayock/projects/3" target="_blank"> The happy reader Project </a>

Through the use of the Kanban board in the projects view in Github, the project was divided into a few different sections:
* No status
* Backlog
* Current Iteration
* In Progress
* Done

![Kanban board github](https://res.cloudinary.com/dyhess8yw/image/upload/v1670436094/Kamban_board_r9euxi.png)
Layout.

Github issues were used to create User Stories and any other Fixes or Updates for the project. This is where the project user was assigned; labels were added to show at a glance importance of tasks and help prioritize jobs. User story was added to the appropriate Iteration and the project. Each User Story, Fix or Update had a clear title, acceptance criteria and smaller tasks (if applicable).

Milestones were used to create Iterations. There were 3 Iterations, each dated appropriately. User Stories were completed based on the current Iteration that was in progress.

### User Stories

**Iteration 1**
* As a Site Admin I can create, read, update and delete posts to manage my blog content.
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
* As a user I can access my list of saved books and see the comments and likes I have left on Book reviews so that I can easily track my activity on the site and interact with the blog owners' content
* As a user I can view a list of books genres/categories so that I can see a list of books relating to the child's specific interests or genres.
* As a user I can save books so that I have a list of books I approve of for my children for future reading.

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
On the first view, The Happy Reader website has four pages visible from the navigation bar; the Age group drop-down filters the correct information onto the page, which is only accessible from the home page. Sign-in and log-in are available on the first landing and a contact us page. Two other pages are available on the nav bar when the user signs in. These are View reviews and Add a review. In the View Reviews page, you can choose one of the reviews you previously created to either amend or Delete. This ensures that only authorized users can add or amend information from the database.

The Home page, Log-in, Signup Age group and Contact pages can be accessed by all users. Once a user logs in or signs-up, they have access to the Reviews dropdown that shows Add review or see reviews. The Signup page is removed from the navbar once the user logs in, and the log-in page is changed to a log-out page.


## Design Choices

### Color Scheme

The color scheme chosen was a dark, almost black colour with white contrast and a bright green used as highlights. I chose colours that would allow the imagery to stand out.

![Site colour scheme](/the_happy_reader/Docs/colours.png)

### Typography
One font was chosen for this website, and that was Source Sans Pro from google fonts. It is clear and simple to read. 

I also chose Kalam for the Logo on both the Navbar and Footer.

[Back to top](<#contents>)

# Features

## Navigation

* The site navigation is done through the navigation bar at the top of each page, and this does not change in style throughout the user's navigation of the website.
* Tabs on the navigation bar change depending on whether the user is logged in or not.

    ![Navbar Admin Logged In](/the_happy_reader/Docs/nav-logged-in.png)

    * If the user logs in or signs up, those two tabs are removed to be replaced with a log-out tab.

    ![Log out tab](/the_happy_reader/Docs/nav-logged-out.png)

    * Once the user logs in or signs up, a completely new tab appears called Reviews, which is essentially the user's page

## Home Screen

 * The Home Page page of the website that's visible first when the site loads. It is designed that the purpose of the website easily determined.

 ![Homepage Desktop](/the_happy_reader/Docs/Main%20screen%20L.png)

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

  ![Log In page desktop](/the_happy_reader/Docs/signin%20d.png)
 

* The Log In page is accessed from either the navigation bar or a button on the homepage.
* The Log In page contains a link to the Sign Up page for the user who may have misclicked and needs to Sign Up rather than log in.
* It uses django-allauth to provide all the settings for user authentication.
* Styles are consistent with the rest of the website
* The page is fully responsive


## Sign Up Page

![Sign Up page desktop](/the_happy_reader/Docs/signup%20p.png)

* The Sign Up page is accessed from either the navigation bar or a button on the homepage.
* The Sign Up page contains a link to the Log In page for the user who may have misclicked and already has an account.
* It uses django-allauth to provide all the settings for user authentication.
    * Unique username
    * Strength of password
* Styles are consistent with the rest of the website
* The page is fully responsive


## Log Out Page

![Log out page desktop](/the_happy_reader/Docs/logout%20d.png)

* The Log Out page can only be accessed from the navigation bar and only when the user is logged in.
* The Log Out page has a button for users to confirm they wish to log out.
* It uses django-allauth to provide all the settings for user authentication.
* Styles are consistent with the rest of the website
* The page is fully responsive

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

In a future integer, I would like to add a search bar on the main screen to make it easier to search specifically for book titles or authors. This will help ensure that users are not adding more reviews on the same book.

## Social Media Login

For ease of use, users could use their social media credentials to log in rather than creating another password to remember.


## User Profile Page

A user profile page to include the ability of the user to add saved reviews in categories to organize them; for example, Read Again or Must Read or Read. To show all comments they have made on other reviews.

The page could also provide more user details that could also be added to the user profile in general. Such as a profile picture or avatar that could be utilized in their reviews, and the total number of books they have reviewed or bookmarked could be visible on their profile. As well as specifying the age of the children they are browsing for.

## Genre section

A genre section so that books can be chosen on the bases of the child's interests or an underlying lesson you would like the child to learn about.

## Upload images

The user to be able to upload their own images via the 'add review' form.
[Back to top](<#contents>)

# Technologies Used

* HTML - Used to structure all the templates on the site
* CSS - to provide extra styling to the site
* Python - To provide the functionality to the site. Packages used in the project can be found in requirements.txt
* Django - Python framework used in the project
* Heroku - Used to deploy the site publicly
* Heroku ElephantSQL - Used for the database during development and deployment
* Javascript - Minimum javascript was used to fade out alerts after a few seconds and to create a button that would bring the user back to the top of the screen.
* Bootstrap 4 -  used for providing layouts and styling the html in the templates
* Basimiq - Used to create wireframes for the project
* Cloudinary - Used to host Static files for the site

[Back to top](<#contents>)

# Testing

## Validation

### Html Validation

Html validation was done with [https://validator.w3.org/nu/](https://validator.w3.org/nu/). The deployed link from the site was used the below errors were highlighted.

![HTML VALIDATION](/the_happy_reader/Docs/HTML%20error.png)

After researching the error message I learned on Slack that this issue was caused by a closing tag being in the wrong place. It needed to be placed after.

### CSS Validation

The stylesheet was validated using [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)

![Stylesheet validation](/the_happy_reader/Docs/css%20validation.png)


### Python Validation

Python code was validated using [Code institues Python validator](https://pep8ci.herokuapp.com/#)

Only minor errors such as missing blank spacing or whitespace. These were rectified easily.

### Javascript Validation

Javascript was validated using [jshint](https://jshint.com/)

Apart from minor errors such as semicolans missing the validations was a success. All minor errors
were delt with easily.

### Lighthouse Testing

# Home page

Lighthouse testing ![Lighthouse testing](/the_happy_reader/Docs/lighthouse%20for%20homepage.png)
Most pages scored hight.
The ligth house testing came up quite poor especially in the Preformance section and Best Practice. 

* I removed two unnecessary google font links in my code. 
* Compressed the  main images and gave images a height and width.

![Lighthouse final results desktop](/the_happy_reader/Docs/lighhouse%20home%20final%20test.png)
![Lighthouse final results mobile](/the_happy_reader/Docs/lighhouse%20home%20final%20test%20mobile.png)

# Age page
![Lighthouse age page](/the_happy_reader/Docs/age%20page.png)

* I amended the font size in the age section to help with accessibility.

## Manual Testing

In addition to the other tests, I have conducted a manual check list for myself to carry out to make sure that everything is working as intended.

| Status | **Navigation Bar - User Logged Out**
|:-------:|:--------|
| &check; | Clicking the navbar logo loads the home page
| &check; | That the navbar shows the tabs Home, Bookshelf, Login, Signup and Contact if the user is logged out
| &check; | Clicking the Home tab on the navbar loads the home page
| &check; | Clicking the Bookshelf tab on the navbar loads the bookshelf page
| &check; | Clicking the Login tab on the navbar loads the login Page
| &check; | Clicking the Signup tab on the navbar loads the signup page
| &check; | Clicking the Contact tab on the navbar loads the contact page

| Status | **Navigation Bar - User Logged In**
|:-------:|:--------|
| &check; | Clicking the navbar logo loads the home page
| &check; | That the navbar shows the tabs Home, Bookshelf, My Books, Logout and Contact if the user is logged in
| &check; | That the navbar shows the username of the logged in user and that clicking this leads to the user My Books page
| &check; | Clicking the Home tab on the navbar loads the home page
| &check; | Clicking the Bookshelf tab on the navbar loads the bookshelf page
| &check; | Clicking the My Books tab on the navbar loads the user's my books Page
| &check; | Clicking the Logout tab on the navbar loads the logout page
| &check; | Clicking the Contact tab on the navbar loads the contact page
| &check; | Clicking user's username in the navbar loads the user's my books page


| Status | **Footer - User Logged Out/In**
|:-------:|:--------|
| &check; | Clicking the youtube icone loads the youtube home page in a new tab
| &check; | Clicking the instagram icon loads the instagram home page in a new tab
| &check; | Clicking the facebook icon loads the facebook home page in a new tab
| &check; | Clicking the twitter icon loads the twitter home page in a new tab

| Status | **Home Page - User Logged Out**
|:-------:|:--------|
| &check; | That a Login and Signup button appear in the hero section
| &check; | Clicking the Login button in the hero section of the home page loads the login page
| &check; | Clicking the Signup button in the hero section of the home page loads the signup page


| Status | **Home Page - User Logged In**
|:-------:|:--------|
| &check; | That a Welcome text appears with the user's username in the hero section
| &check; | That an 'add reviews' and 'Your reviews' button appears below the welcome text
| &check; | That the 'Your reviews' button loads the user's reviews page


| Status | **Age range Page**
|:-------:|:--------|
| &check; | That the page reflects the age range chosen
| &check; | That they are approved books.
| &check; | That the book listing card shows the book image and an excerpt of the book blurb


| Status | **Log In Page - User Logged Out**
|:-------:|:--------|
| &check; | Clicking the sign up link above the user input loads the sign up page
| &check; | That the username input field is required
| &check; | That the password input field is required
| &check; | That if the username does not match the password the user cannot log in and user feedback is provided
| &check; | That if the correct credentials are given the user is logged in when the log in button is clicked
| &check; | That when the user is logged in they are redirected to the the home page and an alert message informs the user that they logged in successfully
| &check; |That when the user is logged in successfully their username will appear in the navbar indicating their logged in status

| Status | **Log In Page - User Logged In**
|:-------:|:--------|
| &check; | That the user cannot access the login tab from the navbar if they have logged in

| Status | **Sign Up Page - User Logged Out**
|:-------:|:--------|
| &check; | Clicking the log in link above the user input loads the log in page
| &check; | That the username input field is required
| &check; | That both password input fields is a required field
| &check; | That if you provide a username and password that is too similiar that the user cannot sign up and user feedback is provided
| &check; | That if your password doesn't match in both password fields, the user cannot sign up and user feedback is provided
| &check; | That if the user provides a password less that 8 character, the user cannot sign up and user feedback is provided
| &check; | That if you provide a good username and password but the email field does not contain a proper email address, the user cannot sign up and user feedback is given
| &check; | That the email input field is optional
| &check; | Clicking the Sign Up button signs the user up and logs the user in if the correct user information was provided for sign up
| &check; |That when the user signs up, they are redirected to the home page and an alert message informs the user that they sisgned up successfully
| &check; |That when the user signs up and is logged in successfully their username will appear in the navbar indicating their logged in status

| Status | **Sign Up Page - User Logged In**
|:-------:|:--------|
| &check; | That the user cannot access the signup tab from the navbar if they have logged in

| Status | **Log Out Page - User Logged Out**
|:-------:|:--------|
| &check; | That the user cannot access the log out tab from the navbar if they have logged out

| Status | **Log Out Page - User Logged In**
|:-------:|:--------|
| &check; | Clicking the logout button logs the user out
| &check; | When the user logs out they are redirected to the home page and a message alerts the user that they have logged out
| &check; | Once the user logs out the username in the navbar is removed

| Status | **Add a review - User Logged In**
|:-------:|:--------|
| &check; | That the Title input field is required
| &check; | That the Book Author field is required
| &check; | That the Age Range field is required
| &check; | That the Genre Range field is required
| &check; | That the Book Blurb field is required
| &check; | That the review field is required
| &check; | That the form cannot be submitted without all the required fields and user feedback is given if a user forgets a  required field
| &check; | That none of the input fields accept empty fields
| &check; | That none of the fields accept just spaces in an input field
| &check; | That when the form is submitted a book slug is automatically created from the title and book author input fields in the form
| &check; | That when the book is added, the user is redirected back to the 'Your Reviews page and a message alert informs the user that they successfully added a book and it's waiting for approval
| &check; | That when a book is added it is automatically set as unapproved (False) until changed otherwise (to True) by an admin

| Status | **User Edit Review Page - User Logged Out**
|:-------:|:--------|
| &check; | That if the user tries to access the edit review url they recieve a warning.

| Status | **User Edit Review Page - User Logged In**
|:-------:|:--------|
| &check; | That the user can see the book title of the review they are updating
| &check; | That the user can see their username name in the posting as section
| &check; | That the user can see the review input field is already prepoulated with the review as it currently is
| &check; | That review input field is required and cannot be submitted empty or with just spaces
| &check; | Clicking Update Review, updates the review, changes the status of the approval to False again, and redirects the user back to the My Books page
| &check; | That the an alert message informs the user that their review has been updated and is flagged for approval


| Status | **User Delete Review Page - User Logged Out**
|:-------:|:--------|
| &check; | That if the user tries to access the delete review url that they will receive a error message.

| Status | **User Delete Review Page - User Logged In**
|:-------:|:--------|
| &check; | That the user can see the book title and review details of the the review they would like to delete
| &check; | Clicking the Delete button redirects back to the My Books page
| &check; | That an alert message informs the user that they successfully deleted their review
| &check; | That the review is completely deleted and doesnt show up in the database or subsequently any place on the website


| Status | **Contact Page- User Logged Out/In**
|:-------:|:--------|
| &check; | That First Name input field is required
| &check; | That Last Name input field is required
| &check; | That Email input field is required
| &check; | That Message input field is required
| &check; | That none of the fields can be submitted blank
| &check; | That the email field only accepts proper email syntax (@ symbol has to be present)
| &check; | That none of the fields can accept just blank spaces
| &check; | That user feedback is provided if none of the required criteria to sub,it the form are met
| &check; | Clicking the Send button sends the email to the Dummy Email account set up via EmailJS, that the user is redirected to the contact page.
| &check; | That an alert message informs the user that their message was sent successfully upon the user sending the message

##Bugs

![env.py deleting](/the_happy_reader/Docs/Going%20back%20to%20old%20repo.png)

I tried to open a new workspace by and then deleted the old workspaces which caused my env.py not to appear on my new workspace. I created an new env.py and it fixed the issue but by fixing it i lost of the work i had done.

# Initial deployemnt
* I origionally had an issue delpoying to Heroku. It was due to the word Gunicorn being spelt incorrectly in the proc file.
[Error with procfile](/the_happy_reader/Docs/heroku%20deployment%20error%206-12.png)

# Error when deleting table from database
 
![delete from database](/the_happy_reader/Docs/Error%20when%20i%20delete%20the%20table%20from%20the%20database.png)

* Migration had to be reversed and information deleted from that table before table could sucessfully be deleted. I deleted this table for the following reasons:
     * I had no plans to use the infromation from the model.
     * It ment that users could add reviews from authors that havent previously been added by me.

# Sticky footer.
* The footer would cover the submit button in the 'add review' page making it impossible for the user to submit their form.

* Fix- ![body css](/the_happy_reader/Docs/footer%20fix.png)
       ![footer css](/the_happy_reader/Docs/footer%20fix1.png)
By adding a height of 60px on the footer and adding a margin bottom of 60px on the body it ensures that there was enough room at the bottom of the pages for buttons.

# Add a review form had a drop down for review author. 
This bug allowed others to create a review in others name.

* Fix - ![view code to approve author of review](/the_happy_reader/Docs/author%20fix.png)
The highlighted code allows the review author to be omitted from the 'add review form' and the field.

# Heroku deployment issues.

![H10 heroku bug](/the_happy_reader/Docs/heroku%20bug.png)

* Fix
    * Removed the Data Collection Config Var in the Heroku website.
    * Added a os.environ in the env.py file for DEV
      ![env.py file](/the_happy_reader/Docs/environ.png)
    * Change the Debug to equal Dev in the settings file
      ![settings](/the_happy_reader/Docs/settings.png)






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
* [Scroll button](https://www.w3schools.com/)
* []()
* [Pexcel](https://www.pexels.com/)
* []()
* []()

[Back to top](<#contents>)

# Acknowledgements

This website was designed and developed in conjunction with the Full Stack Software Developer Diploma course (eccommerce) at the Code Institute. I would like to thank my family, my cohort facilitator, the members of our cohort, the Slack community and Code Institute for all their support.


[Back to top](<#contents>)


