const nombre = document.getElementById("name")
const email = document.getElementById("email")
const direccion = document.getElementById("direction")
const pass = document.getElementById("password")
const gender = document.getElementById("categoria")
const form = document.getElementById("form")
const parrafo = document.getElementById("warnings")



form.addEventListener("submit", e=>{
    e.preventDefault()
    let warnings = ""
    let entrar = false
    let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/
    parrafo.innerHTML = ""
    if(nombre.value.length <6){
        warnings += `El nombre ingresado no es valido <br>`
        entrar = true
    }

    if(direccion.value.length <12){

        warnings += ` La direccion ingresada no es valida <br>`
        entrar = true 
    }


    if(!regexEmail.test(email.value)){
        warnings += `El email ingresado no es valido <br>`
        entrar = true
    }
    if(pass.value.length < 8){
        warnings += `La contraseña ingresada no es valida <br>`
        entrar = true
    }

    if(gender.value == ""){

        warnings += `Debes seleccionar una categoria <br>` 
        entrar = true  
    }


    var indexes = form.tecnologia;
    var indexSelected = false;

    for(var i = 0; i<indexes.length; i++){

        if(indexes[i].checked){

            indexSelected = true;
            

        }

    }
    if(!indexSelected){
        warnings += `Debes tickear un genero <br>` 
        entrar = true
        

    }


   
    
   



    if(entrar){
        parrafo.innerHTML = warnings
    }else{
        parrafo.innerHTML = "Enviado Correctamente."
    }
})