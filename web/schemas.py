from pydantic import BaseModel

from typing import List, Optional
from enum import Enum


class Unit(Enum):
    g = 'г'
    kg = 'кг'
    l = 'л'
    ml = 'мл'
    lspoon = 'ст.л'
    smspoon = 'ч.л'
    cup = 'стакан'
    pcs = 'шт'


class RecipeType(Enum):
    soup = 'суп'
    main_dish = 'основное'
    dessert = 'десерт'
    salad = 'салат'
    drink = 'напиток'
    snacks = 'закуска'
    pizza = 'пицца'
    sauce = 'соус'


class RecipeBase(BaseModel):
    recipe_name: str
    manual: str
    temp: Optional[float]
    time: int
    type: RecipeType
    price: float
    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class IngredientsBase(BaseModel):
    ing_name: str
    unit: Unit
    quantity: Optional[float]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class RecipeSchema(RecipeBase):
    ingredients: List[IngredientsBase]


class IngredientsSchema(IngredientsBase):
    recipe: List[RecipeBase]

class RecipeOut(RecipeSchema):
    recipe_id: int
