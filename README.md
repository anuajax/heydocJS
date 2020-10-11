# heydocJS
Initially implemented ejs using Express server on localhost:3000/
But we will call Api and add weavy our pages 
to add weavy simply we pass token from our auth route and use that token in pagename.ejs file to create weavy
eg:
from POST req on /auth/login we do following:
assign a token to the user and pass the token and render dashboard.ejs
and inside dashboard.ejs
we write
<script>
var weavy = new Weavy(().....etc
</script>
