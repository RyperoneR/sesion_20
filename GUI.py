import PySimpleGUI as sg

layout = [
    [sg.Input(size=(6, 1), key='-DISPLAY-', justification='right', font=('Helvetica', 20))],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('/')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('*')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('-')],
    [sg.Button('C'), sg.Button('0'), sg.Button('='), sg.Button('+')],
]

window = sg.Window('Calculadora', layout, return_keyboard_events=True)

current_input = ''

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event in '0123456789':
        current_input += event
    elif event in ('+', '-', '*', '/'):
        current_input += f' {event} '
    elif event == 'C':
        current_input = ''
    elif event == '=':
        try:
            current_input = str(eval(current_input))
        except Exception:
            current_input = 'Error'

    window['-DISPLAY-'].update(current_input)

window.close()
