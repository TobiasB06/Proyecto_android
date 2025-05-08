import flet as ft
from utils.stock_logic import stock_logic_function as stock_logic
def stock_view():
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
            
            expand=True
        )
        lv=ft.ListView(expand=True, spacing=10, padding=10, auto_scroll=True)
        lv.controls.append(tabla_stock)
        boton_agregar = ft.IconButton(
            icon=ft.icons.ADD,
            tooltip="Agregar",
            icon_color=ft.colors.GREEN_300,
            on_click=pop_up_agregar_componente,
            scale=0.8,
            height=20
        )

        boton_eliminar = ft.IconButton(
            icon=ft.icons.DELETE,
            icon_color=ft.colors.RED_300,
            tooltip="Eliminar",
            on_click=pop_up_eliminar_componente,
            scale=0.8,
            height=20
            )

        boton_modificar = ft.IconButton(
            icon=ft.icons.EDIT,
            icon_color=ft.colors.YELLOW_300,
            tooltip="Modificar",
            on_click=pop_up_modificar_componente,
            scale=0.8,
            
        )

        return ft.Column(
            controls=[
                ft.Row(
                    controls=[Campo_busqueda, selector_tipo],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                ),
                lv,
                ft.Row(
                    controls=[
                        boton_agregar,boton_eliminar,boton_modificar,
                    ],
                    
                    alignment=ft.MainAxisAlignment.END,
                    spacing=10
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            expand=True
            )   
        
    def pop_up_agregar_componente(e):
        pass
    def pop_up_eliminar_componente(e):
        pass
    def pop_up_modificar_componente(e):
        pass
    return componentes()