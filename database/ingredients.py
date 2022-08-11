from sqlalchemy.orm import Session, joinedload
from sqlalchemy import insert, select, update, delete

from database.models import RecipeModel, IngredientsModel


class IngredientsRepo:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data):
        ing_name, unit = data
        statement = insert(IngredientsModel).values(ing_name=ing_name, unit=unit)
        result = self._session.execute(statement)
        return result.inserted_primary_key[0]

    def get(self, ing_id):
        result = self._session.query(IngredientsModel).options(joinedload(IngredientsModel.recipe)).filter(IngredientsModel.ingredient_id==ing_id).one()
        return result

    def get_ingredient_by_name(self, ing_name):
        result = self._session.query(IngredientsModel).filter(IngredientsModel.ing_name == ing_name).first()
        return result

    def all(self):
        result = self._session.query(RecipeModel).options(joinedload(RecipeModel.ingredients)).all()
        return result

    def update(self, recipe_id, new_value):
        pass

