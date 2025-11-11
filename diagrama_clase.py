<mxfile>
  <diagram name="Diagrama de Clases SIGA">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Clase Producto -->
        <mxCell id="producto" value="Producto" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;" vertex="1" parent="1">
          <mxCell x="100" y="100" width="180" height="150" as="geometry"/>
        </mxCell>
        <mxCell id="producto_attrs" value="- id: String&#10;- nombre: String&#10;- descripcion: String&#10;- precio: Double&#10;- stock: Integer&#10;- stockMinimo: Integer" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingTop=4;childLayout=stackLayout;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;" vertex="1" connectable="0" parent="producto">
          <mxCell y="30" width="180" height="90" as="geometry"/>
        </mxCell>
        <mxCell id="producto_methods" value="+ actualizarStock()&#10;+ verificarStockMinimo()&#10;+ buscar()" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingTop=4;childLayout=stackLayout;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;" vertex="1" connectable="0" parent="producto">
          <mxCell y="120" width="180" height="60" as="geometry"/>
        </mxCell>

        <!-- Clase Venta -->
        <mxCell id="venta" value="Venta" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;" vertex="1" parent="1">
          <mxCell x="400" y="100" width="180" height="150" as="geometry"/>
        </mxCell>
        <mxCell id="venta_attrs" value="- id: String&#10;- fecha: Date&#10;- total: Double&#10;- estado: String" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingTop=4;childLayout=stackLayout;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;" vertex="1" connectable="0" parent="venta">
          <mxCell y="30" width="180" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="venta_methods" value="+ calcularTotal()&#10;+ aplicarDescuento()&#10;+ generarBoleta()" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=4;spacingTop=4;childLayout=stackLayout;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;" vertex="1" connectable="0" parent="venta">
          <mxCell y="90" width="180" height="60" as="geometry"/>
        </mxCell>

        <!-- Relaciones -->
        <mxCell id="rel1" value="1 *" style="edgeStyle=entityRelationEdgeStyle;startArrow=ERone;startFill=1;endArrow=ERmany;endFill=0;" edge="1" parent="1" source="venta" target="producto">
          <mxCell width="100" height="100" relative="1" as="geometry">
            <mxPoint x="490" y="150" as="sourcePoint"/>
            <mxPoint x="190" y="150" as="targetPoint"/>
          </mxCell>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>