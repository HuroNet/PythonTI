// ejercicios

let curso = {
  titulo: "Curso profecional de JS",
  formato: " video",
  bloques: ["Introduction", "fuctions"],
  inscribir: function () {
    console.log("inscritos");
  },
};
// console.log(curso.titulo)
print(''hola mundo")
// shorthand syntax

let nombre = "carlos";
let usuario = { nombre };
console.log(usuario.nombre);

//convinaciones
let user = {
  edad: 20,
  nombre: "adrian",
};

let esquema = { nivel: 2 };
let admin = { ...user, ...esquema, permisos: true };

// console.log(admin);
//operacion asincrona

let request = require("request");

request("http://www.google.com", function () {
  console.log("termine");
});

//promesas
