from ariadne import convert_kwargs_to_snake_case
from .models import Vehicle


def listVehicles_resolver(obj, info):
    try:
        vehicles = [vehicle.to_dict() for vehicle in Vehicle.query.all()]
        print(vehicles)
        payload = {
            "success": True,
            "vehicles": vehicles
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def getVehicle_resolver(obj, info, id):
    try:
        vehicle = Vehicle.query.get(id)
        payload = {
            "success": True,
            "vehicle": vehicle.to_dict()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Vehicle item matching {id} not found"]
        }
    return payload