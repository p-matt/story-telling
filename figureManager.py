import plotly.express as px
import plotly.graph_objs as go


def get_figure_from_df(dfs):
    df_monde = dfs[0]
    df_continent = dfs[1]
    df_inter = dfs[2]
    df_europe = dfs[3]
    df_usa = dfs[4]

    fig_monde = get_fig_monde(df_monde)
    fig_continent = get_fig_continent(df_continent)
    fig_inter = get_fig_inter(df_inter)
    fig_europe = get_fig_europe(df_europe)
    fig_usa = get_fig_usa(df_usa)

    figs = [fig_monde, fig_continent, fig_inter, fig_europe, fig_usa]

    set_figures(figs)

    return figs


def set_figures(figs):
    figs[0][1].data[0].name = 'Nombre de morts par jour'
    figs[0][1].data[1].name = 'Nombre de cas par jour'
    figs[0][1].update_yaxes(title_text="Date")
    figs[2][0].update_xaxes(tickmode='linear')
    figs[2][1].update_xaxes(tickmode='linear')
    figs[2][2].update_traces(marker_sizemin=3)
    figs[2][3].update_traces(marker_sizemin=3)
    figs[2][2].update_layout(xaxis_range=[.3, 1])
    figs[2][5].update_traces(marker_sizemin=4)
    figs[3][4].update_traces(marker_sizemin=2.5)
    # for i, fig in enumerate(figs):
    #
    #     if i == 0 or i == 1:
    #         fig
    #         continue
    #     fig.update_xaxes(tickmode='auto')


# region monde
def get_fig_monde(df):
    fig0 = get_fig_monde0(df[0])
    fig1 = get_fig_monde1(df[1])

    return [fig0, fig1]


def get_fig_monde0(df):
    df["total_healings"] = df.total_cases - df.total_deaths
    return px.scatter(df, x=df.date_months.astype(str),
                      y=["total_deaths", "total_cases", "total_healings"]).update_traces(
        mode="lines+markers")


def get_fig_monde1(df):
    mpj = df.groupby("date")["morts par jour"].sum()
    cpj = df.groupby("date")["cas par jour"].sum()
    date = df.date.unique()

    return px.line(df, x=date, y=[mpj, cpj])


# endregion

# region continent

def get_fig_continent(df):
    fig0 = get_fig_continent0(df[0])
    fig1 = get_fig_continent1(df[0])
    fig2 = get_fig_continent2(df[0])
    return [fig0, fig1, fig2]


def get_fig_continent0(df):
    fig = go.Figure()
    df = df.groupby(["location", "date_months"]).tail(1)
    df = df.groupby(["continent", "date_months"])["total_cases"].sum().reset_index()

    for x, row in df.groupby(["continent"]):
        fig.add_scatter(x=row.date_months.astype(str), y=row.total_cases, name=row.continent.values[0],
                        mode='lines+markers')
    return fig


def get_fig_continent1(df):
    fig = go.Figure()
    df = df.groupby(["location", "date_months"]).tail(1)
    df = df.groupby(["continent", "date_months"])["total_deaths"].sum().reset_index()

    for x, row in df.groupby(["continent"]):
        fig.add_scatter(x=row.date_months.astype(str), y=row.total_deaths, name=row.continent.values[0],
                        mode='lines+markers')
    return fig


def get_fig_continent2(df):
    df = df.groupby(["location", "date_months"]).tail(1)
    df = df.groupby(["continent", "date_months"])[["total_deaths", "total_cases"]].sum().reset_index()

    fig = px.scatter(df, x="total_cases", y="total_deaths", color="continent",
                     marginal_x="box", trendline="ols", template="simple_white")

    results = px.get_trendline_results(fig)
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
    slopes = []
    text_positions = [(-2 * 10 ** 6, 19000), (1.255 * 10 ** 7, 224264), (7 * 10 ** 6, 307790), (9.85 * 10 ** 6, 333600),
                      (-2 * 10 ** 6, 1000), (9 * 10 ** 6, 280000)]

    for i in range(results.shape[0]):
        slopes.append(round(results.iloc[i]["px_fit_results"].params[1], 3))

    coeffs_colors_pos = list(zip(slopes, colors, text_positions))

    for ccp in coeffs_colors_pos:
        fig.add_annotation(dict(font=dict(color=ccp[1], size=12),
                                x=ccp[2][0],
                                y=ccp[2][1],
                                showarrow=False,
                                text=ccp[0],
                                textangle=0,
                                xanchor='left',
                                xref="x",
                                yref="y"))
    return fig


# endregion

# region inter
def get_fig_inter(df):
    fig0 = get_fig_inter0(df[0])
    fig1 = get_fig_inter1(df[0])
    fig2 = get_fig_inter2(df[0])
    fig3 = get_fig_inter3(df[0])
    fig4 = get_fig_inter4(df[1])
    fig5 = get_fig_inter5(df[1])
    fig6 = get_fig_inter6(df[1])
    fig7 = get_fig_inter7(df[1])

    return [fig0, fig1, fig2, fig3, fig4, fig5, fig6, fig7]


def get_fig_inter0(df):
    df = df[df['total_deaths'].notna()].sort_values(by="total_deaths")[-50:]
    return px.bar(df, x="iso_code", y="total_deaths", color="total_deaths", hover_name="location")


def get_fig_inter1(df):
    df = df[df.death_by_citizen.notna()].sort_values(by="death_by_citizen")[-50:]
    return px.bar(df, x="iso_code", y="death_by_citizen", color="death_by_citizen", hover_name="location")


def get_fig_inter2(df):
    df = df[df['human_development_index'].notna()].sort_values(by="human_development_index")
    df.total_cases = df.total_cases.fillna(0)
    return px.scatter(df, x="human_development_index", y="death_by_citizen", size="total_cases",
                      color="total_cases", hover_name="location")


def get_fig_inter3(df):
    df = df[df.gdp_per_capita.notna()].sort_values(by="gdp_per_capita")
    df.total_cases = df.total_cases.fillna(0)
    return px.scatter(df, x="gdp_per_capita", y="death_by_citizen", size="total_cases", color="total_cases",
                      hover_name="location")


def get_fig_inter4(df):
    grouped = df.groupby(["location", "date_months"]).nth([1, 15, -1]).reset_index()
    return px.choropleth(grouped, locations="iso_code", color="total_deaths", hover_name="location",
                         animation_frame=grouped.date_months.astype(str))


def get_fig_inter5(df):
    grouped = df.groupby(["location", "date_months"]).nth([1, 15, -1]).reset_index()
    grouped = grouped[grouped.total_cases.notna()]
    return px.scatter_geo(grouped, locations="iso_code", color="total_cases", hover_name="location", size="total_cases",
                          animation_frame=grouped.date_months.astype(str), scope="world", projection="natural earth")


def get_fig_inter6(df):
    fig = go.Figure()
    grouped = df.sort_values(by=["total_cases", "location"], ascending=False).groupby(["location"],
                                                                                      sort=False)  ## SORT = FALSE
    i = 0
    for x, row in grouped:
        if i == 10:
            break
        fig.add_scatter(x=row.date, y=row.total_cases, name=row.location.values[0],
                        mode='lines')
        i += 1
    return fig


def get_fig_inter7(df):
    fig = go.Figure()
    grouped = df.sort_values(by=["total_deaths", "location"], ascending=False).groupby(["location"],
                                                                                       sort=False)  ## SORT = FALSE
    i = 0
    for x, row in grouped:
        if i == 10:
            break
        fig.add_scatter(x=row.date, y=row.total_deaths, name=row.location.values[0],
                        mode='lines')
        i += 1
    return fig


# endregion

# region europe
def get_fig_europe(df):
    fig0 = get_fig_europe0(df[0])
    fig1 = get_fig_europe1(df[0])
    fig2 = get_fig_europe2(df[0])
    fig3 = get_fig_europe3(df[0])
    fig4 = get_fig_europe4(df[0])
    return [fig0, fig1, fig2, fig3, fig4]


def get_fig_europe0(df):
    interested_locations = df.sort_values(by="total_deaths", ascending=False)["location"].unique()[:10]
    df = df[df["location"].isin(interested_locations)]
    return px.line(df, x="date", y="total_deaths", color="location", hover_name="location")


def get_fig_europe1(df):
    interested_locations = df.sort_values(by="total_cases", ascending=False)["location"].unique()[:10]
    df = df[df["location"].isin(interested_locations)]
    return px.line(df, x="date", y="total_cases", color="location", hover_name="location")


def get_fig_europe2(df):
    interested_locations = df.sort_values(by="total_deaths", ascending=False)["location"].unique()[:10]
    df = df[df["location"].isin(interested_locations)]
    return px.line(df, x="date", y="morts par jour", color="location", hover_name="location")


def get_fig_europe3(df):
    interested_locations = df.sort_values(by="total_cases", ascending=False)["location"].unique()[:11]
    df = df[df["location"].isin(interested_locations)]
    df = df[df["location"] != "Spain"]
    return px.line(df, x="date", y="cas par jour", color="location", hover_name="location")


def get_fig_europe4(df):
    df.loc[df["cas par jour"] < 0, "cas par jour"] = 0
    return px.scatter_geo(df, scope="europe", projection="orthographic", locations="iso_code", size="cas par jour",
                          color="cas par jour", hover_name="location",
                          animation_frame="date")


# endregion

# region USA
def get_fig_usa(df):
    fig0 = get_fig_usa0(df[0])
    fig1 = get_fig_usa1(df[0])
    fig2 = get_fig_usa2(df[0])

    return [fig0, fig1, fig2]


def get_fig_usa0(df):
    df = df.sort_values(by=["Pop Density"], ascending=False)[1:]
    return px.scatter(df, x=df["Pop Density"], y=["Deaths by citizens", "Infections by citizens"],
                      trendline="ols")


def get_fig_usa1(df):
    df = df.groupby("Age 65+")[["Deaths by citizens", "Infections by citizens"]].mean().reset_index()
    return px.scatter(df, x=df["Age 65+"], y=["Deaths by citizens", "Infections by citizens"]).update_traces(
        mode="markers")


def get_fig_usa2(df):
    return px.scatter(df, x=df["Smoking Rate"], y=["Deaths by citizens", "Infections by citizens"]).update_traces(
        mode="markers")

# endregion
