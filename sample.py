import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output
import plotly.express as px

# Load dataset
df = pd.read_csv('superstore.csv', encoding='ISO-8859-1')

# Data preprocessing
df['Order.Date'] = pd.to_datetime(df['Order.Date'])
df['Year'] = df['Order.Date'].dt.year

# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout
app.layout = dbc.Container([
    html.H1("Global Superstore Dashboard", className='text-center my-4'),
    dbc.Row([
        dbc.Col([
            dcc.DatePickerRange(
                id='date-range',
                start_date=df['Order.Date'].min(),
                end_date=df['Order.Date'].max(),
                display_format='YYYY-MM-DD'
            ),
            dcc.Dropdown(
                id='region-dropdown',
                options=[{'label': region, 'value': region} for region in df['Region'].unique()],
                value=df['Region'].unique().tolist(),
                multi=True
            )
        ], width=4),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='sales-over-time'), width=6),
        dbc.Col(dcc.Graph(id='regional-sales'), width=6),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='top-products'), width=6),
        dbc.Col(dcc.Graph(id='customer-segments'), width=6),
    ])
], fluid=True)

# Callbacks
@app.callback(
    Output('sales-over-time', 'figure'),
    Output('regional-sales', 'figure'),
    Output('top-products', 'figure'),
    Output('customer-segments', 'figure'),
    Input('date-range', 'start_date'),
    Input('date-range', 'end_date'),
    Input('region-dropdown', 'value')
)
def update_charts(start_date, end_date, selected_regions):
    mask = (df['Order.Date'] >= start_date) & (df['Order.Date'] <= end_date) & (df['Region'].isin(selected_regions))
    filtered_df = df.loc[mask]

    sales_over_time = px.line(filtered_df, x='Order.Date', y='Sales', title='Sales Over Time')
    regional_sales = px.bar(filtered_df.groupby('Region')['Sales'].sum().reset_index(), x='Region', y='Sales', title='Regional Sales')
    top_products = px.bar(filtered_df.groupby('Product.Name')['Sales'].sum().nlargest(10).reset_index(), x='Product.Name', y='Sales', title='Top 10 Products')
    customer_segments = px.pie(filtered_df, names='Segment', values='Sales', title='Customer Segments')

    return sales_over_time, regional_sales, top_products, customer_segments

# Run app
if __name__ == '__main__':
    app.run(debug=True)
