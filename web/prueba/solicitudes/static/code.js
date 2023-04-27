document.addEventListener('DOMContentLoaded', async () => {
    const response = await fetch('http://localhost:8000/getSolicitudes/2');

    const data = await response.json()


    if (data.cantSolicitudes > 0) {
        document.querySelector('.cant-sol').textContent = data.cantSolicitudes;
    }


})