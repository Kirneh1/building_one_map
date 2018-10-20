from building_one_items import *
from building_one_furniture import *


#Basement(rooms)
cell_room = {
    
    "name": "player_name cell",
    
    "description": """ I hate this bloody cell. But the only way out
    is north, to the security room """,

    "exits": {"north":"Securityroom"},

    "furniture": {"Search bed": "Bed", "Use lock": "Lock"},

    "items":[item_stool]
}

security_room = {
    
    "name": "Security room",

    "description":""" One step closer to getting out of here. The staircase is
    to the west of the security room. But you better check this room carefully
    there could be useful items here.""",

    "exits": {"south": "Cell", "west": "Redstairs"},

    "furniture": {"Search desk": "Desk", "Use chair": "Chair"},

    "items":[item_security_baton]
}

red_staircase = {
    
    "name": "red staircase",

    "description":""" This seems to be the only way to get to
    the floor above. Go up to enter the ground floor. """,

    "exits": {"up":"Groundfloor", "east": "Securityroom"},

    "furniture":[],

    "items":[]
}


#Basement

basement_floor = {
    
    "Cell": cell_room,
    "Securityroom": security_room,
    "Redstairs": red_staircase
}

#Ground floor(rooms)
blue_staircase = {
    
    "name": "blue starcase",

    "description":""" Going down will bring you to the basement floor.
    going up will bring you to the first floor. """,

    "exits": {"up":"Firstfloor", "down": "Basement" , "east": "Recepetion"},

    "furniture":[],

    "items":[]
}

reception_room = {
    
    "name": "Reception",

    "description":""" This is the reception room. The entrance to the building
    is north. However, you will need a door card to pass. To get back to
    the staircase go west.""",

    "exits": {"north": """LEAVE BUILDING_ONE""", "west":"Staircase"},

    "furniture":{"Search table": "Table", "Use chair": "Chair"}, 

    "items": []
}

#Ground floor
ground_floor = {
    
    "Bluestairs": blue_staircase,
    "Reception": reception_room
}

#First floor(rooms
yellow_staircase = {
    
    "name": "yellow stairs",

    "description":"""Going down will bring you back to the ground floor.
    Going up will bring you to the roof.""",

    "exits": {"up": "Roof", "down": "Groundfloor", "east": "Lobby"},

    "furniture":[],

    "items":[]
}

lobby_room = {
    
    "name": "The lobby",

    "description":""" You are at the lobby. Seems rather empty. Room A is north
    and room b is south. To get back to the staircase go west.""",

    "exits": {"west":"Staircase", "south": "RoomA", "north": "RoomB"},

    "furniture": {"Search sofa": "Sofa"},

    "items":[]
}

room_a = {
    
    "name": "Rooma",

    "description":""".....""",

    "exits": {"north": "Lobby"},

    "furniture":[],

    "items":[]
}

room_b = {
    
    "name": "Roomb",

    "description":""".....""",

    "exits": {"south": "Lobby"},

    "furniture":[],

    "items":[]
}


#First floor
first_floor = {
    
    "Yellowstairs": yellow_staircase,
    "Lobby": lobby_room,
    "RoomA": room_a,
    "RoomB": room_b
}

#Roof
roof_floor = {
    
    "name":"Building_one Roof",

    "description":""" You are on the roof. Its too high to jump down, I wonder
    there is another way. To go back to the first floor go down.""",

    "exits": {"down": "Firstfloor"},

    "furniture":{"Search airconditioning": "Airconditioning"},

    "items":[item_rope]

}

#Building One
building_one = {

    "Basement": basement_floor,
    "Groundfloor":  ground_floor,
    "Firstfloor":   first_floor,
    "Roof": roof_floor

}
