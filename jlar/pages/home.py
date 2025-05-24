import reflex as rx
from rxconfig import config
from ..components.header import header
from ..components.navbar import navbar
from ..components.footer import footer


class State(rx.State):


    ...

@rx.page(route="/pages/home", title="Home",)
def home() -> rx.Component:
    # Welcome Page (Index)
    return rx.container( 
        header(),
        navbar(),
        rx.flex(
            rx.video(url='/video2.mp4', width='100%', height='100%'),
                width='100%',
                min_height='65vh',
        ),
        footer(),
        bg='#000000',
        color='white',
        width='100%',
    )
                                                                                                                                                                   
app = rx.App()
