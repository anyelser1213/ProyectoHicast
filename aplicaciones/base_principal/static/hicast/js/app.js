

function enviar() {
    var email = document.getElementById('email').value;
    var pass = document.getElementById('pass').value;
    
}
function verificar() {
    
}
function acceso() {
    var emailA = document.getElementById('emailA').value;
    var passA = document.getElementById('passA').value;
    
}
function cerrar() {
    
}
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


  
  // Función que se ejecuta cuando se envía el formulario
  function submitForm(event) {
    event.preventDefault();
  
    // Obtener valores de los campos del formulario
    var nombre = document.getElementById("nombre").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
  
    // Agregar los datos a la base de datos
    database.ref("formulario").push({
      nombre: nombre,
      email: email,
      password: password
    });
  
    // Mostrar un mensaje de éxito
    alert("Los datos se han guardado con éxito");

    // Dentro de la función acceso()

// Verificar si el usuario está autenticado correctamente en Firebase
// Si el usuario está autenticado, mostrar el botón "Ingresar"
// Si el usuario no está autenticado, mostrar el mensaje "SIN ACCESO"
if (usuarioAutenticado) {
    document.getElementById("btnIngresar").style.display = "inline-block";
    document.getElementById("mensajeSinAcceso").style.display = "none";
  } else {
    document.getElementById("btnIngresar").style.display = "none";
    document.getElementById("mensajeSinAcceso").style.display = "block";
  }
  
    
  }