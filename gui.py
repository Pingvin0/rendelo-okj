import PySimpleGUI as sg
sg.theme('BrownBlue')

spaces =""

col1 = sg.Column([
            [sg.Text("")],
            [sg.Text('dátum:', size=(8,1))],
            [sg.Text(' ')],
            [sg.Text('óra:', size=(8,1))],
            [sg.Text(spaces)],
            [sg.Text('perc:', size=(8,1))],
            [sg.Text(spaces)],
            [sg.Text('név:', size=(8,1))],
            [sg.Text(spaces)],
            [sg.Text('telefon:', size=(8,1))],
            [sg.Text(spaces)],
            [sg.Button("    Ment    ")]
            
    ])

col2 = sg.Column([
    [sg.Text('')],
    [sg.Input(size=(27,1))],
    [sg.Slider(range=(8,20), orientation='h', tick_interval=2)],
    [sg.Radio('00', group_id='perc', pad=((0,0), (16,0))), sg.Radio('20', group_id='perc', pad=((0,0), (16,0))), sg.Radio('40', group_id='perc', default=True, pad=((0,0), (16,0)))],
    [sg.Text('')],
    [sg.Input(size=(27,1))],
    [sg.Text('')],
    [sg.Input(size=(27,1))],
    [sg.Text('')],
    [sg.Text('                    '),sg.Button("    Keres    ")]
    ])


col3 = sg.Column([
    [sg.Text('Orvosok')],
    [sg.Listbox(size=(15,14), values=("Szia","tetya"))]
    
    ])

col4 = sg.Column([
    [sg.Text('Előjegyzések')],
    [sg.Listbox(size=(54,14), values=("s","t"))],
    [sg.Button('     Töröl     ')]
    ])

layout = [
    [col1,col2,col3,col4],

    

          ]

window = sg.Window('Rendelő', layout)

while True:
    event, values = window.read()
    if event in  (None, 'Cancel'):
        break
    print('you entered', values)

window.close()
