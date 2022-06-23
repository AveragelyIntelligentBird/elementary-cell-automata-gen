# Final Project for CS1800, Summer I 2022
# Prof. John Rachlin
# Elementary Cellular Automata Pattern Generator
# Completed by Anfisa Bogdanenko

import PySimpleGUI as PyGUI
from automaton import Automaton

NUM_ROWS = 100
NUM_COLS = NUM_ROWS * 2 - 1
CELL_SIDE = 600 // NUM_ROWS


def define_layouts():
    """Defining the layout of the app"""
    PyGUI.theme('Dark Blue')

    layout = [[PyGUI.Text('Rule no.', font=('Helvetica', 20)),
               PyGUI.Input(size=10, font=('Helvetica', 20), key='-RULE-', enable_events=True),
               PyGUI.Text('shows a pattern produced by a corresponding elementary cellular automaton',
                          font=('Helvetica', 15), pad=(10, 10), key='-MESSAGE-'),
               PyGUI.Push(),
               PyGUI.Button('GENERATE', font=('Helvetica', 15), pad=(10, 0), key='-GO-')],
              [PyGUI.Canvas(size=(NUM_COLS * CELL_SIDE, NUM_ROWS * CELL_SIDE), key='-PATTERN-')]]

    return layout


if __name__ == "__main__":
    automaton = Automaton(NUM_ROWS, NUM_COLS, CELL_SIDE)

    window = PyGUI.Window('Elementary Cellular Automata Pattern Generator', define_layouts())

    while True:
        event, values = window.read()
        print(event, values)

        if event == PyGUI.WIN_CLOSED:
            break

        # Enforces only numeric input
        if event == '-RULE-' and values['-RULE-'] and values['-RULE-'][-1] not in '0123456789':
            window['-RULE-'].update(values['-RULE-'][:-1])

        if event == '-GO-' and not values['-RULE-'] == "":
            rule = int(values['-RULE-'])
            if rule > 255:
                window['-MESSAGE-'].update("Invalid rule: Enter a rule no. between 0 and 255")
            else:
                automaton.update_rule(rule)
                automaton.draw(window['-PATTERN-'])

                window['-MESSAGE-'].update('shows a pattern produced by a corresponding elementary cellular automaton')

    window.close()
