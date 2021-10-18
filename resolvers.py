from datetime import datetime
from database import Database
from common.structures import Instrument, GmosNorthFPU, GmosSouthFPU, GmosNorthDisperser, GmosSouthDisperser
import os

resource_path = os.path.join('database', 'data')
odb = Database(path=resource_path)
odb.load()


def get_instruments(site: str, date: str):
    date_time = datetime.strptime(date, "%Y-%m-%d")
    return [Instrument(inst) for inst in odb.instruments[site][date_time]]


def get_north_disperser(date: str):
    date_time = datetime.strptime(date, "%Y-%m-%d")
    if date_time not in odb.grat['n']:
        prve_date = odb._previous(odb.grat['n'].keys(), date_time)
        return [GmosNorthDisperser(disp) for disp in odb.grat['n'][prve_date]]
    else:
        return [GmosNorthDisperser(disp) for disp in odb.grat['n'][date_time]]


def get_south_disperser(date: str):
    date_time = datetime.strptime(date, "%Y-%m-%d")
    if date_time not in odb.grat['n']:
        prve_date = odb._previous(odb.grat['s'].keys(), date_time)
        return [GmosSouthDisperser(disp) for disp in odb.grat['s'][prve_date]]
    else:
        return [GmosSouthDisperser(disp) for disp in odb.grat['s'][date_time]]


def get_north_fpus(date: str):
    date_time = datetime.strptime(date, "%Y-%m-%d")
    return [GmosNorthFPU(fpu) for fpu in odb.fpur['n'][date_time]]


def get_south_fpus(date: str):
    date_time = datetime.strptime(date, "%Y-%m-%d")
    return [GmosSouthFPU(fpu) for fpu in odb.fpur['s'][date_time]]
