import reflex as rx
from rxconfig import config
from ..components.header import header
from ..components.navbar import navbar
from ..components.footer import footer


class State(rx.State):


    ...

@rx.page(route="/pages/contact", title="Contact",)
def contact() -> rx.Component:
    # Welcome Page (Index)
    return rx.container( 
        header(),
        navbar(),
        rx.hstack(
            rx.flex(
                rx.image(src='/Diapositiva1.jpg', border_radius='10px'),
                    width='50%',
                    min_height='65vh',
                    align='center',
                    justify='center',
            ),
            rx.flex(
                rx.text("Contact Us", size='5', color='white',),
                rx.input(placeholder="Name", width='100%', required=True),
                rx.input(placeholder="Last Name", width='100%', required=True),
                rx.input(placeholder="Email", type='email', width='100%', required=True),
                rx.text_area(placeholder="Message", width='100%', required=True),
                rx.button("Send", color='white', bg='#ff0000', width='100%', size='3',), 
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
