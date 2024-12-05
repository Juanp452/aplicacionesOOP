from nicegui import ui

class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
v = ui.checkbox('visible', value=True)
with ui.column().bind_visibility_from(v, 'value'):
    ui.slider(min=1, max=5).bind_value(demo, 'number')
    ui.toggle({1: 'Algebra', 2: 'Baile', 3: 'Cocina', 4: 'Comida', 5: 'Coco'}).bind_value(demo, 'number')
    ui.number().bind_value(demo, 'number')

ui.run()