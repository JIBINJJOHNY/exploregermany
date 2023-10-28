# Explore Deutschland
Live Version: [Explore Deutschland](https://exploregermany-c3b93e179fbb.herokuapp.com/)
![Explore Deutschland](documentation/homepage.png)
## About

The Explore Deutschland website is your gateway to discovering the hidden gems, rich history, and breathtaking landscapes of Germany. Designed for travelers, adventurers, and anyone with a passion for exploration, this website offers a comprehensive guide to Germany's most iconic and lesser-known tourist destinations.

## Key Features:
#### Tourist Places: 
Explore Deutschland's extensive database of tourist places across Germany, from historic landmarks to natural wonders. Detailed descriptions, photos, and ratings provide all the information you need to plan your next adventure.

#### State Profiles: 
 Dive deep into Germany's diverse states. Each state profile offers insights into its unique culture, traditions, and attractions, helping you tailor your journey to your interests.

#### User Reviews:
Hear from fellow travelers! Read and contribute user reviews and ratings to help others make informed decisions about their destinations.

#### Packages: 
 Plan your visit with curated packages that combine the best places to create an unforgettable experience.

 #### Booking:
 Ready to explore? Book packages and accommodations through the website with a straightforward booking system.

 #### User-Friendly Design:
 Our website's intuitive design ensures easy navigation and a seamless user experience.


## User Story: 

### First-Time Visitor

 As a First-Time Visitor to Explore Deutschland, I want to understand the website's purpose and quickly find information about popular tourist places in Germany.

1. Website Introduction:

 + Upon arriving at the website, I am greeted with an introduction that explains the website's purpose and how it can assist me in planning my trip to Germany.


2. Browsing Tourist Places:

+ I can easily browse a list of tourist places with create an account and login.

+ Each place includes a brief description,location map and captivating images to pique my interest.

3.Learning About States:
+ The website provides a section where I can learn about the different states in Germany, including their unique cultural and geographical features.

4. User Reviews and Ratings:
+ I can read user reviews and ratings to gain insights into the quality and popularity of each tourist place.
+ The option to leave my own reviews and ratings is available but not mandatory.

5. User-Friendly Navigation:
+ The website's navigation is intuitive, allowing me to easily access the information I need without getting lost.

### Travel Enthusiast

As a Travel Enthusiast and Regular Explorer, I want a feature-rich experience on Explore Deutschland to discover new places and plan my next adventure in Germany.

1. Advanced Tourist Place Search:

+ I can utilize advanced search filters to find specific tourist places based on criteria such as state, type, and user ratings.

2. Interactive Maps:

+ The website offers interactive maps that display the locations of tourist places.
+ I can use these maps to visualize and plan my travel itinerary.

3.Customizable Packages:

+ I can create personalized travel packages by selecting multiple tourist places.
+ The website calculates the package cost and provides options for customization.

4. Comprehensive State Profiles:

+ The state profiles offer in-depth information, history, and cultural insights to help me make informed travel decisions.

5. User Contributions and Community:

+ I can actively contribute to the website's community by adding my own reviews, photos, and recommendations.
+ Explore Deutschland fosters a sense of community among travelers. 

## Technologies used
- ### Languages:
    + [Python 3.9.13](https://www.python.org/downloads/release/python-3913/): the main language utilized to create the website's server side.
    + [JS](https://www.javascript.com/): the main language utilized to create the website's interactive elements.
    + [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): the markup language that was utilized to make the webpage.
    + [CSS](https://developer.mozilla.org/en-US/docs/Web/css): the language of styling that was applied to the website.

- ### Frameworks and libraries:
    + [Django](https://www.djangoproject.com/): This entire logic was created using a Python framework.
    + [jQuery](https://jquery.com/): was employed to send AJAX requests and manage click events.

- ### Databases:

    + [SQLite](https://www.sqlite.org/): served as a database for development.
    + [PostgreSQL](https://www.postgresql.org/): the database that contained all of the data.
    

- ### Other tools:

    + [Git](https://git-scm.com/): the version control system used to manage the code.
    + [Pip3](https://pypi.org/project/pip/): the dependencies were installed using the package manager.
    + [Gunicorn](https://gunicorn.org/): the webserver used to run the website.
    + [Spycopg2](https://www.python.org/dev/peps/pep-0249/): the database driver that established the database connection.
    + [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): the authentication library used to create the user accounts.
    + [Render](https://render.com/): the cloud computing system that houses the website.
    + [ElephantSQL](https://www.elephantsql.com/): the cloud database used to store all the data.
    + [GitHub](https://github.com/): used to store the source code for the website.
    + [VSCode](https://code.visualstudio.com/): the IDE used to develop the website.
    + [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
    + [Font Awesome](https://fontawesome.com/): was used in the creation of the website's icons.
    + [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
    + [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
    + [JShint](https://jshint.com/): was used to validate JS code for the website.
    + [PEP8](https://pep8.org/): was used to validate Python code for the website.

## Design
The Explore Deutschland travel website embodies a modern and user-centric design philosophy. With simplicity at its core, the website's minimalistic aesthetics and strategic use of white space create an uncluttered and visually engaging platform. Responsive design ensures a consistent experience across devices. Our purpose is to inspire and assist travelers in exploring Germany, making their journeys meaningful and memorable.


---
## Testing

Please refer to the [TESTING.md](TESTING.md) file for all test-related documentation.

---

## Information Architecture

### Database
* SQLite was used to create the database in the early phases of the project. Next, PostgreSQL was used to migrate the database.

### Data Modeling


1. **State Model**
The State model represents information about a state.

|Field Name      | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| Name      | name      | CharField     |  max_length=100,unique=True,  blank=False, null=False  |
|Description       | description       | TextField   | blank=False, null=False   |
| Image   | image   | CloudinaryField     | folder='state_images/', null=True, blank=True    |
| Alt Text    | alt     | CharField     | max_length=250, blank=True, null=True   |

2. **TouristPlace Model**
The TouristPlace model represents information about a tourist place.


| Field Name         | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| Name    | name      | CharField     | max_length=100, unique=True, blank=False, null=False   |
| Description        | description        | TextField    | blank=False, null=False    |
| Location   | location    | CharField     | max_length=100, blank=False, null=False    |
| State    | state    | ForeignKey     | to State, on_delete=models.CASCADE, blank=False, null=False    |
| Slug | slug        | SlugField   | max_length=150, unique=True, blank=False, null=False   |
| Google Map Src         | google_map_src       | CharField  | max_length=500, blank=True, null=True    |

3.**Tourist Place Image Model**
The TouristPlaceImage model represents images associated with a tourist place.


| Field Name         | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| Tourist Place   | touristplace     | ForeignKey    | to TouristPlace, on_delete=models.CASCADE, blank=False, null=False   |
| Image       | image        | CloudinaryField   | folder='touristplace_images', null=True, blank=True    |
| Alt Text   | alt_text    | CharField     | max_length=300, blank=True, null=True   |
| Default Image   | default_image   | BooleanField     | default=False   |
| Is Active | is_active       | BooleanField   | default=True   |
| Created At         | created_at       | DateTimeField | auto_now_add=True    |
| Updated At        | updated_at      | DateTimeField | auto_now=True    |


4.**Review Model**
The Review model represents reviews for tourist places.

| Field Name         | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| User | user    | ForeignKey    | to User, on_delete=models.CASCADE, blank=False, null=False   |
|Tourist Place     | tourist_place       | ForeignKey  | to TouristPlace, on_delete=models.CASCADE, blank=False, null=False   |
| Rating  | rating    | IntegerField    | choices=STAR_CHOICES, default=1 |
| Comment   | comment	   | TextField    | max_length=1000, blank=True, null=True  |
| Created At         | created_at       | DateTimeField | auto_now_add=True    |

```python
    STAR_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
```

5.**Package Model**
The Package model represents different travel packages for exploring tourist places.

| Field Name         | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| State | state    | ForeignKey    | to State, on_delete=models.CASCADE, blank=False, null=False   |
|Package Type    | package_type       | CharField  | max_length=10, choices=[('1', '1 Day'), ('2', '2 Days')], blank=False, null=False  |
| Price | price    | DecimalField    | max_digits=10, decimal_places=2, blank=False, null=False |
| Places Limit   | places_limit	   | IntegerField    | choices=PLACES_LIMIT_CHOICES, blank=False, null=False  |
|Tourist Places       | places     | ManyToManyField | to TouristPlace, blank=False, null=False
 |

+ get_places_limit_display(): A method to get the display value of the places limit based on the choices.
+ get_description(): A method that returns a description based on the package type.

6.**Booking Model**
The Booking model represents a booking made by a user.


| Field Name         | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| User | user    | ForeignKey    | to User, on_delete=models.CASCADE, blank=False, null=False   |
|Booking Date   | date      | DateField  | blank=False, null=False |
| Number of Guests | no_of_guests  | IntegerField   | validators=[MinValueValidator(1), MaxValueValidator(6)], default=1, blank=False, null=False |
| Package  | package	   | ForeignKey   | to Package, on_delete=models.CASCADE, blank=False, null=False |
|Booking Status    | status   |CharField | max_length=20, choices=STATUS_CHOICES, default='pending', blank=True, null=True|
|Payment Amount   | payment_amount  |CharField | max_digits=10, decimal_places=2, blank=True, null=True|
|Payment Method    | payment_method  |CharField| max_length=50, choices=PAYMENT_METHOD_CHOICES, blank=True|
|Contact Email   | contact_email |EmailField| blank=False, null=False| 
|Contact Phone   | contact_phone |CharField| max_length=15, blank=True| 
|Special Requests  | special_requests |TextField| blank=True| 


## Deployment


The app and associated resources were deployed as follows:

- **Application Deployment**: The site was deployed to [Heroku](https://www.heroku.com). 

- **Database Deployment**: The database is hosted on Heroku using PostgreSQL. Heroku provides a managed PostgreSQL database for this application.

For any documentation pertaining to deployment, please refer to the [DEPLOYMENT.md](DEPLOYMENT.md) file.

---

## Credits

- [GitHub](https://github.com/) for providing the design concept for the project.
- [Django](https://www.djangoproject.com/) for the framework.
- [Font awesome](https://fontawesome.com/) for the icons' free access.
- [Heroku](https://www.heroku.com) for hosting of website
- [jQuery](https://jquery.com/) for providing a range of tools to enhance the visual appeal of standard HTML code.
- [Postgresql](https://www.postgresql.org/)for providing a database.
- [birme](https://www.birme.net/): for providing free service to center and crop images.
- [googlefonts](https://fonts.google.com/) for providing free fonts.
- [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb/related?hl=en) for offering a free platform for testing the responsiveness of websites
- [GoFullPage](https://gofullpage.com/)  for allowing to create free full web page screenshots;
- [Favicon Generator](https://realfavicongenerator.net/) for providing a free platform to generate favicons.
- [Mihai-Constantin](https://codepen.io/Mihai-Constantin) for bootstrap footer design.

##  Images

#### States
[User login image](https://www.flaticon.com/free-icon/user_6017051) 
[Carousel 1](https://global.rutgers.edu/program-search/details/fu-best-freie-university-germany) 
[Carousel 2](https://www.aesu.com/blog/marvel-medieval-germany-romantic-road/) 
[Carousel 3](https://travelaway.me/beautiful-places-germany/) 
[Berlin](https://www.glint-berlin.de/en/rooftop-bars/)
[Thuringia](https://www.thueringen-entdecken.de/en/our-history)
[Rhineland-Palatinate](https://www.tsy.my/germany)
[North Rhine-Westphalia](https://www.tripsavvy.com/best-free-things-to-do-in-cologne-1520220)
[Bavaria](https://www.planetware.com/tourist-attractions-/bavaria-state-d-ba-ba.htm)
[Baden-Württemberg](https://www.getyourguide.com/heidelberg-l24/)
[Hessen](https://tourscanner.com/blog/things-to-do-in-frankfurt/)
[Bremen](https://www.bremen.eu/tourism/sights/bremen-town-musicians)
[Brandenburg](https://www.lonelyplanet.com/germany/around-berlin)
#### Tourist Places
[Berlin Cathedral](https://www.getyourguide.com/berlin-cathedral-l3097/)
[Berlin Cathedral](https://www.croisieurope.co.uk/news/croisimag-april-2023)
[Berlin Cathedral](https://www.photohound.co/country/germany/images)
[Berlin Cathedral](https://www.flickr.com/photos/grahamcsmith/6250668673)
[Berlin Cathedral](https://www.flickr.com/photos/smileymanwithahat/14318483660)
[Berline Fernsehturm ](https://motelplus-berlin.de/experience-berlin/)
[Brandenburg Gate](https://prussianhistory.com/5-prussian-historical-landmarks-to-visit/)
[Berlinwall Memorial](https://www.stripes.com/migration/thirty-years-after-its-fall-berlin-wall-memorial-is-a-chilling-reminder-of-the-past-1.605502)
[Reichstag Building](https://www.history.ac.uk/library/collections/german-history)
[Tiergarten](https://stock.adobe.com/de/search?k=berlin-tiergarten)
[Bad Homburg](https://www.schloesser-hessen.de/en/bad-homburg)
[Frankfurt](https://www.linkedin.com/in/nathanvallred)
[Marburg](https://www.britannica.com/place/Marburg-Germany)
[Römerberg](https://www.globalarbitrationnews.com/2022/03/03/german-supreme-court-confirms-that-achmea-decision-is-transferable-to-arbitration-clauses-in-other-bits/)
[Rüdesheim am Rhein](https://www.tripadvisor.com/HotelsList-Frankfurt-Quiet-Hotels-zfp848631.html)
[Wiesbaden](https://www.germany.travel/en/cities-culture/spa-towns.html)
[Phantasialand](http://ling-bao-bruehl.nrwestphaliahotels.com/en/)
[Horn bad meinberg](https://www.hornbadmeinberg.de/)
[Aachen Cathedral](https://t24hs.com/relive-history-with-these-things-to-do-in-aachen-german/)
[Dusseldorf](https://victoriasymphony.ca/support/the-majestic-rhine-cruise-beethoven-the-german-romantics/)
[Lindt Chocolate Museum](https://www.cologne-tourism.com/arts-culture/sights/detail/chocolate-museum)
[Cologne Cathedral](https://gsgii.org/nabs/germany/)



[Blautopf](https://reisebloegle.de/blautopf/)
[Heidelberg Castle](https://planetofhotels.com/guide/en/germany/heidelberg)
[Mainau Island](https://www.mainau.de/en/home)
[Outletcity Metzingen](https://www.tripadvisor.com/Attraction_Review-g562796-d2283313-Reviews-Outletcity_Metzingen-Metzingen_Baden_Wurttemberg.html)
[Mercedes Benz Museum](https://julianherzog.com/albums/architecture/content/mercedes-benz-museum-stuttgart/)
[Europa Park](https://www.esslinger-zeitung.de/inhalt.europa-park-in-rust-so-nutzt-der-freizeitpark-die-zeit-ohne-besucher.a99612a0-fd15-4282-)
[Oberstdorf](https://nextvame.com/ski-jumping-additional-continental-cup-in-oberstdorf/)
[Linderhof Palace](https://en.idei.club/48946-linderhof-palace.html)
[Füssen](https://www.linkedin.com/in/hazel-smith-0016ab9/?originalSubdomain=uk)
[Garmisch Partenkirchen](https://www.makemytrip.com/hotels-international/en-sg/germany/garmisch_partenkirchen-hotels/werdenfelserei-details.html)
[Berchtesgarden](https://eu-message.usatoday.com/)
[Munich](https://wwiifoundation.org/wp-content/uploads/2023/10/The-World-War-II-Foundation-2024.pdf)
[St.Petri Dom](https://slivenmedia.com/news/minuti-za-pateshestvie-bremen-po-patya-na-muzikantite)
[Bremen town Hall](https://www.locationscout.net/locations/2301-bremen)
[Rhododendron Park](https://www.wfb-bremen.de/de/page/stories/standortmarketing/lebensqualitaet/warum-ein-besuch-im-rhododendron-park-bremen-ganzjaehrig-lohnt)
[Schlachte](https://zhuanlan.zhihu.com/p/141603098)
[Schnoor](https://www.wfb-bremen.de/en/page/bremen-invest/schnoor-in-bremen)
[Universum Bremen](https://www.google.com/search?q=universum+bremen&sca_esv=577336729&rlz=1C5CHFA_enDE951DE951&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjuzI6ZxJeCAxVv1QIHHdoKDOwQ_AUoAnoECAQQBA&biw=1440&bih=813&dpr=2#imgrc=tDoyLnkHP67BvM&imgdii=nGXEjF_aL-8p3M)













## Acknowledgments

- [Iuliia Konovalova](https://github.com/IuliiaKonovalova) my mentor has been a great supporter, guiding me through the development of the project and helping me to learn a lot of new things by challenging me to do something new.
- [Code Institute](https://codeinstitute.net/de/)  tutors and Slack community members for their support and help.
- [Iuliia Konovalova](https://github.com/IuliiaKonovalova) for review star rating idea .
- [Mihai-Constantin](https://codepen.io/Mihai-Constantin) footer design.