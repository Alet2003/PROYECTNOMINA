function validarcredito(){
    var edad = document.getElementById("edad").value ;
    var salariom = document.getElementById("Salario_mensual").value ;
    if (edad >= 30 && salariom >= 2000000) {
        document.getElementById("verificar").setAttribute("href", "/fronted/indexcreditolibreinversion2")
    }
}
function validarcreditohipotecario(){
    var edad = document.getElementById("edad").value ;
    var salariom = document.getElementById("Salario_mensual").value ;
    if (edad >= 30 && salariom >= 2000000) {
        document.getElementById("verificar").setAttribute("href", "/fronted/indexcreditohipotecario2")
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


function Creditoeducativo() {
    const tipoCarrera = document.getElementById("tipo_carrera").value;
    const tipoCredito = document.getElementById("tipo_credito").value;
    const valorSemestre = parseFloat(document.getElementById("valor_del_semestre").value);
 
    if (tipoCarrera && tipoCredito && !isNaN(valorSemestre)) {
        if (
            (tipoCarrera === "tecnologico" || tipoCarrera === "profesional") &&
            (tipoCredito === "completa" || (tipoCredito === "semestre" && valorSemestre <= 2800000))
        ) {
            Swal.fire({
                title: 'Espere un momento',
                text: `Su credito esta siendo aprobado`,
            })
            var nombre = document.getElementById("nombre").value
            var MontoCredito = document.getElementById("valor_del_semestre").value;
            var TasaInteres = 0;
            var PlazoCredito = document.getElementById("plazo").value;
            const cci = MontoCredito/ PlazoCredito
            var CuotasMensuales = cci.toFixed(2);
            var EstadoCredito = "aprobado";
            var IDEmpleado = document.getElementById("documento").value;
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
                            text: `el empleado ${nombre} ha obtenido un credito por el monto de ${MontoCredito}, el credito debe ser pagado en un plazo de ${PlazoCredito} meses, el valor de las cuotas es de : $ ${CuotasMensuales}`,
                        })

                    } else {

                    }
                })
                .catch(function (error) {
                    console.error(error);
                });


        } else {
            Swal.fire({
                title: 'Por favor, verifique los requisitos para el crédito.',
                text: `verifique que el valor del semestre no sea mayor de 2800000`,
            })
        }
    } else {
        Swal.fire({
            title: 'Por favor, llene todos los campos obligatorios.',
            text: `verifique que todos los campos esten correctamente llenos`,
        })
    }
}