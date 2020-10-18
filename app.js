require('dotenv').config();
const express = require("express");
const bodyParser=require("body-parser");
const app = express();
const port = 3000 || process.env.PORT;
app.set("view engine","ejs");
app.listen(3000, ()=>console.log(`Server active on port No: ${port}`));
app.use(express.static(__dirname + "/styles"));
const authRoutes = require("./routes/auth");
const otherRoutes = require("./routes/commonRoutes");
const indexRoutes = require('./routes/index');
const  expressSanitizer = require('express-sanitizer');
 app.use(express.json());
 app.use(express.urlencoded({extended: true}));
// app.use(bodyParser.urlencoded({extended: true}));
app.use(expressSanitizer());
app.use("/auth",authRoutes);
app.use("/user",otherRoutes);
app.use("/",indexRoutes);
app.get('/',(req,res)=>{
    res.render("landing.ejs");
})