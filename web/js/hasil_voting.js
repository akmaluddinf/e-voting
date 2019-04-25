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
    url:'http://localhost:5000/hasilVotingPresiden',
    method: 'GET',
    
    success: function(response) {
        console.log(response)
        for (let i=0; i<response.data.length; i++){
            $("#hasil-vote-presiden").append(
            `<tr>
                <th scope="row">`+response.data[i].nama+`</th>
                <td style="font-weight: 800;">`+response.data[i].jumlah_suara+`</td>
            </tr>`
            )
            console.log(response.data[i].nama)
        } 

    },
    error: function(error){
        alert(error)
    }
    // complete: function() {

    // }
})


$.ajax({
    url:'http://localhost:5000/hasilVotingDPR',
    method: 'GET',
    
    success: function(response) {
        console.log(response)
        for (let i=0; i<response.data.length; i++){
            $("#hasil-vote-dpr").append(
            `<tr>
                <th scope="row">`+response.data[i].nama+`</th>
                <td style="font-weight: 800;">`+response.data[i].jumlah_suara+`</td>
            </tr>`
            )
            console.log(response.data[i].nama)
        } 

    },
    error: function(error){
        alert(error)
    }
    // complete: function() {

    // }
})