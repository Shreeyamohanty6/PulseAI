document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('form');
  form.addEventListener('submit', validate);
});

function validate(e) {

  let f_name = document.querySelector('#f_name').value;
  let l_name = document.querySelector('#l_name').value;
  let u_name = document.querySelector('#u_name').value;
  let email = document.querySelector('#email').value;
  let password = document.querySelector('#pass').value;
  let password2 = document.querySelector('#pass2').value;

  let error = false;

  // First Name Validation
  if (f_name === "" || f_name === null) {
    document.querySelector('#f_nameError').innerHTML = "Please enter your first name";
    document.querySelector('#f_name').style.border = "1px solid red";
    error = true;
  } else {
    document.querySelector('#f_nameError').innerHTML = "";
    document.querySelector('#f_name').style.border = "1px solid black";
  }

  // Last Name Validation
  if (l_name === "" || l_name === null) {
    document.querySelector('#l_nameError').innerHTML = "Please enter your last name";
    document.querySelector('#l_name').style.border = "1px solid red";
    error = true;
  } else {
    document.querySelector('#l_nameError').innerHTML = "";
    document.querySelector('#l_name').style.border = "1px solid black";
  }

  // Username Validation
  if (u_name === "" || u_name === null) {
    document.querySelector('#u_nameError').innerHTML = "Please enter your username";
    document.querySelector('#u_name').style.border = "1px solid red";
    error = true;
  } else {
    document.querySelector('#u_nameError').innerHTML = "";
    document.querySelector('#u_name').style.border = "1px solid black";
  }

  // Email Validation
  let emailPattern = /^[a-z]+[a-z0-9\._]{3,}@[a-z]{3,10}\.[a-z\.]{2,8}$/;
  if (email === "" || email === null) {
    document.querySelector('#emailError').innerHTML = "Please enter your Email";
    document.querySelector('#email').style.border = "1px solid red";
    error = true;
  } else if (!email.match(emailPattern)) {
    document.querySelector('#emailError').innerHTML = "Please enter a valid Email";
    document.querySelector('#email').style.border = "1px solid red";
    error = true;
  } else {
    document.querySelector('#emailError').innerHTML = "";
    document.querySelector('#email').style.border = "1px solid black";
  }

  // Password Validation
  let validPassword = true;
  let passError = "";
  if (!password.match(/[a-z]/)) {
    passError += "Password should contain at least one lowercase character<br>";
    validPassword = false;
  }
  if (!password.match(/[A-Z]/)) {
    passError += "Password should contain at least one uppercase character<br>";
    validPassword = false;
  }
  if (!password.match(/[0-9]/)) {
    passError += "Password should contain at least one number<br>";
    validPassword = false;
  }
  if (!password.match(/[!@#$%^&*()_]/)) {
    passError += "Password should contain at least one special character<br>";
    validPassword = false;
  }
  if (password.length < 8 || password.length > 16) {
    passError += "Password must be 8-16 characters long<br>";
    validPassword = false;
  }
  if (!validPassword) {
    document.querySelector("#passwordError").innerHTML = passError;
    document.querySelector("#pass").style.border = "1px solid red";
    error = true;
  } else {
    document.querySelector("#passwordError").innerHTML = "";
    document.querySelector("#pass").style.border = "1px solid black";
  }

  // Confirm Password Validation
  if (password2 === "" || password2 === null) {
    document.querySelector("#password2Error").innerHTML = "Confirm Password is required";
    document.querySelector("#pass2").style.border = "1px solid red";
    error = true;
  } else if (password !== password2) {
    document.querySelector("#password2Error").innerHTML = "Password and Confirm Password do not match";
    document.querySelector("#pass2").style.border = "1px solid red";
    error = true;
  } else {
    document.querySelector("#password2Error").innerHTML = "";
    document.querySelector("#pass2").style.border = "1px solid black";
  }

  // Prevent form submission if there are errors
  if (error) {
    e.preventDefault();
    console.log("Form submission prevented due to validation errors.");
  } else {
    console.log("Form submitted successfully.");
  }
}



