import flet as ft
from flet import (
    Page, Container, Row, Column, Text, IconButton, 
    NavigationBar, NavigationDestination, Icon, 
    DataTable, DataColumn, DataRow, DataCell, 
    TextField, ElevatedButton, Dropdown, 
    Tabs, Tab, BarChart, PieChart, colors, 
    dropdown, icons, alignment
)
import random

# Datos de ejemplo
componentes = [
    {"id": 1, "nombre": "Procesador Intel i7", "tipo": "CPU", "precio": 350, "stock": 15},
    {"id": 2, "nombre": "Memoria RAM 16GB", "tipo": "RAM", "precio": 80, "stock": 30},
    {"id": 3, "nombre": "SSD 1TB", "tipo": "Almacenamiento", "precio": 120, "stock": 25},
    {"id": 4, "nombre": "Tarjeta Gráfica RTX 3070", "tipo": "GPU", "precio": 550, "stock": 8},
    {"id": 5, "nombre": "Placa Base ASUS", "tipo": "Motherboard", "precio": 180, "stock": 12},
    {"id": 6, "nombre": "Fuente 750W", "tipo": "PSU", "precio": 90, "stock": 20},
    {"id": 7, "nombre": "Gabinete ATX", "tipo": "Case", "precio": 70, "stock": 18},
    {"id": 8, "nombre": "Monitor 27\"", "tipo": "Periférico", "precio": 250, "stock": 10},
    {"id": 41, "nombre": "Tarsjeta Gráfica RTX 3070", "tipo": "GPU", "precio": 550, "stock": 8},
    {"id": 55, "nombre": "Plasca Base ASUS", "tipo": "Motherboard", "precio": 180, "stock": 12},
    {"id": 66, "nombre": "Fue}nte 750W", "tipo": "PSU", "precio": 90, "stock": 20},
    {"id": 37, "nombre": "Gab{inete ATX", "tipo": "Case", "precio": 70, "stock": 18},
    {"id": 58, "nombre": "Moñnitor 27\"", "tipo": "Periférico", "precio": 250, "stock": 10},
    {"id": 441, "nombre": "Tlarjeta Gráfica RTX 3070", "tipo": "GPU", "precio": 550, "stock": 8},
    {"id": 355, "nombre": "Plhaca Base ASUS", "tipo": "Motherboard", "precio": 180, "stock": 12},
    {"id": 166, "nombre": "Fuegnte 750W", "tipo": "PSU", "precio": 90, "stock": 20},
    {"id": 23537, "nombre": "Gafbinete ATX", "tipo": "Case", "precio": 70, "stock": 18},
    {"id": 558, "nombre": "Modnitor 27\"", "tipo": "Periférico", "precio": 250, "stock": 10}
    
]

tipos_componentes = ["Todos", "CPU", "RAM", "Almacenamiento", "GPU", "Motherboard", "PSU", "Case", "Periférico"]

def main(page: Page):
    page.title = "Gestión de Componentes"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    
    # Estado de la aplicación
    componentes_filtrados = componentes.copy()
    componentes_presupuesto = []
    vista_actual = 0
    
    # Estilos comunes
    estilo_contenedor = {
        "padding": 15,
        "border_radius": 10,
        "bgcolor": "#ffffff",
        "shadow": ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color=ft.colors.with_opacity(0.2, ft.colors.BLACK),
        )
    }
    
    color_acento = "#6750A4"  # Violeta como color de acento
    
    # Función para calcular el total del presupuesto
    def calcular_total():
        return sum(item["precio"] * item["cantidad"] for item in componentes_presupuesto)
    
    # Vista de Stock
    def crear_vista_stock():
        # Función para filtrar componentes
        def filtrar_componentes(e):
            texto_busqueda = campo_busqueda.value.lower()
            tipo_seleccionado = selector_tipo.value
            
            componentes_filtrados.clear()
            for comp in componentes:
                if texto_busqueda in comp["nombre"].lower() and (
                    tipo_seleccionado == "Todos" or comp["tipo"] == tipo_seleccionado
                ):
                    componentes_filtrados.append(comp)
            
            actualizar_tabla_stock()
            page.update()
        
        # Función para actualizar la tabla de stock
        def actualizar_tabla_stock():
            tabla_stock.rows.clear()
            for comp in componentes_filtrados:
                color_stock = "#4CAF50" if comp["stock"] > 10 else "#FFC107" if comp["stock"] > 5 else "#F44336"
                tabla_stock.rows.append(
                    DataRow(
                        cells=[
                            DataCell(Text(comp["nombre"])),
                            DataCell(Text(comp["tipo"])),
                            DataCell(Text(f"${comp['precio']}")),
                            DataCell(
                                Container(
                                    content=Text(str(comp["stock"]), color="#ffffff"),
                                    bgcolor=color_stock,
                                    border_radius=5,
                                    padding=5,
                                    alignment=alignment.center,
                                    width=50
                                )
                            ),
                        ]
                    )
                )
        
        # Función para agregar nuevo componente
        def mostrar_dialogo_agregar(e):
            def cerrar_dialogo(e):
                dialogo.open = False
                page.update()
            
            def guardar_componente(e):
                nuevo_id = max(comp["id"] for comp in componentes) + 1
                nuevo_componente = {
                    "id": nuevo_id,
                    "nombre": campo_nombre.value,
                    "tipo": campo_tipo.value,
                    "precio": float(campo_precio.value),
                    "stock": int(campo_stock.value)
                }
                componentes.append(nuevo_componente)
                componentes_filtrados.append(nuevo_componente)
                actualizar_tabla_stock()
                cerrar_dialogo(e)
            
            campo_nombre = TextField(label="Nombre del componente", autofocus=True)
            campo_tipo = Dropdown(
                label="Tipo",
                options=[dropdown.Option(t) for t in tipos_componentes if t != "Todos"]
            )
            campo_precio = TextField(label="Precio", keyboard_type=ft.KeyboardType.NUMBER)
            campo_stock = TextField(label="Stock", keyboard_type=ft.KeyboardType.NUMBER)
            
            dialogo = ft.AlertDialog(
                title=Text("Agregar nuevo componente"),
                content=Column([
                    campo_nombre,
                    campo_tipo,
                    campo_precio,
                    campo_stock,
                ], spacing=10, width=400),
                actions=[
                    ElevatedButton("Cancelar", on_click=cerrar_dialogo),
                    ElevatedButton("Guardar", on_click=guardar_componente, bgcolor=color_acento, color="white"),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
            
            page.dialog = dialogo
            dialogo.open = True
            page.update()
        
        # Componentes de la vista de Stock
        campo_busqueda = TextField(
            label="Buscar componente",
            prefix_icon=icons.SEARCH,
            on_change=filtrar_componentes,
            expand=True
        )
        
        selector_tipo = Dropdown(
            label="Filtrar por tipo",
            options=[dropdown.Option(t) for t in tipos_componentes],
            value="Todos",
            on_change=filtrar_componentes,
            width=200
        )
        
        boton_agregar = ElevatedButton(
            "Agregar componente",
            icon=icons.ADD,
            on_click=mostrar_dialogo_agregar,
            bgcolor=color_acento,
            color="white"
        )
        
        tabla_stock = DataTable(
            columns=[
                DataColumn(Text("Nombre")),
                DataColumn(Text("Tipo")),
                DataColumn(Text("Precio")),
                DataColumn(Text("Stock")),
            ],
            rows=[],
            border_radius=10,
            border=ft.border.all(1, "#EEEEEE"),
            vertical_lines=ft.border.BorderSide(1, "#EEEEEE"),
            horizontal_lines=ft.border.BorderSide(1, "#EEEEEE"),
            sort_column_index=0,
            sort_ascending=True,
            heading_row_height=50,
            data_row_min_height=50,
            data_row_max_height=80,
            column_spacing=50,
            expand=True
        )
        
        actualizar_tabla_stock()
        
        return Container(
            content=Column([
                Row([
                    campo_busqueda,
                    selector_tipo,
                ], spacing=10, alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                tabla_stock,
                Row([ft.Container(expand=True), boton_agregar], alignment=ft.MainAxisAlignment.END)
            ], spacing=20, expand=True),
            **estilo_contenedor,
            expand=True
        )
    
    # Vista de Presupuesto
    def crear_vista_presupuesto():
        # Función para actualizar la tabla de presupuesto
        def actualizar_tabla_presupuesto():
            tabla_presupuesto.rows.clear()
            for item in componentes_presupuesto:
                tabla_presupuesto.rows.append(
                    DataRow(
                        cells=[
                            DataCell(Text(item["nombre"])),
                            DataCell(Text(f"${item['precio']}")),
                            DataCell(
                                Row([
                                    IconButton(
                                        icon=icons.REMOVE,
                                        icon_color=color_acento,
                                        on_click=lambda e, i=item: cambiar_cantidad(i, -1)
                                    ),
                                    Text(str(item["cantidad"])),
                                    IconButton(
                                        icon=icons.ADD,
                                        icon_color=color_acento,
                                        on_click=lambda e, i=item: cambiar_cantidad(i, 1)
                                    ),
                                ], spacing=0, alignment=ft.MainAxisAlignment.CENTER)
                            ),
                            DataCell(Text(f"${item['precio'] * item['cantidad']}")),
                        ]
                    )
                )
            texto_total.value = f"Total: ${calcular_total()}"
            page.update()
        
        # Función para cambiar la cantidad de un componente
        def cambiar_cantidad(item, delta):
            item["cantidad"] += delta
            if item["cantidad"] <= 0:
                componentes_presupuesto.remove(item)
            actualizar_tabla_presupuesto()
        
        # Función para agregar componente al presupuesto
        def agregar_al_presupuesto(e):
            comp_id = int(selector_componente.value)
            comp = next((c for c in componentes if c["id"] == comp_id), None)
            
            if comp:
                # Verificar si ya existe en el presupuesto
                item_existente = next((i for i in componentes_presupuesto if i["id"] == comp_id), None)
                
                if item_existente:
                    item_existente["cantidad"] += 1
                else:
                    componentes_presupuesto.append({
                        "id": comp["id"],
                        "nombre": comp["nombre"],
                        "precio": comp["precio"],
                        "cantidad": 1
                    })
                
                actualizar_tabla_presupuesto()
        
        # Función para guardar presupuesto
        def guardar_presupuesto(e):
            if not componentes_presupuesto:
                return
                
            dialogo = ft.AlertDialog(
                title=Text("Presupuesto guardado"),
                content=Text(f"Se ha guardado el presupuesto por un total de ${calcular_total()}"),
                actions=[
                    ElevatedButton("Aceptar", on_click=lambda e: setattr(dialogo, "open", False))
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
            
            page.dialog = dialogo
            dialogo.open = True
            page.update()
        
        # Componentes de la vista de Presupuesto
        selector_componente = Dropdown(
            label="Seleccionar componente",
            options=[dropdown.Option(key=str(c["id"]), text=f"{c['nombre']} - ${c['precio']}") for c in componentes],
            width=400
        )
        
        boton_agregar_componente = ElevatedButton(
            "Agregar al presupuesto",
            icon=icons.ADD_SHOPPING_CART,
            on_click=agregar_al_presupuesto,
            bgcolor=color_acento,
            color="white"
        )
        
        tabla_presupuesto = DataTable(
            columns=[
                DataColumn(Text("Componente")),
                DataColumn(Text("Precio unitario")),
                DataColumn(Text("Cantidad")),
                DataColumn(Text("Subtotal")),
            ],
            rows=[],
            border_radius=10,
            border=ft.border.all(1, "#EEEEEE"),
            vertical_lines=ft.border.BorderSide(1, "#EEEEEE"),
            horizontal_lines=ft.border.BorderSide(1, "#EEEEEE"),
            heading_row_height=50,
            data_row_min_height=50,
            data_row_max_height=80,
            column_spacing=50,
            expand=True
        )
        
        texto_total = Text(
            f"Total: ${calcular_total()}",
            size=20,
            weight=ft.FontWeight.BOLD,
            color=color_acento
        )
        
        boton_guardar = ElevatedButton(
            "Guardar presupuesto",
            icon=icons.SAVE,
            on_click=guardar_presupuesto,
            bgcolor=color_acento,
            color="white"
        )
        
        return Container(
            content=Column([
                Row([
                    selector_componente,
                    boton_agregar_componente,
                ], spacing=10, alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                tabla_presupuesto,
                Row([
                    texto_total,
                    ft.Container(expand=True),
                    boton_guardar
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            ], spacing=20, expand=True),
            **estilo_contenedor,
            expand=True
        )
    
    # Vista de Dashboard
    def crear_vista_dashboard():
        # Datos para los gráficos
        componentes_mas_usados = [
            {"nombre": "Procesador Intel i7", "cantidad": 45},
            {"nombre": "Memoria RAM 16GB", "cantidad": 72},
            {"nombre": "SSD 1TB", "cantidad": 58},
            {"nombre": "Tarjeta Gráfica RTX 3070", "cantidad": 32},
            {"nombre": "Placa Base ASUS", "cantidad": 29},
        ]
        
        componentes_stock_bajo = [c for c in componentes if c["stock"] < 10]
        
        # Crear gráfico de barras para componentes más usados
        grafico_barras = Container(
            content=Column([
                Text("Componentes más utilizados", size=16, weight=ft.FontWeight.BOLD),
                Container(
                    content=ft.BarChart(
                        bar_groups=[
                            ft.BarChartGroup(
                                x=i,
                                bar_rods=[
                                    ft.BarChartRod(
                                        from_y=0,
                                        to_y=comp["cantidad"],
                                        width=20,
                                        color=color_acento,
                                        tooltip=f"{comp['nombre']}: {comp['cantidad']}",
                                        border_radius=0,
                                    ),
                                ],
                            )
                            for i, comp in enumerate(componentes_mas_usados)
                        ],
                        bottom_axis=ft.ChartAxis(
                            labels=[
                                ft.ChartAxisLabel(
                                    value=i,
                                    label=Text(comp["nombre"].split()[0], size=10, rotation=ft.pi/4)
                                )
                                for i, comp in enumerate(componentes_mas_usados)
                            ],
                            labels_size=32,
                        ),
                        left_axis=ft.ChartAxis(
                            labels=[
                                ft.ChartAxisLabel(value=0, label=Text("0")),
                                ft.ChartAxisLabel(value=25, label=Text("25")),
                                ft.ChartAxisLabel(value=50, label=Text("50")),
                                ft.ChartAxisLabel(value=75, label=Text("75")),
                            ],
                        ),
                        horizontal_grid_lines=ft.ChartGridLines(
                            color=colors.with_opacity(0.2, colors.GREY),
                            width=1,
                            dash_pattern=[3, 3],
                        ),
                        tooltip_bgcolor=colors.with_opacity(0.8, colors.GREY_800),
                        max_y=80,
                        interactive=True,
                        expand=True,
                    ),
                    height=250,
                    expand=True,
                ),
            ]),
            **estilo_contenedor,
            expand=True,
        )
        
        # Crear gráfico circular para stock bajo
        grafico_circular = Container(
            content=Column([
                Text("Componentes con stock bajo", size=16, weight=ft.FontWeight.BOLD),
                Container(
                    content=ft.PieChart(
                        sections=[
                            ft.PieChartSection(
                                value=comp["stock"],
                                title=f"{comp['nombre']}",
                                title_style=ft.TextStyle(
                                    size=12,
                                    color=ft.colors.WHITE,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                color=ft.colors.from_rgb(
                                    random.randint(100, 200),
                                    random.randint(100, 200),
                                    random.randint(100, 200)
                                ),
                                radius=80,
                            )
                            for comp in componentes_stock_bajo
                        ],
                        sections_space=1,
                        center_space_radius=40,
                        expand=True,
                    ),
                    height=250,
                    expand=True,
                ),
            ]),
            **estilo_contenedor,
            expand=True,
        )
        
        # Crear tarjetas de resumen
        tarjeta_total_componentes = Container(
            content=Column([
                Text("Total de componentes", size=14, color=ft.colors.GREY_700),
                Text(str(sum(c["stock"] for c in componentes)), size=28, weight=ft.FontWeight.BOLD),
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            **estilo_contenedor,
            height=100,
            expand=True,
        )
        
        tarjeta_valor_inventario = Container(
            content=Column([
                Text("Valor del inventario", size=14, color=ft.colors.GREY_700),
                Text(f"${sum(c['stock'] * c['precio'] for c in componentes):,.2f}", size=28, weight=ft.FontWeight.BOLD),
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            **estilo_contenedor,
            height=100,
            expand=True,
        )
        
        tarjeta_componentes_agotados = Container(
            content=Column([
                Text("Componentes agotados", size=14, color=ft.colors.GREY_700),
                Text(str(sum(1 for c in componentes if c["stock"] == 0)), size=28, weight=ft.FontWeight.BOLD),
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            **estilo_contenedor,
            height=100,
            expand=True,
        )
        
        return Column([
            Row([
                tarjeta_total_componentes,
                tarjeta_valor_inventario,
                tarjeta_componentes_agotados,
            ], spacing=10, expand=True),
            Row([
                grafico_barras,
                grafico_circular,
            ], spacing=10, expand=True),
        ], spacing=10, expand=True)
    
    # Función para cambiar de vista
    def cambiar_vista(e):
        nonlocal vista_actual
        vista_actual = e.control.selected_index
        actualizar_contenido()
        page.update()
    
    # Función para actualizar el contenido según la vista actual
    def actualizar_contenido():
        if vista_actual == 0:
            contenido_principal.content = crear_vista_stock()
        elif vista_actual == 1:
            contenido_principal.content = crear_vista_presupuesto()
        else:
            contenido_principal.content = crear_vista_dashboard()
    
    # Barra de navegación inferior
    barra_navegacion = NavigationBar(
        destinations=[
            NavigationDestination(
                icon=icons.INVENTORY,
                label="Stock",
            ),
            NavigationDestination(
                icon=icons.CALCULATE,
                label="Presupuesto",
            ),
            NavigationDestination(
                icon=icons.DASHBOARD,
                label="Dashboard",
            ),
        ],
        selected_index=vista_actual,
        on_change=cambiar_vista,
        bgcolor="#ffffff",
        shadow_color=ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color=ft.colors.with_opacity(0.2, ft.colors.BLACK),
        ),
    )
    
    # Contenedor principal para el contenido
    contenido_principal = Container(
        expand=True,
        padding=10,
    )
    
    # Inicializar la primera vista
    actualizar_contenido()
    
    # Estructura principal de la aplicación
    page.add(
        Container(
            content=Column([
                contenido_principal,
                barra_navegacion,
            ]),
            expand=True,
            bgcolor="#F5F5F5",
        )
    )

ft.app(target=main)