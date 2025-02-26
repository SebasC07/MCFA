from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Modelo de datos
class Pet(BaseModel):
    id: int
    name: str
    age: int
    species: str

# Base de datos en memoria
pets_db: List[Pet] = []

# Crear mascota (POST)
@app.post("/pets/", response_model=Pet)
def create_pet(pet: Pet):
    for existing_pet in pets_db:
        if existing_pet.id == pet.id:
            raise HTTPException(status_code=400, detail="Pet ID already exists")
    pets_db.append(pet)
    return pet

# Obtener todas las mascotas (GET)
@app.get("/pets/", response_model=List[Pet])
def get_pets():
    return pets_db

# Obtener una mascota por ID (GET)
@app.get("/pets/{pet_id}", response_model=Pet)
def get_pet(pet_id: int):
    for pet in pets_db:
        if pet.id == pet_id:
            return pet
    raise HTTPException(status_code=404, detail="Pet not found")

# Modificar una mascota (PUT)
@app.put("/pets/{pet_id}", response_model=Pet)
def update_pet(pet_id: int, updated_pet: Pet):
    for i, pet in enumerate(pets_db):
        if pet.id == pet_id:
            pets_db[i] = updated_pet
            return updated_pet
    raise HTTPException(status_code=404, detail="Pet not found")

# Borrar una mascota (DELETE)
@app.delete("/pets/{pet_id}")
def delete_pet(pet_id: int):
    for i, pet in enumerate(pets_db):
        if pet.id == pet_id:
            del pets_db[i]
            return {"message": "Pet deleted successfully"}
    raise HTTPException(status_code=404, detail="Pet not found")

# Obtener el promedio de edad de las mascotas (GET)
@app.get("/pets/average_age/")
def get_average_age():
    if not pets_db:
        return {"message": "No pets in database"}
    avg_age = sum(pet.age for pet in pets_db) / len(pets_db)
    return {"average_age": avg_age}
