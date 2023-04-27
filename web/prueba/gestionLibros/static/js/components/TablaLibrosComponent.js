import BookService from "../services/BookService.js";

export default class TablaLibrosComponent extends HTMLElement {
    #template = 
    `
    <!-- Bootstrap -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.min.js"></script>
    <!-- JQUERY -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
    <!-- DataTable -->
    <script src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
    <link rel="stylesheet" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
    <table id="tTabLibros">
        <thead>
            <tr>
                <th>ISBN</th>
                <th>Nombre</th>
                <th>Paginas</th>
                <th>Autor</th>
            </tr>
        </thead>
        <tbody>
            
        </tbody>
    </table>
    `;

    #librosService;

    #shadowRoot;

    // Inicializo los atributos
    constructor() {
        // Llamo al constructor del padre (HTMLElement)
        super();
        // Declaro mi shadowRoot (DOM aislado del DOM principal)
        this.#shadowRoot = this.attachShadow({ mode: 'open' });
        // Inserto el HTML que necesito (lo tengo declarado en la variable template)
        this.#shadowRoot.innerHTML = this.#template;
        // Declaro el servicio con el que realizaré los fetch
        
        this.#librosService = new BookService();
    }
    
    async connectedCallback() {
        const libros = await this.#librosService.getAllBooks();
        const tbody = this.#shadowRoot.querySelector('tbody');
        console.log(libros)
        libros.forEach(libro => {
            const nTr = document.createElement('tr');
            tbody.innerHTML += `
                <tr>
                    <td>${libro.isbn}</td>
                    <td>${libro.nombre}</td>
                    <td>${libro.paginas}</td>
                    <td>${libro.autor}</td>
                </tr>    
            `
        })

        let table = this.#shadowRoot.querySelector('table');
        let datatable = $(table).DataTable({});
        console.log(datatable)
    }
}

window.customElements.define('tabla-libros', TablaLibrosComponent);