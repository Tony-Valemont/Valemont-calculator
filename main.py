import flet as ft

def main(page: ft.Page):
    # Настройки страницы
    page.title = "Gold Calculator"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.bgcolor = "black"

    GOLD = "#D4AF37"
    DARK_GOLD = "#9E7C19"

    def input_box(label=""):
        return ft.Container(
            width=260,
            height=52,
            alignment=ft.Alignment(0, 0), 
            border_radius=16,
            border=ft.border.all(1, GOLD),
            content=ft.TextField(
                border=ft.InputBorder.NONE,
                text_align=ft.TextAlign.CENTER,
                keyboard_type=ft.KeyboardType.NUMBER,
                hint_text=label,
                text_style=ft.TextStyle(size=22, color=GOLD, weight="bold"),
                bgcolor="transparent"
            )
        )

    weight_box = input_box("0.00")
    probe_box = input_box("585")

    result_text = ft.Text("0.00", size=32, weight="bold", color=GOLD)

    def calculate(e):
        try:
            w_val = weight_box.content.value
            p_val = probe_box.content.value
            weight = float(w_val.replace(",", ".") if w_val else 0)
            probe = float(p_val.replace(",", ".") if p_val else 585)
            
            if weight > 0 and probe > 0:
                result = (weight * (probe / 1000)) / 0.585
                result_text.value = f"{result:.2f}"
            else:
                result_text.value = "0.00"
        except ValueError:
            result_text.value = "---"
        page.update()

    calculate_button = ft.Container(
        width=260,
        height=56,
        alignment=ft.Alignment(0, 0),
        border_radius=20,
        bgcolor=GOLD,
        on_click=calculate,
        content=ft.Text("CALCULATE", size=18, weight="bold", color="black"),
    )

    page.add(
        ft.Container(
            expand=True,
            padding=ft.padding.symmetric(horizontal=24),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=28,
                controls=[
                    ft.Text("WEIGHT (g)", color=GOLD),
                    weight_box,
                    ft.Text("PURITY (‰)", color=GOLD),
                    probe_box,
                    result_text,
                    calculate_button
                ]
            )
        )
    )

ft.app(target=main)