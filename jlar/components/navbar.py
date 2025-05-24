import reflex as rx

def navbar() -> rx.Component:
    return rx.flex(
        rx.button("Home", size='3', bg='#ff0000', width='25%', on_click=rx.redirect('/pages/home')),
        rx.button("R&D", size='3', bg="#ff0000", width='25%', on_click=rx.redirect('/pages/jota')),
        rx.button("Contact", size='3', bg="#ff0000", width='25%', on_click=rx.redirect('/pages/about')),
        rx.button("Exit", size='3', bg="#ff0000", width='25%', on_click=rx.redirect('http://www.google.com', is_external=True)),
        width='100%',
        height='10vh',
        align='center',
        justify='center',
        spacing='1',
    )