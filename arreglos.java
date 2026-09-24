public class GestionVentas {

    // Arreglo bidimensional: 12 filas (meses) x 3 columnas (departamentos)
    private double[][] ventas;

    private static final String[] MESES = {
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    };
    private static final String[] DEPARTAMENTOS = {"Ropa", "Deportes", "Juguetería"};

    public GestionVentas() {
        this.ventas = new double[12][3];
    }

    // 1. Método para insertar elementos en el arreglo
    public void insertarVenta(int mesIdx, int deptoIdx, double monto) {
        if (mesIdx >= 0 && mesIdx < 12 && deptoIdx >= 0 && deptoIdx < 3) {
            this.ventas[mesIdx][deptoIdx] = monto;
            System.out.println("Venta de $" + monto + " registrada en " + MESES[mesIdx] + " - " + DEPARTAMENTOS[deptoIdx]);
        } else {
            System.out.println("Índices fuera de rango.");
        }
    }

    // 2. Método para buscar un elemento en particular
    public double buscarVenta(int mesIdx, int deptoIdx) {
        if (mesIdx >= 0 && mesIdx < 12 && deptoIdx >= 0 && deptoIdx < 3) {
            double monto = this.ventas[mesIdx][deptoIdx];
            System.out.println("La venta en " + MESES[mesIdx] + " (" + DEPARTAMENTOS[deptoIdx] + ") es: $" + monto);
            return monto;
        } else {
            System.out.println("Índices fuera de rango.");
            return -1;
        }
    }

    // 3. Método para eliminar una venta en particular (restablece a 0.0)
    public void eliminarVenta(int mesIdx, int deptoIdx) {
        if (mesIdx >= 0 && mesIdx < 12 && deptoIdx >= 0 && deptoIdx < 3) {
            this.ventas[mesIdx][deptoIdx] = 0.0;
            System.out.println("Venta eliminada (reiniciada a $0.0) en " + MESES[mesIdx] + " - " + DEPARTAMENTOS[deptoIdx]);
        } else {
            System.out.println("Índices fuera de rango.");
        }
    }
