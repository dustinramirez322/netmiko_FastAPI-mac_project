from sqlalchemy import desc
from sqlalchemy.orm import Session
import models
import utilities


# Return a list of all known mac addresses and their descriptions
def select_all_known_mac(db: Session):
    return db.query(models.MacAddressTable).all()


# Return information about an individual mac addresss
def select_indiv_known_mac(db: Session, mac_address=None):
    return db.query(models.MacAddressTable).filter(models.MacAddressTable.mac_address == mac_address).first()


# Insert the current datetime into the datetime_table
def insert_datetime(db: Session, datetime):
    datetime = models.DatetimeTable(datetime_id=datetime)
    db.add(datetime)
    db.commit()
    db.refresh(datetime)
    return datetime


# Insert datetime and macs into the Datetime Mac Junction Table
def insert_dt_macs(db: Session, datetime, mac_list):
    for m in mac_list:
        mac_insert = models.DatetimeMacJunction(datetime_id=datetime, mac_address=m)
        db.add(mac_insert)
        db.commit()
        db.refresh(mac_insert)


def select_recent_datetime(db: Session):
    return db.query(models.DatetimeTable).order_by(desc(models.DatetimeTable.datetime_id)).first()


def select_recent_macs(db: Session):
    most_recent = select_recent_datetime(db)
    recent_raw = most_recent.__repr__()
    recent_dt = recent_raw.strftime("%Y-%m-%d %H:%M:%S")
    return db.query(models.DatetimeMacJunction).filter(models.DatetimeMacJunction.datetime_id == recent_dt).all()


def insert_unk_mac(db: Session, unk_mac):
    mac_address = models.MacAddressTable(mac_address=unk_mac)
    db.add(mac_address)
    db.commit()
    db.refresh(mac_address)
    return mac_address