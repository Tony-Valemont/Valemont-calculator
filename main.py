import flet as ft

def main(page: ft.Page):
    # Максимально лёгкие настройки (быстро грузится)
    page.title = "VALEMONT"
    page.bgcolor = "#000000"
    page.padding = 16
    page.horizontal_alignment = "center"
    page.scroll = "auto"

    GOLD = "#D4AF37"

    # Поля ввода — цифры на телефоне
    weight_input = ft.TextField(
        label="ВЕС (Г)",
        value="",
        width=260,
        text_align="center",
        border_color=GOLD,
        color="white",
        keyboard_type=ft.KeyboardType.NUMBER
    )

    source_probe = ft.TextField(
        label="ИСХОДНАЯ ПРОБА",
        value="",
        width=260,
        text_align="center",
        border_color=GOLD,
        color="white",
        keyboard_type=ft.KeyboardType.NUMBER
    )

    target_probe = ft.TextField(
        label="ЦЕЛЕВАЯ ПРОБА",
        value="585",
        width=260,
        text_align="center",
        border_color=GOLD,
        color="white",
        keyboard_type=ft.KeyboardType.NUMBER
    )

    result_text = ft.Text("0.000", size=36, color=GOLD)

    def calculate(e):
        try:
            w = float((weight_input.value or "0").replace(",", "."))
            p1 = float((source_probe.value or "0").replace(",", "."))
            p2 = float((target_probe.value or "585").replace(",", "."))

            if w > 0 and p1 > 0 and p2 > 0:
                result_text.value = "{:.3f}".format((w * p1) / p2)
            else:
                result_text.value = "0.000"
        except:
            result_text.value = "Ошибка"

        page.update()

    calc_button = ft.ElevatedButton(
        "РАССЧИТАТЬ",
        bgcolor=GOLD,
        color="black",
        width=260,
        height=48,
        on_click=calculate
    )

    page.add(
        ft.Column(
            spacing=14,
            horizontal_alignment="center",
            controls=[
                ft.Text("VALEMONT", size=28, color=GOLD),
                ft.Text("ЮВЕЛИРНЫЙ КАЛЬКУЛЯТОР", size=10, color=GOLD),
                weight_input,
                source_probe,
                target_probe,
                result_text,
                calc_button
            ]
        )
    )

# 🔑 ВАЖНО: открывается на телефоне
ft.app(target=main, view=ft.AppView.WEB_BROWSER)