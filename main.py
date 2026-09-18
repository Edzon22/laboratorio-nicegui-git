from nicegui import ui

# Encabezado principal
ui.label('Portal de Artículos de Tecnología').classes('text-3xl font-bold text-center text-blue-800 my-4')
ui.label('Bienvenido a nuestro blog colaborativo').classes('text-gray-600 text-center mb-6')

# Contenedor de artículos
with ui.row().classes('w-full justify-center gap-4'):
    # Artículo 1
    with ui.card().classes('w-80 p-4 shadow-lg'):
        ui.label('Introducción a Git y GitHub').classes('text-xl font-bold text-gray-800')
        ui.label('Aprende las bases del control de versiones y cómo colaborar en equipo.').classes('text-sm text-gray-600 my-2')
        ui.button('Leer más', on_click=lambda: ui.notify('Abriendo artículo de Git...')).classes('bg-blue-500 text-white')

    # Artículo 2
    with ui.card().classes('w-80 p-4 shadow-lg'):
        ui.label('Desarrollo Web con NiceGUI').classes('text-xl font-bold text-gray-800')
        ui.label('Crea interfaces gráficas web rápidamente usando solo código Python.').classes('text-sm text-gray-600 my-2')
        ui.button('Leer más', on_click=lambda: ui.notify('Abriendo artículo de NiceGUI...')).classes('bg-green-500 text-white')

ui.run(title='Portal de Artículos')