#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 10:31:12 2023

@author: joao.melchior
"""

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

q = pd.read_csv('./data/qdia-uv-iat.csv', parse_dates=True, index_col='datahora')
z = pd.read_csv('./data/zdia-uv-iat.csv', parse_dates=True, index_col='datahora')

fig = make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Scatter(x = q.index, y = q['Q'], marker_color = 'black', name = 'Vazões médias diárias (m3/s)'), secondary_y=False)
fig.add_trace(go.Scatter(x = z.index, y = z['Z'], marker_color='blue', name = 'Cotas médias diárias (cm)'), secondary_y=True)
fig.update_layout(title_text = 'Vazões e cotas médias diárias em União da Vitória')
fig.update_xaxes(title_text = 'Data')
fig.update_yaxes(title_text = 'Vazões médias diárias (m3/s)', secondary_y = False)
fig.update_yaxes(title_text = 'Cotas médias diárias (cm)', secondary_y = True)
# fig.write_html('./plots/cota-vazao-uv-iat.html')

qjoin = pd.read_csv('./data/qdia-uv-iat-plus-simepar.csv', parse_dates=True, index_col='datahora')

fig = go.Figure()
fig.add_trace(go.Scatter(x = qjoin.index, y = qjoin['Q'], marker_color = 'black', name = 'Vazões médias diárias (m3/s)'))
fig.update_xaxes(title_text = 'Data')
fig.update_yaxes(title_text = 'Vazões médias diárias (m3/s)')
fig.add_trace(go.Scatter(x = qjoin.index, y=[qjoin['Q'].mean()]*len(qjoin.index), name='Média de Longo Termo - MLT', marker_color='cyan', line_width=5))#, showlegend=False))
fig.add_trace(go.Scatter(x = qjoin.index, y=[1350]*len(qjoin.index), name='1350m3/s - Cota de desapropriação', marker_color='red', line_width=3))
fig.add_trace(go.Scatter(x = qjoin.index, y=[1600]*len(qjoin.index), name='1600m3/s - Inundação natural em UV', marker_color='red', line_width=3))
fig.add_trace(go.Scatter(x = qjoin.index, y=[2000]*len(qjoin.index), name='2000m3/s', marker_color='red', line_width=3))#, showlegend=False))
fig.add_trace(go.Scatter(x = qjoin.index, y=[2500]*len(qjoin.index), name='2500m3/s', marker_color='red', line_width=3))#, showlegend=False))
fig.add_trace(go.Scatter(x = qjoin.index, y=[3000]*len(qjoin.index), name='3000m3/s - limiar quatro grandes cheias', marker_color='red', line_width=3))#, showlegend=False))
fig.update_layout(title_text = 'Vazões médias diárias em União da Vitória', showlegend=True)
fig.write_html('./plots/qdia-uv.html')

qmax = qjoin['1931':'2022'].resample('Y').max() # maximos anuais

fig = go.Figure()
fig.add_trace(go.Scatter(x = qmax.index, y = qmax['Q'], marker_color = 'black', name = 'Vazões médias diárias (m3/s)'))
fig.update_layout(title_text = 'Vazões máximas anuais em União da Vitória')
fig.update_xaxes(title_text = 'Data')
fig.update_yaxes(title_text = 'Vazões máximas anuais (m3/s)')
fig.add_trace(go.Scatter(x = qmax.index, y=[qmax['Q'].mean()]*len(qmax.index), name='Média de Longo Termo - MLT', marker_color='cyan', line_width=5))#, showlegend=False))
fig.add_trace(go.Scatter(x = qmax.index, y=[1350]*len(qmax.index), name='1350m3/s - Cota de desapropriação', marker_color='red', line_width=3))
fig.add_trace(go.Scatter(x = qmax.index, y=[1600]*len(qmax.index), name='1600m3/s - Inundação natural em UV', marker_color='red', line_width=3))
fig.add_trace(go.Scatter(x = qmax.index, y=[2000]*len(qmax.index), name='2000m3/s', marker_color='red', line_width=3))#, showlegend=False))
fig.add_trace(go.Scatter(x = qmax.index, y=[2500]*len(qmax.index), name='2500m3/s', marker_color='red', line_width=3))#, showlegend=False))
fig.add_trace(go.Scatter(x = qmax.index, y=[3000]*len(qmax.index), name='3000m3/s - limiar quatro grandes cheias', marker_color='red', line_width=3))#, showlegend=False))
fig.write_html('./plots/qmax-uv.html')