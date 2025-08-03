from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models import DroneMission, Product
from typing import List, Optional

router = APIRouter(prefix="/drones", tags=["Drone Missions"])


@router.get("/missions", summary="🚁 Get active drone missions", response_model=List[dict])
def get_active_drone_missions(db: Session = Depends(get_db)):
    """
    Returns a list of active drone missions with related product info.
    """
    missions = db.query(DroneMission).filter(
        DroneMission.status == "in-transit"
    ).all()

    output = []

    for m in missions:
        product = db.query(Product).filter(Product.id == m.product_id).first()
        output.append({
            "id": m.id,
            "drone_id": m.drone_id,
            "product_name": product.name if product else "Unknown",
            "destination": m.destination,
            "status": m.status,
            "eta": m.eta
        })

    return output
