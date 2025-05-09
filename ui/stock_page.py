import flet as ft
from utils.stock_logic import stock_logic_function as stock_logic
from const.constantes import tipos_componentes

def stock_view(page: ft.Page):
    def pop_up_agregar_componente(e):
        def cerrar_dialogo(e):
                dialogo.open = False
                page.update()
        def guardar_componente(e):
            pass
        campo_nombre = ft.TextField(label="Nombre del componente", autofocus=True)
        campo_tipo = ft.Dropdown(
            label="Tipo",
            options=[ft.dropdown.Option(t) for t in tipos_componentes if t != "Todos"]
        )
        campo_precio = ft.TextField(label="Precio", keyboard_type=ft.KeyboardType.NUMBER)
        campo_stock = ft.TextField(label="Stock", keyboard_type=ft.KeyboardType.NUMBER)
        campo_imagen = ft.TextField(label="Imagen", keyboard_type=ft.KeyboardType.URL)
        dialogo = ft.AlertDialog(
            title=ft.Text("Agregar nuevo componente"),
            content=ft.Column([
                campo_nombre,
                campo_tipo,
                campo_precio,
                campo_stock,
                campo_imagen
            ], spacing=10, width=400),
            actions=[
                ft.ElevatedButton("Cancelar", on_click=cerrar_dialogo),
                ft.ElevatedButton("Guardar", on_click=guardar_componente, bgcolor="#6750A4", color="white"),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        page.overlay.append(dialogo)
        dialogo.open = True
        page.update()
        
    def pop_up_eliminar_componente(e):
        pass
    def pop_up_modificar_componente(e):
        pass
    def ver_imagen_grande(imagen,nombre):
            if not imagen:
                return
            dialogo = ft.AlertDialog(
                title = ft.Text("Imagen de " + nombre),
                content=ft.Image(src=imagen, width=400, height=400, fit=ft.ImageFit.CONTAIN),
                actions=[ft.TextButton("Cerrar", on_click=lambda e: cerrar_dialogo(dialogo))],
            )
            page.overlay.append(dialogo)
            dialogo.open = True
            page.update()

    def cerrar_dialogo(dialogo):
            dialogo.open = False
            page.update()
    def componentes():
        
        Campo_busqueda = ft.TextField(label="Buscar",
            prefix_icon= ft.icons.SEARCH,
            on_change=stock_logic.filtrar_componentes,
            expand=True)
        
        selector_tipo = ft.Dropdown(
            label="Filtrar por tipo",
            options=stock_logic.obtener_tipos_componentes(),
            value="Todos",
            on_change=stock_logic.filtrar_componentes,
            expand=True,
        )

            
        def cargar_tabla():
            tabla_stock.rows.clear()  # por si se recarga
            componentes = stock_logic.cargar_componentes_stock()
            for c in componentes:
                if c.get("imagen"):
                    imagen_componente = ft.Image(src=c["imagen"], width=20, height=20,)
                else:
                    imagen_componente = ft.Text("") # Texto por defecto si no hay imagen
                fila = ft.DataRow(
                    on_select_changed=lambda e, src=c["imagen"]if c.get("imagen")else None,nombre= c["nombre"]: ver_imagen_grande(src,nombre),
                    cells=[
                        ft.DataCell(ft.Text(c["nombre"],overflow=True)),
                        ft.DataCell(ft.Text(c["tipo"],overflow=False)),
                        ft.DataCell(ft.Text(str(c["precio"]))),
                        ft.DataCell(ft.Text(str(c["stock"]))),
                        ft.DataCell(imagen_componente),  # imagen por ahora
                    ]
                )
                tabla_stock.rows.append(fila)

          # Llamás para llenar la tabla al inicio

        # Después la tabla la agregás al layout como ya venías haciendo

        tabla_stock = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Nombre")),
                ft.DataColumn(ft.Text("Tipo")),
                ft.DataColumn(ft.Text("Precio")),
                ft.DataColumn(ft.Text("Stock")),
                ft.DataColumn(ft.Text("Imagen")),
            ],
            rows=[],
            border_radius=5,
            border=ft.border.all(1, "#EEEEEE"),
        
            vertical_lines=ft.border.BorderSide(1, "#EEEEEE"),
            horizontal_lines=ft.border.BorderSide(1, "#EEEEEE"),
            heading_row_height=35,
            data_row_min_height=50,
            data_row_max_height=80,
            column_spacing=10,
            expand=True,
        )
        cargar_tabla()
        
        lv = ft.ListView(
            expand=1, 
            spacing=10, 
            padding=5,
        )
        lv.controls.append(tabla_stock)
        
        
        boton_agregar = ft.FloatingActionButton(
            icon=ft.icons.ADD,
            tooltip="Agregar",
            foreground_color=ft.colors.BLUE_300,
            on_click=pop_up_agregar_componente,
            scale=0.8
        )

        boton_eliminar = ft.FloatingActionButton(
            icon=ft.icons.DELETE,
            foreground_color=ft.colors.RED_300,
            tooltip="Eliminar",
            on_click=pop_up_eliminar_componente,
            scale=0.8
            )

        boton_modificar = ft.FloatingActionButton(
            icon=ft.icons.EDIT,
            foreground_color=ft.colors.YELLOW_300,
            tooltip="Modificar",
            on_click=pop_up_modificar_componente,
            scale=0.8
        )
        
        
        return ft.Container(
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[Campo_busqueda, selector_tipo],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10
                    ),
                    ft.Stack(
                        controls=[
                            lv,
                            ft.Container(
                                    ft.Row(
                                        controls=[boton_agregar,boton_eliminar,boton_modificar],
                                        alignment=ft.alignment.center),
                                   right=0,
                                   bottom=0)
                            
                        ],
                        alignment=ft.alignment.top_left,  # Alineación superior izquierda
                        expand=True,
                    )

                ],
            )
        )
    
    return componentes()
        
   