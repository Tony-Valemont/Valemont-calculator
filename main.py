import flet as ft

def main(page: ft.Page):
    page.title = "Ювелирный калькулятор"
    page.theme_mode = "dark"
    page.padding = 40
    page.bgcolor = "#000000"  # Чистый черный фон
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    # Адаптация для мобильных
    page.viewport_width = 360 

    GOLD = "#D4AF37"
    TEXT_FIELD_BG = "#1A1A1A"

    def input_style(hint):
        return ft.TextField(
            label=hint,
            label_style=ft.TextStyle(color=GOLD, size=12),
            border_color=GOLD,
            border_radius=15,
            bgcolor=TEXT_FIELD_BG,
            color=ft.colors.WHITE,
            text_align="center",
            keyboard_type="number",
            height=60,
            width=280,
            text_style=ft.TextStyle(weight="bold", size=18)
        )

    # Поля ввода
    weight_input = input_style("ВЕС (г)")
    source_probe = input_style("ИСХОДНАЯ ПРОБА")
    target_probe = input_style("ЦЕЛЕВАЯ ПРОБА (напр. 585)")
    # Установим 585 по умолчанию для удобства
    target_probe.value = "585"

    result_text = ft.Text("0.000", size=40, color=GOLD, weight="bold")

    def calculate(e):
        try:
            # Заменяем запятые на точки и считаем
            w = float(weight_input.value.replace(",", ".") or 0)
            p1 = float(source_probe.value.replace(",", ".") or 0)
            p2 = float(target_probe.value.replace(",", ".") or 585)
            
            if w > 0 and p1 > 0 and p2 > 0:
                # Универсальная формула: (Вес * Исходная) / Целевая
                res = (w * p1) / p2
                result_text.value = "{:.3f}".format(res)
            else:
                result_text.value = "0.000"
        except:
            result_text.value = "Ошибка"
        page.update()

    calc_button = ft.Container(
        content=ft.Text("РАССЧИТАТЬ", color="#000000", weight="bold", size=16),
        bgcolor=GOLD,
        padding=ft.padding.symmetric(vertical=15, horizontal=50),
        border_radius=20,
        on_click=calculate,
        alignment=ft.alignment.center,
        width=280
    )

    # Собираем интерфейс
    page.add(
        ft.Column(
            horizontal_alignment="center",
            spacing=20,
            controls=[
                ft.Text("PROFESSIONAL TOOL", color=GOLD, size=14, weight="bold", letter_spacing=2),
                weight_input,
                source_probe,
                target_probe,
                ft.Divider(height=20, color="transparent"),
                ft.Text("ИТОГОВЫЙ ВЕС:", color=GOLD, size=12, opacity=0.7),
                result_text,
                ft.Container(height=10),
                calc_button
            ]
        )
    )

ft.app(target=main)