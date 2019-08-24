import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

r = requests.get('https://www.infomoney.com.br/')

soup = BeautifulSoup(r.text, 'html.parser')

table = soup.find(
    'div', class_='border-t-brown-3 widget-table w-altas-baixas-box')

data = []

for row in table.find_all('tr'):
    data.append(row.get_text())

dataclean = []

for i in data:
    datastr = i.replace('\n', ' ')
    datastr = datastr.strip()
    datastr = datastr.replace(',', '.')
    space = list(datastr)
    del space[8]
    space = ''.join(space)
    space = space.replace(' ', ',')
    dataclean.append(space)

del dataclean[0]

new_list = [[i] for i in dataclean]
new = []

for dt in new_list:
    for item in dt:
        item = item.split(',')
        new.append(item)

new = np.array(new)

ix = []
ix_var = 0

for item in new:
    ix_var += 1
    ix.append(ix_var)
    
dataframe = pd.DataFrame(data=new[0:, 0:],
                         index=ix,
                         columns=['Código', 'Últ.(R$)', 'Var. Dia(%)', 'Vol.(R$)', 'Neg.(Nº)', 'Hora'])

print(dataframe)
