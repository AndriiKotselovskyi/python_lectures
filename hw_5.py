import os
import csv
import argparse


def route():
    """ З командної стрічки отримуємо шлях до файлу .csv за допомогою аргумента -path (way)
    та кількість рядків кінцевого виводу за допомогою аргумента -bed (nlines)"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-path', type=str, required=True, help='Path to the file')
    parser.add_argument('-bed', type=int, required=True, help='Number of displayed HRR rows')
    args = parser.parse_args()
    
    way = args.path    
    nlines = args.bed
    
    return way, nlines
    
    
def csv_reader(way: str, filename:str = 'HRR Scorecard_ 20 _ 40 _ 60 - 20 Population.csv'):
    """Читаємо .csv файл з директорії way:
    На виході отримуємо ліст сортованих даних по Госпіталь-відсоток вільних ліжок"""
    with open(os.path.join(way, filename)) as csv_file:
        readed_csv = csv.DictReader(csv_file)
        
        s_col = list()
        for lines in readed_csv:
            #Відбираємо потрібні колонки і переводимо дані для подальших обрахунків в числові типи
            if (lines['Total Hospital Beds'] and lines['Available Hospital Beds']) != '':
                s_col.append((lines['HRR'], 
                        float(lines['Total Hospital Beds'].replace(',','')),
                        float(lines['Available Hospital Beds'].replace(',',''))
                        ))
    #Рахуємо відсоток вільних ліжок і сортуємо дані по спаданні кількості
    perc_av = lambda data: ((data[2]/data[1]),data[0])
    sort_dat = sorted(list(map(perc_av, s_col)), reverse=True)
    
    return sort_dat

   
ui = route()

for val in csv_reader(ui[0])[:ui[1]]:
    print('{} {:2.2%}'.format(val[1],val[0]))
