from pydantic import BaseModel, Field
from typing import List, Optional


class UnitBase(BaseModel):
    id: int
    unit: str

    class Config:
        orm_mode = True


class RecipeTypeBase(BaseModel):
    id: int
    type: str

    class Config:
        orm_mode = True


class RecipeBase(BaseModel):
    id: int = Field(alias='recipe_id')
    recipe_name: str = Field(alias='recipe_name')
    process: str
    temp: float
    time: int
    type_id: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class IngredientsBase(BaseModel):
    id: int = Field(alias='ingredient_id')
    ing_name: str = Field(alias='ing_name')
    unit_id: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class RecipeSchema(RecipeBase):
    ingredients: List[IngredientsBase]


class IngredientsSchema(IngredientsBase):
    recipes: List[RecipeBase]