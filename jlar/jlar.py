import reflex as rx
from rxconfig import config


class State(rx.State):


    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Jlar"),
            rx.text("This is a simple Reflex app."),
            rx.button("Click Me!", color_scheme="teal"),
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
