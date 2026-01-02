import flet as ft

def main(page: ft.Page):
    # Самые примитивные настройки, которые поймет любая версия
    page.title = "VALEMONT"
    page.bgcolor = "#000000"
    page.padding = 20
    
    GOLD = "#D4AF37"

    # Поля ввода без сложных украшений
    weight = ft.TextField(label="ВЕС (Г)", border_color=GOLD, color="white")
    p_from = ft.TextField(label="ИЗ ПРОБЫ", border_color=GOLD, color="white")
    p_to = ft.TextField(label="В ПРОБУ", value="585", border_color=GOLD, color="white")
    
    res_val = ft.Text("0.000", size=40, color=GOLD, weight="bold")

    def click(e):
        try:
            # Математика с заменой запятой
            w = float(weight.value.replace(",", "."))
            pf = float(p_from.value.replace(",", "."))
            pt = float(p_to.value.replace(",", "."))
            # Расчет: (Вес * Исходная) / Целевая
            total = (w * pf) / pt
            res_val.value = "{:.3f}".format(total)
        except:
            res_val.value = "Ошибка"
        page.update()

    # Кнопка
    btn = ft.ElevatedButton(
        "РАССЧИТАТЬ",
        color="black",
        bgcolor=GOLD,
        width=300,
        on_click=click
    )

    # Простая сборка экрана сверху вниз
    page.add(
        ft.Text("VALEMONT", size=30, color=GOLD, weight="bold"),
        ft.Text("ЮВЕЛИРНЫЙ РАСЧЕТ", color=GOLD),
        ft.Divider(color="transparent"),
        weight,
        p_from,
        p_to,
        ft.Divider(color="transparent"),
        ft.Text("РЕЗУЛЬТАТ:", color=GOLD),
        res_val,
        ft.Divider(color="transparent"),
        btn
    )

ft.app(target=main)