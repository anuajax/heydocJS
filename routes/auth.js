const { render, renderFile } = require("ejs");


const express= require('express');
const router = express.Router();

router.get("/login",(req,res)=> {
    res.render("login.ejs")
});
router.get("/signup/doctor",(req,res)=> {
    res.render("doctorsignup.ejs")
});
router.get("/signup/patient",(req,res)=>{
    res.render("patsignup.ejs")
});
router.post("/login",(req,res)=>{
	res.render("login.ejs")
    /*assign token and redirect to dashboard page*/
})
router.get("/doctor/dashboard",(req,res)=>{
	res.render("docDashboard.ejs")
})
router.get("/doctor/appointments",(req,res)=>{
	res.render("docAppointments.ejs")
})
router.get("/doctor/patients",(req,res)=>{
	res.render("docPatients.ejs")
});
module.exports = router;