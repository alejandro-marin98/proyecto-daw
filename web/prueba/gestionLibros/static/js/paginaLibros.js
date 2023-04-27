document.addEventListener('DOMContentLoaded', () => {
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
                    zeroRecords: "No se han encontrado opiniones.",
                    info: "Mostrando _START_ - _END_ de _TOTAL_ opiniones",
                    infoEmpty: "Ninguna opinión encontrado.",
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
    

        let datatable = $('#opiniones').DataTable(dataTableOptions);

        const select = document.querySelector('select');
        select.addEventListener('change', e => {
                document.querySelector('.cont button').style.display = 'block';

                if (e.target.value == 'sin_guardar') {
                        e.target.classList.value = 'op1'
                        console.log(e.target)
                }

                if (e.target.value == 'pendiente') {
                        e.target.classList.value = 'op2'
                        console.log(e.target)
                }

                if (e.target.value == 'leyendo') {
                        e.target.classList.value = 'op3'
                        console.log(e.target)
                }

                if (e.target.value == 'leido') {
                        e.target.classList.value = 'op4'
                        console.log(e.target)
                }
        })

});