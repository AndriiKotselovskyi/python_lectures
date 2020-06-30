import sqlite3
import datetime
import csv
import os
import argparse


def read_csv(filename):
    # фунція готує дані csv файлу filename до імпорту в базу даних 
    with open(filename) as csv_file:
        csv_readed = csv.reader(csv_file)
        
        next(csv_readed)
    
        rows_csv = list()
        for line in csv_readed:
           rows_csv.append(line)

    return rows_csv
    
    

def project_name():
    # З командної стрічки отримуємо назву проекта для запиту до бази
    parser = argparse.ArgumentParser()
    parser.add_argument('-project', type=str, required=True, help='Projects: "Casino", "Wallet", "Sport"')
    args = parser.parse_args()
    
    project = args.project
    
    return project
    
    
def db_exist (db_name):
    # перевірка і видалення бази з обраною назвою, якщо така існує в директорії
    if os.path.isfile(db_name):
        os.remove(db_name)
        
db_exist('casino.sqlite')
    
conn = sqlite3.connect('casino.sqlite') # створюємо базу даних
cur = conn.cursor() 

""" Створюємо в базі даних таблиці "Project" i "Tasks".
    Наповнюємо їх даними з csv файлів 'Project.csv' і 'Tasks.csv' """      
cur.execute("CREATE TABLE IF NOT EXISTS Project (Name TEXT, description TEXT, deadline DATE)")
cur.execute('''CREATE TABLE IF NOT EXISTS Tasks (id INTEGER PRIMARY KEY, priority INTEGER, details TEXT,
               status TEXT, deadline DATE, completed DATE, Project TEXT)''')
cur.executemany("INSERT INTO project VALUES (?,?,?)", (read_csv('Project.csv')))
cur.executemany("INSERT INTO Tasks VALUES(?,?,?,?,?,?,?)",(read_csv('Tasks.csv')))

# Робимо запит до бази даних по назві проекту з командної стрічки
cur.execute("SELECT * FROM Tasks WHERE Project = :proj",{"proj": project_name()})
row = cur.fetchall()
for lines in row:
    print(lines)

conn.close()
