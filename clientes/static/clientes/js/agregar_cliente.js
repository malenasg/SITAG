document.addEventListener("DOMContentLoaded", function() {
    const tipoSelect = document.getElementById("tipo_cliente");
    const fisica = document.getElementById("datos-fisica");
    const juridica = document.getElementById("datos-juridica");

    // Función para mostrar/ocultar campos según tipo de cliente
    function actualizarTipo() {
        if(tipoSelect.value === "juridica") {
            fisica.style.display = "none";
            fisica.querySelectorAll("input").forEach(i => i.disabled = true);

            juridica.style.display = "block";
            juridica.querySelectorAll("input").forEach(i => i.disabled = false);
        } else {
            juridica.style.display = "none";
            juridica.querySelectorAll("input").forEach(i => i.disabled = true);

            fisica.style.display = "block";
            fisica.querySelectorAll("input").forEach(i => i.disabled = false);
        }
    }

    tipoSelect.addEventListener("change", actualizarTipo);
    actualizarTipo();

    // =======================
    // Departamentos y Localidades
    // =======================
    const departamentos = {
        "1º de Mayo": ["Barrio de los Pescadores", "Colonia Benítez", "Lote 1", "Margarita Belén"],
        "2 de Abril": ["Hermoso Campo", "Itín"],
        "9 de Julio": ["Las Breñas", "Las Piedritas"],
        "12 de Octubre": ["Gancedo", "General Capdevila", "General Pinedo", "Mesón de Fierro", "Pampa Landriel"],
        "25 de Mayo": ["Colonia Aborigen", "Machagai", "Napalpí"],
        "Almirante Brown": ["Concepción del Bermejo", "Los Frentones", "Pampa del Infierno", "Río Muerto", "Taco Pozo"],
        "Bermejo": ["General Vedia", "Isla del Cerrito", "La Leonesa", "Las Palmas", "Puerto Bermejo", "Puerto Eva Perón"],
        "Chacabuco": ["Charata"],
        "Comandante Fernández": ["Presidencia Roque Sáenz Peña"],
        "Fray Justo Santa María de Oro": ["Chorotis", "Santa Sylvina", "Venados Grandes"],
        "General Belgrano": ["Corzuela"],
        "General Donovan": ["La Escondida", "Lapachito", "La Verde", "Makallé"],
        "General Güemes": ["Comandancia Frías", "El Espinillo","El Sauzal","El Sauzalito", "Fortín Belgrano", "Fortín Lavalle", "Fuerte Esperanza", "Juan José Castelli","Las Hacheras", "Miraflores", "Nueva Pompeya", "Puerto Lavalle","Tartagal", "Tres Pozos", "Villa Río Bermejito", "Wichi", "Zaparinqui"],                    
        "Independencia": ["Avia Terai", "Campo Largo","Colonia José Mármol", "Fortín Las Chuñas", "Napenay"],
        "Libertad": ["Colonia Popular", "Estación General Obligado","Laguna Blanca", "Puerto Tirol"],
        "Libertador General San Martín": ["Ciervo Petiso", "General José de San Martín", "La Eduvigis", "Laguna Limpia", "Pampa Almirón", "Pampa del Indio","Presidencia Roca", "Selvas del Río de Oro"],
        "Maipú": ["Colonia La Matanza", "Kilómetro 855", "Kilómetro 884", "La Curva", "Tres Isletas"],
        "Mayor Luis Jorge Fontana": ["Colonia Pegouriel", "El Pastoril", "Enrique Urién", "Villa Ángela"],
        "O'Higgins": ["La Clotilde", "La Tigra", "San Bernardo"],
        "Presidencia de la Plaza": ["Presidencia de la Plaza"],
        "Quitilipi": ["El Paraisal","Quitilipi", "Villa El Palmar"],
        "San Fernando": ["Barranqueras", "Basail","Colonia Baranda", "Fontana", "Puerto Vilelas", "Resistencia"],
        "San Lorenzo": ["Samuhú", "Villa Berthet"],
        "Sargento Cabral": ["Capitán Solari", "Colonia Elisa", "Colonias Unidas", "Ingeniero Barbet", "Las Garcitas"],
        "Tapenagá": ["Charadai", "Cote Lai","Haumonia", "Horquilla", "La Sabana"]
    };

    const departamentoSelect = document.getElementById("departamento");
    const localidadSelect = document.getElementById("localidad");

    if (departamentoSelect && localidadSelect) {
        // Limpiar departamentos antes de agregar opciones
        departamentoSelect.innerHTML = '<option value="">Seleccione un departamento</option>';

        Object.keys(departamentos).forEach(dep => {
            const option = document.createElement("option");
            option.value = dep;
            option.textContent = dep;
            departamentoSelect.appendChild(option);
        });

        departamentoSelect.addEventListener("change", function () {
            localidadSelect.innerHTML = '<option value="">Seleccione una localidad</option>';
            (departamentos[this.value] || []).forEach(loc => {
                const option = document.createElement("option");
                option.value = loc;
                option.textContent = loc;
                localidadSelect.appendChild(option);
            });
        });
    }

    // =======================
    // Asegurar que los campos correctos estén habilitados al enviar
    // =======================
    const form = document.querySelector('form');
    form.addEventListener('submit', function() {
        if(tipoSelect.value === "juridica") {
            juridica.querySelectorAll("input").forEach(i => i.disabled = false);
        } else {
            fisica.querySelectorAll("input").forEach(i => i.disabled = false);
        }
    });
});
