from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
]
# Janela
janela = sg.Window('Tela de login', layout)
# Eventos na Tela
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'felipe' and valores['senha'] == '123456':
            print('Bem vindo a LoginFelipe!')
            
