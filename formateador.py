import json
import re

def transformar_archivo(input_file):

    with open(input_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()


    match = re.search(r'\{(.*)\}', raw_text, re.DOTALL)
    if not match:
        raise ValueError('No se encontró un JSON válido en el archivo')


    json_text = '{' + match.group(1) + '}'


    data = json.loads(json_text)

   
    camera_id = data.get('camera_id', '')
    location = data.get('location', '')
    priority = data.get('priority', '')
    video_file = data.get('video_file', '')
    date = data.get('date', '')

    object_types = set()
    for timeslot in data.get('timeslots', []):
        object_counts = timeslot.get('object_counts', {})
        object_types.update(object_counts.keys())
    object_types = sorted(object_types)  

  
    lines = []

    for timeslot in data.get('timeslots', []):
        hour = timeslot.get('hour', '')
        object_counts = timeslot.get('object_counts', {})
        
        
        object_values = [str(object_counts.get(obj, 0)) for obj in object_types]
        

        line = f"{camera_id},{location},{priority},{video_file},{date},{hour}," + ",".join(object_values)
        lines.append(line)

    
    output_file = input_file.replace('.txt', '_formateado.txt')

    
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

    print(f'Archivo "{output_file}" creado exitosamente sin encabezado.')

transformar_archivo('cam_10_campus2_2024-04-13.txt')
