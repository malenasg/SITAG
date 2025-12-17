document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("searchInput");
    const table = document.getElementById("clientesTabla");
    if (searchInput && table) {
        const rows = table.getElementsByTagName("tr");

        // Filtrar tabla
        searchInput.addEventListener("keyup", function() {
            const filter = searchInput.value.toLowerCase();
            for (let i = 1; i < rows.length; i++) {
                const cells = rows[i].getElementsByTagName("td");
                let match = false;
                for (let j = 0; j < 3; j++) {
                    if (cells[j] && cells[j].textContent.toLowerCase().includes(filter)) {
                        match = true;
                        break;
                    }
                }
                rows[i].style.display = match ? "" : "none";
            }
        });
    }

    // Confirmación para ocultar cliente
    window.confirmarOcultar = function(event) {
        event.preventDefault();
        if (confirm("¿Seguro que deseas ocultar este cliente?")) {
            window.location.href = event.target.closest("a").href;
        }
        return false;
    };

    // Confirmación para mostrar cliente
    window.confirmarMostrar = function(event) {
        event.preventDefault();
        if (confirm("¿Desea reactivar este cliente?")) {
            window.location.href = event.target.closest("a").href;
        }
        return false;
    };
});
