const express = require("express");
const router = express.Router();

router.get("/doctor/:username",(req,res)=> {
    res.render("docProfile.ejs")
})

router.get("/patient/:username",(req,res)=> {
    res.render("patProfile.ejs")
})
module.exports = router;