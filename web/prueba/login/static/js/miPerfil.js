document.addEventListener('DOMContentLoaded', setup);

async function setup() {
    console.log('Ha cargado el html')
    let datatable;


    const dataTableOptions = {

        columnDefs: [
            { orderable: false, targets: [3] },
            { searchable: false, targets: [1, 2, 3] }

        ],

        pageLength: 5,

        destroy: true,

        language: {
            lengthMenu: "Mostrar _MENU_ registros por página",
            zeroRecords: "No se han encontrado libros.",
            info: "Mostrando _START_ - _END_ de _TOTAL_ libros",
            infoEmpty: "Ningún libro encontrado.",
            infoFiltered: "(filtrados desde _MAX_ registros totales)",
            search: "Buscar por título:",
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

    datatable = $('#tabla-libros').DataTable(dataTableOptions);

    document.querySelector('#label-info').addEventListener('click', () => {
        let divs = document.querySelectorAll('.esconder');
        divs[0].classList.remove('desaparecer');
        divs[1].classList.add('desaparecer');
        divs[2].classList.add('desaparecer');
    })
    document.querySelector('#label-about').addEventListener('click', () => {
        let divs = document.querySelectorAll('.esconder');
        divs[0].classList.add('desaparecer');
        divs[1].classList.remove('desaparecer');
        divs[2].classList.add('desaparecer');
    })
    document.querySelector('#label-list').addEventListener('click', () => {
        let divs = document.querySelectorAll('.esconder');
        divs[0].classList.add('desaparecer');
        divs[1].classList.add('desaparecer');
        console.log(divs[2])
        divs[2].classList.remove('desaparecer');
        datatable.columns.adjust().draw();
    })


}