from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes import account
from db.database import init_db
import uvicorn
import asyncio

# Global variables - just templates for now
template_engine = None

# FastAPI application instance
app = FastAPI(docs_url=None, redoc_url=None)


def main():
    configure()
    uvicorn.run(app, host='127.0.0.1, port=8000')


def configure():
    configure_templates()
    configure_routes()
    configure_db()


def configure_db():
    asyncio.run(init_db())


def configure_templates():
    global template_engine
    template_engine = Jinja2Templates(directory="templates")


def configure_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(account.router)


if __name__ == '__main__':
    main()
else:
    configure()

