import reflex as rx
from jlar.app import app
from rxconfig import config


class State(rx.State):


    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container( 
        rx.flex(
            rx.text("Welcome to Jlar!", size='7',),
            rx.color_mode.button(position='bottom-left'),
            width='100%',
        ),
        rx.flex(
            rx.button("Home", size='3', bg='#ff0000', width='25%', on_click=rx.redirect('/pages/home')),
            rx.button("R&D", size='3', bg="#ff0000", width='25%', on_click=rx.redirect('/pages/jota')),
            rx.button("Contact", size='3', bg="#ff0000", width='25%', on_click=rx.redirect('/pages/about')),
            rx.button("Exit", size='3', bg="#ff0000", width='25%', on_click=rx.redirect('http://www.google.com', is_external=True)),
                width='100%',
                height='10vh',
                align='center',
                justify='center',
                spacing='1',
        ),
        rx.flex(
            rx.video(url='/video2.mp4', width='100%', height='100%'),
                width='100%',
                min_height='65vh',
        ),
        rx.flex(
            rx.button(
                rx.text("Copyright © 2023 Jlar", size='2', color='white',), bg='#ff0000', size='3', width='80%'
            ),
            height='10vh',
            width='100%',
            align='center',
            justify='center',
        ),
        bg='#000000',
    )
                                                                                                                                                                      
app = rx.App()
app.add_page(index)
