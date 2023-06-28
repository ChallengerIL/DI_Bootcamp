let loginForm = document.querySelector('#loginForm');
let signUpForm = document.querySelector('#signUpForm');


loginForm.addEventListener("submit", function (e) {
    e.preventDefault();
    let formdata = new FormData(loginForm);
    let username = formdata.get("loginUsername");
    let password = formdata.get("loginPassword");

    let userdata = {
        username,
        password
    }

    fetch('http://localhost:3000/login',{
      method: 'POST',
      headers: {
        'Content-Type':'application/json'
      },
      body: JSON.stringify(userdata)
    })
    .then(res => res.json())
    .then(data => {
      document.querySelector('#loginOutput').textContent = data.message;
    })
    .catch(err => {
      document.querySelector('#loginOutput').textContent = err;
    })
});

signUpForm.addEventListener("submit", function (e) {
    e.preventDefault();
    let formdata = new FormData(signUpForm);
    let first_name = formdata.get("first_name");
    let last_name = formdata.get("last_name");
    let email = formdata.get("email");
    let username = formdata.get("username");
    let password = formdata.get("password");

    let userdata = {
        first_name,
        last_name,
        email,
        username,
        password
      }

      fetch('http://localhost:3000/register',{
        method: 'POST',
        headers: {
          'Content-Type':'application/json'
        },
        body: JSON.stringify(userdata)
      })
      .then(res => res.json())
      .then(data => {
        if (typeof data.message !== 'undefined') {
          document.querySelector('#signUpOutput').textContent = data.message;
        } else {
          document.querySelector('#signUpOutput').textContent = `OK Hello ${data[0].first_name} ${data[0].last_name}. Your ID is ${data[0].user_id}`;
        }
      })
      .catch(err => {
        document.querySelector('#signUpOutput').textContent = err;
      })
});
