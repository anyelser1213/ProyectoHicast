

$(document).ready(function () {
    $('#loginRestro').change(function () {
        if ($(this).is(':checked')) {
            $('#areaLogin').hide();
            $('#areaRegistro').show();
            console.log("Probando aqui");
        }
        else {
            $('#areaLogin').show();
            $('#areaRegistro').hide();
        }
    });
});


  