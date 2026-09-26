from fastapi import FastAPI,Body,Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field


app = FastAPI()

class ModelMoviesPost(BaseModel):
    id:int
    tittle:str
    overview:str
    rating:float
    category:str


class ModelMoviesUpdate(BaseModel):
    tittle:str
    overview:str
    rating:float
    category:str

movies = [
    {
     "id":1,
     "tittle":"Avatar",
     "overview":"En un planeta llamado pandora vive los Navi, seres que...",
     "rating":7.8,
     "category":"Aventura"
    },
    {
    "id":2,
    "tittle":"Titanic",
    "overview":"El barco mas grande del mundo jamas creado zarpa a EEUU",
    "rating":8.8,
    "category":"Romance"
    }
]

#se agrega el campo tags para mostrar los subtitulos en la vista de documentacion swagger
@app.get("/",tags=['Home'])
def index():
    return {"key":"hola mundo fastApi"}

#HTMLResponse se utiliza para devolver contenido html dentro de un string
@app.get("/movies",tags=['Movies'])
def movie():
    #return HTMLResponse('<h1>Hola esto es una etiqueta de html</h1>')
    return movies

#parametro en ruta
#@app.get("/movies/{id}/{nombre}/{apellido}",tags=["Movies"])
#def get_movie_by(id:int,nombre:str,apellido:str):
#    return f"{id} {nombre} {apellido}"
@app.get("/movies/{id}",tags=["Movies"])
def get_movie_by_id(id:int):
    for peli in movies:
        if peli['id']==id:
            return peli
    return []

#parametro query /movies/?id=89
#@app.get("/movies/query/",tags=["Movies"])
#def get_movie_by_query(year:int,category:str):
#    return f"{category}-{year}"
@app.get("/movies/search/",tags=['Movies'])
def get_movie_by_category(category:str):
    for peli in movies:
        if peli['category']==category:
            return peli
    return[]


#metodo post "Envio de datos"
@app.post("/movies",tags=['Movies'])
#def create_movie(id:int=Body(),tittle:str=Body(),overview:str=Body(),rating:float=Body(),category:str=Body()):
def create_movie(body:ModelMoviesPost):
    movies.append( body.model_dump() )
    return movies

#metodo put "Actualizar datos"
@app.put("/movies/{id}",tags=['Movies'])
def update_movie(id:int,body:ModelMoviesUpdate):
    for peli in movies:
        if peli['id']==id:
            peli.update(body.model_dump()) #otra alternativa valida
            """
            peli['tittle'] = body.tittle
            peli['overview'] = body.overview    
            peli['rating']=body.rating
            peli['category']=body.category
            """

    return movies

#metodo delete "Borrar datos"
@app.delete('/movies/{id}',tags=['Movies'])
def delete_movie(id:int):
    for peli in movies:
        if peli['id']==id:
            movies.remove(peli)

    return movies  