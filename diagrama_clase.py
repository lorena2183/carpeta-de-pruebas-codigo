class DiagramaClases:
    def __init__(self):
        self.clases = []
    
    def agregar_clase(self, nombre, atributos, metodos):
        clase = {
            'nombre': nombre,
            'atributos': atributos,
            'metodos': metodos
        }
        self.clases.append(clase)
    
    def agregar_relacion(self, clase_origen, clase_destino, tipo, multiplicidad):
        relacion = {
            'origen': clase_origen,
            'destino': clase_destino,
            'tipo': tipo,
            'multiplicidad': multiplicidad
        }
        # Implementar lógica de relaciones
    
    def generar_diagrama(self):
        print("=== DIAGRAMA DE CLASES SIGA ===")
        for clase in self.clases:
            self._dibujar_clase(clase)
    
    def _dibujar_clase(self, clase):
        print(f"\n┌─────────────────┐")
        print(f"│   {clase['nombre']:^13}  │")
        print(f"├─────────────────┤")
        
        for attr in clase['atributos']:
            print(f"│ {attr:15} │")
        
        if clase['atributos']:
            print(f"├─────────────────┤")
        
        for metodo in clase['metodos']:
            print(f"│ {metodo:15} │")
        
        print(f"└─────────────────┘")

# Uso del generador
def crear_diagrama_clases():
    diagrama = DiagramaClases()
    
    # Definir clases del sistema
    diagrama.agregar_clase(
        "Producto",
        ["- id: String", "- nombre: String", "- precio: Double", "- stock: Int"],
        ["+ actualizarStock()", "+ buscar()"]
    )
    
    diagrama.agregar_clase(
        "Venta",
        ["- id: String", "- fecha: Date", "- total: Double"],
        ["+ calcularTotal()", "+ generarBoleta()"]
    )
    
    diagrama.agregar_clase(
        "Cliente",
        ["- id: String", "- nombre: String", "- rut: String"],
        ["+ registrar()", "+ buscar()"]
    )
    
    diagrama.generar_diagrama()

# Ejecutar
crear_diagrama_clases()