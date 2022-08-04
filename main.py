import uvicorn


if __name__ == '__main__':
    uvicorn.run('application:get_app', reload=True)



# @app.get("/menu", response_model=List[RecipeSchema])
# def get_menu(db: Session = Depends(get_recipes_repo)):
#     db_menu = db.get_all()
#     return db_menu
#
