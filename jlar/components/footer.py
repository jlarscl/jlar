import reflex as rx


def footer() -> rx.Component:
    return rx.flex(
        rx.button(
            rx.text("Copyright © 2023 Jlar", size='2', color='white',), bg='#ff0000', size='3', width='80%'
        ),
        height='10vh',
        width='100%',
        align='center',
        justify='center',
    )