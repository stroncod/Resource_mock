import strawberry
from typing import List
from common.structures import GmosNorthDisperser, GmosNorthFPU, GmosSouthDisperser, GmosSouthFPU, Instrument
from resolvers import get_instruments, get_south_fpus, get_north_fpus, get_north_disperser, get_south_disperser


@strawberry.type
class Query:
    instruments: List[Instrument] = strawberry.field(resolver=get_instruments)
    southFpus: List[GmosSouthFPU] = strawberry.field(resolver=get_south_fpus)
    northFpus: List[GmosNorthFPU] = strawberry.field(resolver=get_north_fpus)
    southDisperser: List[GmosNorthDisperser] = strawberry.field(resolver=get_south_disperser)
    northDisperser: List[GmosSouthDisperser] = strawberry.field(resolver=get_north_disperser)
