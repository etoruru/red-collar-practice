import sqlalchemy as sa
from sqlalchemy import Table, MetaData
from sqlalchemy.orm import as_declarative, relationship
from sqlalchemy.ext.associationproxy import association_proxy

engine = sa.create_engine('postgresql:///recipes')
metadata = MetaData()


@as_declarative(metadata=metadata)
class Base:
    __tablename__: str
    __table__: Table


class UnitModel(Base):
    __tablename__ = 'unit'

    id: int = sa.Column(sa.Integer, primary_key=True)
    unit: str = sa.Column(sa.String)
    ingredient = relationship('RecipeIngredients', back_populates='unit')


class RecipeType(Base):
    __tablename__ = 'recipe_type'

    id: int = sa.Column(sa.Integer, primary_key=True)
    type: str = sa.Column(sa.String)


class RecipeIngredients(Base):
    __tablename__ = 'recipe_ingredients'
    recipe_id = sa.Column(sa.ForeignKey("recipes.recipe_id"), primary_key=True)
    ingredient_id = sa.Column(sa.ForeignKey("ingredients.ingredient_id"), primary_key=True)
    quantiy = sa.Column(sa.REAL)
    unit_id: int = sa.Column(sa.Integer, sa.ForeignKey('unit.id'))
    unit = relationship('UnitModel', back_populates='ingredient')
    recipe = relationship("RecipeModel", back_populates='ingredients')
    ingredient = relationship("IngredientsModel", back_populates='recipe')

    #proxies
    recipe_name = association_proxy(target_collection='RecipeModel', attr='recipe_name')
    ingredient_name = association_proxy(target_collection='IngredientsModel', attr='ing_name')


class RecipeModel(Base):
    __tablename__ = 'recipes'

    recipe_id: int = sa.Column(sa.Integer, primary_key=True)
    recipe_name: str = sa.Column(sa.String)
    process: str = sa.Column(sa.Text)
    temp: float = sa.Column(sa.REAL)
    time: int = sa.Column(sa.Integer)
    type_id: int = sa.Column(sa.Integer, sa.ForeignKey('recipe_type.id'))
    ingredients = relationship("RecipeIngredients", back_populates='recipe')


class IngredientsModel(Base):
    __tablename__ = 'ingredients'

    ingredient_id: int = sa.Column(sa.Integer, primary_key=True)
    ing_name: str = sa.Column(sa.String)
    recipe = relationship("RecipeIngredients", back_populates='ingredient')


Base.metadata.create_all(engine)

