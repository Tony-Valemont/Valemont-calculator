import flet as ft

def main(page: ft.Page):
    # Максимально простые настройки
    page.title = "VALEMONT"
    page.bgcolor = "#000000"
    page.padding = 20
    page.horizontal_alignment = "center"
    page.scroll = "auto"

    GOLD = "#D4AF37"
    INPUT_BG = "#121212"

    # Поля ввода — ТОЛЬКО через label/value
    weight_input = ft.TextField(
        label="ВЕС (ГРАММЫ)",
        value="",
        width=280,
        text_align="center",
        bgcolor=INPUT_BG,
        border_color=GOLD,
        color="white"
    )

    source_probe = ft.TextField(
        label="ИСХОДНАЯ ПРОБА",
        value="",
        width=280,
        text_align="center",
        bgcolor=INPUT_BG,
        border_color=GOLD,
        color="white"
    )

    target_probe = ft.TextField(
        label="ЦЕЛЕВАЯ ПРОБА",
        value="585",
        width=280,
        text_align="center",
        bgcolor=INPUT_BG,
        border_color=GOLD,
        color="white"
    )

    # Результат
    result_text = ft.Text("0.000", size=42, color=GOLD, weight="bold")

    def calculate(e):
        try:
            w = float((weight_input.value or "0").replace(",", "."))
            p1 = float((source_probe.value or "0").replace(",", "."))
            p2 = float((target_probe.value or "585").replace(",", "."))

            if w > 0 and p1 > 0 and p2 > 0:
                res = (w * p1) / p2
                result_text.value = "{:.3f}".format(res)
            else:
                result_text.value = "0.000"
        except:
            result_text.value = "Ошибка"

        page.update()

    # Кнопка — старый синтаксис
    calc_button = ft.ElevatedButton(
        "РАССЧИТАТЬ",
        bgcolor=GOLD,
        color="black",
        width=280,
        height=50,
        on_click=calculate
    )

    # Интерфейс
    page.add(
        ft.Column(
            spacing=18,
            horizontal_alignment="center",
            controls=[
                ft.Text("VALEMONT", size=32, color=GOLD, weight="bold"),
                ft.Text("ЮВЕЛИРНЫЙ ИНСТРУМЕНТ", size=11, color=GOLD),
                weight_input,
                source_probe,
                target_probe,
                ft.Text("ИТОГОВЫЙ ВЕС", size=12, color=GOLD),
                result_text,
                calc_button
            ]
        )
    )

ft.app(target=main)