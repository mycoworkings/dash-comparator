# This example displays how to get all contacts from a HubID and paginate through them using the 'offset' parameter.
# The end result is a python list containing all parsed contacts.

import pandas as pd
from sqlalchemy import create_engine
import dash
import dash_table
import dash_html_components as html


def get_percentage_of_data_by_country(dataframe, col, country):
    value = 100 * (dataframe[dataframe.country == country][col].count() /
                   dataframe[dataframe.country == country][col].size)
    return f'{round(value, 2)} %'


# engine = create_engine("postgresql://:@localhost:5432/aitorlucas")
# df = pd.read_sql_table("hubspot", con=engine)

df = pd.read_csv("/home/aitor/Escritorio/hubspot_contacts.csv", low_memory=False)

fields = ["pet_name", "size_cat", "size_dog", "zip", "f_t_protection", "frequency_to_the_vet",
          "bravecto_client", "mobilephone", "date_birth_pet", "country"]

df = df[fields]
fields.remove("country")
new_df = pd.DataFrame()

for col in fields:
    data = dict()
    data["FIELD"] = col
    for country in df.country.dropna().unique():
        data[country] = get_percentage_of_data_by_country(df, col, country)

    new_df = new_df.append(data, ignore_index=True)

new_df = new_df.reindex(columns=list(data.keys()))

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H3(
        children='PERCENTAGE OF THE AMOUNT OF DATA BY COUNTRY',
        style={
            'textAlign': 'center',
            'font-family': 'sans-serif'
        }
    ),

    dash_table.DataTable(

        id='table',
        columns=[{"name": i, "id": i} for i in new_df.columns],
        data=new_df.to_dict('records'),
        style_cell_conditional=[
            {'if': {'column_id': 'FIELD'},
             'width': '15%'},

            {'textAlign': 'center',
             'border': '1px solid black',
             'font-family': 'sans-serif'}

        ],
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)',
            }
        ],
        style_header={
            'backgroundColor': 'rgb(51, 225, 237)',
            'fontWeight': 'bold',
            'border': '1px solid black'
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)