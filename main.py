import flet as ft

def main(page: ft.Page):
    # Настройки страницы
    page.title = "Золотой калькулятор"
    page.theme_mode = "dark"
    page.padding = 0
    page.viewport_width = 360 

    # Цвета
    GOLD = "#D4AF37"
    DARK_GOLD = "#9E7C19"
    # Цвета для серебристого фона
    SILVER_LIGHT = "#C0C0C0"
    SILVER_DARK = "#707070"

    def input_box(label=""):
        return ft.Container(
            width=260,
            height=55,
            alignment=ft.Alignment(0, 0), 
            border_radius=16,
            border=ft.border.all(1, GOLD),
            content=ft.TextField(
                border="none",
                text_align="center",
                keyboard_type="number",
                hint_text=label,
                text_style=ft.TextStyle(size=22, color=GOLD, weight="bold"),
                bgcolor="transparent"
            )
        )

    weight_box = input_box("0.000")
    probe_box = input_box("585")
    result_text = ft.Text("0.000", size=36, weight="bold", color=GOLD)

    def calculate(e):
        try:
            w_val = weight_box.content.value.replace(",", ".")
            p_val = probe_box.content.value.replace(",", ".")
            w = float(w_val if w_val else 0)
            p = float(p_val if p_val else 585)
            
            if w > 0 and p > 0:
                res = (w * (p / 1000)) / 0.585
                # ТОЧНОСТЬ 3 ЗНАКА: теперь будет 5.858
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
        bgcolor=GOLD,
        on_click=calculate,
        content=ft.Text("РАССЧИТАТЬ", size=18, weight="bold", color="black")
    )

    # Создаем программный серебристый фон вместо картинки
    page.add(
        ft.Container(
            expand=True,
            alignment=ft.Alignment(0, 0),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=[SILVER_DARK, SILVER_LIGHT, SILVER_DARK],
            ),
            content=ft.Column(
                alignment="center",
                horizontal_alignment="center",
                spacing=25,
                controls=[
                    ft.Text("ВЕС (г)", color=GOLD, weight="bold"),
                    weight_box,
                    ft.Text("ПРОБА (‰)", color=GOLD, weight="bold"),
                    probe_box,
                    ft.Text("ИТОГ (585):", color=GOLD, size=14),
                    result_text,
                    ft.Container(height=10),
                    calculate_button
                ]
            )
        )
    )

ft.app(target=main)