import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.associationproxy import association_proxy

from web.schemas import Unit, RecipeType


Base = declarative_base()


class RecipeIngredients(Base):
    __tablename__ = 'recipe_ingredients'

    recipe_id = sa.Column(sa.ForeignKey("recipes.recipe_id", ondelete="CASCADE"), primary_key=True )
    ingredient_id = sa.Column(sa.ForeignKey("ingredients.ingredient_id", ondelete="CASCADE"), primary_key=True )
    quantity = sa.Column(sa.Float, nullable=False)
    recipe = relationship("RecipeModel", back_populates='ingredients', cascade="all, delete")
    ingredient = relationship("IngredientsModel", back_populates='recipe')

    #proxies
    recipe_name = association_proxy(target_collection='recipe', attr='recipe_name')
    ing_name = association_proxy(target_collection='ingredient', attr='ing_name')
    unit = association_proxy(target_collection='ingredient', attr='unit')


class RecipeModel(Base):
    __tablename__ = 'recipes'

    recipe_id: int = sa.Column(sa.Integer, primary_key=True)
    recipe_name: str = sa.Column(sa.String)
    manual: str = sa.Column(sa.Text)
    temp: float = sa.Column(sa.Integer)
    time: int = sa.Column(sa.Integer)
    type: str = sa.Column(sa.Enum(RecipeType))
    price: float = sa.Column(sa.Float)
    ingredients = relationship("RecipeIngredients", back_populates='recipe', cascade="all, delete-orphan", single_parent=True)


class IngredientsModel(Base):
    __tablename__ = 'ingredients'

    ingredient_id: int = sa.Column(sa.Integer, primary_key=True)
    ing_name: str = sa.Column(sa.String)
    unit: str = sa.Column(sa.Enum(Unit))
    recipe = relationship("RecipeIngredients", back_populates='ingredient')


