function validarcredito(){
    var edad = document.getElementById("edad").value ;
    var salariom = document.getElementById("Salario_mensual").value ;
    if (edad >= 30 && salariom >= 2000000) {
        document.getElementById("verificar").setAttribute("href", "/fronted/indexcreditolibreinversion2")
    }
}

function validarcreditoeducativo(){
    var edad = document.getElementById("edad").value ;
    var salariom = document.getElementById("Salario_mensual").value ;
    if (edad >= 30 && salariom >= 2000000) {
        document.getElementById("verificar").setAttribute("href", "/fronted/indexcreditoeducativo2")
    }
}
function credito() {
    var nombre = document.getElementById("nombre").value
    var MontoCredito = document.getElementById("monto").value;
    var TasaInteres = 0;
    var PlazoCredito = document.getElementById("plazo").value;
    var CuotasMensuales = document.getElementById("cuotas").value;
    var EstadoCredito = "aprobado";
    var IDEmpleado = document.getElementById("documento").value;
    if (MontoCredito < 5000000) {
        TasaInteres = 0.25;
    } else {
        TasaInteres = 0.2;
    }
    var cci = MontoCredito * TasaInteres
    var cuotas = cci + MontoCredito /  PlazoCredito / CuotasMensuales
    console.log( MontoCredito, TasaInteres, PlazoCredito, CuotasMensuales, EstadoCredito, IDEmpleado);

    axios.post('/api/save_creditos', {
        MontoCredito: MontoCredito,
        TasaInteres: TasaInteres,
        PlazoCredito: PlazoCredito,
        CuotasMensuales: CuotasMensuales,
        EstadoCredito: EstadoCredito,
        IDEmpleado: IDEmpleado
    }, {
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(function (respuesta) {
        console.log(respuesta.data);
        if (respuesta.data === "aprobado") {
            Swal.fire({
                title: 'Felicidades credito aprobado',
                text: `el empleado ${nombre} ha obtenido un creito por el monto de ${MontoCredito}, las cuotas tienen un valor de ${cuotas.toFixed(2)}, el credito debe ser pagado en un plazo de ${PlazoCredito}` ,
            })
        
        } else {
            
        }
    })
    .catch(function (error) {
        console.error(error);
    });
}