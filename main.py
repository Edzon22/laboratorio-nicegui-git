from nicegui import ui

ui.label('¡Hola, NiceGUI y Git!').classes('text-2xl font-bold text-blue-600')
ui.button('Hacer Clic', on_click=lambda: ui.notify('¡Hola desde NiceGUI!'))

ui.run(title='Laboratorio NiceGUI')