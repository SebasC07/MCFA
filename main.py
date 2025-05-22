from fastapi import FastAPI
<<<<<<< HEAD
from controller import abb_controller

app = FastAPI()

app.include_router(abb_controller.abb_route)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

=======
from controller import LocationController, TypedocController, PersonController

app = FastAPI()

app.include_router(LocationController.router)
app.include_router(TypedocController.router)
app.include_router(PersonController.router)
>>>>>>> 558fcee (Acrualizacion Proyecto)
