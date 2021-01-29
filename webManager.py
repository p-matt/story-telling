import dash
import dash_core_components as dcc
import dash_html_components as html


def get_page_idx(app):
    return html.Div([
        html.Div(
            [
                dcc.Link(
                    [html.Label("Évolution à échelle mondiale"),
                     html.Img(src=app.get_asset_url('/img/monde.png'))
                     ], href='/monde'),
            ], className="elem"),
        html.Div(
            [
                dcc.Link(
                    [html.Label("Évolution à échelle continentale"),
                     html.Img(src=app.get_asset_url('/img/continent.png'))
                     ], href='/continent'),
            ], className="elem"),
        html.Div(
            [
                dcc.Link(
                    [html.Label("Évolution à échelle internationale"),
                     html.Img(src=app.get_asset_url('/img/pays.png'))
                     ], href='/inter'),
            ], className="elem"),
        html.Div(
            [
                dcc.Link(
                    [html.Label("Focus sur l'Europe"),
                     html.Img(src=app.get_asset_url('/img/eu.png'))
                     ], href='/europe'),
            ], className="elem"),
        html.Div(
            [
                dcc.Link(
                    [html.Label("Focus sur les États-Unis"),
                     html.Img(src=app.get_asset_url('/img/usa.png'))
                     ], href='/usa'),
            ], className="elem"),
        html.Div(
            [
                dcc.Link(
                    [html.Label("Analyse des données"),
                     html.Img(src=app.get_asset_url('/img/analyse.jpg'))
                     ], href='/data-analyse'),
            ], className="elem"),

        html.Br()
    ])


def get_page_world(figs):
    return html.Div(
        [
            html.H1("Statistiques Monde"),
            html.Div(
                [
                    html.H3("Parallèle entre le nombre de cas, le nombre de mort et le nombre de guérisons totales"),
                    dcc.Graph(figure=figs[0])
                ], className="row"),

            html.Div(
                [
                    html.H3("Parallèle entre le nombre de cas et le nombre de mort par jour"),
                    dcc.Graph(figure=figs[1])
                ], className="row"),
        ])


def get_page_continent(figs):
    return html.Div([
        html.H1("Statistiques Continents"),
        html.Div(
            [
                html.H3("Évolution du nombre de cas"),
                dcc.Graph(figure=figs[0])
            ], className="row"),
        html.Div(
            [
                html.H3("Évolution du nombre de morts"),
                dcc.Graph(figure=figs[1])
            ], className="row"),
        html.Div(
            [
                html.H3("Évolution du nombre de mort par cas"),
                dcc.Graph(figure=figs[2])
            ], className="row")
    ])


def get_page_inter(figs):
    return html.Div([
        html.H1("Statistiques Pays"),
        html.Div(
            [
                html.Div(
                    [
                        html.H3("Nombre de morts total"),
                        dcc.Graph(figure=figs[0])
                    ], className="cellule"),

                html.Div(
                    [
                        html.H3("Nombre de mort par habitants"),
                        dcc.Graph(figure=figs[1])
                    ], className="cellule"),
            ], className="row"),

        html.Div(
            [
                html.Div(
                    [
                        html.H3(
                            "Nombre de morts par habitants en fonction de l'Indice de développement et du nombre total de cas"),
                        dcc.Graph(figure=figs[2])
                    ], className="cellule"),

                html.Div(
                    [
                        html.H3(
                            "Nombre de morts par habitants en fonction du PIB moyen par habitant et du nombre total de cas"),
                        dcc.Graph(figure=figs[3])
                    ], className="cellule"),
            ], className="row"),

        html.Div(
            [
                html.Div(
                    [
                        html.H3(
                            "Évolution du nombre de morts sur une période de 10 mois"),
                        dcc.Graph(figure=figs[4])
                    ], className="cellule"),
                html.Div(
                    [
                        html.H3(
                            "Évolution du nombre de cas sur une période de 10 mois"),
                        dcc.Graph(figure=figs[5])
                    ], className="cellule"),

            ], className="row"),

        html.Div(
            [
                html.Div(
                    [
                        html.H3(
                            "Évolution du nombre de cas"),
                        dcc.Graph(figure=figs[6])
                    ])

            ], className="row"),
        html.Div(
            [
                html.Div(
                    [
                        html.H3(
                            "Évolution du nombre de morts"),
                        dcc.Graph(figure=figs[7])
                    ])

            ], className="row"),

    ], )


def get_page_europe(figs):
    return html.Div(
        [
            html.H1("Statistiques Europe"),
            html.Div([
                html.H3("Pays les plus touchés: Évolution du nombre de mort"),
                dcc.Graph(figure=figs[0])
            ], className="row"),

            html.Div([
                html.H3("Pays les plus touchés: Évolution du nombre de cas"),
                dcc.Graph(figure=figs[1])
            ], className="row"),

            html.Div([
                html.H3("Pays les plus touchés: Évolution du nombre de morts par jour"),
                dcc.Graph(figure=figs[2])
            ], className="row"),

            html.Div([
                html.H3("Pays les plus touchés: Évolution des cas par jour"),
                dcc.Graph(figure=figs[3])
            ], className="row"),

            html.Div([
                html.H3("Propogation du virus, nombre de nouveau cas par jour"),
                dcc.Graph(figure=figs[4])
            ], className="row")

        ])


def get_page_usa(figs):
    return html.Div([
        html.H1("Statistiques États-Unis"),
        html.Div(
            [
                html.H3(
                    "USA - Tendances dégagées: taux de morts/cas en fonction de la densité de la population"),
                dcc.Graph(figure=figs[0])
            ], className="row"),

        html.Div(
            [
                html.H3(
                    "USA - Évolution moyenne du nombre de morts/cas par habitants en fonction du taux de personnes "
                    "agés dans la population"),
                dcc.Graph(figure=figs[1])
            ], className="row"),

        html.Div(
            [
                html.H3(
                    "USA - Corrélation du nombre de morts/cas par habitants en fonction du taux de fumeurs dans la "
                    "population"),
                dcc.Graph(figure=figs[2])
            ], className="row")
    ])


def get_page_data_analyse():
    p = open('assets/data/p.txt', "r", encoding='utf-8').read()
    return html.Div(
        [
            html.H1("Analyses des données"),
            html.Div(
                [
                    html.P(p)
                ], className="row", id="p-container")
        ]
    )


def get_page(app, figs):
    page_index = get_page_idx(app)
    page_world = get_page_world(figs[0])
    page_continent = get_page_continent(figs[1])
    page_inter = get_page_inter(figs[2])
    page_europe = get_page_europe(figs[3])
    page_usa = get_page_usa(figs[4])
    page_data_analyse = get_page_data_analyse()

    return page_index, page_world, page_continent, page_inter, page_europe, page_usa, page_data_analyse


def get_app_layout(app):
    return html.Div(
        [
            dcc.Location(id='url'),
            html.Nav([
                dcc.Link([
                    html.Img(src=app.get_asset_url('/img/home.png'))], href="/"),
                html.H1("Statistiques liées à l'impact du covid19")
            ]),
            html.H2(),
            html.Div(id='page-content')
        ])


class Web:

    def __init__(self, figs):
        external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
        self.app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
        self.server = self.app.server
        self.app.layout = get_app_layout(self.app)
        page_index, page_world, page_continent, page_inter, page_europe, page_usa, page_data_analyse = get_page(self.app, figs)

        @self.app.callback(dash.dependencies.Output('page-content', 'children'),
                           [dash.dependencies.Input('url', 'pathname')])
        def display_page(pathname):
            if pathname == '/monde':
                return page_world
            elif pathname == '/continent':
                return page_continent
            elif pathname == '/inter':
                return page_inter
            elif pathname == '/europe':
                return page_europe
            elif pathname == '/usa':
                return page_usa
            elif pathname == '/data-analyse':
                return page_data_analyse
            else:
                return page_index

    def run(self):
        self.app.run_server(debug=True)
