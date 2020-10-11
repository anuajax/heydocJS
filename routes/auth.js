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
router.post("/login",()=>{
    /*assign token and redirect to dashboard page*/
})
module.exports = router;