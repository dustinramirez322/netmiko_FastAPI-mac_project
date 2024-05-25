import database
import net_cmds
from datetime import datetime
import crud


def iden_unk_macs(current_macs, known_macs):
    unk_macs = []
    # compare macs currently online and add to unk_macs list if not found
    for c in current_macs:
        if c in known_macs:
            pass
        else:
            unk_macs.append(c)
    return unk_macs


def scheduled_mac_get():
    # Get and post datetime
    session = database.start_db()
    ran_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    crud.insert_datetime(session, ran_time)
    # Get and compare macs
    raw_known_macs = crud.select_all_known_mac(session)
    known_macs = []
    for r in raw_known_macs:
        known_macs.append(r.return_macs())
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
        crud.insert_dt_macs(session, ran_time, current_macs)
    database.close_db(session)

