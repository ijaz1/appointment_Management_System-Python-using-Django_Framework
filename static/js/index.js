function pasVal() {
    var pas = document.getElementById('password').value
    if (pas.length < 8) {
        document.getElementById('firstPassError').innerHTML = 'password must be 8 charectors'
        document.getElementById('signUp_button').type = 'button'
    }
    else if (pas.length > 10) {
        document.getElementById('firstPassError').innerHTML = 'password must be less than 10'
        document.getElementById('signUp_button').type = 'button'
    }
    else {
        document.getElementById('firstPassError').innerHTML = ''
        document.getElementById('signUp_button').type = 'submit'
    }

}

function pasCheck() {
    var firstpass = document.getElementById('password').value
    var secondpass = document.getElementById('conpassword').value
    if (firstpass == secondpass) {
        document.getElementById('secondPassError').innerHTML = ''
        document.getElementById('signUp_button').type = 'submit'
    }
    else {
        document.getElementById('secondPassError').innerHTML = 'password is not eaqual'
        document.getElementById('signUp_button').type = 'button'
    }
}

