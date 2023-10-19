// $(document).ready(function() {
//     $('#example').DataTable();
// } );

window.addEventListener('load', function () {
    viewhistorial();
});

$.noConflict();
jQuery(document).ready(function ($) {
    viewhistorial();
});

function viewhistorial() {
    let table = jQuery('#tabla-historial').DataTable();

    axios.get('/api/HistorialPagos', {
        responseType: 'json'
    })
        .then(function (response) {
            let datos = response.data;

            if (Array.isArray(datos)) {
                datos.forEach(function (historial) {
                    table.row.add([
                        historial.IDRegistro,
                        historial.FechaPago,
                        historial.TipoPago,
                        historial.MontoPago,
                        historial.IDEmpleado,
                    ]).draw(false);
                });
            } else if (typeof datos === 'object') {
                Object.values(datos).forEach(function (historial) {
                    table.row.add([
                        historial.IDRegistro,
                        historial.FechaPago,
                        historial.TipoPago,
                        historial.MontoPago,
                        historial.IDEmpleado,
                    ]).draw(false);
                });
            } else {
                console.log('Los datos recibidos no son válidos.');
            }
        })
        .catch(function (error) {
            console.log(error);
        });
}
