"""
pydantic model for species data coming from https://swapi.dev/api/species
"""
from typing import Optional, List
from models.basemodel import Base


class Species_(Base):
    """
       Data model for passing the data of species from `star_wars API`
   """
    name: str
    classification: str
    designation: str
    average_height: str
    skin_colors: str
    hair_colors: str
    average_lifespan: str
    homeworld: str
    language: str

    people: Optional[List[str]]
    films: Optional[List[str]]


if __name__ == "__main__":
    data = {"name": "Human",
            "classification": "mammal",
            "designation": "sentient",
            "average_height": "180",
            "skin_colors": "caucasian, black, asian, hispanic",
            "hair_colors": "blonde, brown, black, red",
            "eye_colors": "brown, blue, green, hazel, grey, amber",
            "average_lifespan": "120",
            "homeworld": "https://swapi.dev/api/planets/9/",
            "language": "Galactic Basic",
            "people": [
                "https://swapi.dev/api/people/66/",
                "https://swapi.dev/api/people/67/",
                "https://swapi.dev/api/people/68/",
                "https://swapi.dev/api/people/74/"
            ],
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/4/",
                "https://swapi.dev/api/films/5/",
                "https://swapi.dev/api/films/6/"
            ],
            "created": "2014-12-10T13:52:11.567000Z",
            "edited": "2014-12-20T21:36:42.136000Z",
            "url": "https://swapi.dev/api/species/1/"
            }

    obj = Species(**data)
    print(obj)
