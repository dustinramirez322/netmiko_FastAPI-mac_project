import requests
import database
import net_cmds
from datetime import datetime
import crud

# Remove later
url = 'http://127.0.0.1:8000/known_macs'


def iden_unk_macs(current_macs, known_macs):
    unk_macs = []
    # compare macs currently online and add to unk_macs list if not found
    for c in current_macs:
        if c in known_macs:
            pass
        else:
            unk_macs.append(c)
    return unk_macs


def scheduled_mac_get(url):
    # Get and post datetime
    session = database.start_db()
    ran_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    crud.insert_datetime(session, ran_time)
    # Get and compare macs
    raw_known_macs = requests.get(url).json()
    known_macs = []
    for r in raw_known_macs:
        known_macs.append(r['mac_address'])
    current_macs = net_cmds.get_wrt_macs()
    # Get a list of any unknown macs
    unk_macs = iden_unk_macs(current_macs, known_macs)
    # If unk_macs list is greater than zero then insert mac into mac table with a general description
    if len(unk_macs) > 0:
        # execute if a new mac is found
        for u in unk_macs:
            crud.insert_unk_mac(session, u)
    # execute if no unknown macs are found
    else:
        crud.insert_macs(session, ran_time, current_macs)
    database.close_db(session)

def get_recent_dt():
    session = database.start_db()
    # pull the most recent datetime entry from the datetime_table
    most_recent = crud.select_recent_datetime(session)
    database.close_db(session)
    # change the datetime output
    recent_raw = most_recent.__repr__()
    recent_dt = recent_raw.strftime("%Y-%m-%d %H:%M:%S")
    return recent_dt

