import dash
from dash import html, dcc
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("data/comparison.csv")

app = dash.Dash(__name__)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['ds'], y=df['y'],
    mode='lines+markers',
    name='Actual Revenue (£)',
    line=dict(color='gray', width=1)
))

fig.add_trace(go.Scatter(
    x=df['ds'], y=df['yhat'],
    mode='lines',
    name='Predicted Revenue (£)',
    line=dict(color='blue', width=2)
))

fig.add_trace(go.Scatter(
    x=df['ds'], y=df['yhat_lower'],
    mode='lines',
    name='Lower Bound',
    line=dict(color='lightblue', dash='dot')
))

fig.add_trace(go.Scatter(
    x=df['ds'], y=df['yhat_upper'],
    mode='lines',
    name='Upper Bound',
    line=dict(color='lightblue', dash='dot')
))

fig.update_layout(
    title='Daily Revenue Forecast (Prophet)',
    xaxis_title='Date',
    yaxis_title='Revenue (£)',
    template='plotly_white'
)

app.layout = html.Div([
    html.H1("E-Commerce Revenue Forecast Dashboard", style={'textAlign': 'center'}),
    html.P("My First Project", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
