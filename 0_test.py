import json

file_path = 'score.json'

name = 'daeyong'
score = 5

record = {'champion' : name,
          'Highest Score' : score}

with open(file_path, 'w') as f :
    json.dump(record, f)

with open(file_path, 'r') as f :
    a = json.load(f)
    print(a['champion'])