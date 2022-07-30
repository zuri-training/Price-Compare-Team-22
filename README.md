# Team 22_Price Compare Project
# PriceZilla - A Price Comparison Platform


PriceZilla is a price comparison web app that allows users compare the prices of products across different retailers, stores, and brands. It takes the hassle of visiting various eCommerce store to find best deals. Consumers can benefit from this by comparing the prices of their favourite HOME EQUIPMENTS from different categories.



## Table of Content

- General Information

- Live Site

- Technologies Used

- Architecture

- Prerequisites

- Features

- How to Use PriceZilla

- Contributing

- Contributors

- Acknowledgements

- Author



## General Information


PriceZilla allow users to compare prices and analyze options side by side within the niche of HOME EQUIPMENTS across various categories. The minimum and maximum prices of the products are then displayed for users.

PriceZilla solves the problem of helping users make a well-informed decision on the most cost-effective choice within their overall budget and on any specific features.


By having these products all in one location (PriceZilla), our target audience may also save time by avoiding the need to browse through multiple eCommerce platforms just to get the best pricing offers that fit their needs.




## Live Site

Coming Soon....


## Technologies Used

- ### Product Designers

Tool: 

Figma for UI designs. FigJam for UX designs.


- ### Frontend Developers

Languages: 
HTML, CSS, JAVASCRIPT. These languages were used to structure, style, and let users interact with the UI of the platform.

Framework: BootStrap version 5. This CSS framework was used to create a responsive web app. 

- ### Backend Developers

Language: Python

Framework: Django

Concept: Web Scraping

Library: Beautiful Soup



## Architecture



The entire project is built on Django, a high-level python web framework for rapid development and clean design. 

PriceZilla uses the concept of Web scraping to obtain a large amount of data from various eCommerce stores. The data obtained data will be converted into structured data with the help of a python library, Beautiful Soup, and this relevant information will be extracted. To connect the frontend and backend, Django REST framework, a python tool will be used to build a web API. This API will listen for requests from the Front-end, run the logic in the backend, query the database where necessary, and return a response


## Prerequisites

- You will need the following technologies installed to get the service running:

- A compatible broswer

- An IDE

- Python app

- GIT

## Installation Guide
- Clone the repo
- Open command prompt and type git clone https://github.com/zuri-training/Price-Compare-Team-22.git

- Open the folder you just cloned using your IDE and open the terminal window.
- To set up your virtual environment type, python -m venv env

- To activate virtual environment: env\Scripts\activate
- Install dependencies : pip install -r requirements.txt

 You're all set!





## How to Use PriceZilla


- Visit the platform using the live link

- Browse through various products.

- Register to access more features.

- Create and personalize profile.


- Use the search area to find your desired products.


- See full product listings and information.

- Compare prices and products.

- Place order on your preferred product on the original retailer website. 

- Leave product and store reviews after.


## User Stories 
- A user can compare the prices of products faster
- A user has variety of options to choose from before making a purchase


## Features

#### Unauthenticated Users

- Home Page
    Users can view basic information about the platform. These information includes: What We Do, Best Selling Products, Promo Deals, Navigation Menus.
    
 - Navigation Bar
    Users can navigate the site and move from one page accessible to them to another. Pages includes: About Page, 
    
 - Search
     Users can search for products by typing the ‌keyword in the search bar. However, they are limited to viewing products in a category.
    
  - Categories
      Users can only view products in one category across THREE different retailers.
      
  - Call To Action (CTA)
       Users will be receive prompts to take certain initiative and become a registered member. These features include: A prompt to register and become authenticated. Newsletter Opt-in
       
   - Footer: Pages include: Contact Page, Social Media Proof, Terms and Conditions, Support, Privacy and FAQ.


#### Authenticated Users

- Navigation Bar
  Users who did not save login information will have to sign in using the email and password method.
  
- Search and Filters
    Users can search for their preferred item across all categories and can narrow the search to their specific need.
    
 - Product page
    Users have access to view all categories, listings, best selling products and promo deals.
  
  - User Area
     Users can edit profile, save search and browsing history, save to and remove products from wishlist.
    
  - Reviews
     Users can leave store and product reviews. They can also check reviews made by others.
     
   - Price Comparison
     Users can compare prices of products.
     
  - To make a purchase, users are redirected to the original retailer where they can place orders.





## Contributing

Contributions are always welcome!

- #### Fork the project repository

Find the project's repository on GitHub, and then "fork" it by clicking the Fork button in the upper right corner.

- #### Clone your fork
While still in your repository, click the green Clone or download button and then copy the HTTPS URL.

Using Git on your local machine, clone your fork using the URL you just copied: git clone URL_OF_FORK.


- #### Add the project repository as the "upstream" remote

Add the project repository as the "upstream" remote using: git remote add upstream URL_OF_PROJECT.

Use git remote -v to check that you now have two remotes: an origin that points to your fork, and an upstream that points to the project repository.

- #### Pull the latest changes from upstream into your local repository

Use git pull upstream master to "pull" any changes from the "master" branch of the "upstream" into your local repository. (If the project repository uses "main" instead of "master" for its default branch, then you would use git pull upstream main instead.)


- #### Create a new branch

Use git checkout -b BRANCH_NAME to create a new branch and then immediately switch to it. The name of the branch should briefly describe what you are working on, and should not contain any spaces.

- #### Make changes in your local repository 
Using an text editor or IDE.


- #### Commit your changes
After you make a set of changes, use git add -A to stage your changes and git commit -m "DESCRIPTION OF CHANGES" to commit them.


- #### Push your changes to your fork

Upload these changes to your fork using git push origin BRANCH_NAME. This "pushes" your changes to the "BRANCH_NAME" branch of the "origin" (which is your fork on GitHub).

- #### Begin the pull request



Return to your fork on GitHub, and refresh the page. Click the green Compare & pull request button to begin the pull request. Alternatively, you can switch to your branch using the Branch button and then click the New pull request button.  


- #### Create the pull request


Below the pull request form, you will see a list of the commits you made in your branch, as well as the "diffs" for all of the files you changed.

If everything looks good, click the green Create pull request button!

- #### Synchronize your fork with the project repository

At this point, your fork is out of sync with the project repository's master branch.

To get it back in sync, you should first use Git to pull the latest changes from "upstream" (the project repository) into your local repository: git pull upstream master.

Then, push those changes from your local repository to the "origin" (your fork): git push origin master.


Congratulations
You have successfully made an contribution to our repository!!!





## Acknowledgements

Many thanks to the [Ingressive For Good and Zuri Team](https://training.zuri.team/) for the training and inspiring this project.


## Author

Debbie Jackson

- GitHub - [@debbiejackson14](https://github.com/debbiejackson14)



