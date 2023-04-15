import sys
import csv
import json

if len(sys.argv) < 4 or not sys.argv[2] or not sys.argv[4]:
    print("Usage: python3 test.py --type <g_type> --file <file_name>")
    sys.exit()


if len(sys.argv) == 5:
    g_type = sys.argv[2]
    file_name = sys.argv[4]
else:
    g_type = 'elliptical'
    file_name = sys.argv[3]

ans = {}

with open(file_name, encoding='utf8') as csvfile:
    reader = csv.reader(csvfile, delimiter=':', quotechar='"')
    next(reader)  # пропускаем заголовок файла
    for row in reader:
        if row[2].strip() == g_type:
            ans[row[1]] = round(int(row[4]) / int(row[3]), 1)

with open('relations.json', 'w') as jsonfile:
    json.dump(ans, jsonfile)
