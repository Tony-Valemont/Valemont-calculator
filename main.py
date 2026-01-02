import flet as ft

def main(page: ft.Page):
    # Настройки страницы
    page.title = "VALEMONT Calculator"
    page.theme_mode = "dark"
    page.padding = 30
    page.bgcolor = "#000000"  # Черный фон
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.viewport_width = 360 

    GOLD = "#D4AF37"
    INPUT_BG = "#121212"

    def create_input(label_text, default_val=""):
        """Создает поле ввода, совместимое со старыми версиями Flet"""
        return ft.TextField(
            label=label_text,
            value=default_val,
            text_align="center",
            width=280,
            height=60,
            bgcolor=INPUT_BG,
            border_color=GOLD,
            border_radius=15,
            color="white",
            keyboard_type="number",
            text_style=ft.TextStyle(size=18, weight="bold")
        )

    # Поля ввода
    weight_field = create_input("ВЕС (ГРАММ)")
    source_field = create_input("ИСХОДНАЯ ПРОБА")
    target_field = create_input("ЦЕЛЕВАЯ ПРОБА", "585")

    result_text = ft.Text("0.000", size=45, color=GOLD, weight="bold")

    def calculate_logic(e):
        try:
            # Читаем значения, заменяя запятую на точку
            w = float(weight_field.value.replace(",", ".") or 0)
            p1 = float(source_field.value.replace(",", ".") or 0)
            p2 = float(target_field.value.replace(",", ".") or 585)
            
            if w > 0 and p1 > 0 and p2 > 0:
                # Универсальная формула: (Вес * Исходная) / Целевая
                res = (w * p1) / p2
                # Формат .3f дает точность до 3 знаков (например, 5.858)
                result_text.value = "{:.3f}".format(res)
            else:
                result_text.value = "0.000"
        except:
            result_text.value = "Ошибка"
        page.update()

    # Кнопка
    calc_button = ft.Container(
        content=ft.Text("РАССЧИТАТЬ", color="black", weight="bold", size=16),
        bgcolor=GOLD,
        width=280,
        height=55,
        border_radius=20,
        alignment=ft.Alignment(0, 0),
        on_click=calculate_logic
    )

    # Собираем экран
    page.add(
        ft.Column(
            horizontal_alignment="center",
            spacing=20,
            controls=[
                ft.Text("VALEMONT", size=30, color=GOLD, weight="bold", letter_spacing=5),
                ft.Text("PREMIUM CALCULATOR", size=10, color=GOLD, opacity=0.6),
                ft.Container(height=10),
                weight_field,
                source_field,
                target_field,
                ft.Container(height=10),
                ft.Text("ИТОГОВЫЙ ВЕС:", size=12, color=GOLD),
                result_text,
                ft.Container(height=10),
                calc_button
            ]
        )
    )

ft.app(target=main)