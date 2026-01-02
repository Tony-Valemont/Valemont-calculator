import flet as ft

def main(page: ft.Page):
    page.title = "Золотой калькулятор"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.bgcolor = "black"
    page.window_width = 360
    page.window_height = 800

    GOLD = "#D4AF37"
    DARK_GOLD = "#9E7C19"

    def input_box(label=""):
        """Стилизованное поле ввода"""
        text_field = ft.TextField(
            border=ft.InputBorder.NONE,
            text_align=ft.TextAlign.CENTER,
            keyboard_type=ft.KeyboardType.NUMBER,
            hint_text=label,
            text_style=ft.TextStyle(size=22, color=GOLD, weight="bold"),
            bgcolor="transparent",
            cursor_color=GOLD
        )
        return ft.Container(
            width=260,
            height=55,
            alignment=ft.Alignment.center,
            border_radius=16,
            border=ft.border.all(1, GOLD),
            content=text_field
        )

    weight_box = input_box("0.000")
    probe_box = input_box("585")

    result_text = ft.Text("0.000", size=36, weight="bold", color=GOLD)

    def calculate(e):
        try:
            w_val = weight_box.content.value or "0"
            p_val = probe_box.content.value or "585"
            
            weight = float(w_val.replace(",", "."))
            probe = float(p_val.replace(",", "."))
            
            if weight > 0 and probe > 0:
                result = (weight * (probe / 1000)) / 0.585
                result_text.value = f"{result:.3f}"
            else:
                result_text.value = "0.000"
        except ValueError:
            result_text.value = "Ошибка"
        
        page.update()

    calculate_button = ft.Container(
        width=260,
        height=60,
        alignment=ft.Alignment.center,
        border_radius=20,
        bgcolor=GOLD,
        on_click=calculate,
        content=ft.Text("РАССЧИТАТЬ", size=18, weight="bold", color="black"),
        shadow=ft.BoxShadow(blur_radius=15, spread_radius=1, color=DARK_GOLD)
    )

    main_layout = ft.Container(
        expand=True,
        padding=24,
        bgcolor="black",
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=25,
            controls=[
                ft.Text("ВЕС (г)", color=GOLD, size=14, weight="bold"),
                weight_box,
                ft.Text("ПРОБА (‰)", color=GOLD, size=14, weight="bold"),
                probe_box,
                ft.Text("ИТОГ В 585 ПРОБЕ:", color=GOLD, size=12),
                result_text,
                calculate_button
            ]
        )
    )

    page.add(main_layout)

ft.app(target=main)