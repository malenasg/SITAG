document.addEventListener("DOMContentLoaded", () => {

    // Auto-submit filtros
    document.querySelectorAll(".filtros select").forEach(s => {
        s.addEventListener("change", () => s.form.submit());
    });

    // Verificación de datos
    if (!window.estadosData || !window.mensualData) {
        console.error("Los datos de los gráficos no llegaron desde Django.");
        return;
    }

    // ----------------------------
    // GRAFICO DONUT
    // ----------------------------
    const donutCanvas = document.getElementById("chartEstados");
    if (donutCanvas) {
        new Chart(donutCanvas, {
            type: "doughnut",
            data: {
                labels: window.estadosData.labels,
                datasets: [{
                    data: window.estadosData.values,
                    backgroundColor: ["#0a3d2e", "#7cb38f", "#bfbfbf"]
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false, // <--- permite que llene el contenedor
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: { boxWidth: 15, padding: 10 }
                    }
                }
            }
        });
    }

    // ----------------------------
    // GRAFICO BARRAS
    // ----------------------------
    const barCanvas = document.getElementById("chartMensual");
    if (barCanvas) {
        new Chart(barCanvas, {
            type: "bar",
            data: {
                labels: window.mensualData.labels,
                datasets: [{
                    data: window.mensualData.values,
                    backgroundColor: "#0a3d2e",
                    borderRadius: 5 // bordes redondeados
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false, // <--- permite que llene el contenedor
                scales: {
                    y: { beginAtZero: true, grid: { color: "#eee" } },
                    x: { grid: { color: "#f9f9f9" } }
                }
            }
        });
    }

});
