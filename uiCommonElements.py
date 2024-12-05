from nicegui import ui
from nicegui.events import ValueChangeEventArguments

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

ui.button('Haz click', on_click=lambda: ui.notify('Clic'))
with ui.row():
    ui.checkbox('Puchale play', on_change=show)
    ui.switch('Switch', on_change=show)
ui.radio(['1', '2', '3'], value='1', on_change=show).props('inline')
with ui.row():
    ui.input('Escribe algo', on_change=show)
    ui.select(['primero', 'Segundo'], value='primero', on_change=show)
ui.link('Perro...', '/documentation').classes('mt-8')

ui.run()