import flet as ft

def main(page: ft.Page):
    # Basic settings for older versions
    page.title = "VALEMONT"
    page.bgcolor = "#000000"  # Black background
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    
    # Colors
    GOLD = "#D4AF37"
    INPUT_BG = "#121212"

    # 1. Weight input field
    weight_input = ft.TextField(
        label="WEIGHT (GRAMS)",
        text_align="center",
        width=280,
        bgcolor=INPUT_BG,
        border_color=GOLD,
        color="white"
    )

    # 2. Source probe field
    source_probe = ft.TextField(
        label="SOURCE PROBE",
        text_align="center",
        width=280,
        bgcolor=INPUT_BG,
        border_color=GOLD,
        color="white"
    )

    # 3. Target probe field
    target_probe = ft.TextField(
        label="TARGET PROBE",
        value="585",
        text_align="center",
        width=280,
        bgcolor=INPUT_BG,
        border_color=GOLD,
        color="white"
    )

    result_text = ft.Text("0.000", size=45, color=GOLD)

    def calculate(e):
        try:
            # Read numbers, replacing comma with dot
            w = float(weight_input.value.replace(",", ".") or 0)
            p1 = float(source_probe.value.replace(",", ".") or 0)
            p2 = float(target_probe.value.replace(",", ".") or 585)
            
            if w > 0 and p1 > 0 and p2 > 0:
                # Universal conversion formula
                res = (w * p1) / p2
                # Format .3f gives 5.858
                result_text.value = "{:.3f}".format(res)
            else:
                result_text.value = "0.000"
        except:
            result_text.value = "Error"
        page.update()

    # Button with simplified style
    calc_button = ft.Container(
        content=ft.Text("CALCULATE", color="black", size=16),
        bgcolor=GOLD,
        width=280,
        height=50,
        border_radius=15,
        alignment=ft.Alignment(0, 0),
        on_click=calculate
    )

    # Adding elements to the page
    page.add(
        ft.Column(
            horizontal_alignment="center",
            spacing=15,
            controls=[
                ft.Text("VALEMONT", size=32, color=GOLD),
                ft.Text("PREMIUM TOOLS", size=10, color=GOLD),
                ft.Container(height=10),
                weight_input,
                source_probe,
                target_probe,
                ft.Text("FINAL WEIGHT:", size=12, color=GOLD),
                result_text,
                ft.Container(height=10),
                calc_button
            ]
        )
    )

ft.app(target=main)