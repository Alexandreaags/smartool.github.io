import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output
import random

app = dash.Dash(__name__)

# Create a simple dashboard layout
app.layout = html.Div([
    html.Div(
        children=[
            html.Img(src='assets/logo-fraunhofer-ipk.png', style={'height': '30px', 'width': 'auto'}),
            html.Img(src='assets/senai-logo.png', style={'height': '50px', 'width': 'auto'}),
            # html.H1('Real-time Dashboard', style={'margin-left': '20px'}),
        ],
        style={'display': 'flex', 'align-items': 'center', 'margin': '20px'}
    ),
    html.Div([
        html.Div(id='card-1'),
        html.Div(id='card-2'),
        html.Div(id='card-3'),
        html.Div(id='card-4'),
        html.Div(id='card-5'),
        html.Div(id='card-6'),
        html.Div(id='card-7'),
        html.Div(id='card-8'),
        html.Div(id='card-9'),
        html.Div(id='card-10'),
    ],
    style={
            'display': 'grid',
            'grid-template-columns': 'repeat(5, 1fr)',  # Adjust the number of columns as needed
            'grid-gap': '5px',
            'margin': '5px'
        }
    ),
    dcc.Interval(
        id='interval-component',
        interval=3*1000,  # in milliseconds
        n_intervals=0
    )
])


# Update the content of the cards every second
@app.callback(
    [Output('card-1', 'children'),
     Output('card-2', 'children'),
     Output('card-3', 'children'),
     Output('card-4', 'children'),
     Output('card-5', 'children'),
     Output('card-6', 'children'),
     Output('card-7', 'children'),
     Output('card-8', 'children'),
     Output('card-9', 'children'),
     Output('card-10', 'children')],
    [Input('interval-component', 'n_intervals')]
)
def update_metrics(n):
    data_parts_produced = round(random.uniform(100000, 200000), 2)
    data_parts_Out_tolerance = round(random.uniform(1000, 10000), 2)
    data_Feasable_parts = round(random.uniform(100000, 200000), 2)
    data_cycles = round(random.uniform(100000, 200000), 2)
    data_last_force = round(random.uniform(400, 500), 2)
    data_Mean_force = round(random.uniform(480, 500), 2)
    data_Set_force = 500
    data_last_amb = round(random.uniform(35, 39), 2)
    data_mean_amb = round(random.uniform(35, 39), 2)
    data_last_hum = round(random.uniform(45, 50), 2)
    data_mean_hum = round(random.uniform(48, 50), 2)
    data_last_temp = round(random.uniform(100, 110), 2)
    data_mean_temp = round(random.uniform(105, 110), 2)
    data_set_temp = 110
    data_last_press = round(random.uniform(900, 1000), 2)
    data_mean_press = round(random.uniform(950, 1000), 2)
    data_set_press = 1000
    status_list = ['Closing', 'Injecting', 'Opening', 'Demolding']
    data_status = random.choice(status_list)
    # data_8 = round(random.uniform(0, 100), 2)
    # data_9 = round(random.uniform(0, 100), 2)
    # data_10 = round(random.uniform(0, 100), 2)
    card_info = html.Div(
            children=[
                html.H3(f"INFO"),
                html.P(f"Tool Nr: ------------------------ 125698DE"),
                html.P(f"Manufactured in: -------------- 12/05/2023"),
                html.P(f"Sent to Producer in: ---------- 16/07/2023"),
                html.P(f"Time Running: ---------------------- 289 h"),
                html.Hr(),  # Add a horizontal line for separation
            ],
            className='card',
            style={'flex': '0 0 20%', 'margin': '5px', 'padding': '10px', 'border': '1px solid #ccc', 'border-radius': '20px'}
        )
    card_status = html.Div(
            children=[
                html.H3(f"Process Status: {data_status}..."),
                html.Hr(),  # Add a horizontal line for separation
            ],
            className='card',
            style={'flex': '0 0 20%', 'margin': '5px', 'padding': '10px', 'border': '1px solid #ccc', 'border-radius': '20px'}
        )
    card_parts = html.Div(
            children=[
                html.H3(f"Manufactured Parts"),
                html.P(f"Parts Produced: {data_parts_produced}"),
                html.P(f"Parts Out of Tolerance: {data_parts_Out_tolerance}"),
                html.P(f"Feasable Parts: {data_Feasable_parts}"),
                html.Hr(),  # Add a horizontal line for separation
            ],
            className='card',
            style={'flex': '0 0 20%', 'margin': '5px', 'padding': '10px', 'border': '1px solid #ccc', 'border-radius': '20px'}
        )
    card_cycles = html.Div(
            children=[
                html.H3(f"Cycles"),
                html.P(f"Cycles until overhaul: {data_cycles}/200.000 "),
                html.Hr(),  # Add a horizontal line for separation
            ],
            className='card',
            style={'flex': '0 0 20%', 'margin': '5px', 'padding': '10px', 'border': '1px solid #ccc', 'border-radius': '20px'}
        )
    card_force = html.Div(
            children=[
                html.H3(f"Clamping Force"),
                html.P(f"Last measured value: {data_last_force}kN"),
                html.P(f"Mean value: {data_Mean_force}kN"),
                html.P(f"Set value in machine: {data_Set_force}kN"),
                html.Hr(),  # Add a horizontal line for separation
            ],
            className='card',
            style={'flex': '0 0 20%', 'margin': '5px', 'padding': '10px', 'border': '1px solid #ccc', 'border-radius': '20px'}
        )
    card_amb = html.Div(
            children=[
                html.H3(f"Ambient Temperature"),
                html.P(f"Last measured value: {data_last_amb}°C"),
                html.P(f"Mean value: {data_mean_amb}°C"),
                # html.P(f"Quantidade Vendida: {row['Quantidade']}"),
                # html.P(f"ID da Loja: {row['ID Loja']}"),
                html.Hr(),  # Add a horizontal line for separation
            ],
            className='card',
            style={'flex': '0 0 20%', 'margin': '5px', 'padding': '10px', 'border': '1px solid #ccc', 'border-radius': '20px'}
        )
    card_hum = html.Div(
            children=[
                html.H3(f"Ambient Humidity"),
                html.P(f"Last measured value: {data_last_hum}%"),
                html.P(f"Mean value: {data_mean_hum}%"),
                # html.P(f"Quantidade Vendida: {row['Quantidade']}"),
                # html.P(f"ID da Loja: {row['ID Loja']}"),
                html.Hr(),  # Add a horizontal line for separation
            ],
            className='card',
            style={'flex': '0 0 20%', 'margin': '5px', 'padding': '10px', 'border': '1px solid #ccc', 'border-radius': '20px'}
        )
    card_temp = html.Div(
            children=[
                html.H3(f"Cavity Temperature"),
                html.P(f"Last measured value: {data_last_temp}°C"),
                html.P(f"Mean value: {data_mean_temp}°C"),
                html.P(f"Set value in machine: {data_set_temp}°C"),
                # html.P(f"Quantidade Vendida: {row['Quantidade']}"),
                # html.P(f"ID da Loja: {row['ID Loja']}"),
                html.Hr(),  # Add a horizontal line for separation
            ],
            className='card',
            style={'flex': '0 0 20%', 'margin': '5px', 'padding': '10px', 'border': '1px solid #ccc', 'border-radius': '20px'}
        )
    card_press = html.Div(
            children=[
                html.H3(f"Cavity Pressure"),
                html.P(f"Last measured value: {data_last_press}Bar"),
                html.P(f"Mean value: {data_mean_press}Bar"),
                html.P(f"Set value in machine: {data_set_press}Bar"),
                # html.P(f"Quantidade Vendida: {row['Quantidade']}"),
                # html.P(f"ID da Loja: {row['ID Loja']}"),
                html.Hr(),  # Add a horizontal line for separation
            ],
            className='card',
            style={'flex': '0 0 20%', 'margin': '5px', 'padding': '10px', 'border': '1px solid #ccc', 'border-radius': '20px'}
        )
    card_location = html.Div(
            children=[
                html.H3(f"Location"),
                html.Img(src='assets/location.png', style={'height': '300px', 'width': 'auto', 'display': 'block', 'margin': 'auto'}),
                # html.P(f"Quantidade Vendida: {row['Quantidade']}"),
                # html.P(f"ID da Loja: {row['ID Loja']}"),

            ],
            className='card',
            style={'flex': '0 0 20%', 'margin': '5px', 'padding': '10px', 'border': '1px solid #ccc', 'border-radius': '20px'}
        )
    return card_info, card_status, card_parts, card_cycles, card_force, card_amb, card_hum, card_temp, card_press, card_location


if __name__ == '__main__':
    app.run_server(debug=True)