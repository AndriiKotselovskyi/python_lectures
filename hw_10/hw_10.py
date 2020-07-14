import pymongo
from pymongo import MongoClient
import json
import csv
import datetime

cluster = MongoClient('localhost', 27017) # встановлюємо зв"язок з локальним клієнтом MongoDB
db = cluster["test"] #Створюємо кластер (базу даних) "test"
collection_project = db ["project"] #створюємо підбазу "project" у базі "test"
collection_tasks = db ["tasks"] #створюємо підбазу "tasks" у базі "test"

def csv_to_json(csv_file_name, json_file_name):
    """ Функція переформатовує csv файл у json"""   
    csv_file = open(csv_file_name, 'r')
    json_file = open(json_file_name, 'w')

    readed = csv.DictReader(csv_file)
    for row in readed:
        json.dump(row, json_file)
        json_file.write('\n')
           
    return json_file_name
    
    
def json_to_db(json_file_name, collection):
    """Функція додає дані з json файлу у обрану як атрибут "collection" підбазу
        приєднаної бази"""
    with open(json_file_name) as json_file:
        data = json.load(json_file)
        collection.insert_many(data)
    

project_json = csv_to_json('Project.csv','project.json')
json_to_db(project_json, collection_project) # додаємо дані у підбазу даних "Project"
tasks_json = csv_to_json('Tasks.csv','tasks.json')
json_to_db(tasks_json, collection_tasks) # додаємо дані у підбазу даних "Tasks"

for result in collection_tasks.find({"status":"canceled"}): #знаходимо проекти, де є статус canceled 
    print(result["Project"])

cluster.close()
