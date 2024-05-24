from sqlalchemy import Column, DATE, VARCHAR
from database import Base


# Define the Datetime DB class
class DatetimeTable(Base):
    __tablename__ = "datetime_table"
    datetime_id = Column(DATE, primary_key=True)

    def __repr__(self):
        return self.datetime_id

# Define the MAC Address Table DB class
class MacAddressTable(Base):
    __tablename__ = "mac_address_table"
    mac_address = Column(VARCHAR, primary_key=True)
    description = Column(VARCHAR)

    def return_macs(self):
        return self.mac_address

    def return_desc_and_mac(self):
        return {'mac_address': self.mac_address, 'description': self.description}

# Define the MAC and datetime junction Table DB class
class DatetimeMacJunction(Base):
    __tablename__ = "datetime_mac_junction"
    mac_address = Column(VARCHAR, primary_key=True)
    datetime_id = Column(DATE, primary_key=True)

