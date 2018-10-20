from building_one_items import *

#Basement 
furniture_cell_bed = {

    "id": "cell bed",
    
    "name": "player_name bed",

    "description":""" Never had a good dream sleeping on this bed """,

    "item":[item_hair_pin]
}


furniture_cell_lock = {

    "id": "lock",
    
    "name": "cell lock",

    "description":""" Probably not the strongest locks """,

    "item":[]
}


furniture_security_desk = {

    "id": "security desk",
    
    "name": "basement security desk",

    "description": """ Seems like a good place to keep valuable items """,

    "item":[item_map, item_door_card]
}

#ground floor
furniture_reception_table = {

    "id": "reception table",
    
    "name": "ground floor reception table",

    "description":""" If only I had a table this big""",

    "item":[item_skill_book]
}


furniture_reception_chair = {

    "id": "chair",
    
    "name": "reception desk chair",

    "description":""" Id rather stand than sit on that """,

    "item":[]
}

#First floor 
furniture_sofa = {

    "id": "sofa",
    
    "name": "Lobby sofa",

    "description":""" Ah finally something worth sitting on """,

    "item":[]
}
#Roof 
furniture_airconditioning = {

    "id": "airconditioning",
    
    "name": "secuirty room airconditioning vent",

    "description":""" Thank god they keep these outside """,

    "item":[]
}

#All furnitures in building_one
building_one_furniture = {
    "Bed": furniture_cell_bed,
    "Lock": furniture_cell_lock,
    "Desk": furniture_security_desk,
    "Table": furniture_reception_table,
    "Chair": furniture_reception_chair,
    "Sofa": furniture_sofa,
    "Airconditioning": furniture_airconditioning
}

