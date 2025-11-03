import dash
from dash import html, dcc
import plotly.graph_objs as go
import pandas as pd

# --- 1. Veriyi oku ---
df = pd.read_csv("data/comparison.csv")

# --- 2. Dash uygulamasını başlat ---
app = dash.Dash(__name__)

# --- 3. Prophet sonuçlarını görselleştir ---
fig = go.Figure()

# Gerçek gelir
fig.add_trace(go.Scatter(
    x=df['ds'], y=df['y'],
    mode='lines+markers',
    name='Actual Revenue (£)',
    line=dict(color='gray', width=1)
))

# Tahmin gelir
fig.add_trace(go.Scatter(
    x=df['ds'], y=df['yhat'],
    mode='lines',
    name='Predicted Revenue (£)',
    line=dict(color='blue', width=2)
))

# Alt tahmin sınırı
fig.add_trace(go.Scatter(
    x=df['ds'], y=df['yhat_lower'],
    mode='lines',
    name='Lower Bound',
    line=dict(color='lightblue', dash='dot')
))

# Üst tahmin sınırı
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

# --- 4. Layout (sayfa görünümü) ---
app.layout = html.Div([
    html.H1("E-Commerce Revenue Forecast Dashboard", style={'textAlign': 'center'}),
    html.P("Created by Cihan 🧠", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

# --- 5. Uygulamayı başlat ---
if __name__ == "__main__":
    app.run(debug=True)
