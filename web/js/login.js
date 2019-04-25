// ========================================================LOGIN=============================================

// set cookie
function setCookie(name, value, days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}
// get cookie
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

// erase cookie
function eraseCookie(name) {
  document.cookie = name +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}


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
            console.log(typeof no_ktp,password)
            alert(response.pesan)
            if (response.pesan == "Berhasil login"){
                window.location.href = 'home.html'
                setCookie('nama', response.data.nama, 7)
                setCookie('no_ktp', response.data.no_ktp, 7)
            }

            else{
                window.location.href = 'index.html'
            }

        },
        error: function(error){
            console.log(error)
            alert(error.responseJSON.pesan)
        }
        // complete: function() {

        // }
    })
}