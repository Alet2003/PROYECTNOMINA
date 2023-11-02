// $(document).ready(function() {
//     $('#example').DataTable();
// } );

window.onload = viewhistorial;

function viewhistorial() {
    let table = jQuery('#tabla-historial').DataTable();
    jQuery('#tabla-historial').on('click', '.edit-button', function() {
        // Obtener el ID del registro desde el atributo data-id
        var idRegistro = jQuery(this).data('id');
        // Implementa la lógica de edición aquí
        // Puedes abrir un modal o redirigir a una página de edición
    });
    
    jQuery('#tabla-historial').on('click', '.delete-button', function() {
        // Obtener el ID del registro desde el atributo data-id
        var idRegistro = jQuery(this).data('id');
        // Implementa la lógica de eliminación aquí
        // Puedes abrir un modal de confirmación o realizar una solicitud para eliminar el registro
    });
    
    axios.get('/api/HistorialPagos', {
        responseType: 'json'
    })
        .then(function (response) {
            let datos = response.data;
            table.clear().draw();

            if (Array.isArray(datos)) {
                datos.forEach(function (historial) {
                    // Agrega botones de edición y eliminación a la última columna
                    let editButton = '<button class="edit-button" data-id="' + historial.IDRegistro + '">Editar</button>';
                    let deleteButton = '<button class="delete-button" data-id="' + historial.IDRegistro + '">Eliminar</button>';

                    table.row.add([
                        historial.IDRegistro,
                        historial.FechaPago,
                        historial.TipoPago,
                        historial.MontoPago,
                        historial.IDEmpleado,
                        editButton + ' ' + deleteButton, // Agrega los botones aquí
                    ]).draw();
                });
            } else {
                console.log('Los datos recibidos no son un array válido. Datos recibidos:', datos);
            }
        })
        .catch(function (error) {
            // Manejo de errores
        });
}
