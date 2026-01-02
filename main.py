import flet as ft

def main(page: ft.Page):
    # Настройки страницы для старых версий сервера
    page.title = "VALEMONT"
    page.bgcolor = "#000000"  # Глубокий черный фон
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    
    # Цвета для интерфейса
    GOLD = "#D4AF37"
    INPUT_BG = "#121212"

    # Поля ввода на русском языке
    weight_input = ft.TextField(
        label="ВЕС (ГРАММЫ)",
        text_align="center",
        width=280,
        bgcolor=INPUT_BG,
        border_color=GOLD,
        color="white"
    )

    source_probe = ft.TextField(
        label="ИСХОДНАЯ ПРОБА",
        text_align="center",
        width=280,
        bgcolor=INPUT_BG,
        border_color=GOLD,
        color="white"
    )

    target_probe = ft.TextField(
        label="ЦЕЛЕВАЯ ПРОБА",
        value="585",
        text_align="center",
        width=280,
        bgcolor=INPUT_BG,
        border_color=GOLD,
        color="white"
    )

    # Текст результата (золотой)
    result_text = ft.Text("0.000", size=45, color=GOLD)

    def calculate(e):
        try:
            # Читаем числа и меняем запятую на точку
            w = float(weight_input.value.replace(",", ".") or 0)
            p1 = float(source_probe.value.replace(",", ".") or 0)
            p2 = float(target_probe.value.replace(",", ".") or 585)
            
            if w > 0 and p1 > 0 and p2 > 0:
                # Универсальная формула (Вес * Проба1 / Проба2)
                res = (w * p1) / p2
                # Точность до 3 знаков (даст 5.858)
                result_text.value = "{:.3f}".format(res)
            else:
                result_text.value = "0.000"
        except:
            result_text.value = "Ошибка"
        page.update()

    # Кнопка «Рассчитать»
    calc_button = ft.Container(
        content=ft.Text("РАССЧИТАТЬ", color="black", size=16),
        bgcolor=GOLD,
        width=280,
        height=55,
        border_radius=15,
        alignment=ft.Alignment(0, 0),
        on_click=calculate
    )

    # Собираем интерфейс VALEMONT
    page.add(
        ft.Column(
            horizontal_alignment="center",
            spacing=20,
            controls=[
                ft.Text("VALEMONT", size=32, color=GOLD),
                ft.Text("ЮВЕЛИРНЫЙ ИНСТРУМЕНТ", size=10, color=GOLD),
                ft.Container(height=10),
                weight_input,
                source_probe,
                target_probe,
                ft.Text("ИТОГОВЫЙ ВЕС:", size=12, color=GOLD),
                result_text,
                ft.Container(height=10),
                calc_button
            ]
        )
    )

ft.app(target=main)