import flet as ft
import ui.stock_page as stock

def main(page: ft.Page):
    page.title = "Gestor de Componentes"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_width = 360
    page.window_height = 700

    # Páginas simuladas
    stock_view = stock.stock_view()
    presupuesto_view = ft.Text("🧮 Crear Presupuesto", size=30)
    dashboard_view = ft.Text("📊 Dashboard de Ventas y Stock", size=30)

    # Contenedor dinámico para la vista actual
    current_view = ft.Container(content=stock_view, padding=20)

    # Función para cambiar de pestaña
    def change_view(e):
        selected_index = nav_bar.selected_index
        if selected_index == 0:
            current_view.content = stock_view
        elif selected_index == 1:
            current_view.content = presupuesto_view
        elif selected_index == 2:
            current_view.content = dashboard_view
        page.update()

    # Barra inferior de navegación
    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.INVENTORY_2, label="Stock"),
            ft.NavigationDestination(icon=ft.icons.CALCULATE, label="Presupuesto"),
            ft.NavigationDestination(icon=ft.icons.INSIGHTS, label="Dashboard")
        ],
        selected_index=0,
        on_change=change_view
    )

    # Agregamos los elementos a la página
    page.add(
        current_view,
        nav_bar
    )

