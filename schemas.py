import datetime
from typing import Union

from pydantic import BaseModel, Json
from pydantic_extra_types.mac_address import MacAddress

class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class MacAddressDict(BaseModel):
    mac_address_dict: dict

class MacAddress(BaseModel):
    mac_address:  MacAddress
    description: str

class DateTime_MAC(BaseModel):
    mac_address: MacAddress
    date: datetime.datetime
