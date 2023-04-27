const template = `
    <style>
        div.container-spinner {
            position: absolute;
            left: 0;
            top: 0;
            z-index: 1000;
            width: 100vw;
            height: 100vh;
            display: grid;
            place-content: center;
            background-color: rgba(0, 0, 0, 0.4);
            overflow: hidden;
        }

        .espiner {
            width: 200px !important;
            height: 200px !important;

        }


    </style>

    <div id="tDlgSpinner" class="container-spinner">
        <div class="spinner">
        <div class="spinner-border text-primary espiner" role="status">
  <span class="sr-only">Loading...</span>
</div>
        
        </div>
    </div id="">
`;

export function openSpinner() {
    const nDivContainer = document.createElement('div');
    nDivContainer.setAttribute('id', 'tDivContainerSpinner');
    nDivContainer.innerHTML = template;
    document.body.appendChild(nDivContainer);
}

export function closeSpinner() {
    document.body.removeChild(document.querySelector('#tDivContainerSpinner'));
}