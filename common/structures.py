import strawberry
from enum import Enum


@strawberry.type
class Instrument:
    name: str


@strawberry.enum
class GmosSouthFPU(Enum):

    BHROS = "BHROS"
    NS1 = "NS1"
    NS2 = "NS2"
    NS3 = "NS3"
    NS4 = "NS4"
    NS5 = "NS5"
    LONG_SLIT_0_25 = "0.25arcsec"
    LONG_SLIT_0_50 = "0.5arcsec"
    LONG_SLIT_0_75 = "0.75arcsec"
    LONG_SLIT_1_00 = "1.0arcsec"
    LONG_SLIT_1_50 = "1.5arcsec"
    LONG_SLIT_2_00 = "2.0arcsec"
    LONG_SLIT_5_00 = "5.0arcsec"
    IFU1 = "IFU1"
    IFU2 = "IFU-2"
    IFU3 = "IFU3"
    IFU_N = "IFU-N"
    IFU_NB = "IFU-B"
    IFU_NR = "IFU-R"


@strawberry.enum
class GmosNorthFPU(Enum):
    
    NS0 = "NS0"
    NS1 = "NS1"
    NS2 = "NS2"
    NS3 = "NS3"
    NS4 = "NS4"
    NS5 = "NS5"
    LONG_SLIT_0_25 = "0.25arcsec"
    LONG_SLIT_0_50 = "0.5arcsec"
    LONG_SLIT_0_75 = "0.75arcsec"
    LONG_SLIT_1_00 = "1.0arcsec"
    LONG_SLIT_1_50 = "1.5arcsec"
    LONG_SLIT_2_00 = "2.0arcsec"
    LONG_SLIT_5_00 = "5.0arcsec"
    IFU1 = "IFU1"
    IFU2 = "IFU-2"
    IFU3 = "IFU3"


@strawberry.enum
class GmosNorthDisperser(Enum):
 
    MIRROR = "MIRROR"
    B1200_G5301 = "B1200"
    R831_G5302 = "R831"
    B600_G5303 = "B600"
    B600_G5307 = "B600"
    R600_G5304 = "R600"
    B480_G5309 = "B480"
    R400_G5305 = "R400"
    R150_G5306 = "R150"
    R150_G5308 = "R150"


@strawberry.enum
class GmosSouthDisperser(Enum):

    MIRROR = "MIRROR"
    B1200_G5321 = "B1200"
    R831_G5322 = "R831"
    B600_G5323 = "B600"
    R600_G5324 = "R600"
    B480_G5327 = "B480"
    R400_G5325 = "R400"
    R150_G5326 = "R150"
