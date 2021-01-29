from dataManager import get_dataframe
from figureManager import get_figure_from_df
from webManager import Web
import sys
sys.setrecursionlimit(10**6)

dataframes = get_dataframe()
figures = get_figure_from_df(dataframes)
webManager = Web(figures)
server = webManager.server # Procfile

if __name__ == '__main__':
    webManager.run()
