import flet as ft

def main(page: ft.Page):
    # Убираем все настройки, кроме цвета фона
    page.bgcolor = "#000000"
    page.horizontal_alignment = "center"
    
    # Цвет золота
    GOLD = "#D4AF37"

    # Создаем поля ввода без единого сложного атрибута
    w = ft.TextField(label="VES (GR)", border_color=GOLD, color="white", text_align="center", width=250)
    p1 = ft.TextField(label="IZ PROBY", border_color=GOLD, color="white", text_align="center", width=250)
    p2 = ft.TextField(label="V PROBU", value="585", border_color=GOLD, color="white", text_align="center", width=250)
    
    # Текст для вывода (точность 3 знака)
    res_txt = ft.Text("0.000", size=40, color=GOLD)

    def on_click(e):
        try:
            # Считаем по формуле (Вес * Проба1) / Проба2
            val = (float(w.value.replace(",", ".")) * float(p1.value.replace(",", "."))) / float(p2.value.replace(",", "."))
            res_txt.value = "{:.3f}".format(val)
        except:
            res_txt.value = "Error"
        page.update()

    # Простая кнопка-контейнер
    calc_btn = ft.Container(
        content=ft.Text("RASSCHITAT", color="black", weight="bold"),
        bgcolor=GOLD,
        padding=15,
        border_radius=10,
        on_click=on_click,
        alignment=ft.alignment.center,
        width=250
    )

    # Добавляем всё в колонку
    page.add(
        ft.Column(
            horizontal_alignment="center",
            controls=[
                ft.Text("VALEMONT", size=30, color=GOLD),
                w, 
                p1, 
                p2,
                ft.Text("RESULT:", color=GOLD),
                res_txt,
                calc_btn
            ]
        )
    )

ft.app(target=main)