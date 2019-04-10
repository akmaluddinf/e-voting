// ========================================================LOGIN=============================================

function login() {
    var no_ktp = document.getElementById('no-ktp').value
    var password = document.getElementById('password').value
    $.ajax({
        url:'http://localhost:5000/login',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            no_ktp: no_ktp,
            password: password

        }),
        success: function(response) {
            alert(response.message)
            window.location.href = 'home.html'
        },
        error: function(error){
            alert("Login gagal")
        }
        // complete: function() {

        // }
    })
}