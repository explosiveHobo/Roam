import codex
from random import choice

# for reversing direction when creating vectors back and forth between locations
opposite_directions = {
    'west': 'east',
    'east': 'west',
    'north': 'south',
    'south': 'north'
}


# Vector (Edge) represents a distance to another location node on the map
class Vector:
    def __init__(self, distance, locations):
        super().__init__()
        self.distance = distance
        self.locations = locations
        self.name = 'the path between ' + locations[0].name + ' and ' + locations[1].name


# Location (Node) represents the points where the player can perform non combat actions
class Location:
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.vectors = {}

    # creates a vector connecting this location to "destination" location under key "direction"
    def create_vector_between(self, distance, direction, destination):
        self.vectors[direction] = Vector(distance, [self, destination])
        destination.vectors[opposite_directions[direction]] = (Vector(distance, [destination, self]))

    # returns true if this location already has a vector connection to parameter
    def connected_to(self, location):
        for direction, vector in self.vectors.items():
            if vector.locations.__contains__(location):
                return True
        return False


# distance distribution
LONG_DISTANCE_CURVE = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
CLASSIC_DISTANCE_CURVE = [1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5]
SHORT_DISTANCE_CURVE = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


# creates all location nodes and connects them with vectors, of width and height (dimensions)
def generate_world(dimensions, distance_curve=LONG_DISTANCE_CURVE):
    # throwaway data structures
    locations = {}
    used_names = []

    # create locations in dimensions
    for x in range(dimensions):
        for y in range(dimensions):
            # randomly name location

            # force a unique name
            random_name = None
            while random_name is None or used_names.__contains__(random_name):
                random_name = choice(codex.LOCATION_PREFIXES) + ' ' + choice(codex.LOCATION_SUFFIXES)

            locations[(x, y)] = Location(random_name)
            used_names.append(random_name)

    # connect all nodes to adjacent nodes by psuedo-random distances with vectors
    for coord, location in locations.items():
        adjacents = [(coord[0] - 1, coord[1]),
                     (coord[0] + 1, coord[1]),
                     (coord[0], coord[1] - 1),
                     (coord[0], coord[1] + 1)]

        directionals = {
            adjacents[0]: 'west',
            adjacents[1]: 'east',
            adjacents[2]: 'north',
            adjacents[3]: 'south'
        }

        # go through adjacent points and connect locations
        for adj in adjacents:
            # if the map contains this adjacent point and there is not yet a vector connection
            if locations.__contains__(adj) and not locations[adj].connected_to(location):
                location.create_vector_between(choice(distance_curve), directionals[adj], locations[adj])

        # if x is 0, loop west
        if coord[0] == 0:
            location.create_vector_between(choice(distance_curve), 'west', locations[(dimensions - 1, coord[1])])
        # if x is max, loop east
        elif coord[0] == dimensions - 1:
            location.create_vector_between(choice(distance_curve), 'east', locations[(0, coord[1])])
        # if y is 0, loop north
        elif coord[1] == 0:
            location.create_vector_between(choice(distance_curve), 'north', locations[(coord[0], dimensions - 1)])
        # if y is max, loop south
        elif coord[1] == dimensions - 1:
            location.create_vector_between(choice(distance_curve), 'south', locations[(coord[0], 0)])

    # return root for player to start at
    return locations[(int(dimensions / 2), int(dimensions / 2))]
