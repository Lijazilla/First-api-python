from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional


app = FastAPI()
app.title = "Mi first App with Fast API"
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str

movies = [
    {
        "id": 1,
        "title": "Blade Runner",
        "overview": "Un cazador de androides persigue a replicantes rebeldes en un futuro distópico.",
        "year": 1982,
        "rating": 8.1,
        "category": "Ciencia Ficción"
    },
    {
        "id": 2,
        "title": "The Matrix",
        "overview": "Un hacker descubre la verdad sobre la realidad simulada en la que vive la humanidad.",
        "year": 1999,
        "rating": 8.7,
        "category": "Ciencia Ficción"
    },
    {
        "id": 3,
        "title": "Inception",
        "overview": "Un ladrón de sueños entra en la mente de las personas para robar secretos.",
        "year": 2010,
        "rating": 8.8,
        "category": "Ciencia Ficción"
    },
    {
        "id": 4,
        "title": "The Terminator",
        "overview": "Un asesino cyborg viaja en el tiempo para eliminar a la madre del líder de la resistencia humana.",
        "year": 1984,
        "rating": 8.0,
        "category": "Ciencia Ficción"
    },
    {
        "id": 5,
        "title": "Star Wars: Episode IV - A New Hope",
        "overview": "Un granjero se convierte en un héroe intergaláctico en una galaxia muy, muy lejana.",
        "year": 1977,
        "rating": 8.6,
        "category": "Ciencia Ficción"
    },
    {
        "id": 6,
        "title": "E.T. the Extra-Terrestrial",
        "overview": "Un niño forma un vínculo con un extraterrestre perdido y lo ayuda a regresar a casa.",
        "year": 1982,
        "rating": 7.8,
        "category": "Ciencia Ficción"
    },
    {
        "id": 7,
        "title": "Alien",
        "overview": "Una tripulación en el espacio profundo encuentra una forma de vida mortal.",
        "year": 1979,
        "rating": 8.4,
        "category": "Ciencia Ficción"
    },
    {
        "id": 8,
        "title": "The Empire Strikes Back",
        "overview": "La lucha contra el Imperio continúa en esta secuela de Star Wars.",
        "year": 1980,
        "rating": 8.7,
        "category": "Ciencia Ficción"
    },
    {
        "id": 9,
        "title": "Blade Runner 2049",
        "overview": "Un nuevo cazador de androides descubre un secreto que podría cambiar el mundo.",
        "year": 2017,
        "rating": 8.0,
        "category": "Ciencia Ficción"
    },
    {
        "id": 10,
        "title": "The Fifth Element",
        "overview": "En un futuro distópico, un taxista se encuentra con una misteriosa mujer que es clave para salvar la Tierra.",
        "year": 1997,
        "rating": 7.7,
        "category": "Ciencia Ficción"
    },
    {
        "id": 11,
        "title": "2001: A Space Odyssey",
        "overview": "Un viaje espacial se convierte en una odisea en busca de la inteligencia artificial.",
        "year": 1968,
        "rating": 8.3,
        "category": "Ciencia Ficción"
    },
    {
        "id": 12,
        "title": "Avatar",
        "overview": "Un marine discapacitado se involucra en un conflicto épico en un planeta alienígena.",
        "year": 2009,
        "rating": 7.8,
        "category": "Ciencia Ficción"
    },
    {
        "id": 13,
        "title": "The Martian",
        "overview": "Un astronauta queda atrapado en Marte y lucha por sobrevivir hasta su rescate.",
        "year": 2015,
        "rating": 8.0,
        "category": "Ciencia Ficción"
    },
    {
        "id": 14,
        "title": "District 9",
        "overview": "Alienígenas refugiados son forzados a vivir en guetos en Sudáfrica.",
        "year": 2009,
        "rating": 7.9,
        "category": "Ciencia Ficción"
    },
    {
        "id": 15,
        "title": "Interstellar",
        "overview": "Un grupo de astronautas busca un nuevo hogar para la humanidad en un agujero de gusano.",
        "year": 2014,
        "rating": 8.6,
        "category": "Ciencia Ficción"
    },
    {
        "id": 16,
        "title": "The War of the Worlds",
        "overview": "La Tierra es invadida por máquinas alienígenas tripuladas.",
        "year": 1953,
        "rating": 7.1,
        "category": "Ciencia Ficción"
    },
    {
        "id": 17,
        "title": "Donnie Darko",
        "overview": "Un joven tiene visiones extrañas y descubre secretos sobre el tiempo y la realidad.",
        "year": 2001,
        "rating": 8.0,
        "category": "Ciencia Ficción"
    },
    {
        "id": 18,
        "title": "The Day the Earth Stood Still",
        "overview": "Un alienígena llega a la Tierra con un mensaje de paz, pero los humanos no lo reciben bien.",
        "year": 1951,
        "rating": 7.7,
        "category": "Ciencia Ficción"
    },
    {
        "id": 19,
        "title": "Children of Men",
        "overview": "En un mundo sin niños, una mujer embarazada se convierte en la esperanza de la humanidad.",
        "year": 2006,
        "rating": 7.9,
        "category": "Ciencia Ficción"
    },
    {
        "id": 20,
        "title": "The Hunger Games",
        "overview": "Jóvenes luchan por sobrevivir en un juego mortal en un futuro distópico.",
        "year": 2012,
        "rating": 7.2,
        "category": "Ciencia Ficción"
    },
    {
        "id": 21,
        "title": "The Hunger Games",
        "overview": "Jóvenes luchan por sobrevivir en un juego mortal en un futuro distópico.",
        "year": 2012,
        "rating": 7.2,
        "category": "Ciencia Ficción"
    }
]


@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1>Hello World</h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []

@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies if item['category'] == category]

@app.post('/movies', tags=['movies'])
def create_movie(movie: Movie):
    movies.append(movie)
    
    return movies

@app.put('/movies/{id}', tags=['movies'])
def update_movie(id: int, movie: Movie):
    for item in movies:
         if item["id"] == id:
             item['title'] == movie.title
             item['overview'] = movie.overview
             item['year'] = movie.year
             item['rating'] = movie.rating
             item['categpry'] = movie.category
             return movies
         
@app.delete('/movies/{id}', tags=['movies'])
def delete_movies(id: int):
    for item in movies:
         if item["id"] == id:
             movies.remove(item)
             return movies
         
