document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("searchInput");
    const table = document.getElementById("facturasTabla, presupuestosTabla");
    const rows = table.getElementsByTagName("tr");

    searchInput.addEventListener("keyup", function() {
        const filter = searchInput.value.toLowerCase();
        for (let i = 1; i < rows.length; i++) {
            const cells = rows[i].getElementsByTagName("td");
            let match = false;
            for (let j = 0; j < 5; j++) { // filtra por las 5 primeras columnas
                if (cells[j] && cells[j].textContent.toLowerCase().includes(filter)) {
                    match = true;
                    break;
                }
            }
            rows[i].style.display = match ? "" : "none";
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("searchInput");
    const table = document.getElementById("presupuestosTabla");
    const rows = table.getElementsByTagName("tr");

    searchInput.addEventListener("keyup", function() {
        const filter = searchInput.value.toLowerCase();
        for (let i = 1; i < rows.length; i++) {
            const cells = rows[i].getElementsByTagName("td");
            let match = false;
            for (let j = 0; j < 5; j++) { // filtra por las primeras 5 columnas
                if (cells[j] && cells[j].textContent.toLowerCase().includes(filter)) {
                    match = true;
                    break;
                }
            }
            rows[i].style.display = match ? "" : "none";
        }
    });
});

