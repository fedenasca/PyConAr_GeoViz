import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Output, Input, State

from plotly import graph_objs as go

import pandas as pd

mapbox_access_token = 'pk.eyJ1IjoiamFja2x1byIsImEiOiJjajNlcnh3MzEwMHZtMzNueGw3NWw5ZXF5In0.fk8k06T96Ml9CLGgKmk81w'

conj_name = {
    15615: 'Boa Aventura',
    16070: 'Nova Friburgo',
    16068: 'Campo do Coelho',
    15616: 'Vale dos Peoes',
    16069: 'Conselheiro Paulino'
}

#################################
trd = pd.read_csv('./data/UNI_TRD_ENF17.csv')
#################################

######################

map_layout= go.Layout(
            mapbox=go.layout.Mapbox(
                accesstoken=mapbox_access_token,
                center=dict(lat=trd.lat.mean(), lon=trd.lon.mean()),
                zoom=10,
                pitch=45,
                style='outdoors'),
            margin=dict(l=0, t=0, b=0, r=0)
        )
######################

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([

    html.H1("Mapa de distribucion Electrica"),
    html.H3("Seleccione Regiones"),

    dcc.Dropdown(
        id= 'dd_region',
        multi= True,
        options= [dict(label=conj_name[x], value=x) for x in trd.CONJ.unique()],
        value= trd.CONJ.unique()),

    dcc.Graph(
        id = 'map'
    )
])

############################################################

@app.callback( #defino el componente de entrada y el componente de salida
    Output(component_id='map', component_property='figure'), #proper.. es lo que voy a modificar.. Esta funcion va a retornar una figura
    [Input('dd_region','value')] #cual es componente y qué propiedad. Aca usamos el "value" que es el valor instantáneo
)
def update_map(region):
    print(region)

    trd_selecion = trd[trd.CONJ.isin(region)]

    map_data=[
        go.Scattermapbox(
            lat= trd_selecion.lat,
            lon= trd_selecion.lon,
            mode='markers')
    ]

    return go.Figure(data= map_data, layout= map_layout)


if __name__ == '__main__':
    app.run_server(debug=True)