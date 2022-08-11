from sqlalchemy.orm import Session, joinedload
from sqlalchemy import insert, select

from database.models import RecipeModel
from web.schemas import RecipeSchema


class RecipesRepo:
    def __init__(self, session: Session):
        self._session = session

    def create(self, data:RecipeSchema):
        #new_recipe = RecipeModel(recipe_name=data.recipe_name, temp=data.temp, time=data.time, type=data.type, manual=data.manual)
        statement = insert(RecipeModel).values(recipe_name=data.recipe_name, temp=data.temp, time=data.time, type=data.type, manual=data.manual, price=data.price)
        result = self._session.execute(statement)
        return result.inserted_primary_key[0]

    def get(self, recipe_id):
        result = self._session.query(RecipeModel).options(joinedload(RecipeModel.ingredients)).filter(RecipeModel.recipe_id==recipe_id).first()
        return result

    def get_recipe_by_name(self, recipe_name):
        result = self._session.query(RecipeModel).filter(RecipeModel.recipe_name == recipe_name).first()
        return result

    def all(self):
        result = self._session.query(RecipeModel).options(joinedload(RecipeModel.ingredients)).all()
        return result

    def get_menu(self):
        statement = select(RecipeModel.recipe_name, RecipeModel.price)
        result = self._session.execute(statement).all()
        return result

    def update_name(self, recipe, new_value):
        recipe.recipe_name = new_value
        updated_recipe_id = self.create(recipe)
        return self.get(updated_recipe_id)

    def delete_recipe(self, recipe_id):
        recipe = self._session.query(RecipeModel).filter(RecipeModel.recipe_id==recipe_id).first()
        self._session.delete(recipe)
        return "ok"

