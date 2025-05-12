from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib import const
import json # Import the json module

def get_planetary_positions(date_str, time_str, latitude, longitude, timezone_str='+03:00'):
    """
    Calculates planetary positions for a given birth date, time, and location.

    Args:
        date_str (str): Birth date in 'YYYY/MM/DD' format.
        time_str (str): Birth time in 'HH:MM' format.
        latitude (float): Latitude of the birth location.
        longitude (float): Longitude of the birth location.
        timezone_str (str): Timezone string (e.g., '+03:00').

    Returns:
        dict: A dictionary with planet names as keys and their signs and other info as values.
              Returns an error dictionary if calculation fails.
    """
    try:
        location = GeoPos(latitude, longitude)
        dt = Datetime(date_str, time_str, timezone_str)
        chart = Chart(dt, location)

        positions = {}
        # You can extend this list to include other celestial bodies or points
        celestial_bodies = {
            const.SUN: "Sun",
            const.MOON: "Moon",
            const.MERCURY: "Mercury",
            const.VENUS: "Venus",
            const.MARS: "Mars",
            const.JUPITER: "Jupiter",
            const.SATURN: "Saturn",
            const.NORTH_NODE: "NorthNode",
            const.SOUTH_NODE: "SouthNode", # Often inferred from North Node
            const.SYZYGY: "Syzygy",
            const.PARS_FORTUNA: "ParsFortuna",
        }
        
        # Define houses in order
        houses = [
            (const.HOUSE1, "House1"),
            (const.HOUSE2, "House2"),
            (const.HOUSE3, "House3"),
            (const.HOUSE4, "House4"),
            (const.HOUSE5, "House5"),
            (const.HOUSE6, "House6"),
            (const.HOUSE7, "House7"),
            (const.HOUSE8, "House8"),
            (const.HOUSE9, "House9"),
            (const.HOUSE10, "House10"),
            (const.HOUSE11, "House11"),
            (const.HOUSE12, "House12"),
        ]

        for body_const in celestial_bodies:
            obj = chart.get(body_const)
            if obj: # Check if the object exists in the chart
                positions[body_const] = {
                    "sign": obj.sign,
                    "sign_position": obj.signlon, # Position within the sign (longitude)
                }
        
        # Get Ascendant and Midheaven
        asc = chart.get(const.ASC)
        mc = chart.get(const.MC)
        if asc:
            positions["Ascendant"] = {
                "sign": asc.sign,
                "sign_position": asc.signlon,
            }
        if mc:
            positions["Midheaven"] = {
                "sign": mc.sign,
                "sign_pos": mc.signlon,
            }

        # Get house cusps in order
        houses_info = {}
        for house_const, house_name in houses:
            house_cusp = chart.get(house_const)
            houses_info[house_name] = {
                "sign": house_cusp.sign,
                "sign_position": house_cusp.signlon,
            }
        positions["houses"] = houses_info

        return positions

    except Exception as e:
        return {"error": str(e)}

# Example of how to use the function and print JSON output:
if __name__ == "__main__":
    # 1. Input: Date, time, and location
    birth_date = '2001/08/31'
    birth_time = '09:30'
    birth_latitude = 39.77  # Eskişehir coordinates
    birth_longitude = 30.52
    birth_timezone = '+03:00'  # Timezone Europe/Istanbul

    chart_data = get_planetary_positions(
        birth_date, 
        birth_time, 
        birth_latitude, 
        birth_longitude, 
        birth_timezone
    )
    
    # Print the result as a JSON string
    # This is what your React Native app would eventually receive
    print(json.dumps(chart_data, indent=4))
