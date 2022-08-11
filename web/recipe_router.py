from fastapi import Depends, HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from typing import List

from web.dependencies import get_recipes_repo, get_db, get_ingredients_repo
from web.schemas import RecipeSchema, RecipeOut
from database.recipe import RecipesRepo
from database.ingredients import IngredientsRepo
from database.models import RecipeIngredients


router = APIRouter()


@router.get('/menu')
def get_menu(
        recipe_repo: RecipesRepo = Depends(get_recipes_repo),
        session: Session = Depends(get_db)):
    with session.begin():
        return recipe_repo.get_menu()


@router.get('/', response_model=List[RecipeOut])
def get_all(
        recipe_repo: RecipesRepo = Depends(get_recipes_repo),
        session: Session = Depends(get_db)):
    with session.begin():
        return recipe_repo.all()


@router.get('/search/{recipe_name}', response_model=RecipeOut)
def get_recipe_by_name(
        recipe_name,
        recipe_repo: RecipesRepo = Depends(get_recipes_repo),
        session: Session = Depends(get_db)
):
    with session.begin():
        return recipe_repo.get_recipe_by_name(recipe_name)


@router.get('/{recipe_id}', response_model=RecipeOut)
def get_recipe(
        recipe_id: int,
        recipe_repo: RecipesRepo = Depends(get_recipes_repo),
        session: Session = Depends(get_db)
):
    with session.begin():
        return recipe_repo.get(recipe_id)


def create_ingredients(
        ingredients,
        ingredient_repo: IngredientsRepo):
    ings_id = []
    for ing in ingredients:
        ingredient= ingredient_repo.get_ingredient_by_name(ing.ing_name)
        if ingredient:
            ings_id.append((ingredient.ingredient_id, ing.quantity))
        else:
            ing_id = ingredient_repo.create((ing.ing_name, ing.unit))
            ings_id.append((ing_id, ing.quantity))
    return ings_id


def create_associations(recipe_id, ings_id):
    associations = []
    for ing_id, amount in ings_id:
        recipe_ing = RecipeIngredients(recipe_id=recipe_id, ingredient_id=ing_id, quantity=amount)
        associations.append(recipe_ing)
    return associations


@router.post('/')
def create_recipe(
        new_recipe: RecipeSchema,
        recipe_repo: RecipesRepo = Depends(get_recipes_repo),
        session: Session = Depends(get_db)):
    ingredient_repo = get_ingredients_repo(session)
    with session.begin():
        recipe = recipe_repo.get_recipe_by_name(new_recipe.recipe_name)
        if recipe:
            raise HTTPException(status_code=400, detail='Рецепт уже существует')
        recipe_id = recipe_repo.create(new_recipe)
        ingredients_id = create_ingredients(new_recipe.ingredients, ingredient_repo)
        associations = create_associations(recipe_id, ingredients_id)
        session.add_all(associations)
        return recipe_repo.get(recipe_id)


@router.put('/{recipe_id}')
def change_recipe_name(
        recipe_id: int,
        new_name,
        recipe_repo: RecipesRepo = Depends(get_recipes_repo),
        session: Session = Depends(get_db)):
    with session.begin():
        recipe = recipe_repo.get(recipe_id)
        return recipe_repo.update_name(recipe, new_name)



@router.delete('{recipe_id}')
def delete_recipe(
        recipe_id: int,
        recipe_repo: RecipesRepo = Depends(get_recipes_repo),
        session: Session = Depends(get_db)):
    with session.begin():
        return recipe_repo.delete_recipe(recipe_id)
