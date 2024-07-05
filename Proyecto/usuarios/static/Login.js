let loginDiv = document.getElementById("login");
let registerDiv = document.getElementById("register");
let regBtn = document.getElementById("regBtn");




function validar(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if(username === "" || password === "" ){
        alert("No puede haber ningun campo vacio");
    }
};

function validarRegistro(){
    var telefono = document.getElementById("telefono").value;
    var correo = document.getElementById("correo").value;
    var nombre = document.getElementById("username").value;
    var nombre = document.getElementById("p_nombre").value;
    var nombre = document.getElementById("apellido").value;
    var contraseña = document.getElementById("password").value;
    var edad = parseInt(document.getElementById("edad").value)
    if(telefono === "" || correo === "" || nombre==="" || contraseña==="" || isNaN(edad)){
        alert("No puede haber ningun campo vacio");
    }
};

