# Sistema de Control de Ventas Mensuales por Departamento

Este proyecto implementa la gestión de ventas de una tienda utilizando arreglos bidimensionales (matrices) en **Java** y **Python**. El sistema almacena la información de 3 departamentos a lo largo de los 12 meses del año.

## Estructura de la Matriz

El arreglo bidimensional maneja una dimensión de **12 filas x 3 columnas**:
* **Filas (12):** Representan los meses del año (0 = Enero, 1 = Febrero, ..., 11 = Diciembre).
* **Columnas (3):** Representan los departamentos (0 = Ropa, 1 = Deportes, 2 = Juguetería).

---

## Explicación de los Métodos

### 1. Método para Insertar Elementos (`insertar_venta` / `insertarVenta`)
* **Descripción:** Permite asignar o actualizar el monto de venta en un mes y departamento específicos.
* **Funcionamiento:** Recibe tres parámetros (índice del mes, índice del departamento y monto). Valida que los índices estén dentro del rango permitido (meses de 0 a 11 y departamentos de 0 a 2) y asigna el valor ingresado a la posición de la matriz `matriz[mes][departamento]`.

### 2. Método para Buscar un Elemento (`buscar_venta` / `buscarVenta`)
* **Descripción:** Permite consultar la cantidad asignada a una celda en particular.
* **Funcionamiento:** Recibe los índices del mes y departamento. Tras validar que los índices sean correctos, obtiene e imprime el valor almacenado en esa celda específica.

### 3. Método para Eliminar una Venta (`eliminar_venta` / `eliminarVenta`)
* **Descripción:** Permite borrar un registro de venta existente.
* **Funcionamiento:** Como los arreglos estáticos no pueden cambiar dinámicamente de tamaño, la eliminación se realiza restableciendo el valor de la celda elegida a `0.0`.
