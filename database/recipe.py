from sqlalchemy.orm import Session
from sqlalchemy import insert, delete, select
from db import RecipeModel


class Recipe:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data):
        statement = insert(RecipeModel).values(**data.dict())
        result = self._session.execute(statement)
        return result.inserted_primary_key[0]

    def get(self, recipe_id):
        statement = select(RecipeModel).where(RecipeModel.recipe_id == recipe_id)
        result = self._session.execute(statement).scalars().unique().one()
        