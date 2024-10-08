# The Stave
The Stave is a musical instrument webstore with a speciality in classical music instruments.\
Instruments are grouped into their respective families; Strings, Woodwind, Brass, Percussion and Keyboards.\
Users of the webstore are able to create a profile to fill in personal informaiton to make purchasing easier and see their order history.\
A special part of the webstore is dedicated to the auction of antiques and special instruments.\
The store also offers the services of rental of instruments and a notice board for lessons.\
This project was created to meet the criteria of the Code Institute Milestone Project 4.

![AmIResponsive Screenshot](media/readme/amiresponsive.png)

View Repository in GitHub Pages:\
https://github.com/mparker-landt/Milestone_Project_4

View Website Link:\
TBC

Author: Marcus Parker\
Github: [mparker-landt](https://github.com/mparker-landt)

## Table of Contents
+ [UX](#ux "UX")
  + [User Demographic](#user-demographic "User Demographic")
  + [User Stories](#user-stories "User Stories")
    + [First time Visitor Goals](#first-time-visitor-goals "First time Visitor Goals")
    + [Returning Visitor Goals](#returning-visitor-goals "Returning Visitor Goals")
    + [Store Owner Goals](#store-owner-goals "Store Owner Goals")
  + [Design](#design "Design")
    + [Wireframes](#wireframes "Wireframes")
    + [Colour Scheme](#colour-scheme "Colour Scheme")
    + [Typography](#typography "Typography")
    + [Images](#images "Images")
+ [Features](#features "Features")
  + [Models](#models "Models")
  + [Functional Features](#functional-features "Functional Features")
    + [Static Pages](#static-pages "Static Pages")
    + [Store](#store "Store")
    + [Rentals](#rentals "Rentals")
    + [Auction](#auction "Auction")
    + [Enquiries](#enquiries "Enquiries")
    + [User Profile](#user-profile "User Profile")
    + [Superuser Features](#superuser-features "Superuser Features")
  + [Design Features](#design-features "Design Features")
    + [Header](#header "Header")
    + [Footer](#footer "Footer")
    + [Homepage](#homepage "Homepage")
    + [Static Pages](#static-pages "Static Pages")
    + [Contact Us Page](#contact-us-page "Contact Us Page")
    + [Store](#store "Store")
    + [Rentals](#rentals "Rentals")
    + [Auctions](#auctions "Auctions")
    + [Shopping Cart Page](#shopping-cart-page "Shopping Cart Page")
    + [Checkout Page](#checkout-page "Checkout Page")
    + [Checkout Success Page](#checkout-success-page "Checkout Success Page")
    + [User Profile Page](#user-profile-page "User Profile Page")
    + [User Profile Control Pages](#user-profile-control-pages "User Profile Control Pages")
    + [Error Pages](#error-pages "Error Pages")
  + [Future Features](#future-features "Future Features")
+ [Resources](#resources "Resources")
  + [Technologies](#technologies "Technologies")
  + [Django and Python Extra Packages](#django-and-python-extra-packages "Django and Python Extra Packages")
  + [External Resources](#external-resources "External Resources")
+ [Testing](#testing "Testing")
  + [Performance Testing](#performance-testing "Performance Testing")
  + [HTML Validator Testing](#html-validator-testing "HTML Validator Testing")
  + [CSS Validator Testing](#css-validator-testing "CSS Validator Testing")
  + [JS Testing](#js-testing "JS Testing")
  + [Python Testing](#python-testing "Python Testing")
+ [Development & Deployment](#development--deployment "Development & Deployment")
  + [Development](#development "Development")
  + [Deployment](#deployment "Deployment")
+ [Credits and Acknowledgements](#credits-and-acknowledgements "Credits and Acknowledgements")

## UX
### User Demographic

### User Stories
#### First time Visitor Goals:
- As a first-time visitor I want to be able to browse products.
- As a first-time visitor I want to be able to add products to the shopping cart.
- As a first-time visitor I want to be able to make a purchase without signing in.
- As a first-time visitor I want to be able to make an account and fill in personal information.

#### Returning Visitor Goals:
- As a returning user I want to login to my account with a username and password.
- As a returning user I want to be able to edit my account information.
- As a returning user I want to be able to browse products.
- As a returning user I want to be able to add products to the shopping cart.
- As a returning user I want to be able to make a purchase with my information auto filled.
- As a returning user I want to be able to view my purchase order history.

#### Store Owner Goals:
- As a store owner I want to login to my account with a username and password.
- As a store owner I want to be able to add new products.
- As a store owner I want to be able to edit and delete existing products.

### Design
#### Wireframes
Wireframes were drawn on paper as a rough draft and then made in [Draw.io](https://www.drawio.com/) digitally.\
Homepage:\
![Wireframes - Homepage](media/readme/wireframes-homepage.png)\
Static:\
![Wireframes - Static Pages](media/readme/wireframes-staticpage.png)\
Store:\
![Wireframes - Store](media/readme/wireframes-store.png)\
Product Details:\
![Wireframes - Product Details](media/readme/wireframes-details.png)\
User Profile:\
![Wireframes - User Profile](media/readme/wireframes-profile.png)\
Contact:\
![Wireframes - Contact Us](media/readme/wireframes-contact.png)

#### Colour Scheme
For the colour scheme [Coolors](https://coolors.co) was used to generate different schemes and then one was chosen.
- <span style="color:#38182F;font-weight:bold;">#38182F</span>
- <span style="color:#2F394D;font-weight:bold;">#2F394D</span>
- <span style="color:#56666B;font-weight:bold;">#56666B</span>
- <span style="color:#BB4430;font-weight:bold;">#BB4430</span>
- <span style="color:#EEE1B3;font-weight:bold;">#EEE1B3</span>

#### Typography
For the colour scheme [Google Fonts](https://fonts.google.com/) was used to source different fonts for the body and header titles.

#### Images
Images were sourced from TBC and TBC. These are freestock and licensed to use in a non-commercial setting.
Icons for the website were acquired from [Boxicons](https://boxicons.com) and [Flaticon](https://www.flaticon.com)

## Features
### Models
The available models are available on the site split into their respective apps.
* Checkout
  - Order
  - OrderLineItem
* Home
  - Enquiry
* Profiles
  - UserProfile
* Store
  - Category
  - Product
  - Auction
  - Rentals

### Functional Features
#### Static Pages
There are numerous static pages on the site such as Homepage, FAQ, Policies etc. These are to provide links to the main sections of the website and provide any information that a user may have.
In the footer social account links can also be navigated to which would link to the stores social accounts.

#### Store
The main store hosts all the products for the website. For each product a card displays the critical information at a glance.
The products can be filtered by either a search bar or a sort box. 
For more information about a product a user can click the card to navigate to the projects detaisl webpage. On this page some more specific information is displayed about the product as well as the ability to add the product to the shopping cart.

#### Rentals
Similar to the main store the Rentals page displays the available products to rent in a grid of cards with critical information.
Products again can be filtered by search bar or sort box input.
Rental Cards can be clicked to go to the Rental Product details page where a user can select how long they need to rent and product and add it to their shopping cart.

#### Auction
On the Auction page users can search user added products as well as add their own. Cards with auction information are displayed and can be filtered via a search bar or sort box.
In the Auction Product details page more details about the product can be found. If a user is logged in and not the user that added the product they can make a bid for the product. When the product period comes to an end the product is added to the bidders shopping cart.
The user who added the Auction Product can edit/delete their product as well as the websites admin.

#### Enquiries
Enquiries can be made by filling in the contact information page. The enquiry is given a subject and message as well as the users details for contact. Enquiries can be viewed by the admins via a dropdown in the navbar which is only visible to them.

#### User Profile
Users can buy products without the need to login but can register and login to their account to make accessing the site simpler.
Profile information can be filled in to make ordering quicker and user order history can be viewed.
Logging into an account also allows a user to make an Auction Product or make a bid on an Auction Product.

#### Superuser features
Superusers or site admins have some extra features to manage the webapp. Main Store Products and Rental Products can be added/edited or deleted. Enquiries made by users of the website can be viewed on an Enquiries page.
The admins also have the ability to access the Django admin page where the information can also be viewed or edited.

### Design Features
#### Header
The Header for the site contains links to the Store, Rental and Auction Product pages and Enquiry page.
A subbar contains icon links to a User Profile with dropdown options or Shopping Cart page.
On mobile the header collapses to to dropdowns, one for the pages and one for the User Profile and Shopping Cart.\
![Design - Header Website](media/readme/design-header.png)\

#### Footer
The Footer mirrors the Header and contains links to all of the website static pages as well as the Product pages and Enquiry Page.
A subbar contains social media links which open the social media websites in a new page.\
![Design - Footer](media/readme/design-footer.png)

#### Homepage
The homepage is used as a landing page where users can quickly navigate to most of the sites main attractions or information. The page is split into sections to allow for the user to navigate whilst being visually appealing.
At the bottom of the page User Reviews are displayed in a carousel to attract positive attention to the site.\

#### Static Pages
The About Us, FAQ, Privacy Policy and Warranty Policy are all stylised in the same manner where the information is displayed simply yet effectively between the header and footer. External links referenced on the pages navigate to other parts of the site.\
![Design - About Us](media/readme/design-static-about.png)\
![Design - FAQ](media/readme/design-static-faq.png)\
![Design - Cookie Policy](media/readme/design-static-cookies.png)\
![Design - Privacy Policy](media/readme/design-static-privacy.png)

#### Contact Us Page
The Enquries page contains information about making an enquiry and a form to submit information. Mandatory information is displayed via an asterisk and the subject of the enquiry can be chosend via a Dropdown box with the options.
All Enquiries can be viewed by a logged in admin user on a specific enquiries page.\
![Design - Enquiry Page](media/readme/design-enquiry.png)\
![Design - Enquiries Page](media/readme/design-enquiries.png)

#### Store
The Main Products Store page displays the available products in a grid pattern of cards with critical information for each product displayed to the user at a glance.
At the top of the page information for the page is displayed with a searchbox and dropdown selection box to filter the products. If a admin is logged in this is where the ability to edit or delete a product is displayed.
In the Product details page  specific product information is displayed and buttons to either return to the store main page or add the product to the shopping cart.\
![Design - Store](media/readme/design-store.png)\
![Design - Store Details](media/readme/design-store-details.png)\
![Design - Store Add](media/readme/design-store-add.png)

#### Rentals
The Main Rentals Store page displays the available rental products in a grid pattern of cards with critical information for each rental product displayed to the user at a glance.
At the top of the page information for the page is displayed with a searchbox and dropdown selection box to filter the rental products. If a admin is logged in this is where the ability to edit or delete a product is displayed.
In the Rental Product details page specific rental product information is displayed, a datebox is displayed to choose the rental period and buttons to either return to the store main page or add the product to the shopping cart.\

#### Auctions
The Main Auction Store page displays the available auctio products in a grid pattern of cards with critical information for each auction product displayed to the user at a glance.
At the top of the page information for the page is displayed with a searchbox and dropdown selection box to filter the auction products. A button is displayed to a user to add a product if the user is logged in.
If a admin is logged in this is where the ability to edit or delete a product is displayed. If a user is logged in who added the product a edit/delete for their added products is also displayed.
In the Auction Product details page specific auction product information is displayed, a textbox to enter a price and buttons to either return to the store main page or submit their bid for the product.\
![Design - Auction](media/readme/design-auction.png)\
![Design - Auction Details](media/readme/design-auction-details.png)\
![Design - Auction Add](media/readme/design-auction-add.png)

#### Shopping Cart Page
The Shopping Cart page displays either the products added to the Shopping Cart or that the Shopping Cart is empty. Main Products, Rental Products and Auction Products are displayed here if available to purchase.
The ability to return to the website or navigate to a checkout are displayed at the bottom of the page.\
![Design - Shopping Cart](media/readme/design-cart.png)

#### Checkout Page
When a purchase is to be made the Checkout page displays a form for users to add their Billing, Shipping and Card Information.\
![Design - Checkout](media/readme/design-checkout.png)

#### Checkout Success Page
If purchased successfully a Checkout Success Page is displayed with information to summarise the order. A link to navigate to the website is displayed.\
![Design - Checkout Success](media/readme/design-checkout-success.png)

#### User Profile Page
The User Profile dropdown displays the navigation to the User Profile page or the ability to logout. If a user is an admin links to add a main product or rental product are also displayed as well as the ability to navigate to an Enquiries page to see all available enquiries.\
![Design - User Profile](media/readme/design-profile.png)

#### User Profile Control Pages
The Register, Login and Logout pages are displayed as simply as possible whilst keeping the visual aspect of the website. Information is kept to a minimum and presented in a simple form manner.\
![Design - Register](media/readme/design-register.png)\
![Design - login](media/readme/design-login.png)\
![Design - Logout](media/readme/design-logout.png)

#### Error Pages
If the user hits an error Error Pages are displayed explaining the particular error and an image. The user can navigate back to anywhere on the site by using the header and footer which are still available.\

### Future Features

## Resources
### Technologies
- [HTML](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JS](https://en.wikipedia.org/wiki/JavaScript)
- [Jquery](https://jquery.com)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

### Django and Python Extra Packages
- python-dotenv - Used to access the project environments file used to store sensitive variables
- allauth - Package that manages aspects of a User Profile such as login, logout, register etc
- pillow - Provides file format support and image processing capabilities
- django-countries - Package that contains information and details for every country
- django-crispy-forms - Bootstrap package to make forms more visually appealing
- stripe - Payment service that allows payments to be made on the site and can send info about the payment via webhooks 
- dj_database_url - Utility to allow the 12factor database environmental variable to configure Django
- psycopg2 - PostgreSQL database adapter for Python
- gunicorn - Python Web Server Gateway Interface Server
- whitenoise - Middleware that transforms how Django handles static files
- django-silk - Utility to handle live profiling and inspection of a Django project
- boto3 - Python API to access AWS services
- django-storages - Collection of custom storage backends for Django 

### External Resources
- [Font Awesome](https://fontawesome.com/) - Used to acquire icons for the project.
- [Draw.io](https://www.drawio.com/) - Used to create the wireframes for the project.
- [Stripe](https://stripe.com/gb) - Service that manages and makes payments successful for the project.
- [AWS](https://aws.amazon.com) - Storage services used to store media.
- [Code Institute](https://learn.codeinstitute.net) - Development course website used for example project as base for ideas.
- [Juliana Bicycles](https://www.julianabicycles.com) - Real webstore used a base idea and template for the project design.
- [Boxicons](https://boxicons.com) - Used to acquire icons for the project.
- [Flaticon](https://www.flaticon.com) - Used to acquire icons for the project
- [Coolors](https://coolors.co) - Used to generate a colour palette for the project.
- [Google Fonts](https://fonts.google.com) - Utility to browse and source fonts.
- [Freepik](https://www.freepik.com/) - Error Page images
- [PureCss](https://purecss.io) - Module that offers minimal CSS classes to improve the look of the website.
- [SwiperJS](https://swiperjs.com) - Library used for carousels in the project.
- [Toastr](https://github.com/CodeSeven/toastr) - Library used for toast notifications on the website.

## Testing

### Performance Testing
The website performance was tested using Google Chrome Developer Tools Lighthouse feature.\
This tested the Performance, Best Practices, SEO and Accessibility of the website.

### HTML Validator Testing
https://validator.w3.org/

### CSS Validator Testing
https://jigsaw.w3.org/css-validator\

### JS Testing
https://jshint.com\
Due to the JavaScript file being extremely simple there were no errors in jshint. The warnings visable were due to jquery being used and could be ignored.\

### Python Testing
Python PEP8 standards were tested by installing the extension Pylint. This allowed for the easy visualisation of errors and warnings when working on the code.\
Although not all warnings were got rid of the ones left were suggestions or Pylint not working fully as expected. \

## Development & Deployment
### Development
Development was carried out using VS Code for code writing and Sourcetree for accessing version control.
The built-in VS Code terminal was used to add packages and run commands.

To setup the environment:
- In VS Code create a new project
- Run the command "python -m venv .venv" to create virtual environment
- Use the setting Python: Select Interpreter and choose python version
- Navigate to the .venv/Scripts directory and activate
- Run the command "python -m pip install django" to install the latest version of Django
- Run the command "Django-admin startproject {NAME}" to start a new Django project where {NAME} is the name of the project .
- Run "python manage.py migrate" to start the local database
- Run "Python mange.py createsuperuser" and go through the settings to create a admin
- Run "python manage.py runserver" and navigate to the URL

- In Github create a new repository with the same name as the project
- Clone the repository in Sourcetree to the existing Django project
- In Sourcetree press commit changes, add a description and then push the changes to Github
- For every major change that needs saving the changes can then be committed and pushed

- To create an app in the project run the command "python manage.py startapp {NAME}"
- The app files can then be modified to add tables to the database, HTML templates, forms etc
- If a model is added the commands "python manage.py makemigrations" and ""python manage.py migrate"" need to be run to push to the database
- To add the app to the project the settings need to be modified for the whole project in {NAME}/settings.py

### Deployment
- Github
- Heroku
- AWS

## Credits and Acknowledgements
With special thanks to:
- Lauren-Nicole Popich - Mentor from the Code Institute who provided help throughout the project and was always available for support.
