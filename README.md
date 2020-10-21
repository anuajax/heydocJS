# HeyDoc 
   This is a web app intended to provide easy one step solutions to any patient who signup, for finding a doctor based on their problems. He or She can search a doctor based on:
   - location
   - name
   - speciality
and quickly book an appointment with just a single click.
They can manage their files/prescriptions and view their current and past treatments.
Similarly, doctors can approve appointments, manage their files with patients, view his/her past and active patients. Doctor's community for new discussion and users will be able to chat privately in a messenger.
Additionaly, a daily update of covid details is also provided, plus an emergency ambulance booking and covid helpline facility. 
## Front-End and Routing
   ### Frameworks and Libraries:
**NodeJS, ExpressJS, BootStrap4, Weavy ClientSDK, Weavy ServerSDK, jQuery, JWT**
   ### Installation

    Clone this repo 
    ```
       git clone https://github.com/anuajax/heydocJS.git
       npm install
    ```
    
    Run an instance of Weavy Server SDK (Weavy.sln) from Visual Studio and Microsoft SQL Server Management Studio
    Add a client to Weavy instance with client id as <heydoc> ans secret as <heydoc>.
    This can be done easily by reading [Weavy documentation](https://docs.weavy.com/server/get-started).

After Weavy is up and running, run a local instance at 
**localhost:3000/**
### Usage
 #### /auth/signup/doctor or /auth/signup/patient
 - After you create an account you will be assigned a secret token(jwt), which will be used to create your Weavy Space.
 - After successsful signup it redirects you to login.
 #### /auth/login/doctor or /auth/login/patient
  - After successfully logging in your data is fetched from AWS serverless lambdas and you will see your dashboard.
  - If you are a patient, you can :
    - Search for a doctor as per your needs.
    - Request booking an appointment with him/her.
    - View his/her profile
    - Manage your prescriptions and files
    - View your current/history of doctors, treatments and appointments.
    - Chat with a doctor
    - Share common space with a doctor so that, if you have to meet him again, you both have the            prescriptions and necessary files.
    - Take emergency ambulance and covid help and view Covid stats.
  - If you are a doctor, you can :
    - Approve an appointment.
    - Manage personal records and files of patients.
    - Share a common space with patient to treat them well and easier management of files.
    - Chat with a doctor or patient.
    - View your current/history of patients, treatments and appointments.
    - View/post/comment feed in doctor's community and check what's going on.
    - View Covid Stats 
**All the links for above mentioned features will be displayed on the dashboard page and the navigation bar.**

 #### Common space for a particular doctor and patient :
   **A Weavy space with files app is created at the intersection of doctor and patient**
    Assigning a unique key to Weavy space, the key being composed of doctor's and patient's unique username.
 #### Messaging and Notifications:
    Unique id/key for weavy app from unique space, key being user's username
 #### Files management: 
    Similarly inside unique Weavy space you have your own files.
 #### Community feed:
    Only for doctor from weavy client SDK posts app for every doctor in his/her personal space.
 #### Covid Stats and other details like emergency ambulance
    Info provided on Dashboard page from 3rd party API's.
### How it Works? 
  - A user visits a route(created using Express.js) , user data and other desired data is fetched from AWS Lambda database and passed to show files.
  - In show templates(ejs being used here) weavy instance is generated with the recieved token and spaces and apps using username and desired data is displayed. 
  - We will call API and add weavy to our pages :
   To add weavy simply we pass token from our auth route and use that token in pagename.ejs file to create weavy
   eg:
   from POST req on /auth/login we do following:
   assign a token to the user and pass the token and render dashboard.ejs
   and inside dashboard.ejs we put, 
   ```
      <script type="text/javascript">
        var weavy = new Weavy({ jwt: userdata.jwt });
        var space = weavy.space({ key: userdata.username });
        space.app({key: "posts-demo",type: "posts",container: "#weavy-container"});
        space.app({ key: "main-messenger", type: "messenger", container: "#messenger"});
        space.app({ key: "main-notifications", type: "notifications", container: "#notifications"});  
      </script>
   ```
### Support
   #### localhost:3000/contact 
   **A contact form has been provided in the app for feedback and support/issues. Feel free to contact the developers via email for any queries or issues.**
### RoadMap and Future Scope :
   - The app can be made scalable with multiple users to enter at the same time and protected routes 
   - New features can be easily integrated with this app :
        - Zoom video call integration in messenger
        - 
### Authors and acknowledgment: 
Thanks to our developers: 
   - @ritikamor
   - @amoranu
   - @anuajax
   - @maniikk
