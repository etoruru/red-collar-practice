from fastapi import Depends
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from web.dependencies import get_unit_repo, get_db
from web.schemas import UnitBase
from database.unit import UnitRepo

router = APIRouter()


@router.post('/')
def create_unit(
        unit: UnitBase,
        unit_repo: UnitRepo = Depends(get_unit_repo),
        session: Session = Depends(get_db)):
    with session.begin():
        unit_id = unit_repo.create(unit)
        return unit_repo.get(unit_id)


@router.get('/')
def get_units(db: Session = Depends(get_unit_repo)):
    all_units = db.get_all()
    return all_units


@router.get('/{unit_id}')
def get_one_unit(unit_id: int, db: Session = Depends(get_unit_repo)):
    result = db.get(unit_id)
    return result
