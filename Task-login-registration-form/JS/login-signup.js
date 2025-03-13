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
    let email = form.email.value
    let password = form.password.value
    let validate_email = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    let text = "";
    let css = "";
    let content = "";
    let count = 0
    let email_flag=false
    let password_flag=false

    for(let i=0;i<details.length;i++){
        let check_email=details[i]['email'];
        if(email==check_email){
            email_flag=true
            if(password==details[i]['password']){
                password_flag=true
            }
            break
        }
    }
    
    if (email == "" || email == null) {
        text = "Email can't be blank"
        css = "2px solid rgba(198, 6, 6, 0.936)"
        content = "visible"
    }
    else if (!validate_email.test(email.trim())) {
        text = "Must be a valid email format!"
        css = "2px solid rgba(198, 6, 6, 0.936)"
        content = "visible"
    }
    else if(!email_flag){
       text ="This email id not registered yet!"
    }
    else {
        text = ""
        css = ""
        content = "hidden"
        count += 1
    }
    document.getElementById("email").innerHTML=text
    document.getElementById("email").innerHTML = text
    emailexcal.style.visibility = content
    form.email.style.border = css
    text = "";
    css = ""
    content = ""
    
    if (password == "" || password == null) {
        text = "Password can't be blank"
        css = "2px solid rgba(198, 6, 6, 0.936)"
    }
    else if (password.trim() == "") {
        text = "Password can't contains spaces"
        css = "2px solid rgba(198, 6, 6, 0.936)"
    }
    else if (password.trim().length < 8) {
        text = "Password must have minimum 8 characters"
        css = "2px solid rgba(198, 6, 6, 0.936)"
    }
    else if(!password_flag){
        text="Password is incorrect for this email!"
    }
    else {
        text = ""
        css = ""
        count += 1
    }
    document.getElementById("password").innerHTML = text
    form.password.style.border = css
    
    if (count == 2) {
        alert("Login successful!")
        form.email.value = ""
        form.password.value = ""
        form.logchk.checked=false
    }
}
function validate_signup() {
    let name = frm.name.value
    let email = frm.mail.value
    let password = frm.pass.value
    let confirm_password = frm.confirmpass.value
    let validate_name = /^[A-Za-z\s]+$/
    let validate_email = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    let validate_password = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$_%^&*])/
    let text = "";
    let css = ""
    let content = ""
    let count = 0
    let email_flag=false
    for(let i=0;i<details.length;i++){
        let check_email=details[i]['email'];
        if(email==check_email){
            email_flag=true
            break
        }
    }
    if (name == "" || name == null) {
        text = "Name can't be blank"
        css = "2px solid rgba(198, 6, 6, 0.936)"
        content = "visible"
    }
    else if (name.trim() == "") {
        text = "Name can't contain spaces in beginning"
        css = "2px solid rgba(198, 6, 6, 0.936)"
        content = "visible"
    }
    else if ((!validate_name.test(name.trim()))) {
        text = "Name conatins only alphabets"
        css = "2px solid rgba(198, 6, 6, 0.936)"
        content = "visible"
    }
    else {
        text = ""
        css = ""
        content = "hidden"
        count += 1
    }
    document.getElementById("name").innerHTML = text
    frm.name.style.border = css
    nameexcal.style.visibility = content
    text = ""
    css = ""
    content = ""
    if (email == "" || email == null) {
        text = "Email can't be blank"
        css = "2px solid rgba(198, 6, 6, 0.936)"
        content = "visible"
    }
    else if (!validate_email.test(email.trim())) {
        text = "Must be a valid email format!"
        css = "2px solid rgba(198, 6, 6, 0.936)"
        content = "visible"
    }
    else if(email_flag){
        text="This email already exists!"
    }
    else {
        text = ""
        css = ""
        content = "hidden"
        count += 1
    }
    document.getElementById("mail").innerHTML = text
    frm.mail.style.border = css
    mailexcal.style.visibility = content
    text = "";
    css = ""
    if (password == "" || password == null) {
        text = "Password can't be blank"
        css = "2px solid rgba(198, 6, 6, 0.936)"
    }
    else if (password.trim() == "") {
        text = "Password can't contains spaces"
        css = "2px solid rgba(198, 6, 6, 0.936)"
    }
    else if (password.trim().length < 8 || password.trim().length > 12) {
        text = "Password must be 8-12 characters"
        css = "2px solid rgba(198, 6, 6, 0.936)"
    }
    else if (password == name || password == email.slice(0, email.indexOf("@"))) {
        text = "Password should not be the same as email/username"
        css = "2px solid rgba(198, 6, 6, 0.936)"
    }
    else if (!validate_password.test(password)) {
        text = `must have at least one uppercase letter, one lowercase letter, one number, and one special character`
        css = "2px solid rgba(198, 6, 6, 0.936)"
    }
    else {
        text = ""
        css = ""
        count += 1
    }
    document.getElementById("pass").innerHTML = text
    frm.pass.style.border = css
    text = ""
    css = ""
    if (password != confirm_password.trim()) {
        text = "Confirm Password must be same as password!"
        css = "2px solid rgba(198, 6, 6, 0.936)"
    } else {
        text = ""
        css = ""
        count += 1
    }
    document.getElementById("confirmpass").innerHTML = text
    frm.confirmpass.style.border = css
    let check = frm.check.checked
    text = ""
    if (check == false) {
        text = "Accept the terms and conditions!"
    } else {
        text = ""
        count += 1
    }
    document.getElementById("terms").innerHTML = text
    if (count == 5) {
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
    }
}

function validate_name() {
    let name = frm.name.value
    let validate_name = /^[A-Za-z\s]+$/
    let text = ""
    let css = ""
    let content = ""
    if ((!validate_name.test(name.trim()))) {
        text = "Name conatins only alphabets"
        css = "2px solid rgba(198, 6, 6, 0.936)"
        content = "visible"
    }
    else {
        text = ""
        css = ""
        content = "hidden"
    }
    document.getElementById("name").innerHTML = text
    nameexcal.style.visibility = content
    frm.name.style.border = css
}
function validate_email() {
    let email = frm.mail.value
    let validate_email = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    let text = ""
    let css = ""
    let content = ""
    if (!validate_email.test(email.trim())) {
        text = "Must be a valid email format!"
        css = "2px solid rgba(198, 6, 6, 0.936)"
        content = "visible"
    }
    else {
        text = ""
        css = ""
        content = "hidden"
    }
    document.getElementById("mail").innerHTML = text
    frm.mail.style.border = css
    mailexcal.style.visibility = content
}
function validate_login_email() {
    let email = form.email.value
    let validate_email = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    let text = ""
    let css = ""
    let content = ""
    if (!validate_email.test(email.trim())) {
        text = "Must be a valid email format!"
        css = "2px solid rgba(198, 6, 6, 0.936)"
        content = "visible"
    }
    else {
        text = ""
        css = ""
        content = "hidden"
    }
    document.getElementById("email").innerHTML = text
    emailexcal.style.visibility = content
    form.email.style.border = css
}
function validate_pass() {
    let name = frm.name.value
    let email = frm.mail.value
    let password = frm.pass.value
    let validate_password = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$_%^&*])/
    let text = "";
    let css = ""
    // let content=""
    // let eye=""
    if (password.trim().length < 8 || password.trim().length > 12) {
        text = "Password must be 8-12 characters"
        css = "2px solid rgba(198, 6, 6, 0.936)"
        // content="visible"
        // eye="hidden"
    }
    else if (password == name || password == email.slice(0, email.indexOf("@"))) {
        text = "Password should not be the same as email/username"
        css = "2px solid rgba(198, 6, 6, 0.936)"
        // content="visible"
        // eye="hidden"
    }
    else if (!validate_password.test(password)) {
        text = `must have at least one uppercase letter, one lowercase letter, one number, and one special character`
        css = "2px solid rgba(198, 6, 6, 0.936)"
        // content="visible"
        // eye="hidden"
    }
    else {
        text = ""
        css = ""
        // content="hidden"
        // eye="visible"
    }
    document.getElementById("pass").innerHTML = text
    // passeye.style.visibility=eye
    frm.pass.style.border = css
    // passexcal.style.visibility=content
}
function validate_login_password() {
    let password = form.password.value
    let text = "";
    let css = ""
    if (password.trim().length < 8 || password.trim().length > 12) {
        text = "Password must be 8-12 characters"
        css = "2px solid rgba(198, 6, 6, 0.936)"
    }
    else {
        text = ""
        css = ""
    }
    document.getElementById("password").innerHTML = text
    form.password.style.border = css
}
function validate_confirm_pass() {
    let confirm_password = frm.confirmpass.value
    let password = frm.pass.value
    let text = ""
    let css = ""
    if (password != confirm_password) {
        text = "Confirm Password must be same as password!"
        css = "2px solid rgba(198, 6, 6, 0.936)"
    } else {
        text = ""
        css = ""
    }
    document.getElementById("confirmpass").innerHTML = text
    frm.confirmpass.style.border = css
}

function validate_forgot() {
    let email = fm.ml.value
    let password = fm.pwd.value
    let confirm_password = fm.confirmpwd.value
    let validate_email = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    let validate_password = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$_%^&*])/
    let text = "";
    let css = ""
    let content = ""
    let count = 0
    let email_flag=false
    for(let i=0;i<details.length;i++){
        let check_email=details[i]['email'];
        if(email==check_email){
            email_flag=true
            break
        }
    }
    if (!validate_email.test(email.trim())) {
        text = "Must be a valid email format!"
        css = "2px solid rgba(198, 6, 6, 0.936)"
        content = "visible"
    }
    else if(!email_flag){
        text="This email id not exists!"
    }
    else {
        text = ""
        css = ""
        content = "hidden"
        count += 1
    }
    document.getElementById("ml").innerHTML = text
    fm.ml.style.border = css
    mlexcal.style.visibility = content
    text = "";
    css = ""
    if (password.trim() == "") {
        text = "Password can't contains spaces"
        css = "2px solid rgba(198, 6, 6, 0.936)"
    }
    else if (password.trim().length < 8 || password.trim().length > 12) {
        text = "Password must be 8-12 characters"
        css = "2px solid rgba(198, 6, 6, 0.936)"
    }
    else if (!validate_password.test(password)) {
        text = `must have at least one uppercase letter, one lowercase letter, one number, and one special character`
        css = "2px solid rgba(198, 6, 6, 0.936)"
    }
    else {
        text = ""
        css = ""
        count += 1
    }
    document.getElementById("pwd").innerHTML = text
    fm.pwd.style.border = css
    text = ""
    css = ""
    if (password != confirm_password) {
        text = "Confirm Password must be same as password!"
        css = "2px solid rgba(198, 6, 6, 0.936)"
    } else {
        text = ""
        css = ""
        count += 1
    }
    document.getElementById("confirmpwd").innerHTML = text
    fm.confirmpwd.style.border = css
    if (count == 3) {
        alert("password changed!")
        for(let i=0;i<details.length;i++){
            let check_email=details[i]['email'];
            if(email==check_email){
                details[i]['password']=password
                break
            }
        }
        console.log(details)
        fm.ml.value = ""
        fm.pwd.value = ""
        fm.confirmpwd.value = ""
        change_forget()
    }
}
function validate_forgot_email() {
    let email = fm.ml.value
    let validate_email = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    let text = ""
    let css = ""
    let content = ""
    if (!validate_email.test(email.trim())) {
        text = "Must be a valid email format!"
        css = "2px solid rgba(198, 6, 6, 0.936)"
        content = "visible"
    }
    else {
        text = ""
        css = ""
        content = "hidden"
    }
    document.getElementById("ml").innerHTML = text
    fm.ml.style.border = css
    mlexcal.style.visibility = content
}
function validate_forgot_pass() {
    let password = fm.pwd.value
    let validate_password = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$_%^&*])/
    let text = "";
    let css = ""
    if (password.trim().length < 8 || password.trim().length > 12) {
        text = "Password must be 8-12 characters"
        css = "2px solid rgba(198, 6, 6, 0.936)"
    }
    else if (!validate_password.test(password)) {
        text = `must have at least one uppercase letter, one lowercase letter, one number, and one special character`
        css = "2px solid rgba(198, 6, 6, 0.936)"
    }
    else {
        text = ""
        css = ""
    }
    document.getElementById("pwd").innerHTML = text
    fm.pwd.style.border = css
}
function validate_forgot_confirm_pass() {
    let confirm_password = fm.confirmpwd.value
    let password = fm.pwd.value
    let text = ""
    let css = ""
    if (password != confirm_password) {
        text = "Confirm Password must be same as password!"
        css = "2px solid rgba(198, 6, 6, 0.936)"
    } else {
        text = ""
        css = ""
    }
    document.getElementById("confirmpwd").innerHTML = text
    fm.confirmpwd.style.border = css
}