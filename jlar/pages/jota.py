import reflex as rx
from rxconfig import config
from ..components.header import header
from ..components.navbar import navbar
from ..components.footer import footer


class State(rx.State):


    ...

@rx.page(route="/pages/jota", title="R&D",)
def jota() -> rx.Component:
    # Welcome Page (Index)
    return rx.container( 
        header(),
        navbar(),
        rx.hstack(
            rx.flex(
                rx.image(src='/Diapositiva3.jpg', border_radius='10px'),
                    width='50%',
                    min_height='65vh',
                    align='center',
                    justify='center',
            ),
            rx.flex(
                rx.text("R&D", size='5', color='white', align='center',),
                rx.link('Custmer Service', href='/pages/login', color='white',),
                rx.text('Examples of AI', color='white',),
                direction='column',
                    width='50%',
                    min_height='65vh',
                    align='center',
                    justify='center',
                    spacing='1',
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
