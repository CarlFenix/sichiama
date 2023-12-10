const { createApp } = Vue
createApp({
data() {
return {
productos:[],
url:'http://localhost:5000/productos',
// si el backend esta corriendo local usar localhost 5000(si no lo subieron a pythonanywhere)
//url:'https://comision23541.pythonanywhere.com/productos', // si ya lo subieron a pythonanywhere
error:false,
cargando:true,
/*atributos para el guardar los valores del formulario */
id:0,
nombre:"",
apellido:"",
edad:0,
email:"",
}
},
methods: {
fetchData(url) {
fetch(url)
.then(response => response.json())
.then(data => {
this.productos = data;
this.cargando=false
})
.catch(err => {
console.error(err);
this.error=true
})
},
eliminar(producto) {
const url = this.url+'/' + producto;
var options = {
method: 'DELETE',
}
fetch(url, options)
.then(res => res.text()) // or res.json()
.then(res => {
location.reload();
})
},
grabar() {
    
    if (!this.nombre.trim()) {
      alert("Por favor, complete el campo Nombre.");
      return;
    }
  
    
     if (!this.apellido.trim()) {
       alert("Por favor, complete el campo Apellido.");
       return;
     }
  
    
    if (isNaN(this.edad) || this.edad < 18) {
      alert("Por favor, ingrese una edad válida igual o mayor a 18.");
      return;
    }
  
    
    if (!this.email.trim() || !this.validateEmail(this.email)) {
      alert("Por favor, ingrese un correo electrónico válido.");
      return;
    }
  
    
    let producto = {
      nombre: this.nombre,
      apellido: this.apellido,
      edad: this.edad,
      email: this.email,
    };
  
    var options = {
      body: JSON.stringify(producto),
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      redirect: 'follow',
    };
  
    fetch(this.url, options)
      .then(() => {
        alert("Registro grabado - Muchas Gracias");
        window.location.href = "../index.html";
      })
      .catch((err) => {
        console.error(err);
        alert("Error al Grabar");
      });
  },
  
  
  validateEmail(email) {
  
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }
  


},

created() {
this.fetchData(this.url)
},
}).mount('#app')