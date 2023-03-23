#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:52:42 2023

@author: joao.melchior
"""

import pandas as pd
import datetime as dt

dados = []
with open('./data/VazoesFluviometricas_1930-2020.txt') as f:
    for row in f:
        linha = row.split(' ')
        linha = [i for i in linha if i != '\n']
        dados.append(linha)
        
df = pd.DataFrame(dados, columns = ['Code', 'Year', 'Month', 'Day', 'Hour', 'Minute', 'Z', 'Q', 'NA', 'NA2']).drop(['NA', 'NA2'], axis=1)

# Cria datetime
df['datahora'] = df.apply(lambda x: dt.datetime(int(x.Year), int(x['Month']), int(x['Day']), int(x['Hour'])), axis=1)

df['Q'] = df.apply(lambda x: x.Q.replace(',','.'), axis=1)

df.set_index('datahora', inplace=True, drop=True)

df = df[df['Q']!='-']

q = df[['Code','Q']].astype({'Code': 'int', 'Q': 'float'}) # vazão
q.to_csv('./data/qdia-uv-iat.csv')

z = df[['Code','Z']].astype({'Code': 'int', 'Z': 'float'}) # cota
z.to_csv('./data/zdia-uv-iat.csv')