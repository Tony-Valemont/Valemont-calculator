import flet as ft

def main(page: ft.Page):
    # Базовые настройки
    page.title = "Золотой калькулятор"
    page.theme_mode = "dark"
    page.padding = 0
    page.bgcolor = "black"
    # Адаптация для мобильных устройств
    page.viewport_width = 360 

    GOLD = "#D4AF37"
    DARK_GOLD = "#9E7C19"

    def input_box(label=""):
        """Поле ввода с универсальными настройками выравнивания"""
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

    # Поля ввода на русском
    weight_box = input_box("0.000")
    probe_box = input_box("585")
    result_text = ft.Text("0.000", size=36, weight="bold", color=GOLD)

    def calculate(e):
        try:
            # Заменяем запятую на точку для правильного счета
            w_val = weight_box.content.value.replace(",", ".")
            p_val = probe_box.content.value.replace(",", ".")
            
            w = float(w_val if w_val else 0)
            p = float(p_val if p_val else 585)
            
            if w > 0 and p > 0:
                # Математический расчет
                res = (w * (p / 1000)) / 0.585
                # ТОЧНОСТЬ 3 ЗНАКА: теперь при 4.28 и 800 будет 5.858
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

    # Используем BoxDecoration для фона, это самый надежный способ для серверов
    main_container = ft.Container(
        expand=True,
        alignment=ft.Alignment(0, 0),
        decoration=ft.BoxDecoration(
            image=ft.DecorationImage(
                src="fon.jpg",
                fit="cover"
            )
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
                ft.Text("ИТОГ (585):", color=GOLD, size=12),
                result_text,
                ft.Container(height=10),
                calculate_button
            ]
        )
    )

    page.add(main_container)

ft.app(target=main)