const express= require('express');
const router = express.Router();
const sgMail = require('@sendgrid/mail');
sgMail.setApiKey(process.env.SENDGRID_API_KEY);

//contact
router.get('/contact', (req, res) => {
	res.render('contact.ejs');
  });

  // POST /contact
router.post('/contact', async (req, res) => {
	let { name, email, message } = req.body;
	name = req.sanitize(name);
	email = req.sanitize(email);
	message = req.sanitize(message);
	const msg = {
	  to: 'hiimanurag122@gmail.com',
	  from: email,
	  subject: `HeyDoc Contact from ${name}`,
	  text: message,
	  html: `
	  <h1>Hi there, this email is from, ${name}</h1>
	  <p>${message}</p>
	  `,
	};
	try {
	  await sgMail.send(msg);
	  console.log("Thanks email sent successfully")
	  //req.flash('success', 'Thank you for your email, we will get back to you shortly.');
	  res.redirect('/contact');
	} catch (error) {
	  console.error(error);
	  if (error.response) {
		console.error(error.response.body)
	  }
	  console.log("Sorry, something went wrong, please contact admin");
	  //req.flash('error', 'Sorry, something went wrong, please contact admin');
	  res.redirect('back');
	}
  });
  module.exports = router;