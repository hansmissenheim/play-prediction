from typing import Iterable

import nfl_data_py as nfl
from pandas import DataFrame

CACHE_ERROR_MESSAGE = "cache file does not exist."


def load_pbp_data(years: int | Iterable[int], downcast: bool = True) -> DataFrame:
    if isinstance(years, int):
        years = [years]
    try:
        data = nfl.import_pbp_data(years, cache=True, downcast=downcast)
    except ValueError as e:
        if CACHE_ERROR_MESSAGE in e.args[0]:
            nfl.cache_pbp(years, downcast=downcast)
            data = nfl.import_pbp_data(years, cache=True, downcast=downcast)
        else:
            raise e
    return data
