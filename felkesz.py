import sqlite3
import PySimpleGUI as sg
sg.theme('BrownBlue')

conn = sqlite3.connect('rendelo.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS elojegyzesek(
id int AUTO_INCREMENT,
orvos varchar(25) NOT NULL,
datum varchar(15) NOT NULL,
ido varchar(6) NOT NULL,
nev varchar(35) NOT NULL,
telefonszam varchar(15) NOT NULL,
PRIMARY KEY (id)
)
"""
)
conn.commit()

def ujElojegyzesek(cursor):
    valasz = cursor.execute("SELECT * FROM elojegyzesek")
    sorok = valasz.fetchall()
    return [f"{i[2]} {i[3]} {i[4]} {i[5]}" for i in sorok]


handle = open("orvosok.txt", "r")


orvosok_lista = [i.strip() for i in handle.read().split("\n")]
handle.close()

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
            [sg.Button("    Ment    ", key='ment')]
            
    ])

col2 = sg.Column([
    [sg.Text('')],
    [sg.Input(size=(27,1), key='datum')],
    [sg.Slider(range=(8,20), orientation='h', tick_interval=2, key='ora')],
    [sg.Radio('00', group_id='perc', pad=((0,0), (16,0)), key='perckey'), sg.Radio('20', group_id='perc', pad=((0,0), (16,0)), key='perckey'), sg.Radio('40', group_id='perc', default=True, pad=((0,0), (16,0)), key='perckey')],
    [sg.Text('')],
    [sg.Input(size=(27,1), key='nev')],
    [sg.Text('')],
    [sg.Input(size=(27,1), key='telefon')],
    [sg.Text('')],
    [sg.Text('                    '),sg.Button("    Keres    ", key='keres')]
    ])


col3 = sg.Column([
    [sg.Text('Orvosok')],
    [sg.Listbox(size=(15,14), values=orvosok_lista, key='orvosok')]
    
    ])

col4 = sg.Column([
    [sg.Text('Előjegyzések')],
    [sg.Listbox(size=(54,14), values=ujElojegyzesek(cursor), key='elojegyzesek')],
    [sg.Button('     Töröl     ', key='torol')]
    ])

layout = [
    [col1,col2,col3,col4],

    

          ]

window = sg.Window('Rendelő', layout)


while True:
    event, values = window.read()
    if event in [None]:
        break
    print(event, 'you entered', values)
    if event == 'ment':
        perc = 0
        if values['perckey']:
            perc = '00'
        if values['perckey0']:
            perc = '20'
        if values['perckey1']:
            perc = '40'
        cursor.execute("INSERT INTO elojegyzesek (orvos,datum,ido,nev,telefonszam) VALUES (?,?,?,?,?)", (values['orvosok'][0], values['datum'], str(int(values['ora']))+":"+str(perc),values['nev'],values['telefon']))
        conn.commit()
        window['elojegyzesek'].Update(values=ujElojegyzesek(cursor))
    if event == 'torol':
        jelenlegi = values['elojegyzesek'][0].split(" ")
        cursor.execute("DELETE FROM elojegyzesek WHERE datum = ? AND ido = ?", (jelenlegi[0], jelenlegi[1]))
        print(jelenlegi)
        conn.commit()
        window['elojegyzesek'].Update(values=ujElojegyzesek(cursor))
       
window.close()
