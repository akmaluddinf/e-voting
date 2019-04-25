if (typeof("no_ktp")  === 'undefined' || getCookie("no_ktp") == undefined){
    window.location.href = 'index.html'}

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

var getCookieNama = getCookie("nama")

    $("#nama").val(getCookieNama)


$.ajax({
    url:'http://localhost:5000/getAllPresiden',
    method: 'GET',
    headers: {
        'Authorization':'Bearer ' ,
        // 'X-CSRF-TOKEN':'xxxxxxxxxxxxxxxxxxxx',
        // 'Content-Type':'application/json'
    },
    
    success: function(response){
        for (var i=0; i<response.length; i++) {
            var no_urut = response[i].no_urut

            var capres =`
            <div class="card" style="width: 18rem; margin: 0px 20px;">
            <img src="img/capres/${response[i].no_urut}.jpg" class="card-img-top" alt="foto-presiden">
                <div class="card-body">
                  <h5 class="card-title" style="text-align: center;">${response[i].nama}</h5>
                  <button class="btn btn-danger font-weight-bold" style="margin: 0px 92px;" onclick="pilihCapres(${response[i].no_urut})">Vote</button>
                </div>
            </div>
            `
            $('#vote-presiden').append(capres)
        }
    },
    error: function(){
    },
    completed: function(){
    },
    statusCode: {
        403: function() {
            window.location.href = 'index.html'
        }
    }
})


function pilihCapres(no_urut){
    var no_ktp = getCookie('no_ktp')
    $.ajax({
        url: `http://localhost:5000/pilihPresiden`,
        method: 'POST',
        contentType: 'application/json',
        headers: {
            'Authorization':'Bearer ' ,
            // 'X-CSRF-TOKEN':'xxxxxxxxxxxxxxxxxxxx',
            // 'Content-Type':'application/json'
        },
        data: JSON.stringify({
            "no_ktp" : no_ktp,
	        "pilihan_presiden" : no_urut
        }),

        success: function (response) {
            // console.log(response)
            if (response.status == 'Berhasil'){
                alert(response.pesan)
                window.location.href = 'hasil_vote.html'
            } else{
                alert(response.pesan)
            }
        },
        error: function (response) {
            alert(response.pesan)
            
        },
        complete: function () {
            // alert('data sudah selesai')
        },

        statusCode: {
            403: function() {
                window.location.href = 'index.html'
            }
        }
    })
}
