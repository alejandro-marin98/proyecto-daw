import BookService from "./services/BookService.js";
import { openSpinner, closeSpinner } from './spinner.lib.js';
document.addEventListener('DOMContentLoaded', setup);

async function setup() {
    let datatable;

    try {
        openSpinner();

        const dataTableOptions = {
            
            // Modificar las columnas de los resultados de la tabla
            columnDefs: [
                // classname es el nombre de la clase que le quieres añadir
                // targets es el indice de las columnas que quieres que sean afectadas
                // { className: "nombre_clase", targets: [0, 1, 2, 3, 4] },
                // // qué columnas NO van a ser ordenables
                // { orderable: false, targets: [4] },
                // { searchable: false, targets: [2, 3, 4] }

            ],

            // Items por página
            pageLength: 5,

            // Que se pueda destruir y volver a crear
            destroy: true,

            // Idioma
            language: {
                lengthMenu: "Mostrar _MENU_ registros por página",
                zeroRecords: "No se han encontrado libros.",
                info: "Mostrando _START_ - _END_ de _TOTAL_ libros",
                infoEmpty: "Ningún libro encontrado.",
                infoFiltered: "(filtrados desde _MAX_ registros totales)",
                search: "Buscar por ISBN o título:",
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

        datatable = $('table').DataTable(dataTableOptions);

        closeSpinner();
    } catch(e) {
        closeSpinner();
        alert(`Lo sentimos, no hemos podido mostrar los datos. Error: ${e}`)
    }

}