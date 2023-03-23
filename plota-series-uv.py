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
fig.update_layout(title_text = 'Vazões médias diárias em União da Vitória')
fig.update_xaxes(title_text = 'Data')
fig.update_yaxes(title_text = 'Vazões médias diárias (m3/s)')
fig.add_hline(y=qjoin['Q'].mean(), name='Média de Longo Termo', line_color='cyan', line_width=5, annotation_text='<b>MLT<b>', annotation_position = 'bottom right', annotation_font_size=30, annotation_font_color='cyan')
fig.add_hline(y=1350, name='1350m3/s - Cota de desapropriação', line_color='red', line_width=3)
fig.add_hline(y=1600, name='1600m3/s - Inundação natural em UV', line_color='red', line_width=3)
fig.add_hline(y=2000, name='2000m3/s', line_color='red', line_width=3)
fig.add_hline(y=2500, name='2500m3/s', line_color='red', line_width=3)
fig.add_hline(y=3000, name='3000m3/s - limiar quatro grandes cheias', line_color='red', line_width=3)
# fig.write_html('./plots/qdia-uv.html')

qmax = qjoin['1931':'2022'].resample('Y').max() # maximos anuais

fig = go.Figure()
fig.add_trace(go.Scatter(x = qmax.index, y = qmax['Q'], marker_color = 'black', name = 'Vazões médias diárias (m3/s)'))
fig.update_layout(title_text = 'Vazões máximas anuais em União da Vitória')
fig.update_xaxes(title_text = 'Data')
fig.update_yaxes(title_text = 'Vazões máximas anuais (m3/s)')
fig.add_hline(y=qmax['Q'].mean(), name='Média de Longo Termo', line_color='cyan', line_width=3, annotation_text='<b>MLT<b>', annotation_position = 'bottom right', annotation_font_size=30, annotation_font_color='cyan')
fig.add_hline(y=1350, name='1350m3/s - Cota de desapropriação', line_color='red', line_width=3)
fig.add_hline(y=1600, name='1600m3/s - Inundação natural em UV', line_color='red', line_width=3)
fig.add_hline(y=2000, name='2000m3/s', line_color='red', line_width=3)
fig.add_hline(y=2500, name='2500m3/s', line_color='red', line_width=3)
fig.add_hline(y=3000, name='3000m3/s - limiar quatro grandes cheias', line_color='red', line_width=3)
# fig.write_html('./plots/qmax-uv.html')