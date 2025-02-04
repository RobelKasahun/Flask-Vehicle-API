from app.utils.csv_file_loader import read_csv
from flask import Flask, render_template, Response
import os
import json

app = Flask(__name__)

vehicles = read_csv()


def get_filtered_vehicles(key, value):
    return list(
        filter(lambda vehicle: vehicle.get(key).lower() == value.lower(), vehicles)
    )


@app.route("/vehicles")
def get_vehicles():
    """Get all vehicles"""
    return Response(json.dumps(vehicles), mimetype="application/json")


@app.route("/vehicles/brands/<brand>")
def get_vehicles_by_brand(brand):
    filtered_vehicles = get_filtered_vehicles("Brand", brand)

    return Response(
        json.dumps(filtered_vehicles, indent=4), mimetype="application/json"
    )


@app.route("/vehicles/models/<model>")
def get_vehicles_by_models(model):
    filtered_vehicles = get_filtered_vehicles("Model", model)

    return Response(
        json.dumps(filtered_vehicles, indent=4), mimetype="application/json"
    )


@app.route("/vehicles/years/<year>")
def get_vehicles_by_year(year):
    filtered_vehicles = get_filtered_vehicles("Year", year)
    return Response(
        json.dumps(filtered_vehicles, indent=4), mimetype="application/json"
    )


@app.route("/vehicles/engine_sizes/<engine_size>")
def get_vehicles_by_engine_size(engine_size):
    filtered_vehicles = get_filtered_vehicles("Engine_Size", engine_size)
    return Response(
        json.dumps(filtered_vehicles, indent=4), mimetype="application/json"
    )


@app.route("/vehicles/fuel_types/<fuel_type>")
def get_vehicles_by_fuel_type(fuel_type):
    filtered_vehicles = get_filtered_vehicles("Fuel_Type", fuel_type)
    return Response(
        json.dumps(filtered_vehicles, indent=4), mimetype="application/json"
    )


@app.route("/vehicles/transmissions/<transmission>")
def get_vehicles_by_transmission(transmission):
    filtered_vehicles = get_filtered_vehicles("Transmission", transmission)
    return Response(
        json.dumps(filtered_vehicles, indent=4), mimetype="application/json"
    )


@app.route("/vehicles/mileages/<mileage>")
def get_vehicles_by_mileage(mileage):
    filtered_vehicles = list(
        filter(
            lambda vehicle: int(vehicle.get("Mileage").lower()) >= int(mileage.lower()),
            vehicles,
        )
    )
    return Response(
        json.dumps(filtered_vehicles, indent=4), mimetype="application/json"
    )


@app.route("/vehicles/doors/<doors>")
def get_vehicles_by_number_of_doors(doors):
    filtered_vehicles = get_filtered_vehicles("Doors", doors)
    return Response(
        json.dumps(filtered_vehicles, indent=4), mimetype="application/json"
    )


@app.route("/vehicles/owner_counts/<owner_count>")
def get_vehicles_by_owner_count(owner_count):
    filtered_vehicles = get_filtered_vehicles("Owner_Count", owner_count)
    return Response(
        json.dumps(filtered_vehicles, indent=4), mimetype="application/json"
    )


@app.route("/vehicles/prices/<price>")
def get_vehicles_by_price(price):
    filtered_vehicles = list(
        filter(
            lambda vehicle: int(vehicle.get("Price").lower()) >= int(price.lower()),
            vehicles,
        )
    )

    return Response(
        json.dumps(filtered_vehicles, indent=4), mimetype="application/json"
    )
