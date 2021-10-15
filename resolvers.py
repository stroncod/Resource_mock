from datetime import datetime
from database import Database
from common.structures import Instrument
import os

resource_path = os.path.join('database', 'data')
odb = Database(path=resource_path)
odb.load()


def get_instruments(site: str, date: str):
    date_time = datetime.strptime(date, "%Y-%m-%d")
    return [Instrument(inst) for inst in odb.instruments[site][date_time]]
