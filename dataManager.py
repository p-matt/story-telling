import pandas as pd
import pycountry_convert as pc

pd.options.mode.chained_assignment = None
pd.set_option('display.max_columns', None)

df_main = pd.read_csv("assets/data/raw_data.csv")
df_main["date_months"] = pd.to_datetime(df_main['date']).dt.to_period('M')
df_main_usa = pd.read_csv("assets/data/usa_data.csv")

removed_cols = [colname for colname in df_main.columns if "Unnamed" in colname]
df_main = df_main.drop(removed_cols, axis=1)


def get_dataframe():
    #  Déclarations des DataFrames
    df_world_static = df_main.groupby(["location", "date_months"]).tail(1).groupby("date_months").sum().reset_index()
    df_world_temporal_by_day = get_df_monde_by_day()

    df_continent_temporal = get_df_continent(df_main)

    df_inter_static = get_df_inter_static()

    df_eu = get_df_europe(df_continent_temporal)

    set_df_usa()

    df_monde = [df_world_static, df_world_temporal_by_day]
    df_continent = [df_continent_temporal]
    df_inter = [df_inter_static, df_main]
    df_europe = [df_eu]
    df_usa = [df_main_usa]
    return [df_monde, df_continent, df_inter, df_europe, df_usa]


def get_df_inter_static():
    df = df_main.groupby("location").tail(1)
    df["death_by_citizen"] = df.total_deaths / df.population

    return df


def set_df_usa():
    df_main_usa["Deaths by citizens"] = df_main_usa["Deaths"] / df_main_usa["Population"]
    df_main_usa["Infections by citizens"] = df_main_usa["Infected"] / df_main_usa["Population"]


def get_df_monde_by_day():
    df = df_main.copy()
    mpj = df_main.sort_values(by="total_deaths", ascending=False).groupby("location").apply(get_deaths_values_by_day)
    cpj = df_main.sort_values(by="total_cases", ascending=False).groupby("location").apply(get_cases_values_by_day)

    df["morts par jour"] = mpj.reset_index(level=0, drop=True)
    df["cas par jour"] = cpj.reset_index(level=0, drop=True)

    return df


def get_df_europe(df_continent):
    df = df_continent[df_continent["continent"] == "EU"]
    mpj = df.sort_values(by="total_deaths", ascending=False).groupby("location").apply(get_deaths_values_by_day)
    cpj = df.sort_values(by="total_cases", ascending=False).groupby("location").apply(get_cases_values_by_day)

    df["morts par jour"] = mpj.reset_index(level=0, drop=True)
    df["cas par jour"] = cpj.reset_index(level=0, drop=True)

    return df


def get_deaths_values_by_day(row):
    return row.total_deaths.diff(periods=-1).fillna(0)


def get_cases_values_by_day(row):
    return row.total_cases.diff(periods=-1).fillna(0)


def get_df_continent(df):
    df["continent"] = df.apply(lambda x: get_continent(x["location"]), axis=1)
    return df


def get_continent(country):
    try:
        iso2 = pc.country_name_to_country_alpha2(country)
        return pc.country_alpha2_to_continent_code(iso2)
    except KeyError:
        if country == "Vatican" or country == "Sint Maarten (Dutch part)" or country == "Kosovo" or country == "Faeroe Islands" or country == "Bonaire Sint Eustatius and Saba":
            return "EU"
        elif country == "Timor":
            return "AS"
        elif country == "Curacao":
            return "NA"
        elif country == "Democratic Republic of Congo" or country == "Cote d'Ivoire":
            return "AF"
