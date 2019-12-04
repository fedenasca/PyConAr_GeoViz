import dash
import dash_core_components as dcc
import dash_html_components as html

from plotly import graph_objs as go

mapbox_access_token = 'pk.eyJ1IjoiamFja2x1byIsImEiOiJjajNlcnh3MzEwMHZtMzNueGw3NWw5ZXF5In0.fk8k06T96Ml9CLGgKmk81w'
#nos pide el key... son gratuitos, 
#hay que entrar a mapbox.como te registrar y te da uno
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([ #para crea un mapa, creamos un elemento graph, y le tenemos que poner la figura y el layout

    html.H1("Mapa de distribucion Electrica"),

    dcc.Dropdown(
        id= 'dd_region',
        options= [
            {'label': 'Centro','value':'centro'},
            {'label': 'Sur', 'value': 'sur'}
        ]),

    dcc.Graph(
        id = 'map',
        figure = go.Figure(
            data= [
                go.Scattermapbox( #solo estamos poniendo un punto... pero lat=[1, 2, 3] le pasamos listas :)... Si tenemos un data set de pandas, le pasamos Archivo n4
                    lat=[4.6008531],
                    lon=[-74.0651495],
                    text=['Universidad De Los Andes'],
                    marker=dict(size=10),
                    mode='markers', #si le pongo modo line... me va marcar linea entre puntos, tambien podemos llenar el area del polígono
                    name='SciPyLA')
            ],
            layout= go.Layout(
                mapbox= go.layout.Mapbox(
                    accesstoken= mapbox_access_token,
                    center= dict(lat=4.6008531, lon=-74.0651495),
                ),
                margin=dict(l=10,r=10,t=10,b=10)
            )
        )
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)