const Login_button = document.getElementById("login-button");
const Register_button = document.getElementById("register-button");


Login_button.addEventListener("click", function() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username === "" || password === "") {
        alert("用户名和密码不能为空");
        return;
    }

    fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = "/chat";
        } else {
            alert(data.message);
        }
    })
    .catch(error => console.error("Error:", error));
});
Register_button.addEventListener("click", function() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username === "" || password === "") {
        alert("用户名和密码不能为空");
        return;
    }

    fetch("/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("注册成功，请登录");
            window.location.href = "/login";
        } else {
            alert(data.message);
        }
    })
    .catch(error => console.error("Error:", error));
});     