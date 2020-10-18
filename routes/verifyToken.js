const jwt = require('jsonwebtoken');

module.exports = function(req,res,next){
    const token = req.header('JWT');
    if(!token)
   return res.status(401).send('No token found Acces Denied!');
    try {
        const verified = jwt.verify(token,process.env.TOKEN_SECRET);
        req.user = verified;
        next();
    } catch (error) {
        res.status(400).send('Invalid token');
    }
}