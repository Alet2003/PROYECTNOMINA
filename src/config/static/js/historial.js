// $(document).ready(function() {
//     $('#example').DataTable();
// } );

window.onload = viewhistorial;

function viewhistorial() {
    let table = jQuery('#tabla-historial').DataTable();

    axios.get('/api/HistorialPagos', {
        responseType: 'json'
    })
        .then(function (response) {
            let datos = response.data;
            table.clear().draw();

            if (Array.isArray(datos)) {
                datos.forEach(function (historial) {
                    table.row.add([
                        historial.IDRegistro,
                        historial.FechaPago,
                        historial.TipoPago,
                        historial.MontoPago,
                        historial.IDEmpleado,
                    ]).draw();
                });
            } else {
                console.log('Los datos recibidos no son un array válido. Datos recibidos:', datos);
            }
        })
        .catch(function (error) {
            if (error.response) {
                console.log('Error de respuesta del servidor:', error.response.data);
            } else if (error.request) {
                console.log('Error de solicitud:', error.request);
            } else {
                console.log('Error:', error.message);
            }
            console.log('Error al obtener datos del servidor:', error.config);
        });
}