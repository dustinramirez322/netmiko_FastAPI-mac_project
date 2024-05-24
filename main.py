from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def api_root():
    return {"Welcome": "This API will display information about MAC addresses on your network",
            "Documentation": "http://127.0.0.1:8000/docs", "Version": '0.1'}


@app.get("/known_macs")
def select_all_known_mac(db: Session = Depends(get_db)):
    known_macs = crud.select_all_known_mac(db)
    return known_macs


@app.get("/known_macs/{mac_address}", response_model=schemas.MacAddress)
async def select_indiv_known_mac(mac_address: str, db: Session = Depends(get_db)):
    mac_address_info = crud.select_indiv_known_mac(db, mac_address=mac_address)
    if mac_address_info == None:
        raise HTTPException(status_code=404, detail="MAC Address not found in database")
    else:
        return mac_address_info

@app.get("/recent_datetime/")
async def select_recent_datetime(db: Session = Depends(get_db)):
    recent_dt = crud.select_recent_datetime(db)
    return recent_dt


@app.get("/current_macs/")
async def select_current_macs(db: Session = Depends(get_db)):
    recent_macs = crud.select_recent_macs(db)
    return recent_macs