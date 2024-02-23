from math import sqrt
from utils import read_csv_file, write_json_file, write_csv_file
from consts import OUTSIDE_AIR_TEMPERATURES, ROOM_TEMPERATURE, MONTHS, DECIMAL_PLACES


def calculate_outer_surface_area(height, living_space, num_floors):
    height, width = sqrt(living_space), sqrt(living_space)
    wall_area = 4 * height * width
    total_area = wall_area * num_floors
    return total_area

def calculate_heat_loss(heat_transfer_coefficient, height, living_space, num_floors, room_temperature, outside_temperature):
    outer_surface_area = calculate_outer_surface_area(height, living_space, num_floors)
    return round(heat_transfer_coefficient * outer_surface_area * (room_temperature - outside_temperature), DECIMAL_PLACES)

def run_heat_loss_transformation(import_filename, export_filename, room_temperature, outside_air_temperatures, file_format = "csv"):
    df = read_csv_file(import_filename)
    for i, outside_air_temperature in enumerate(outside_air_temperatures):
        df[f'P_VALUE_FOR{outside_air_temperatures[i]}_DEGREES'] = df.apply(lambda row, outside_temp = outside_air_temperature: calculate_heat_loss(row['U [W/m2K]'], row['height [m]'], row['total living space [m2]'], row['floors'], room_temperature, outside_temp), axis=1)
    if file_format == "csv":
        write_csv_file(df, export_filename)
    else:
         write_json_file(df, export_filename)

for month in MONTHS:
    import_file = "data/building-data-{}.csv".format(month)
    export_file =  "results/p_values_building-data-{}.json".format(month)
    run_heat_loss_transformation(import_file, export_file, ROOM_TEMPERATURE, OUTSIDE_AIR_TEMPERATURES)
    
