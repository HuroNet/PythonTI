function obtenerClima (){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const clima = 'Soleado';
            resolve(clima);
        }, 2000);
    });
}

obtenerClima()
    .then(clima => {
        console.log(`El clima es: ${clima}`);
    })
    .catch(error => {
        console.error(`Error al obtener el clima: ${error}`);
    });