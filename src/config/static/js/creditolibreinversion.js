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
    var fechaActual = new Date();
    const IDCredito = "";
    var FechaOtorgamiento = fechaActual;
    var MontoCredito = document.getElementById("monto").value;
    var TasaInteres = 0;
    var PlazoCredito = document.getElementById("plazo").value;
    var CuotasMensuales = document.getElementById("cuotas").value;
    var EstadoCredito = "aprobado";
    var IDEmpleado = document.getElementById("documento").value;

    if (MontoCredito < 5000000) {
        TasaInteres = 0.25; // Se corrigió la coma por un punto
    } else {
        TasaInteres = 0.2; // Se corrigió la coma por un punto
    }

    axios.post('/api/save_creditos', {
        IDCredito: IDCredito,
        FechaOtorgamiento: FechaOtorgamiento,
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
    })
    .catch(function (error) {
        console.error(error);
    });
}