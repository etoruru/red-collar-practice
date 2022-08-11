from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, Session

from database.models import Base
from web.router import api_router


def startup(app: FastAPI):

    def _startup():
        engine = create_engine('postgresql:///recipes')
        Base.metadata.create_all(engine)
        session_factory = scoped_session(
            sessionmaker(
                engine,
                expire_on_commit=False,
                class_=Session
            )
        )
        app.state.db_engine = engine
        app.state.session_factory = session_factory
    return _startup


def get_app() -> FastAPI:

    app = FastAPI(
        title="Recipes",
        description="Service for managing recipes",
    )

    app.on_event("startup")(startup(app))

    app.include_router(router=api_router)

    return app