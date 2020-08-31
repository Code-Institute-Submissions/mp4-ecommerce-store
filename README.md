# Shannon Gaels 

The Shannon Gaels Django app 
 
## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

####As a user, I want to browse and search for dessert recipes.

####As a user, I would like to see potential allergens in the recipes.

####As a registered user, I would like to submit my own recipes for others to see

####As a registered user, I would like to be able to edit my recipes and delete if necessary

####As a user, I would like to be able to find equipment I might want to purchase related to the recipes


Please use the following link to access the Figma Wireframe for Just Desserts - https://www.figma.com/file/pcRVh2MevzPhD7HzAyDv5l/Recipe-Site?node-id=0%3A1

## Features


 
### Existing Features
- REGISTRATION - allows users create profiles, by having them fill out a registration form
-- By registering, logged-in users can access news and fixtures relating to the club
- LOGIN - allows previously registered users to log back in
- SHOP - allows users to view and purchase club gear securely through Stripe
- CLUBNEWS - a news section for match reports and club related news


In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Images on fixtures and news posts - currently not loading and due to time constraints, not implemented yet. 
The website is going to be used by the local GAA club so thisfeature will be added shortly. 
- Google Maps location data for club facilities to be added and a hyperlink to Google Maps app. 
- Link the existing fundraising activities to the Django app. Particularly the 404020.ie draw but also future endeavours

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Bootstrap]  (https://getbootstrap.com/)
    - The project uses **Bootstrap** for styling and layout.
- [Django](https://www.djangoproject.com/)
    
- [MongoDB] https://www.mongodb.com/)
    - The project uses **MongoDB** for creating, reading, updating and deleting data from a database.
- [Heroku]  (https://Heroku.com/)
    - The project uses **Heroku** for deploying and hosting the app.
- [Python] (https://python.org)
- [AWS] (https://aws.amazon.com/s3/)
    - **AWS S3 Buckets** used for storing of media and static files


## Testing

#####As a user, I want to browse and search for dessert recipes.
Tested on Chrome, Edge and Firefox - working
#####As a user, I would like to see potential allergens in the recipes.
Tested on Chrome, Edge and Firefox - working
#####As a registered user, I would like to submit my own recipes for others to see

#####As a registered user, I would like to be able to edit my recipes and delete if necessary

#####As a user, I would like to be able to find equipment I might want to purchase related to the recipes
Tested on Chrome, Edge and Firefox - working

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Registration form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits
Base template based on Bootstrap template - ('https://getbootstrap.com/docs/4.5/getting-started/introduction/')
News & fixtures app - based on Codemy - Create A Simple Blog Youtube Playlist

### Content
- The text for the about page was copied from the old Shannon Gaels website - https://shannongaelsgaa.com/club-history/

### Media
- The photos used in this site were obtained from pexels.com

### Acknowledgements

- I received inspiration for this project from the existing Shannon Gaels page while the blue camoflauge overlay was inspired by 
the Brushed Nevis range of O'Neills clubwear - https://www.oneills.com/shannon-gaels-roscommon-nevis-brushed-crew-neck-meltmrn-bot-amb.html