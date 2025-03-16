let details = []

function change_form() {
    let element = document.getElementById("container-id");
    if (element.classList.contains('active')) {
        element.classList.remove('active');
    } else {
        element.classList.add('active');
    }
}
function change_forget() {
    let element = document.getElementById("container-id");
    if (element.classList.contains('act')) {
        element.classList.remove('act');
    } else {
        element.classList.add('act');
    }
}
document.addEventListener("DOMContentLoaded", function () {
    const passwordFields = document.querySelectorAll(".password");
    const toggleIcons = document.querySelectorAll(".showHidePw");

    toggleIcons.forEach((icon, index) => {
        icon.addEventListener("click", () => {
            const passwordField = passwordFields[index];

            if (passwordField.type === "password") {
                passwordField.type = "text";
                icon.classList.replace("uil-eye-slash", "uil-eye");
            } else {
                passwordField.type = "password";
                icon.classList.replace("uil-eye", "uil-eye-slash");
            }
        });
    });
});

function validate_login() {
    if (validate_login_email() && validate_login_password()) {
        alert("Login successful!")
        form.email.value = ""
        form.password.value = ""
        form.logchk.checked = false
    } else {
        validate_login_email()
        validate_login_password()
    }
}
function validate_signup() {
    let name = frm.name.value
    let email = frm.mail.value
    let password = frm.pass.value
    if (validate_name() && validate_email() && validate_pass() && validate_confirm_pass() && validate_terms()) {
        details.push({
            "name": name,
            "email": email,
            "password": password
        })
        alert("Signup completed!")
        frm.name.value = ""
        frm.mail.value = ""
        frm.pass.value = ""
        frm.confirmpass.value = ""
        frm.check.checked = false
        console.log(details)
    } else {
        validate_name()
        validate_email()
        validate_pass()
        validate_confirm_pass()
        validate_terms()
    }
}

function validate_name() {
    let nameInput = document.forms["frm"]["name"];
    let name = nameInput.value;
    let validate_name = /^[A-Za-z\s]+$/;
    let nameMessage = document.getElementById("name");
    let exclamIcon = document.getElementById("nameexcal");
    if (name === "" || name == null) {
        nameMessage.innerHTML = "Name can't be blank";
        nameInput.classList.add("error-border");
        exclamIcon.classList.add("error-exclam");
        return false;
    } else if (name.trim() === "") {
        nameMessage.innerHTML = "Name can't contain spaces at the beginning";
        nameInput.classList.add("error-border");
        exclamIcon.classList.add("error-exclam");
        return false;
    } else if (!validate_name.test(name.trim())) {
        nameMessage.innerHTML = "Name contains only alphabets";
        nameInput.classList.add("error-border");
        exclamIcon.classList.add("error-exclam");
        return false;
    } else {
        nameMessage.innerHTML = "";
        nameInput.classList.remove("error-border");
        exclamIcon.classList.remove("error-exclam");
        return true;
    }
}

function validate_email() {
    let emailInput = document.forms["frm"]["mail"];
    let email = emailInput.value;
    let validate_email = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    let emailMessage = document.getElementById("mail");
    let exclamIcon = document.getElementById("mailexcal");
    let email_flag = false
    for (let i = 0; i < details.length; i++) {
        let check_email = details[i]['email'];
        if (email == check_email) {
            email_flag = true
            break
        }
    }
    if (email === "" || email == null) {
        emailMessage.innerHTML = "Email can't be blank";
        emailInput.classList.add("error-border");
        exclamIcon.classList.add("error-exclam");
        return false;
    } else if (!validate_email.test(email.trim())) {
        emailMessage.innerHTML = "Must be a valid email format!";
        emailInput.classList.add("error-border");
        exclamIcon.classList.add("error-exclam");
        return false;
    }
    else if (email_flag) {
        emailMessage.innerHTML = "This email already exists!"
        emailInput.classList.remove("error-border");
        exclamIcon.classList.remove("error-exclam");
        return false;
    } else {
        emailMessage.innerHTML = "";
        emailInput.classList.remove("error-border");
        exclamIcon.classList.remove("error-exclam");
        return true;
    }
}

function validate_login_email() {
    let emailInput = document.forms["form"]["email"];
    let email = emailInput.value.trim();
    let validate_email = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    let emailMessage = document.getElementById("email");
    let exclamIcon = document.getElementById("emailexcal");
    let email_flag = false

    for (let i = 0; i < details.length; i++) {
        let check_email = details[i]['email'];
        if (email == check_email) {
            email_flag = true
            break
        }
    }
    if (email == "" || email == null) {
        emailMessage.innerHTML = "Email can't be blank"
        emailInput.classList.add("error-border");
        exclamIcon.classList.add("error-exclam");
        return false;
    }
    else if (!validate_email.test(email)) {
        emailMessage.innerHTML = "Must be a valid email format!";
        emailInput.classList.add("error-border");
        exclamIcon.classList.add("error-exclam");
        return false;
    }
    else if (!email_flag) {
        emailMessage.innerHTML = "This email id not registered yet!"
        emailInput.classList.add("error-border");
        exclamIcon.classList.add("error-exclam");
        return false;
    }
    else {
        emailMessage.innerHTML = "";
        emailInput.classList.remove("error-border");
        exclamIcon.classList.remove("error-exclam");
        return true;
    }
}

function validate_pass() {
    let form = document.forms["frm"];
    let name = form["name"].value;
    let email = form["mail"].value;
    let passwordInput = form["pass"];
    let password = passwordInput.value.trim();
    let passwordMessage = document.getElementById("pass");
    
    let errors = [];

    if (password === "" || password == null) {
        passwordMessage.innerHTML="Password can't be blank";
        passwordInput.classList.add("error-border");
        return false;
    }
    else if (password.includes(" ")) {
        passwordMessage.innerHTML="Password can't contain spaces";
        passwordInput.classList.add("error-border");
        return false;
    }
    else if (password === name || password === email.slice(0, email.indexOf("@"))) {
       passwordMessage.innerHTML="Password should not be the same as email/username";
       passwordInput.classList.add("error-border");
       return false;
    }
    else if (password.length < 8 || password.length > 12) {
       passwordMessage.innerHTML="Password must be 8-12 characters";
       passwordInput.classList.add("error-border");
       return false;
    }
    
    let uppercase = /[A-Z]/.test(password);
    let lowercase = /[a-z]/.test(password);
    let number = /\d/.test(password);
    let specialChar = /[!@#$_%^&*]/.test(password);
    
    if (!uppercase) {
        errors.push("Must include at least one uppercase letter");
    }
    if (!lowercase) {
        errors.push("Must include at least one lowercase letter");
    }
    if (!number) {
        errors.push("Must include at least one number");
    }
    if (!specialChar) {
        errors.push("Must include at least one special character (!@#$_%^&*)");
    }

    if (errors.length > 0) {
        passwordMessage.innerHTML = errors.join("<br>"); 
        passwordInput.classList.add("error-border");
        return false;
    } else {
        passwordMessage.innerHTML = "";
        passwordInput.classList.remove("error-border");
        return true;
    }
}

function validate_login_password() {
    let passwordInput = document.forms["form"]["password"];
    let password = passwordInput.value.trim();
    let emailInput = document.forms["form"]["email"];
    let email = emailInput.value.trim();
    let passwordMessage = document.getElementById("password");
    let password_flag = false

    for (let i = 0; i < details.length; i++) {
        let check_email = details[i]['email'];
        if (email == check_email) {
            if (password == details[i]['password']) {
                password_flag = true
            }
            break
        }
    }

    if (password == "" || password == null) {
        passwordMessage.innerHTML = "Password can't be blank"
        passwordInput.classList.add("error-border");
        return false;
    }
    else if (password.length < 8 || password.length > 12) {
        passwordMessage.innerHTML = "Password must be 8-12 characters";
        passwordInput.classList.add("error-border");
        return false;
    }
    else if (!password_flag) {
        passwordMessage.innerHTML = "Password is incorrect for this email!"
        passwordInput.classList.add("error-border");
        return false;
    } else {
        passwordMessage.innerHTML = "";
        passwordInput.classList.remove("error-border");
        return true;
    }
}

function validate_confirm_pass() {
    let form = document.forms["frm"];
    let confirmPasswordInput = form["confirmpass"];
    let password = form["pass"].value;
    let confirmPassword = confirmPasswordInput.value;
    let confirmPasswordMessage = document.getElementById("confirmpass");

    if (password !== confirmPassword) {
        confirmPasswordMessage.innerHTML = "Confirm Password must be the same as Password!";
        confirmPasswordInput.classList.add("error-border");
        return false;
    } else {
        confirmPasswordMessage.innerHTML = "";
        confirmPasswordInput.classList.remove("error-border");
        return true;
    }
}
function validate_terms() {
    let checkBox = document.forms["frm"]["check"];
    let termsMessage = document.getElementById("terms");

    if (!checkBox.checked) {
        termsMessage.innerHTML = "Accept the terms and conditions!";
        return false;
    } else {
        termsMessage.innerHTML = "";
        return true;
    }
}

function validate_forgot() {
    let email = fm.ml.value
    let password = fm.pwd.value

    if (validate_forgot_email() && validate_forgot_pass() && validate_forgot_confirm_pass()) {
        alert("password changed!")
        for (let i = 0; i < details.length; i++) {
            let check_email = details[i]['email'];
            if (email == check_email) {
                details[i]['password'] = password
                break
            }
        }
        console.log(details)
        fm.ml.value = ""
        fm.pwd.value = ""
        fm.confirmpwd.value = ""
        change_forget()
    } else {
        validate_forgot_email()
        validate_forgot_pass()
        validate_forgot_confirm_pass()
    }
}
function validate_forgot_email() {
    let emailInput = document.forms["fm"]["ml"];
    let email = emailInput.value.trim();
    let validate_email = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    let emailMessage = document.getElementById("ml");
    let exclamIcon = document.getElementById("mlexcal");
    let email_flag = false
    for (let i = 0; i < details.length; i++) {
        let check_email = details[i]['email'];
        if (email == check_email) {
            email_flag = true
            break
        }
    }

    if (email == "") {
        emailMessage.innerHTML = "Email can't be blank!";
        emailInput.classList.add("error-border");
        exclamIcon.classList.add("error-exclam");
        return false;
    } else if (!validate_email.test(email)) {
        emailMessage.innerHTML = "Must be a valid email format!";
        emailInput.classList.add("error-border");
        exclamIcon.classList.add("error-exclam");
        return false;
    }
    else if (!email_flag) {
        emailMessage.innerHTML = "This email id not exists!"
        emailInput.classList.add("error-border");
        exclamIcon.classList.add("error-exclam");
        return false;
    } else {
        emailMessage.innerHTML = "";
        emailInput.classList.remove("error-border");
        exclamIcon.classList.remove("error-exclam");
        return true;
    }
}

function validate_forgot_pass() {
    let passwordInput = document.forms["fm"]["pwd"];
    let password = passwordInput.value.trim();
    let passwordMessage = document.getElementById("pwd");
    let errors = [];

    if (password === "" || password == null) {
        passwordMessage.innerHTML="Password can't be blank";
        passwordInput.classList.add("error-border");
        return false;
    }
    else if (password.length < 8 || password.length > 12) {
       passwordMessage.innerHTML="Password must be 8-12 characters";
       passwordInput.classList.add("error-border");
       return false;
    }
    
    let uppercase = /[A-Z]/.test(password);
    let lowercase = /[a-z]/.test(password);
    let number = /\d/.test(password);
    let specialChar = /[!@#$_%^&*]/.test(password);
    
    if (!uppercase) {
        errors.push("Must include at least one uppercase letter");
    }
    if (!lowercase) {
        errors.push("Must include at least one lowercase letter");
    }
    if (!number) {
        errors.push("Must include at least one number");
    }
    if (!specialChar) {
        errors.push("Must include at least one special character (!@#$_%^&*)");
    }

    if (errors.length > 0) {
        passwordMessage.innerHTML = errors.join("<br>");  
        passwordInput.classList.add("error-border");
        return false;
    } else {
        passwordMessage.innerHTML = "";
        passwordInput.classList.remove("error-border");
        return true;
    }
}

function validate_forgot_confirm_pass() {
    let passwordInput = document.forms["fm"]["pwd"];
    let confirmPasswordInput = document.forms["fm"]["confirmpwd"];
    let password = passwordInput.value.trim();
    let confirmPassword = confirmPasswordInput.value.trim();
    let confirmPasswordMessage = document.getElementById("confirmpwd");

    if (password !== confirmPassword) {
        confirmPasswordMessage.innerHTML = "Confirm Password must match the Password!";
        confirmPasswordInput.classList.add("error-border");
        return false;
    } else {
        confirmPasswordMessage.innerHTML = "";
        confirmPasswordInput.classList.remove("error-border");
        return true;
    }
}
