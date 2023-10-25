const SALARIO_MINIMO_VIGENTE = 1160000.00; //

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('nomina-form');
    const resultado = document.getElementById('resultado');
    
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        calcularNomina();
    });
    
    function calcularNomina() {
        const nombre = document.getElementById('nombre').value;
        const edad = parseInt(document.getElementById('documento').value);
        const salarioMensual = parseFloat(document.getElementById('salario-mensual').value);
        const diasTrabajados = parseFloat(document.getElementById('dias-trabajados').value);
        const horasExtras = parseFloat(document.getElementById('horas-extras').value);
        const ventasMes = parseFloat(document.getElementById('ventas-mes').value);
        const tipoLibranza = document.getElementById('libranza').value;

        // Calcula la nómina
        const salarioTotal = (salarioMensual / 30) * diasTrabajados;
        const auxilioTransporte = calcularAuxilioTransporte(salarioTotal);
        const valorHorasExtras = (salarioMensual / 30 / 8) * horasExtras;
        const comisiones = calcularComisiones(ventasMes);
        const totalDevengado = salarioTotal + valorHorasExtras + auxilioTransporte + comisiones;

        // Aplicar descuentos
        const descuentoLibranza = calcularDescuentoLibranza(tipoLibranza);
        const descuentoSalud = totalDevengado * 0.12;
        const descuentoPension = totalDevengado * 0.165;
        const totalDeducido = descuentoLibranza + descuentoSalud + descuentoPension;

        const netoAPagar = totalDevengado - totalDeducido;

        // Muestra los resultados
        resultado.innerHTML = `
            <h2>Resultados de la Nómina para ${nombre}</h2>
            <p>SALARIO TOTAL: ${salarioTotal.toFixed(2)}</p>
            <p>AUXILIO TRANSPORTE: ${auxilioTransporte.toFixed(2)}</p>
            <p>VALOR HORAS EXTRAS: ${valorHorasExtras.toFixed(2)}</p>
            <p>COMISIONES: ${comisiones.toFixed(2)}</p>
            <p>TOTAL DEVENGADO: ${totalDevengado.toFixed(2)}</p>
            <h3>DESCUENTOS:</h3>
            <p>LIBRANZA: ${descuentoLibranza.toFixed(2)}</p>
            <p>SALUD: ${descuentoSalud.toFixed(2)}</p>
            <p>PENSIÓN: ${descuentoPension.toFixed(2)}</p>
            <h3>NETO A PAGAR: ${netoAPagar.toFixed(2)}</h3>
        `;
    }

    function calcularAuxilioTransporte(salarioTotal) {
        if (salarioTotal <= SALARIO_MINIMO_VIGENTE) {
            return 200000; // Valor del auxilio mensual vigente
        } else {
            return 0;
        }
    }

    function calcularComisiones(ventasMes) {
        if (ventasMes > 4000000) {
            return ventasMes * 0.035; // 3.5% de comisión
        } else {
            return ventasMes * 0.015; // 1.5% de comisión
        }
    }

    function calcularDescuentoLibranza(tipoLibranza) {
        switch (tipoLibranza) {
            case "educativo":
                return 200000;
            case "vivienda":
                return 300000;
            case "vehicular":
                return 150000;
            case "almacen":
                return 100000;
            default:
                return 0;
        }
    }
});
