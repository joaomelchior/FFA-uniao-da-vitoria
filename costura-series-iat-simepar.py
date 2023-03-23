#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:18:54 2023

@author: joao.melchior
"""

import pandas as pd
import datetime as dt

qiat = pd.read_csv('./data/qdia-uv-iat.csv', parse_dates=True, index_col='datahora') # IAT
qsim = pd.read_csv('./data/09_Uniao_da_Vitoria.csv', parse_dates=True, index_col='datahora') # Simepar
qsim.index = qsim.index.tz_localize(None) - dt.timedelta(hours=3)

qsimdia = qsim.resample('D', offset='7H').mean() # média diária 7h as 7h

qjoin = pd.concat([qiat, qsimdia])

qdia = qjoin[~qjoin.index.duplicated(keep='first')] # considera a série inteira do IAT (caso queira usar a série inteira do simepar basta substituir 'first' por 'last')
qdia['q-complete'] = qdia['Q'].fillna(qdia['q_m3s'])

qdia['q-complete'].rename('Q').to_csv('./data/qdia-uv-iat-plus-simepar.csv', float_format='%.2f')