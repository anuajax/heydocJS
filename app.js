const express = require("express");
const bodyParser=require("body-parser");
const app = express();
const port = 3000 || process.env.PORT;
app.set("view engine","ejs");
app.listen(3000, ()=>console.log(`Server active on port No: ${port}`));
app.use(express.static(__dirname + "/styles"));
const authRoutes = require("./routes/auth");
const otherRoutes = require("./routes/commonRoutes");

 
app.use(bodyParser.urlencoded({extended: true}));
app.use("/auth",authRoutes);
app.use("/user",otherRoutes);
app.get('/',(req,res)=>{
    res.render("landing.ejs");
})