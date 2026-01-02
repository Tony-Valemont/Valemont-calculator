import flet as ft

def main(page: ft.Page):
    # Page configuration
    page.title = "Gold Calculator"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.bgcolor = "black"

    GOLD = "#D4AF37"
    DARK_GOLD = "#9E7C19"

    def input_box(label=""):
        """Create a styled input box"""
        return ft.Container(
            width=260,
            height=52,
            alignment=ft.alignment.CENTER,
            border_radius=16,
            border=ft.border.all(1, GOLD),
            content=ft.TextField(
                border=ft.InputBorder.NONE,
                text_align="center",
                keyboard_type=ft.KeyboardType.NUMBER,
                hint_text=label,
                text_style=ft.TextStyle(
                    size=22,
                    color=GOLD,
                    weight="bold"
                ),
                bgcolor="transparent"
            )
        )

    weight_box = input_box("0.00")
    probe_box = input_box("585")

    result_text = ft.Text(
        "0.00",
        size=32,
        weight="bold",
        color=GOLD
    )

    def calculate(e):
        """Calculate gold price"""
        try:
            weight_val = weight_box.content.value
            probe_val = probe_box.content.value
            
            weight = float(weight_val.replace(",", ".") if weight_val else 0)
            probe = float(probe_val.replace(",", ".") if probe_val else 585)
            
            if weight > 0 and probe > 0:
                result = (weight * (probe / 1000)) / 0.585
                result_text.value = f"{result:.2f}"
            else:
                result_text.value = "0.00"
        except ValueError:
            result_text.value = "---"
        
        page.update()

    calculate_button = ft.Container(
        width=260,
        height=56,
        alignment=ft.alignment.CENTER,
        border_radius=20,
        bgcolor=GOLD,
        on_click=calculate,
        content=ft.Text(
            "CALCULATE",
            size=18,
            weight="bold",
            color="black",
            letter_spacing=1.5
        ),
        shadow=ft.BoxShadow(
            blur_radius=16,
            spread_radius=1,
            color=DARK_GOLD,
            offset=ft.Offset(0, 6)
        )
    )

    page.add(
        ft.Container(
            expand=True,
            padding=ft.padding.symmetric(horizontal=24),
            decoration=ft.BoxDecoration(
                image=ft.DecorationImage(
                    src="fon.jpg",
                    fit=ft.ImageFit.COVER
                )
            ),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=28,
                controls=[
                    ft.Text("WEIGHT (g)", color=GOLD, size=14),
                    weight_box,
                    ft.Text("PURITY (‰)", color=GOLD, size=14),
                    probe_box,
                    ft.Container(height=10),
                    result_text,
                    ft.Container(height=30),
                    calculate_button
                ]
            )
        )
    )

if __name__ == "__main__":
    ft.app(target=main)