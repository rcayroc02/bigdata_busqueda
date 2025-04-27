import random
import json
from datetime import datetime, timedelta


object_types = [
    "person", "backpack", "car", "bicycle", "dog", "cat",
    "redshirt", "blueshirt", "blackshirt",
    "redcar", "bluecar", "blackcar", "racecar",
    "alto", "pequeño",
    "blueshoes", "redshoes", "blackshoes",
    "bluepants", "redpants", "blackpants"
]

def generate_object_counts():
    """Genera conteos aleatorios para cada tipo de objeto"""
    counts = {}
    for obj in object_types:
        if obj in ["person", "backpack", "car", "bicycle", "dog", "cat"]:
            counts[obj] = random.randint(0, 20)  
        elif obj in ["redshirt", "blueshirt", "blackshirt", "redcar", "bluecar", "blackcar", "racecar"]:
            counts[obj] = random.randint(0, 10) 
        else:
            counts[obj] = random.randint(0, 5)   
    return counts

def generate_hours():
    """Genera las 24 horas del día en formato de rango"""
    hours = []
    start_time = datetime.strptime("00:00", "%H:%M")
    for _ in range(24):
        end_time = start_time + timedelta(hours=1)
        hours.append(f"{start_time.strftime('%H:%M')}-{end_time.strftime('%H:%M')}")
        start_time = end_time
    return hours

def generate_camera_data(camera_id, location, priority, video_file, date):
    """Genera todo el contenido de un archivo"""
    data = {
        "camera_id": camera_id,
        "location": location,
        "priority": priority,
        "video_file": video_file,
        "date": date,
        "timeslots": [],
        "alerts": []
    }
    for hour in generate_hours():
        timeslot = {
            "hour": hour,
            "object_counts": generate_object_counts()
        }
        data["timeslots"].append(timeslot)
    return data

def save_as_txt(data, filename):
    """Guarda la estructura como un .txt"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))

# ------------ CONFIGURACIÓN ----------------

# datos de camara
camera_id = "cam_10"
location = "campus2"
priority = "alta"
video_file = "campus2_2024-04-13.mp4"
date = "2024-04-13"

# salida
output_file = "cam_10_campus2_2024-04-13.txt"

# ------------ EJECUCIÓN --------------------

camera_data = generate_camera_data(camera_id, location, priority, video_file, date)
save_as_txt(camera_data, output_file)

print(f"Archivo {output_file} generado exitosamente ✅")
