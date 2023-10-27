# Testing

## Manual Testing

Every feature that was added to the site was tested before it was integrated into the main file.

The user acceptability test listed below was used to test usability. It was distributed to new users to guarantee testing from a variety of users, on a variety of devices and browsers to ensure problems were identified and, if feasible, fixed during development.

|     | User Actions           | Expected Results | Y/N | Comments    |
|-------------|------------------------|------------------|------|-------------|
| Sign in     |                        |                  |      |             |
| 1           | Click on the Signin button | Redirection to Signin page | Y |          |
| 2           | Click on Sign Up button | Redirection to Sign Up page | Y |          |
| 3           | Enter valid Email id | Fild only accept email address format | Y |          |
| 4           | Enter a valid Password | Field only accept valid passwords | Y |          |
| 5           | Click on the Signin button  | It will redirect to home page | Y |  If the password or emailid not correct shows "The email address and/or password you specified are not correct."         |
| 6           | Click on Forgot Password link | Redirects user to forgot password page | Y |          |
| 7           | Click user image, choose "Logout"| Dropdown menu with 3 options: Account settings,Bookings,Logout | Y |          |
| 8           | Click from droupdown menu choose "Logout"| Takes user to log out page to confirm logout | Y |          |
| 9           | Click "Logout" button  in the the page| Redirects user to home page | Y |          |
| Sign Up     |                        |                  |      |             |
| 2           | Click on Sign Up button | Redirection to Sign Up page | Y |          |
| 3           | Click on the signup link in signin page | Redirection to Sign Up page | Y |          |
| 4           | Click on the sign in link in the form | Redirection to signin page | Y |          |
| 5           | Enter valid email | Field will only accept email address format | Y |          |
| 6           | Enter valid username | Field will only accept no more than 50 characters | Y |          |
| 7           | Enter valid First Name | Field will only accept no more than 30 characters | Y |          |
| 8           | Enter valid Last Name | Field will only accept no more than 30 characters | Y |          |
| 10          | Enter valid password | Field will only accept secure passwords | Y |          |
| 11          | Enter valid password confirmation | Field will only accept the same password from the previous field | Y |          |
| 12          | Click on the Sign Up button | Redirect to home page | Y |          |
| 13          | Click on the Sign Up button | Please Confirm Your Email Address send to user mail id | Y |          |
| 14           | Click user image, choose "Logout"| Dropdown menu with 3 options: Account settings,Bookings,Logout | Y |          |
| 15           | Click from droupdown menu choose "Logout"| Takes user to log out page to confirm logout | Y |          |
| 16           | Click "Logout" button  in the the page| Redirects user to home page | Y |          |
| Navbar        |                        |                  |      |             |
| 1           | Click on the Logo | Redirect to home page  | Y | Available to everyone |
| 2           | Click on About | Redirection to about section | Y | Available to everyone |
| 3           | Click on Destinations | Redirection to states of germany section | Y | Available to everyone|
| 4           | Click on Packages | Redirect to package section | Y | Available  to everyone |
| 5           | Click on Contact | Redirect to contact section | Y | Available  to everyone |
| 6           | Click on user login image |  Dropdown menu with 3 options: Account settings,Bookings,Logout | Y |  Available only for registerd user |
| 7           | Click on accout settings| Redirect to account setting page | Y | Available only for registerd user|
| 8         | Account settings page have three buttons: reset E-Mail,Reset Password,Delete Account.Click on reset E-Mail | Redirect to E-Mail resetting page | Y | Available only for registerd user |
| 9        | Click on Reset password button  | Takes user to Password reset page | Y | Available only for registerd user |
| 10        | Click on account delete button | Takes user to account delete page | Y | Available only for registerd user |
|  11        | Click on bookings | Takes user to booking list page | Y | Available only for registerd user || 
|  12        | If user have booking there is two button:Edit and delete .Click on edit button | Takes user to edit page | Y | Available only for registerd user || 
|  13        | Click on delete button | Takes user to delete booking page | Y | Available only for registerd user || 
|  14        | If there is no booking click on create booking button | Takes user to package list page | Y | Available only for registerd user || 
|  15       | Click on logout | Takes user to logout page | Y | Available only for registerd user || 
|  16        | Click on logout button | redirect to home page | Y | Available only for registerd user || 
Home     |            |                  |      |             |
| 1           |  Click on state name card | Take user to State detail page | Y | Available only Registered Users |
| 2           |  Click on package list State button| Take user to packade detailed page | Y |  Available only registerd user  |
|   State detail Page         |   |  |  |   |
| 1          |  There are buttons for tourist attractions: In each state detail page, there are six buttons for tourist place.Click on any place button | Takes user to place detail page| Y | Available only registerd user |
|  Place detail page         |   |   |  |  |
| 1           |  Click on add review button |  take user to add review page| Y | Available only for registerd user |
| 2           |  select rating | rating is selected | Y | Available only registerd user |
| 3           |  Type review | review appear in comment box| Y | Available only registerd user |
| 4           |  Click on submit review button | user will redirect to view review page | Y | Available only registerd user |
| 5           |  In view review page if user reviews are there then there is two buttons appear:edit and delete | click on edit redirect to edit review page  | Y | Available only registerd user |
| 6          |  Click on delete button| redirected to the review delete page | Y | Available only registerd user |
| 7          |  Click on view more review button| redirected corresponding place view review page | Y | Available only registerd user |
|  Footer          |   |  |  |
| 1          |  click on facebook icon | redirect to facebook page | Y | Available for everyone |
| 2          |  Click on instagram icon | redirect to instagram page | Y | Available for every one |
| 3          |  Click on twitter icon | redirected to twitter page | Y | Available for everyone |
| 4          |  Click on linkedin icon | redirect linkedin page| Y | Available for everyone |
 5           | Click on Github | redirect to Github | Y | Available for every one | 
| 1          |  click on Logo | redirect to home page | Y | Available for everyone |
| 2          |  Click on home link | redirect to home page | Y | Available for every one |
| 3          |  Click on about link | redirected to home page abot section| Y | Available for everyone |
| 4          |  Click on destination link | redirect to home page destination section| Y | Available for everyone |
 5           | Click on Package link | redirect to home page page destination section| Y | Available for everyone |
 6           | Click on Contact link | redirect to home page contact section| Y | Available for everyone |