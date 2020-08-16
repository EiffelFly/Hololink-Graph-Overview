import pandas as pd
import json

processed_data = []



with open('testoutput.json', encoding='utf-8') as file:
    data = json.load(file)

    #for data_col in data:
    for data_col in data:
        article_title = data_col['title']
        article_galaxy = data_col['galaxy']
        article_url = data_col['url']

        nodejson = []
        basestoneNum = 0
        stellarNum = 0

        for key,value in data_col['Final'].items():
            title = value['Title']
            frequency = value['Frequency']
            keyword_type = value['POS']
            if value['POS'] == 'Na' or value['POS'] == 'Nb' or value['POS'] == 'Nc':            
                nodejson.append({"title":title, "frequency":frequency, "group":"stellar", "type":keyword_type})
                stellarNum += 1
            else:
                if value['POS'] == 'DATE' or value['POS'] == 'ORDINAL' or value['POS'] == 'CARDINAL':
                    pass
                else:
                    nodejson.append({"title":title, "frequency":frequency, "group":"basestone", "type":keyword_type})
                    basestoneNum += 1

        processed_data.append({"article":article_title, "galaxy": article_galaxy, "url":article_url, "basestoneNum":basestoneNum, "stellarNum":stellarNum, "nodes": nodejson})

exportJson = json.dumps(processed_data, ensure_ascii=False)
with open('test_ver1.json', 'w', encoding="utf-8") as f:
    f.write(exportJson)
        
        

