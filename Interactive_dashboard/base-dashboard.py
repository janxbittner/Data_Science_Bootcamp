import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

app= dash.Dash(__name__)

app.layout = html.Div(children= [
    html.H1(children='Hallo Dash!'),
    dcc.Graph(
        figure=go.Figure([
            go.Bar(
                x = ['2018','2019','2020'],
                y = [120,110,150],
                name = 'local'

            ),
            go.Bar(
                x = ['2018','2019','2020'],
                y = [400,350,470],
                name = 'global'
            )
        ])
    )
])



if __name__ == '__main__':
    app.run_server(debug=True)

