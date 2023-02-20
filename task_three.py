"""
1. TODO - import all resource classes here
2. TODO - get count of each resource
3. TODO - get singular resource URL from each resource
4. TODO - pull data from random 3 "singular" resource URLs
5. TODO - convert the script into CLI application
"""


from resources.films import Film


if __name__ == "__main__":

    film_object = Film()
    total_films = film_object.get_count()
    print(total_films)
