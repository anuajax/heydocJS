
const { render, renderFile } = require("ejs");
const fetch = require("node-fetch");

const express= require('express');
const router = express.Router();
const app = express();
const bodyParser=require("body-parser");
app.use(bodyParser.urlencoded({extended: true}));

router.get("/login/doctor",(req,res)=> {
    res.render("docLogin.ejs")
});
router.get("/login/patient",(req,res)=> {
    res.render("patLogin.ejs")
});
router.get("/signup/doctor",(req,res)=> {
    res.render("docSignup.ejs")
});
router.get("/signup/patient",(req,res)=>{
    res.render("patSignup.ejs")
});
router.post("/signup/doctor" ,(req,res)=>{
	//creating new patient in the database via API call to AWS
	var signupData = req.body;
	signupData["flag"]="doc";
	var content;
	(async ()=>{
	const response = await fetch('https://j4z72d2uie.execute-api.us-east-1.amazonaws.com/public/sign', {
	headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: 'post',
    body: JSON.stringify(signupData)
  	});
  	content = await response.json();
  	console.log(content);//success:true if user successfully created else false
  	if(content !== undefined)
  	{
  		
	  	if(content.success === true)
	  	{
	  		res.redirect("/login/doctor");
	  	}
	  	else
	  	{
	  		// window.alert("username is already taken please try another username!");
	  		res.render("docSignup.ejs");
	  	}
  	}
  	else
  	{
  		// window.alert("Please try again , there is some error !");
  		res.render("docSignup.ejs");
  	}

  	})();

  	
});
router.post("/signup/patient" ,(req,res)=>{
	//creating new patient in the database via API call to AWS
	var signupData = req.body;
	var content;
	signupData["flag"]="pat";
	(async ()=>{
	const response = await fetch('https://j4z72d2uie.execute-api.us-east-1.amazonaws.com/public/sign', {
	headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: 'post',
    body: JSON.stringify(signupData)
  	});
  	content = await response.json();
  	console.log(content);//success:true if user successfully created else false
  	if(content !== undefined)
  	{
  		if(content.success === true)
	  	{
	  		res.redirect("/login/patient");
	  	}
	  	else
	  	{
	  		// window.alert("username is already taken please try another username!");
	  		res.render("patSignup.ejs");
	  	}
  	}
  	else
  	{
  		// window.alert("Please try again , there is some error !");
  		res.render("patSignup.ejs");
  	}

  	})();
  	
  	
});
router.post("/login/doctor",(req,res)=>{
	var loginData = req.body;
	loginData["flag"] = "doc";
	var content;
	//method to check if the username and password provided are valid
	//API call to AWS, for checking in the database for matching username and password
	(async ()=>{
	const response = await fetch('https://j4z72d2uie.execute-api.us-east-1.amazonaws.com/public/login', {
	headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: 'post',
    body: JSON.stringify(loginData)
  	});
  	content = await response.json();
  	console.log(content); //success:true if valid else false

	  	if(content.success === true)
	  	{
	  		const url = "https://j4z72d2uie.execute-api.us-east-1.amazonaws.com/public/sign?flag=pat&username="+req.body.username;
	  		(async ()=>{
			const response = await fetch(url, {
			headers: {
		      'Accept': 'application/json',
		      'Content-Type': 'application/json'
		    },
		    method: 'get',
		    });
		  	content = await response.json();
		  	console.log(content);
		  	})();
		}

	})();


	res.render("docDashboard.ejs")
    /*assign token and redirect to dashboard page*/
});
router.post("/login/patient",(req,res)=>{
	var loginData = req.body;
	loginData["flag"] = "pat";
	var content;
	//method to check if the username and password provided are valid
	//API call to AWS, for checking in the database for matching username and password
	(async ()=>{
	const response = await fetch('https://j4z72d2uie.execute-api.us-east-1.amazonaws.com/public/login', {
	headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    method: 'post',
    body: JSON.stringify(loginData)
  	});
  	content = await response.json();
  	console.log(content); //success:true if valid else false
		if(content.success === true)
	  	{
	  		const url = "https://j4z72d2uie.execute-api.us-east-1.amazonaws.com/public/sign?flag=pat&username="+req.body.username;
	  		(async ()=>{
			const response = await fetch(url, {
			headers: {
		      'Accept': 'application/json',
		      'Content-Type': 'application/json'
		    },
		    method: 'get',
		    });
		  	content = await response.json();
		  	console.log(content);
		  	})();
		}
		
	})();
  
	res.render("patDashboard.ejs")
    /*assign token and redirect to dashboard page*/
});

router.get("/doctor/dashboard",(req,res)=>{
	res.render("docDashboard.ejs")
})
router.get("/doctor/appointments",(req,res)=>{
	res.render("docAppointments.ejs")
})
router.get("/doctor/patients",(req,res)=>{
	res.render("docPatients.ejs")
});
router.get("/doctor/files",(req,res)=>{
	res.render("docFiles.ejs")
});
router.get("/patient/dashboard",(req,res)=>{
	res.render("patDashboard.ejs")
});
router.get("/patient/appointments",(req,res)=>{
	res.render("patAppointments.ejs")
});
router.get("/patient/doctors",(req,res)=>{
	res.render("patDoctors.ejs")
});
router.get("/patient/files",(req,res)=>{
	res.render("patFiles.ejs")
});

module.exports = router;