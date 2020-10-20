const mapboxtoken = pk.eyJ1IjoibWFwYm94ZXIxMzMyMyIsImEiOiJja2docXQzMDEwZ2JwMnFsaTZnanFoaGxtIn0.IuR3tL1kw4eeLi12J2J4Lw;
const countries ;
fetch("https://covid19.mathdro.id/api/countries")
.then(res=>res.json())
.then(d => {
    console.log(d);
    countries = d; })
.catch(e=>console.log(e));
var details = [];
countries.forEach(c => {
 fetch(`https://covid19.mathdro.id/api/countries/${c.name}`)
 .then(res=>res.json())
 .then(data => {
    details.push(data);
 })
})