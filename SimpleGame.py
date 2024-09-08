# simplegame.py
import PySimpleGUI as sg
import command.command as cmd_p
from command.command import show_current_place
from status.game_status import show_inventory

def make_a_window():
    sg.theme('Dark Blue 3')

    prompt_input = [sg.Text('Enter your command', font='Any 14'), sg.Input(key='-IN-', size=(20, 1), font='Any 14')]
    buttons = [sg.Button('Enter', bind_return_key=True), sg.Button('Inventory'), sg.Button('Exit')]
    command_col = sg.Column([prompt_input, buttons], element_justification='r')

    layout = [[sg.Image(r'forest.png', size=(400, 400), key="-IMG-"), 
               sg.Text(show_current_place(), size=(100, 4), font='Any 12', key='-OUTPUT-')],
              [command_col]]

    return sg.Window('Adventure Game', layout, size=(800, 570))

if __name__ == "__main__":
    window = make_a_window()

    while True:
        event, values = window.read()
        if event == 'Enter':
            command = values['-IN-'].strip().lower()
            if command in ['north', 'south', 'fight', 'run']:
                current_story = cmd_p.game_play(command.capitalize())
                window['-OUTPUT-'].update(current_story)
                window['-IMG-'].update(cmd_p.game_places[cmd_p.game_state]['Image'], size=(400, 400))
        elif event == 'Inventory':
            sg.popup('Your Inventory', show_inventory())
        elif event == 'Exit' or event == sg.WIN_CLOSED:
            break

    window.close()
