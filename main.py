import flet as ft

def main(page: ft.Page):
    page.title = "Золотой калькулятор"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.bgcolor = "black"
    page.viewport_width = 360 

    GOLD = "#D4AF37"
    DARK_GOLD = "#9E7C19"

    def input_box(label=""):
        return ft.Container(
            width=260,
            height=55,
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

    weight_box = input_box("0.000")
    probe_box = input_box("585")
    result_text = ft.Text("0.000", size=36, weight="bold", color=GOLD)

    def calculate(e):
        try:
            w = float(weight_box.content.value.replace(",", ".") or 0)
            p = float(probe_box.content.value.replace(",", ".") or 585)
            if w > 0 and p > 0:
                res = (w * (p / 1000)) / 0.585
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

    page.add(
        ft.Container(
            expand=True,
            image_src="fon.jpg",
            image_fit=ft.ImageFit.COVER,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=25,
                controls=[
                    ft.Text("ВЕС (г)", color=GOLD, weight="bold"),
                    weight_box,
                    ft.Text("ПРОБА (‰)", color=GOLD, weight="bold"),
                    probe_box,
                    ft.Text("ИТОГ (585):", color=GOLD, size=12),
                    result_text,
                    ft.Container(height=10),
                    calculate_button
                ]
            )
        )
    )

ft.app(target=main)