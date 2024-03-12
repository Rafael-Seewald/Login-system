import PySimpleGUI as Sg
from data_treatment import *

txt_creating()
users = []
archive = open("users_data.txt", "r")
content = archive.read()

layout = [[Sg.Text('System of accounts\' credentials saving')],
          [Sg.Text('Email:'), Sg.InputText(key='email', size=32)],
          [Sg.Text('Password:'), Sg.InputText(key='password', size=25)],
          [Sg.Button('Login'), Sg.Button('Register')],
          [Sg.Text('', key='var')]]

window = Sg.Window('Login and Register', layout)

while True:
    events, values = window.read()
    if events == Sg.WIN_CLOSED:
        break
    password = values['password']
    email = values['email']
    if events == 'Register':
        if '@' in email and '.com' in email and ' ' not in email and password:
            if email in content:
                window['var'].update(f'Email already registered.')
            else:
                window['var'].update(f'Register success.')
                users.append(email, password)
                data_to_txt(email, password)
        else:
            if ' ' in email:
                window['var'].update(f'Email can\'t have whitespaces. ')
            elif '@' not in email:
                window['var'].update(f'Email need\'s \'@\'.')
            elif '.com' not in email:
                window['var'].update(f'Email need\'s \'.com\'.')
    if events == 'Login':
        if email in content or email in users:
            if password in content or password in users:
                window['var'].update(f'Login success.')
                print('yes baby')
                window.close()
            else:
                window['var'].update(f'Login failed.')
        else:
            window['var'].update(f'Login failed.')

window.close()
