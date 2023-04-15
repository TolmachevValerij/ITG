import sqlite3
import csv
name = input()
name_table = input().split('.')
con = sqlite3.connect(name)
cur = con.cursor()
result = ''
if name_table[1] == 'luminosity_id':
    result = cur.execute(f"""SELECT id, sign, (SELECT type FROM types WHERE id = {name_table[0]}.type_id),
                            (SELECT range FROM luminosities WHERE id = {name_table[0]}.luminosity_id), size,
                            stars AS minimum FROM {name_table[0]} where luminosity_id  
                            in (1) ORDER BY size desc""").fetchall()
elif name_table[1] == 'stars':
    R = cur.execute(f"""SELECT MIN({name_table[1]}) AS minimum FROM {name_table[0]}""").fetchall()
    result = cur.execute(f"""SELECT id, sign, (SELECT type FROM types WHERE id = {name_table[0]}.type_id),
                        (SELECT range FROM luminosities WHERE id = {name_table[0]}.luminosity_id), size,
                        stars AS minimum FROM {name_table[0]} where {name_table[1]} 
                        in ({R[0][0]}) ORDER BY size desc""").fetchall()
elif name_table[1] == 'size':
    R = cur.execute(f"""SELECT MIN({name_table[1]}) AS minimum FROM {name_table[0]}""").fetchall()
    result = cur.execute(f"""SELECT id, sign, (SELECT type FROM types WHERE id = {name_table[0]}.type_id),
                            (SELECT range FROM luminosities WHERE id = {name_table[0]}.luminosity_id), size,
                            stars AS minimum FROM {name_table[0]} where {name_table[1]} 
                            in ({R[0][0]}) ORDER BY size desc""").fetchall()

k = 0
with open("collisions.csv", 'w') as w_file:
    file_writer = csv.writer(w_file, delimiter=",")
    print('no galaxy type luminosity size stars')
    file_writer.writerow(['no', 'galaxy', 'type', 'luminosity', 'size', 'stars'])
    for elem in result:
        k += 1
        file_writer.writerow([k, elem[1], elem[2], elem[3], elem[4], elem[5]])





con.close()
