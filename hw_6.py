import os
import csv
import argparse
import json


def get_route():
    """ З командної стрічки отримуємо шлях до файлу .csv за допомогою аргумента -csv
        та шлях для запису json файлу"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-csv', type=str, required=True, help='Path to the readed .csv file')
    parser.add_argument('-json', type=str, required=True, help='Name and path to the created json file')
    args = parser.parse_args()
    
    way_csv = args.csv    
    way_json = args.json
    
    return way_csv, way_json
    
    
def get_values_for_json (way: str, filename:str = 'user_details.csv'):
    """Читаємо .csv файл з директорії way:
    На виході отримуємо ліст словників для експорту в json"""
    with open(os.path.join(way, filename)) as csv_file:
        column_names = ('user_id', 'username', 'first_name', 'last_name', 'gender', 'password', 'status')
        readed_csv = csv.DictReader(csv_file, column_names)
        
        next(readed_csv, None)
        
        #Робимо послідовність і вміст даних відаовідним до поставленого завдання
        values_for_json = list()
        for line in readed_csv:
            data = {}
            data['first_name'] = line['first_name']
            data['gender'] = line['gender']
            data['last_name'] = line['last_name']
            data['status'] = line['status']
            data['user_id'] = line['user_id']
            data['username'] = line['username']
            values_for_json.append(data)
    
    return(values_for_json)
            
            
def convert_json (file: list, way: str):
    #Конвертуємо вхідний ліст "file" у json і записуємо його в директорію "way"
    json.dump(file, open(way,'w'),indent=4)  
    


ways = get_route()
file = get_values_for_json(ways[0])
convert_json(file, ways[1])