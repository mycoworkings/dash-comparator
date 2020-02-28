# This example displays how to get all contacts from a HubID and paginate through them using the 'offset' parameter.
# The end result is a python list containing all parsed contacts.

import pandas as pd
from sqlalchemy import create_engine
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px


def get_percentage_of_data_by_country(dataframe, col, country):
    answered = dataframe[dataframe.country == country][col].count()
    total = dataframe[dataframe.country == country][col].size
    value = 100 * (answered / total)
    return f'{round(value, 2)} %', answered, total


engine = create_engine("postgresql://:@localhost:5432/aitorlucas")
df = pd.read_sql_table("hubspot2", con=engine)

fields = ["pet_name", "pet_type_new", "size_cat", "size_dog", "zip", "f_t_protection", "frequency_to_the_vet",
          "bravecto_client", "mobilephone", "date_birth_pet", "country"]

df = df[fields]
fields.remove("country")
new_df = pd.DataFrame()

app = dash.Dash(__name__)
options = [{'label': k, 'value': k} for k in df.country.dropna().unique()]

app.layout = html.Div([
    html.Div([
        dcc.RadioItems(
            id='countries-radio',
            # options=[{'label': "ALL", 'value': "ALL"}, *options],
            options=options,
            value='ES',
            style={
                'textAlign': 'center',
                'display': 'flex',
                'justify-content': 'space-between',
                'max-width': '600px',
                'margin': '0 auto',
                'padding': '10px 0',
                'font-family': 'sans-serif',
                'fontWeight': 'bold',
            }
        ),
    ]),

    html.Div([
        html.Div([dcc.Graph(id='pie0')]),
        html.Div([dcc.Graph(id='pie1')]),
        html.Div([dcc.Graph(id='pie2')]),
        html.Div([dcc.Graph(id='pie3')]),
        html.Div([dcc.Graph(id='pie4')]),
        html.Div([dcc.Graph(id='pie5')]),
        html.Div([dcc.Graph(id='pie6')]),
        html.Div([dcc.Graph(id='pie7')]),
        html.Div([dcc.Graph(id='pie8')]),
        html.Div([dcc.Graph(id='pie9')])
    ], style={'columnCount': 5})

])


@app.callback(
    [Output(component_id='pie0', component_property='figure'),
     Output(component_id='pie1', component_property='figure'),
     Output(component_id='pie2', component_property='figure'),
     Output(component_id='pie3', component_property='figure'),
     Output(component_id='pie4', component_property='figure'),
     Output(component_id='pie5', component_property='figure'),
     Output(component_id='pie6', component_property='figure'),
     Output(component_id='pie7', component_property='figure'),
     Output(component_id='pie8', component_property='figure'),
     Output(component_id='pie9', component_property='figure')],
    [Input(component_id='countries-radio', component_property='value')]
)
def update_pie(countries):
    dff = df
    data = []
    for col in fields:
        percentage, answered, total = get_percentage_of_data_by_country(dff, col, countries)
        data.append([answered, total - answered])

    return go.Figure(data=[go.Pie(labels=["Answered", "Unknown"], values=data)])


        # new_df.append({
        #     "field": col,
        #     "percentage": percentage,
        #     "answered": answered,
        #     "unknown": total - answered
        # }, ignore_index=True)
        # return px.pie(
        #     data_frame=new_df
        # )


if __name__ == '__main__':
    app.run_server(debug=True)
