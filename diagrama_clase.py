from graphviz import Digraph

def crear_diagrama_clases():
    dot = Digraph(comment='Diagrama de Clases SIGA', format='png')
    dot.attr(rankdir='TB')  # Dirección de arriba a abajo

    # Definir las clases
    dot.node('Producto', '''Producto
| 
| - id: String
| - nombre: String
| - precio: Double
| - stock: Int
|
| + actualizarStock()
| + buscar()''', shape='record')

    dot.node('Venta', '''Venta
|
| - id: String
| - fecha: Date
| - total: Double
|
| + calcularTotal()
| + generarBoleta()''', shape='record')

    dot.node('Cliente', '''Cliente
|
| - id: String
| - nombre: String
| - rut: String
|
| + registrar()
| + buscar()''', shape='record')

    dot.node('DetalleVenta', '''DetalleVenta
|
| - cantidad: Int
| - subtotal: Double
|
| + calcularSubtotal()''', shape='record')

    # Relaciones
    dot.edge('Venta', 'Producto', label='1..*', dir='none')
    dot.edge('Venta', 'Cliente', label='1', dir='none')
    dot.edge('Venta', 'DetalleVenta', label='1..*', dir='none')

    # Guardar el diagrama
    dot.render('diagrama_clases_siga', view=True)

if __name__ == '__main__':
    crear_diagrama_clases()