import flet as ft

def main(page: ft.Page):
    # Самые базовые настройки без лишних функций
    page.title = "VALEMONT"
    page.bgcolor = "#000000"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    
    GOLD = "#D4AF37"

    # Поля ввода на русском
    w_input = ft.TextField(label="ВЕС (Г)", border_color=GOLD, color="white", text_align="center", width=280)
    p_from = ft.TextField(label="ИСХОДНАЯ ПРОБА", border_color=GOLD, color="white", text_align="center", width=280)
    p_to = ft.TextField(label="ЦЕЛЕВАЯ ПРОБА", value="585", border_color=GOLD, color="white", text_align="center", width=280)
    
    # Текст результата с точностью 3 знака (5.858)
    res_text = ft.Text("0.000", size=45, color=GOLD)

    def do_calc(e):
        try:
            # Математика: (Вес * Проба1) / Проба2
            weight = float(w_input.value.replace(",", "."))
            pf = float(p_from.value.replace(",", "."))
            pt = float(p_to.value.replace(",", "."))
            
            final = (weight * pf) / pt
            res_text.value = "{:.3f}".format(final) # Даст 5.858
        except:
            res_text.value = "Ошибка"
        page.update()

    # Кнопка без использования атрибутов 'center' или 'colors'
    calc_btn = ft.Container(
        content=ft.Text("РАССЧИТАТЬ", color="black", weight="bold"),
        bgcolor=GOLD,
        padding=15,
        border_radius=12,
        on_click=do_calc,
        alignment=ft.Alignment(0, 0), # Вместо .center
        width=280
    )

    # Собираем интерфейс
    page.add(
        ft.Column(
            horizontal_alignment="center",
            spacing=20,
            controls=[
                ft.Text("VALEMONT", size=35, color=GOLD, weight="bold"),
                w_input,
                p_from,
                p_to,
                ft.Text("РЕЗУЛЬТАТ:", size=12, color=GOLD),
                res_text,
                calc_btn
            ]
        )
    )

ft.app(target=main)