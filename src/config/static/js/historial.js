// $(document).ready(function() {
//     $('#example').DataTable();
// } );

window.onload = viewhistorial;

function viewhistorial() {
    let table = jQuery('#tabla-historial').DataTable();
    jQuery('#tabla-historial').on('click', '.edit-button', function () {
        // Obtener el ID del registro desde el atributo data-id
        var IDRegistro = jQuery(this).data('id');
    });

    jQuery('#tabla-historial').on('click', '.delete-button', function () {
        // Obtener el ID del registro desde el atributo data-id
        var IDRegistro = jQuery(this).data('id');
        Swal.fire({
            title: "Estas seguro de eliminar este registro?",
            text: "Despues de eliminado no podra revertir este cambio!",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "Si, estoy seguro!"
        }).then((result) => {
            if (result.isConfirmed) {
                axios.get(`/api/eliminar_HistorialPagos/${IDRegistro}`, {
                    IDRegistro: IDRegistro
                }, {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                    .then(function (respuesta) {
                        console.log(respuesta.data);
                        if (respuesta.data === "eliminado") {
                            Swal.fire({
                                title: "Eliminado!",
                                text: "El registro fue eliminado correctamente.",
                                icon: "success",
                                confirmButtonColor: "#3085d6",
                                confirmButtonText: "OK",
                            }).then((result) => {
                                if (result.isConfirmed) {
                                    location.reload();
                                }});
                        }
                    })
                    .catch(function (error) {
                        console.error(error);
                    });

            }
        });
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
                    let editButton = '<a href="#modal1" id="edit" name="edit" class="edit-button" data-id="' + historial.IDRegistro + '">Editar</a>';
                    let deleteButton = '<button id="delete" name="delete" class="delete-button" data-id="' + historial.IDRegistro + '">Eliminar</button>';

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
