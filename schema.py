import strawberry
from typing import List
from common.structures import Instrument
from resolvers import get_instruments


@strawberry.type
class Query:
    instruments: List[Instrument] = strawberry.field(resolver=get_instruments)
