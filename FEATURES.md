# Explore Deutschland

## Features

Website contains following pages:
- home page
- state detail page
- place detail page
- add review page
- view review page
- edit review page
- delete review page
- package detail page
- add booking page
- booking detail page
- booking list page
- booking edit page
- booking delete page
- accout setting page

- Each page has a navbar and a footer

**Navbar**

![Navbar](documentation/navbar.png)

navbar contain following links.
- logo 
- home page
- about section
- destination section
- package section 
- about section 
- user image (if user logged in shows user avatar image otherwise shows signin link)
- if click the button shows dropdown menu contains 
    + account settings
    + bookings
    + logout

- account setting page  contains three buttons:
![account setting page](documentation/accountsetting.png)
    + Reset email (redirect to django email reset page )
    + Reset password(redirect to django password reset page)
    + Delete account(redirect to account delete page )
        * in this page delte account confirmation button if click delete account button account will delete permanently
![Delete account page](documentation/deleteaccount.png)

![home page](documentation/home.png)
- if user click logo it shows home page.
- home page contains:
    + about section(Contains brief explanation of website )
    + destination section (includes a list of federal states explore germany offers tours )
    + package section(contains list of federal states explore germany offers tours packages)
    + contact us section(provides company location map address phone and email)


