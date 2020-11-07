require('dotenv').config();
const express = require("express");
const bodyParser=require("body-parser");
const app = express();
const port = 3000 || process.env.PORT;
app.set("view engine","ejs");
app.listen(3000, ()=>console.log(`Server active on port No: ${port}`));
app.use(express.static(__dirname + "/styles"));
// const session = require('express-session'); 
var flash = require('connect-flash');
 
app.use(flash());
const authRoutes = require("./routes/auth");
// const otherRoutes = require("./routes/commonRoutes");
const indexRoutes = require('./routes/index');
const  expressSanitizer = require('express-sanitizer');
 app.use(express.json());
 app.use(express.urlencoded({extended: true}));

app.use(expressSanitizer());
app.use(require("express-session")({
    secret: "My life is mine i decide what to do",
    resave: false,
    saveUninitialized: false
})); 
app.use(function(req,res,next){          //for currentUser
    //res.locals.currentUser = req.user;
    res.locals.error = req.flash("error");
    res.locals.success = req.flash("success");
    next();
    });
app.use("/auth",authRoutes);
//app.use("/user",otherRoutes);
app.use("/",indexRoutes);
app.get('/',(req,res)=>{
    
    res.render("landing.ejs");
});
