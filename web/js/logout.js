// erase cookie
function eraseCookie(name) {
    document.cookie = name +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
  }
// logout 
function logout(){
    eraseCookie('nama')
    eraseCookie('no_ktp')
    window.location.href = 'index.html'
}