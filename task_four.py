"""
    TODO
    1. Pull data for the first movie ("A New Hope") and save in DB.
    2. Replace the data for each endpoint listed in the JSON object and insert
    that data into database table
    For example - "A new hope" movie has following resource endpoints -
    - characters 15
    - planets  7
    - starships   10
    - vehicles  5
    - species  40
"""

from multiprocessing.pool import ThreadPool
from pydantic import parse_obj_as
from typing import List

from resources.films import Film   # resource model
from models.datamodels.films import Film_  # pydantic model
from models.datamodels.characters import Character_
from models.datamodels.planets import Planet_
from models.datamodels.species import Species_
from models.datamodels.starships import Starship_
from models.datamodels.vehicles  import Vehicles_


from dal.db_conn_helper import get_db_conn
from dal.dml import insert_resource
from utils.fetch_data import hit_url,fetch_char_json
from utils.timing import timeit




#without_multithreading
@timeit
def store_characters():
    characters = film_data.characters
    characters_data = []

    char_columns = [
        "name",
        "height",
        "mass",
        "hair_color"
    ]

    for character in characters:
        response = hit_url(character)
        char = response.json()
        char = Character_(**char)
        char_values = [
            char.name,
            char.height,
            char.mass,
            char.hair_color
        ]

        char_id = int(character.split("/")[-2])
        result = insert_resource(
            "characters",
            "char_id",
            char_id,
            char_columns,
            char_values
        )
        characters_data.append(char)
    return characters_data

@timeit
def store_vehicles():
    vehicles = film_data.vehicles
    vehicles_data = []

    vehicle_columns = [
        "cargo_capacity",
        "consumables",
        "model",
        "name"
    ]

    for vehicle in vehicles:
        response = hit_url(vehicle)
        vehicle_ = response.json()
        vehicle_ = Vehicles_(**vehicle_)
        vehicle_values = [
            vehicle_.cargo_capacity,
            vehicle_.consumables,
            vehicle_.model,
            vehicle_.name
        ]

        vehicle_id = int(vehicle.split("/")[-2])
        result = insert_resource(
            "vehicle",
            "vehicle_id",
            vehicle_id,
            vehicle_columns,
            vehicle_values
        )
        vehicles_data.append(vehicle_)
    return vehicles_data

@timeit
def store_starships():
    starships = film_data.starships
    starships_data = []

    starship_columns = [
        "cargo_capacity",
        "consumables",
        "model",
        "name"
    ]

    for starship in starships:
        response = hit_url(starship)
        star = response.json()
        star1 =Starship_(**star)
        starship_values = [
            star1.cargo_capacity,
            star1.consumables,
            star1.model,
            star1.name
        ]

        starship_id = int(starship.split("/")[-2])
        result = insert_resource(
            "starship",
            " starship_id",
            starship_id,
            starship_columns,
            starship_values
        )
        starships_data.append(star1)
    return starships_data


@timeit
def store_species():
    species = film_data.species
    species_data = []
    species_columns = [
        "average_height",
        "average_lifespan",
        "name",
        "skin_colors",

    ]

    for species_url in species:
        response = hit_url(species_url)
        species_1 = response.json()
        species_1= Species_(**species_1)
        species_values = [
            species_1.average_height,
            species_1.average_lifespan,
            species_1.name,
            species_1.skin_colors,

        ]

        species_id = int(species_url.split("/")[-2])
        result = insert_resource(
            "species",
            "species_id",
            species_id,
            species_columns,
            species_values)

        species_data.append(species_1)

    return species_data


@timeit
def store_planets():
    planets=film_data.planets
    planets_data=[]
    planet_columns=[
            "name",
            "diameter",
            "climate",
            "gravity",

    ]

    for planet in planets:
        response=hit_url(planet)
        pla=response.json()
        pla=Planet_(**pla)
        planet_values=[
            pla.name,
            pla.diameter,
            pla.climate,
            pla.gravity,

        ]

        planet_id=int(planet.split("/")[-2])
        result=insert_resource(
            "planet",
            "planet_id",
            planet_id,
            planet_columns,
            planet_values )

        planets_data.append(pla)

    return planets_data


#with_multithreading

@timeit
def store_characters1():
    characters = film_data.characters
    characters_data = []

    char_columns = [
        "name",
        "height",
        "mass",
        "hair_color"
    ]

    pool=ThreadPool(5)
    char_data=pool.map(fetch_char_json,characters)
    char_data_list=parse_obj_as(List[Character_],char_data)

    for char in char_data_list:
        print(char)
        char_values = [
            char.name,
            char.height,
            char.mass,
            char.hair_color
        ]

        char_id = int(char.url.split("/")[-2])
        result = insert_resource(
            "characters",
            "char_id",
            char_id,
            char_columns,
            char_values
        )
        characters_data.append(char)
    return characters_data


@timeit
def store_planets1():
    planets = film_data.planets
    planets_data = []

    pla_columns = [
        "name",
        "diameter",
        "climate",
        "gravity"
    ]

    pool=ThreadPool(5)
    pla_data=pool.map(fetch_char_json,planets)
    pla_data_list=parse_obj_as(List[Planet_],pla_data)

    for planet in pla_data_list:

        pla_values = [
            planet.name,
            planet.diameter,
            planet.climate,
            planet.gravity
        ]

        planet_id = int(planet.url.split("/")[-2])
        result = insert_resource(
            "planet",
            "planet_id",
            planet_id,
            pla_columns,
            pla_values
        )
        planets_data.append(planet)
    return planets_data


@timeit
def store_species1():
    species = film_data.species
    species_data = []

    species_columns = [
        "average_height",
        "average_lifespan",
        "classification",
        "name"
    ]

    pool=ThreadPool(5)
    spe_data=pool.map(fetch_char_json,species)
    spe_data_list=parse_obj_as(List[Species_],spe_data)

    for species_ in spe_data_list:

        species_values = [
            species_.average_height,
            species_.average_lifespan,
            species_.classification,
            species_.name
        ]

        species_id = int(species_.url.split("/")[-2])
        result = insert_resource(
            "species",
            "species_id",
            species_id,
            species_columns,
            species_values
        )
        species_data.append(species_)
    return species_data

@timeit
def store_vehicles1():
    vehicles = film_data.vehicles
    vehicles_data = []

    vehicle_columns = [
        "cargo_capacity",
        "consumables",
        "model",
        "name"
    ]

    pool=ThreadPool(5)
    vehicle_data=pool.map(fetch_char_json,vehicles)
    vehicle_data_list=parse_obj_as(List[Vehicles_],vehicle_data)

    for vehicle in vehicle_data_list:

        vehicle_values = [
            vehicle.cargo_capacity,
            vehicle.consumables,
            vehicle.model,
            vehicle.name
        ]

        vehicle_id = int(vehicle.url.split("/")[-2])
        result = insert_resource(
            "vehicle",
            "vehicle_id",
            vehicle_id,
            vehicle_columns,
            vehicle_values
        )
        vehicles_data.append(vehicle)
    return vehicles_data

@timeit
def store_starship1():
    starships = film_data.starships
    starships_data = []

    starship_columns = [
        "cargo_capacity",
        "consumables",
        "model",
        "name"
    ]

    pool=ThreadPool(5)
    starship_data=pool.map(fetch_char_json,starships)
    starship_data_list=parse_obj_as(List[Starship_],starship_data)

    for starship in starship_data_list:

        starship_values = [
            starship.cargo_capacity,
            starship.consumables,
            starship.model,
            starship.name
        ]

        starship_id = int(starship.url.split("/")[-2])
        result = insert_resource(
            "starship",
            "starship_id",
            starship_id,
            starship_columns,
            starship_values
        )
        starships_data.append(starship)
    return starships_data






if __name__ == "__main__":
    data = Film().get_sample_data(id_=1)
    film_data = Film_(**data)

    # create DB connection
    conn = get_db_conn()

    film_columns = [
        "title",
        "opening_crawl",
        "director",
        "producer",
        "release_date",
        "created",
        "edited",
        "url",
    ]

    film_values = [
        film_data.title,
        film_data.opening_crawl,
        film_data.director,
        film_data.producer,
        film_data.release_date,
        film_data.created.strftime("%y-%m-%d"),
        film_data.edited.strftime("%y-%m-%d"),
        film_data.url,
    ]

    result = insert_resource(
        "film", "film_id", film_data.episode_id, film_columns, film_values
    )




#without_multithreading
    character_data = store_characters()
    planet_data=store_planets()
    species_data=store_species()
    starship_data=store_starships()
    vehicle_data=store_vehicles()

#with_multithreading
    character_data1 = store_characters1()
    planet_data=store_planets1()
    species_data=store_species1()
    vehicle_data=store_vehicles1()
    starship_data=store_starship1()

#completed
#commited 2


