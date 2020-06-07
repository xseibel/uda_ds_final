# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pickle

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = ['assets/base.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


'''If you want to include more datasets, you have to load the
serialized data below (with open(...)). 
Then search for the "dcc.Dropdown" function
and adjust the 'options' parameter accordingly.
'value' has to be equal to the 'ticker' value in the serialized data.
(see make_model.ipynb)
'''

DATASET = {} 
with open('models/GOOG.pkl', 'rb') as pkl:
    pkl_data = pickle.load(pkl)
    DATASET.update({pkl_data["ticker"]: pkl_data})
with open('models/AMZN.pkl', 'rb') as pkl:
    pkl_data = pickle.load(pkl)
    DATASET.update({pkl_data["ticker"]: pkl_data})
with open('models/AAPL.pkl', 'rb') as pkl:
    pkl_data = pickle.load(pkl)
    DATASET.update({pkl_data["ticker"]: pkl_data})



app.layout = html.Div(children=[
    html.H1(children='Stock Price Predictor'),

    html.Div(children='''
        Basic stock price prediction based on ARIMA timeseries forecasting model.\n\n
        Below you can select one pretrained dataset and see the real and predicted values.\n\n (+ predictions 28 days outside of the training data)
    '''),

    html.Div(className='control-tab', children=[
                html.Div(className='app-controls-block', children=[
                            html.Div(
                                className='app-controls-name',
                                children='Dataset: '
                            ),
                            dcc.Dropdown(
                                id='dataset-dropdown',
                                options=[
                                    {'label': 'Google (GOOG)', 'value': 'GOOG'},
                                    {'label': 'Amazon (AMZN)', 'value': 'AMZN'},
                                    {'label': 'Apple (AAPL)', 'value': 'AAPL'}
                                        ],
                            value='GOOG'
                            )
                        ])
             ]),

    dcc.Graph(
            id='stock-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'scatter', 'name': 'dummy'},
                        ],
                'layout': dict(
            xaxis={'title': 'Time'},
            yaxis={'title': 'Stock Price [USD]'},
            legend={'x': 1, 'y': 1},
            hovermode='closest',
            transition = {'duration': 500},
            title={'text': 'dummy'},
        )
                    }
             )



])


@app.callback(
    Output('stock-graph', 'figure'),
    [Input('dataset-dropdown', 'value')]
)
def update_graph(datadset_id):
    traces = []
    """Update chart upon changing dropdown entry."""
    traces.append(dict(
        x=DATASET[datadset_id]['train_df'].index,
        y=DATASET[datadset_id]['train_df'].values,
        text='real',
        name='real',
    ))

    traces.append(dict(
        x=DATASET[datadset_id]['preds_df'].index,
        y=DATASET[datadset_id]['preds_df'].values,
        text='prediction',
        name='prediction',
    ))

    layout= dict(
            xaxis={'title': 'Time'},
            yaxis={'title': 'Adj. Close Price [USD]'},
            legend={'x': 1, 'y': 1},
            hovermode='closest',
            transition = {'duration': 500},
            title={'text':'Stock Price'},
        )
    print(datadset_id)
    return {'data': traces, 'layout': layout}



if __name__ == '__main__':
    app.run_server(debug=False, port=8050, host='0.0.0.0')