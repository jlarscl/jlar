import reflex as rx

def header() -> rx.Component:
    return rx.flex(
            rx.text("Welcome to Jlar!", size='7',),
                width='100%',
        )