from sqlalchemy.orm import Session
from sqlalchemy import insert, select
from database.models import IngredientsModel


class IngredientsRepo:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data):
        statement = insert(IngredientsModel).values(**data.dict())
        result = self._session.execute(statement)
        return result.inserted_primary_key[0]

    def get(self, ingredient_id):
        statement = select(IngredientsModel).where(IngredientsModel.ingredient_id == ingredient_id)
        result = self._session.execute(statement).scalars().unique().one()
        return result

    def get_all(self):
        statement = select(IngredientsModel)
        result = self._session.execute(statement).all()
        return result

