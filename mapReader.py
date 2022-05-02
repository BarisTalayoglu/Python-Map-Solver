import os

class MapReader:

    BASE_MAPS_PATH = f"{os.getcwd()}/maps"

    def getMapContent(mapName: str):
        mapFile = open(f"{MapReader.BASE_MAPS_PATH}/{mapName}", "r")

        return mapFile.read().splitlines()