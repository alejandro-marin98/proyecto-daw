document.addEventListener('DOMContentLoaded', setup);

async function setup() {
    console.log('Ha cargado el html')
    let datatable1;
    let datatable2;

        const dataTableOptions = {

            columnDefs: [

                { orderable: false, targets: [1, 2] },
                { searchable: false, targets: [1, 2] }

            ],
            pageLength: 5,
            destroy: true,
            language: {
                lengthMenu: "Mostrar _MENU_ registros por página",
                zeroRecords: "No se han encontrado usuarios.",
                info: "Mostrando _START_ - _END_ de _TOTAL_ usuarios",
                infoEmpty: "Ningún usuario encontrado.",
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
            "activate": function(event, ui) {
                $( $.fn.dataTable.tables( true ) ).DataTable().columns.adjust();
            }


        };
        
        datatable1 = $('.table-amigos').DataTable(dataTableOptions);
        datatable2 = $('.table-no_amigos').DataTable(dataTableOptions);

        document.querySelector('#label-amigos').addEventListener('click', () => {
            let divs = document.querySelectorAll('.esconder');
            divs[0].classList.remove('desaparecer');
            divs[1].classList.add('desaparecer');
            datatable1.columns.adjust().draw();
        })
        document.querySelector('#label-noamigos').addEventListener('click', () => {
            let divs = document.querySelectorAll('.esconder');
            divs[0].classList.add('desaparecer');
            divs[1].classList.remove('desaparecer');
            datatable2.columns.adjust().draw();
        })


}