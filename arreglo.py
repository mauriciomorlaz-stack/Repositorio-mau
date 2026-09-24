DEPARTAMENTOS = ["Ropa", "Deportes", "Juguetería"]
MESES = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

class GestionVentas:
    def __init__(self):
        # Arreglo bidimensional de 12 filas (meses) x 3 columnas (departamentos)
        self.ventas = [[0.0 for _ in range(3)] for _ in range(12)]

    # 1. Método para insertar elementos en el arreglo
    def insertar_venta(self, mes_idx, depto_idx, monto):
        if 0 <= mes_idx < 12 and 0 <= depto_idx < 3:
            self.ventas[mes_idx][depto_idx] = float(monto)
            print(f"Venta de ${monto:.2f} registrada en {MESES[mes_idx]} - {DEPARTAMENTOS[depto_idx]}")
        else:
            print("Índice de mes o departamento fuera de rango.")

    # 2. Método para buscar un elemento en particular
    def buscar_venta(self, mes_idx, depto_idx):
        if 0 <= mes_idx < 12 and 0 <= depto_idx < 3:
            monto = self.ventas[mes_idx][depto_idx]
            print(f"La venta en {MESES[mes_idx]} ({DEPARTAMENTOS[depto_idx]}) es: ${monto:.2f}")
            return monto
        else:
            print("Índice de mes o departamento fuera de rango.")
            return None

    # 3. Método para eliminar una venta en particular (restablece a 0.0)
    def eliminar_venta(self, mes_idx, depto_idx):
        if 0 <= mes_idx < 12 and 0 <= depto_idx < 3:
            self.ventas[mes_idx][depto_idx] = 0.0
            print(f"Venta eliminada (reiniciada a $0.00) en {MESES[mes_idx]} - {DEPARTAMENTOS[depto_idx]}")
        else:
            print("Índice de mes o departamento fuera de rango.")

if __name__ == "__main__":
    tienda = GestionVentas()
    
    # Pruebas de los métodos
    tienda.insertar_venta(0, 0, 1500.50)  # Enero, Ropa
    tienda.buscar_venta(0, 0)
    tienda.eliminar_venta(0, 0)
    tienda.buscar_venta(0, 0)
