from sqlalchemy.orm import Session
from sqlalchemy import insert, select
from database.models import UnitModel


class UnitRepo:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data):
        statement = insert(UnitModel).values(**data.dict())
        result = self._session.execute(statement)
        return result.inserted_primary_key[0]

    def get(self, unit_id):
        statement = select(UnitModel).where(UnitModel.id == unit_id)
        result = self._session.execute(statement).scalars().unique().one()
        return result

    def get_all(self):
        statement = select(UnitModel)
        result = self._session.execute(statement).all()
        return result
