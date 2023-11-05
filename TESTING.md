# TESTING

## COMPATIBILITY

To ensure the website works on many different browsers, the website was tested on Chrome, Firefox Developer Edition, Edge and Brave.

### CHROME:



### FIREFOX:



### EDGE:



### BRAVE:



## RESPONSIVE BEHAVIOR:

To ensure responsiveness the website was tested on the devtools built into the browsers, Responsively browser and different devices. Apple devices were emulated on Responsively.

### CHROME:



### FIREFOX:



### EDGE:



### BRAVE:



### RESPONSIVELY:



### SAMSUNG S22 ULTRA:



### SAMSUNG TAB S7:

## AUTOMATIC TESTING

## MANUAL TESTING

Manual tests were made by myself, friends and family and CI community members.

 

|             FEATURE              |               ACTION               |               EXPECTED RESULT               | TESTED | PASSED | COMMENT |
| :------------------------------: | :--------------------------------: | :-----------------------------------------: | :----: | :----: | :-----: |
|            Logo Link             |         click on logo link         |           sends user to homepage            |  yes   |  yes   |         |
|            Home Link             |           click on link            |           sends user to home page           |  yes   |  yes   |         |
|           Basics Link            |           click on link            |          sends user to basics page          |  yes   |  yes   |         |
|          Materials Link          |           click on link            |        sends user to materials page         |  yes   |  yes   |         |
|           Models Link            |           click on link            |          sends user to models page          |  yes   |  yes   |         |
|            Help Link             |           click on link            |           sends user to help page           |  yes   |  yes   |         |
|     Navigation Hover Effects     |    hover over navigation links     |     link changes color to accent color      |  yes   |  yes   |         |
|            CTA Button            | click on button to skip to content |     sends user directly to basics page      |  yes   |  yes   |         |
|     CTA Button Hover Effect      |         hover over button          |    button changes color to accent color     |  yes   |  yes   |         |
| Contact Form First Name Validation      |     send form without First Name      | displays a warning because of empty field  |  yes   |  yes   |         |
|  Contact Form Last Name Validation   |     send form without last name       | displays a warning because of empty field  |  yes   |  yes   |         |
|     Contact Form eMail Validation      |     send form without email      | displays a warning because content isnt an email adress  |  yes   |  yes   |         |
| Contact Form Button Hover Effect |       hover over form button       |    button changes color to accent color     |  yes   |  yes   |         |
|   Contact Form Button Function   |  click button when form is filled  |         sends user to response page         |  yes   |  yes   |         |
|   NEXT/BACK Button Hover Effect  |         hover over button          |    button changes color to accent color     |  yes   |  yes   |         |
|     Content Page NEXT Button     |         click next button          |           sends user to next page           |  yes   |  yes   |         |
|     Content Page BACK Button     |         click back button          |         sends user to previous page         |  yes   |  yes   |         |
|    Content Page THANKS Button    |            click button            |           sends user to home page           |  yes   |  yes   |         |
|          Response Page           |             just wait              | sends user back to homepage after 5 seconds |  yes   |  yes   |         |
|           Social Icons           |             click icon             |      sends user to displayed platform       |  yes   |  yes   |         |

## CODE VALIDATION



### NU HTML CHECKER

#### HOMEPAGE

The homepage was tested with  NU HTML checker. These are the results:
<details>
  <summary>NU HTML RESULTS</summary>
<img src="docs/images/testing-images/html-testing/nu-html-landing-page.png" ><br>
</details>

### JIGSAW CSS CHECKER

The CSS was tested with JIGSAW CSS checker. These are the results:
<details>
  <summary>JIGSAW RESULTS</summary>
<img src="docs/images/testing-images/html-testing/jigsaw-css.png" ><br>
</details>

### WAVE ACCESSIBILITY CHECKER

Accessibility was tested with WAVE. These are the results:
<details>
  <summary>WAVE RESULTS</summary>
<img src="docs/images/testing-images/html-testing/wave-result.png" ><br>
</details>

## LIGHTHOUSE REPORTS

### LANDING PAGE
### CONTENT PAGES

## BUGS

### USERS CANT CHANGE THEIR USER IMAGE

- Due to an unresolved bug in the code users cannot change their user image at the moment. However, the code is functional except of this feature. Reason is that the image is not uploaded to cloudinary.
