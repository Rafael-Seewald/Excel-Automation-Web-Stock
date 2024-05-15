import pyautogui
import pandas as pd
from time import sleep

pyautogui.PAUSE = 0.3

# abrir o chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# abrir o site
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
sleep(1.5)

# fazer login com email, depois a senha e entrar
pyautogui.click(x=683, y=409)
pyautogui.write('emailDoUsuario@gmail.com')
pyautogui.press('tab')
pyautogui.write('123456789')
pyautogui.press('tab')
pyautogui.press('enter')

# importando a base de dados para manipula-la
df = pd.read_csv('produtos.csv')
print(df)

# cadastrando todos itens da base de dados no site
for linha in df.index:
    pyautogui.click(x=677, y=295)
    # codigo do produto
    pyautogui.write(str(df.loc[linha, 'codigo']))
    pyautogui.press('tab')
    # marca do produto
    pyautogui.write(str(df.loc[linha, 'marca']))
    pyautogui.press('tab')
    # que tipo de produto
    pyautogui.write(str(df.loc[linha, 'tipo']))
    pyautogui.press('tab')
    # categoria
    pyautogui.write(str(df.loc[linha, 'categoria']))
    pyautogui.press('tab')
    # preco por unidade
    pyautogui.write(str(df.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    # custo
    pyautogui.write(str(df.loc[linha, 'custo']))
    pyautogui.press('tab')
    # alguma observação do produto
    obs = str(df.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')
    # enviar um item e ir para o próximo
    pyautogui.press('enter')
