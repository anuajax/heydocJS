const express = require("express");
const router = express.Router();

router.get("/doctor/:docusername",(req,res)=> {
    res.render("docProfile.ejs")
})

router.get("/patient/:patusername",(req,res)=> {
    res.render("patientProfile.ejs")
})
module.exports = router;