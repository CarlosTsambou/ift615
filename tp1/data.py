import math

# Graph
graph = {

    "Oradea": {
        "Zerind": 71,
        "Sibiu": 151
    },

    "Zerind": {
        "Oradea": 71,
        "Arad": 75
    },

    "Arad": {
        "Zerind": 75,
        "Sibiu": 140,
        "Timisoara": 118
    },

    "Timisoara": {
        "Arad": 118,
        "Lugoj": 111
    },

    "Lugoj": {
        "Timisoara": 111,
        "Mehadia": 70,
        "Rimnicu Vilcea": 91
    },

    "Mehadia": {
        "Lugoj": 70,
        "Drobeta": 75
    },

    "Drobeta": {
        "Mehadia": 75,
        "Craiova": 120
    },

    "Craiova": {
        "Drobeta": 120,
        "Rimnicu Vilcea": 146,
        "Pitesti": 138,
        "Giurgiu": 153
    },

    "Sibiu": {
        "Oradea": 151,
        "Arad": 140,
        "Fagaras": 99,
        "Rimnicu Vilcea": 80
    },

    "Rimnicu Vilcea": {
        "Sibiu": 80,
        "Lugoj": 91,
        "Pitesti": 97,
        "Craiova": 146
    },

    "Fagaras": {
        "Sibiu": 99,
        "Neamt": 187,
        "Bucharest": 211
    },

    "Pitesti": {
        "Rimnicu Vilcea": 97,
        "Craiova": 138,
        "Bucharest": 101
    },

    "Neamt": {
        "Fagaras": 187,
        "Iasi": 87
    },

    "Iasi": {
        "Neamt": 87,
        "Vaslui": 92
    },

    "Vaslui": {
        "Iasi": 92,
        "Urziceni": 142
    },

    "Urziceni": {
        "Vaslui": 142,
        "Bucharest": 85,
        "Hirsova": 98
    },

    "Hirsova": {
        "Urziceni": 98,
        "Eforie": 86
    },

    "Eforie": {
        "Hirsova": 86,
        "Giurgiu": 218
    },

    "Giurgiu": {
        "Craiova": 153,
        "Bucharest": 90,
        "Eforie": 218
    },

    "Bucharest": {
        "Fagaras": 211,
        "Pitesti": 101,
        "Urziceni": 85,
        "Giurgiu": 90
    }
} 

#heuristic
coords = {
    "Oradea": (200, 40),
    "Zerind": (180, 80),
    "Arad": (120, 180),
    "Timisoara": (130, 310),
    "Lugoj": (230, 360),
    "Mehadia": (220, 430),
    "Drobeta": (220, 500),
    "Sibiu": (320, 220),
    "Rimnicu Vilcea": (330, 320),
    "Craiova": (380, 520),
    "Fagaras": (470, 240),
    "Pitesti": (490, 380),
    "Bucharest": (600, 460),
    "Giurgiu": (560, 550),
    "Urziceni": (650, 420),
    "Hirsova": (760, 420),
    "Eforie": (800, 510),
    "Vaslui": (720, 250),
    "Iasi": (680, 130),
    "Neamt": (600, 80)
}


#heuristic function
def heuristic(city, goal):
    x1, y1 = coords[city]
    x2, y2 = coords[goal]

    return math.sqrt(
        (x1 - x2)**2 +
        (y1 - y2)**2
    )
