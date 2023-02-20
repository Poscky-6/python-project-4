"""
ResourceBase
    Character
    Film
    Starship
"""


class ResourceBase(object):
    """
    Base class representing required methods to be implemented by all resource
    classes
    """

    resources = ["planets", "starships", "people",
                 "vehilce", "films", "spacies"]

    def __init__(self) -> None:
        self.home_url = "https://swapi.dev/"

    def get_count(self):
        raise NotImplementedError

    def get_resource_urls(self):
        raise NotImplementedError

    def get_sample_data(self):
        raise NotImplementedError
