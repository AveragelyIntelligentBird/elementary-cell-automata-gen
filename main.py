# Final Project for CS1800, Summer I 2022
# Prof. John Rachlin
# Elementary Cellular Automata Pattern Generator
# Completed by Anfisa Bogdanenko

import PySimpleGUI as gui
from automaton import Automaton

NUM_ROWS = 300
NUM_COLS = NUM_ROWS * 2 - 1
CELL_SIDE = 2


def define_layouts():
    """Defining the layout of the app"""
    gui.theme('Dark Blue')

    layout = [[gui.Text('Rule no.', font=('Helvetica', 20)),
               gui.Input(size=10, font=('Helvetica', 20), key='-RULE-', enable_events=True),
               gui.Text('shows a pattern produced by a corresponding elementary cellular automaton',
                        font=('Helvetica', 15), pad=(10, 10), key='-MESSAGE-'),
               gui.Push(),
               gui.Button('GENERATE', font=('Helvetica', 15), pad=(10, 0), key='-GO-')],
              [gui.Graph(canvas_size=(NUM_COLS * CELL_SIDE, NUM_ROWS * CELL_SIDE),
                         graph_bottom_left=(0, 402), graph_top_right=(402, 0), key='-PATTERN-')]]

    return layout


if __name__ == "__main__":
    automaton = Automaton(NUM_ROWS)

    window = gui.Window('Elementary Cellular Automata Pattern Generator', define_layouts())

    while True:
        event, values = window.read()
        print(event, values)

        if event == gui.WIN_CLOSED:
            break

        # Enforces only numeric input
        if event == '-RULE-' and values['-RULE-'] and values['-RULE-'][-1] not in '0123456789':
            window['-RULE-'].update(values['-RULE-'][:-1])

        if event == '-GO-':
            rule = int(values['-RULE-'])
            if rule > 255:
                window['-MESSAGE-'].update("Invalid rule: Enter a rule no. between 0 and 255")
            else:
                automaton.update_rule(rule)
                automaton.draw(window['-PATTERN-'])

                window['-MESSAGE-'].update('shows a pattern produced by a corresponding elementary cellular automaton')

    window.close()
