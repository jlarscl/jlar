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
                rx.input(placeholder="Username", width='100%', required=True),
                rx.input(placeholder="Password", type='password', width='100%', required=True),
                rx.button("Login", color='white', bg='#ff0000', width='100%', size='3',),
                rx.text("Don't have an account? Sign up now!", size='3', color='white',),
                rx.input(placeholder="Re enter password", type='password', width='100%', required=True),
                rx.input(placeholder="Email", type='email', width='100%', required=True),
                rx.button("Register", color='white', bg='#ff0000', width='100%', size='3',),
                    direction='column',
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
