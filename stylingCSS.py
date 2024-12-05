from nicegui import ui

ui.icon('thumb_up', color='#9c0303').classes('text-9xl')
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML</strong>.')
with ui.row():
    ui.label('Juan').style('color: #9c0303; font-weight: bold,font-family: "Times New Roman",serif; font-size: 2em;')
    ui.label('Tailwind').classes('font-serif')
    ui.label('Quasar').classes('q-ml-xl')
ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run()