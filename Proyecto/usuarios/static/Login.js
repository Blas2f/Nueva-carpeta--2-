(async () => {
    const url = 'https://google-translate1.p.rapidapi.com/language/translate/v2/languages';
    const options = {
        method: 'GET',
        headers: {
            'Accept-Encoding': 'application/gzip',
            'X-RapidAPI-Key': '24e40f3df8msh014f768172b6c7bp1548c6jsn7cd2eea7b61b',
            'X-RapidAPI-Host': 'google-translate1.p.rapidapi.com'
        }
    };
    
    try {
        const response = await fetch(url, options);
        const result = await response.text();
        console.log(result);
    } catch (error) {
        console.error(error);
    }
})();

let loginDiv = document.getElementById("login");
let registerDiv = document.getElementById("register");
let regBtn = document.getElementById("regBtn");
let logRegToggle = true;
registerDiv.style.display = "none";

regBtn.addEventListener("click", () => {
    if (logRegToggle) {
        loginDiv.style.display = "none";
        registerDiv.style.display = "grid";
        logRegToggle = !logRegToggle;
    } else {
        loginDiv.style.display = "grid";
        registerDiv.style.display = "none";
        logRegToggle = !logRegToggle;
    }
});

function validar(){
    var correo = document.getElementById("correo").value;
    var contraseña = document.getElementById("contraseña").value;
    if(correo === "" || contraseña === "" ){
        alert("No puede haber ningun campo vacio");
    }
};

function validarRegistro(){
    var telefono = document.getElementById("fonoR").value;
    var correo = document.getElementById("correoR").value;
    var nombre = document.getElementById("nombreR").value;
    var contraseña = document.getElementById("contraseñaR").value;
    var edad = parseInt(document.getElementById("edadR").value)
    if(telefono === "" || correo === "" || nombre==="" || contraseña==="" || isNaN(edad)){
        alert("No puede haber ningun campo vacio");
    }
};

