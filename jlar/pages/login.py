import reflex as rx
from rxconfig import config
from ..components.header import header
from ..components.navbar import navbar
from ..components.footer import footer


class State(rx.State):


    ...

@rx.page(route="/pages/login", title="Login",)
def login() -> rx.Component:
    # Welcome Page (Index)
    return rx.container( 
        header(),
        navbar(),
        rx.hstack(
            rx.flex(
                rx.image(src='/Diapositiva5.jpg', border_radius='10px'),
                width='50%',
                min_height='65vh',
                align='center',
                justify='center',
            ),
            rx.flex(
                rx.text("Login", size='5', color='white',),
                width='50%',
                min_height='65vh',
                align='center',
                justify='center',
            ),
            width='100%',
            min_height='65vh',
            align='center',
            justify='center',
        ),
        footer(),
        bg='#000000',
        color='white',
        width='100%',
    )
                                                                                                                                                                   
app = rx.App()
