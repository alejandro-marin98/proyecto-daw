import { openSpinner, closeSpinner } from './spinner.lib.js';
document.addEventListener('DOMContentLoaded', setup);

async function setup() {
    let datatable;

    try {
        openSpinner();

        const dataTableOptions = {
            
            columnDefs: [
                { orderable: false, targets: [1, 2] },
            ],

            pageLength: 5,

            destroy: true,

            language: {
                lengthMenu: "Mostrar _MENU_ registros por página",
                zeroRecords: "No se han encontrado solicitudes.",
                info: "Mostrando _START_ - _END_ de _TOTAL_ solicitudes",
                infoEmpty: "Ninguna solicitud encontrada.",
                infoFiltered: "(filtrados desde _MAX_ registros totales)",
                loadingRecords: "Cargando...",
                paginate: {
                    first: "Primero",
                    last: "Último",
                    next: "Siguiente",
                    previous: "Anterior"
                }

            },

            scrollX: true,

        };

        datatable = $('#tTabLibros').DataTable(dataTableOptions);

        closeSpinner();
    } catch(e) {
        closeSpinner();
        alert(`Lo sentimos, no hemos podido mostrar los datos. Error: ${e}`)
    }

}