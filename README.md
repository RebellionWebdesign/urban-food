![urban-food-readme-header](docs/images/readme-images/urban-food-readme-header.png)

## TABLE OF CONTENTS

## OVERVIEW

This project is designed to enable a fictive restaurant to manage table bookings easily. The users are given the ability to create a booking, write a review or to delete their user accounts or their reviews all together. <u>Staff members are given the possibility to review and cancel bookings after the client has contacted the restaurant for a cancellation.</u> <u>This is a business decision so users dont juggle around with booked tables without the restaurant oner knowing.</u> The site was developed using Django, HTML. CSS and JavaScript.

## UX

### PROJECT GOAL

Create a website for the fictive Urban Food restaurant which useful for the users and the site owner as well.

### PROJECT OBJECTIVES

- Create a simple and intuitive user experience
- Add relevant content for the website
- Differentiate between user and staff accounts
- make the website available and functional across multiple different devices

### SCOPE

#### DELIVER A SIMPLE AND INTUITIVE UX

- Ensure the navigation is available and recognizable as such
- Ensure the pages on the website are named appropriately so the user understands how to use them
- Ensure visual feedback so users know what happens when it happens
- Design the website according to the restaurants color scheme

#### RELEVANT CONTENT

- Ensure that the purpose of the website is visible on the frontpage
- Ensure that the restaurants´ information is visible on the frontpage
- Ensure that user reviews are visible on the frontpage

#### FEATURES

- Register on the website using email and password
- Make CRUD available for:
  - The user profile data
  - The user reviews data
  - The user bookings data
  - The site owner
  - The staff members


#### DISTINCTION BETWEEN ACCOUNTS

- Enable users to add, edit and delete their own reviews on the restaurant
- Enable users to add, change and delete their own user data
- Enable users to add their own bookings

------

- Enable the website owner to view all data from the admin area

------

- Enable staff members to view bookings and cancel them (either from admin or from a custom page)

#### RESPONSIVENESS

- Enable responsiveness for Desktop, Tablets and Phones

### STRUCTURE

### SKELETON

#### Wireframes

Wireframes can be accessed in the [docs folder](https://github.com/RebellionWebdesign/urban-food/tree/a952f5ba09719a2e3fe9fb40b3c961918578334b/docs)

### DATABASE
The Urban Food project uses a postgresql database for data storage. This is the final schema:

<details>
  <summary>The Urban Food Database</summary>
<img src="docs/ERD/urban-food-final-erd-1.png" ><br>
</details>

### SURFACE

#### COLOR SCHEME

The chosen color scheme is simple but intuitive for a fast food restaurant. The main color chosen is red because it stands for energy and dynamics.

<details>
  <summary>Color Scheme</summary>
<img src="docs/images/readme-images/color-scheme.png" ><br>
</details>

#### FONTS

The fonts used on this website are [Poppins](https://fonts.google.com/specimen/Poppins?query=poppins) and [Gabarito](https://fonts.google.com/specimen/Gabarito?query=gabarito) provided by Google Fonts

<details>
  <summary>Gabarito Google Font</summary>
<img src="docs/images/readme-images/gabarito-font.png" ><br>
</details>

<details>
  <summary>Poppins Google Font</summary>
<img src="docs/images/readme-images/poppins-font.png" ><br>
</details>
#### VISUAL EFFECTS

Visual effects are sparsingly used in this project. However, there are some:

## AGILE METHODOLOGY

## FEATURES

### EXISTING FEATURES

- Register to the website using email and password
- Log in to the website using email and password
- Users can create a profile, edit the data and delete the profile
- Users can create reviews, edit the reviews and delete the reviews
- Users can create bookings, but not delete or edit them. This is a business decision (see overview for details)
- Admin can do all of the above

### FUTURE FEATURE CONSIDERATIONS

## TOOLS USED

### VSCODE EXTENSIONS

- To ensure that the django templates are formatted correctly, the following [VSCode](https://code.visualstudio.com/) extension was used:
    - [djlint-vscode](https://marketplace.visualstudio.com/items?itemName=monosans.djlint)

### PYTHON PACKAGES

- To further ensure that the [djlint-vscode](https://marketplace.visualstudio.com/items?itemName=monosans.djlint) extension also works, the following
  Python package was used: 
    - [djlint](https://pypi.org/project/djlint/)

- Other packages used - only the main ones installed with `pip install` are listed:
 - [Django v3.2.22](https://pypi.org/project/Django/) please install it with `pip install 'django<4'`
 - [gunicorn](https://pypi.org/project/gunicorn/)
 - [dj_database_url v0.5.0](https://pypi.org/project/dj-database-url/) please install it with `dj_database_url==0.5.0`
 - [psycopg2 v2.9.9](https://pypi.org/project/psycopg2/)
 - [allauth v0.57.0](https://pypi.org/project/django-allauth/)
 - [dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/)
 - [django-summernote](https://pypi.org/project/django-summernote/)

## TESTING

## DEPLOYMENT

### DEPLOY ON HEROKU

### FORK THE REPOSITORY

### CLONE THE REPOSITORY

## CREDITS

### CONTENT

- The profile pictures for the fictive users were taken from [RandomUser](https://randomuser.me/photos)
- The hardcoded images on the home page refer to cloudinary, but were shortened with [ShortUrl](https://www.shorturl.at/shortener.php)
- The hero image and the team image on the front page are generated with [MidJourney AI](https://www.midjourney.com/home)
- Some of the reviews were submitted by friends and family.

## ACKNOWLEDGEMENTS