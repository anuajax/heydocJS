const express = require("express");
var bodyParser=require("body-parser");
const app = express();
const port = 3000 || process.env.PORT;
app.set("view engine","ejs");
app.listen(3000, ()=>console.log(`Server active on port No: ${port}`));
app.use(express.static(__dirname + "/styles"));
const authRoutes = require("./routes/auth");
app.use(bodyParser.urlencoded({extended: true}));
app.use("/auth",authRoutes);
app.get('/',(req,res)=>{
    res.render("landing.ejs");
})