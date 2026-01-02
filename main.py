import flet as ft

def main(page: ft.Page):
    # Базовые настройки страницы
    page.title = "Золотой калькулятор"
    page.theme_mode = "dark"
    page.padding = 0
    # Серебристый фон страницы
    page.bgcolor = "#C0C0C0" 
    page.viewport_width = 360 

    GOLD = "#D4AF37"
    BLACK = "#000000"

    def input_box(label=""):
        return ft.Container(
            width=260,
            height=55,
            # Используем координаты вместо слов 'center', чтобы не было ошибок
            alignment=ft.Alignment(0, 0), 
            border_radius=16,
            border=ft.border.all(2, GOLD),
            bgcolor=BLACK,
            content=ft.TextField(
                border="none",
                text_align="center",
                keyboard_type="number",
                hint_text=label,
                text_style=ft.TextStyle(size=22, color=GOLD, weight="bold"),
            )
        )

    # Поля на русском языке
    weight_box = input_box("0.000")
    probe_box = input_box("585")
    result_text = ft.Text("0.000", size=36, weight="bold", color=BLACK)

    def calculate(e):
        try:
            w_val = weight_box.content.value.replace(",", ".")
            p_val = probe_box.content.value.replace(",", ".")
            w = float(w_val if w_val else 0)
            p = float(p_val if p_val else 585)
            
            if w > 0 and p > 0:
                res = (w * (p / 1000)) / 0.585
                # ТОЧНОСТЬ 3 ЗНАКА: выдаст 5.858
                result_text.value = "{:.3f}".format(res)
            else:
                result_text.value = "0.000"
        except:
            result_text.value = "Ошибка"
        page.update()

    calculate_button = ft.Container(
        width=260,
        height=60,
        alignment=ft.Alignment(0, 0),
        border_radius=20,
        bgcolor=BLACK,
        on_click=calculate,
        content=ft.Text("РАССЧИТАТЬ", size=18, weight="bold", color=GOLD)
    )

    # Главный экран
    page.add(
        ft.Container(
            expand=True,
            alignment=ft.Alignment(0, 0),
            content=ft.Column(
                alignment="center",
                horizontal_alignment="center",
                spacing=25,
                controls=[
                    ft.Text("ВЕС (г)", color=BLACK, weight="bold", size=16),
                    weight_box,
                    ft.Text("ПРОБА (‰)", color=BLACK, weight="bold", size=16),
                    probe_box,
                    ft.Text("ИТОГ (585):", color=BLACK, weight="bold", size=14),
                    result_text,
                    ft.Container(height=10),
                    calculate_button
                ]
            )
        )
    )

ft.app(target=main)