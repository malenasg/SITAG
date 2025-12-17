document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("searchInput");
    const rows = document.getElementById("trabajosTabla").getElementsByTagName("tr");

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
});