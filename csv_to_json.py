import pandas as pd
import json


nodejson = []
nodevalidator = []
linkjson = []
linkvalidator = []

data = pd.read_csv('Hololink_Tags_chinaIndia.csv')

for i,j,k,z in zip(data['title'], data['media'], data['url'],data['tags']):
    if i not in nodevalidator:
        nodejson.append({"id":f"{i}", "url":f"{k}"})
        nodevalidator.append(i)

    if j not in nodevalidator:
        nodejson.append({"media":f"{j}", "publish":0})
        nodevalidator.append(j)

    tags = z.split(',')


    for tag in tags:
        tag = tag.strip()
        if tag not in nodevalidator:
            nodejson.append({"id":f"{tag}", "connection":0})
            nodevalidator.append(tag)
        
        for node in nodejson:
            try:
                if node['id'] == tag:
                    node['connection'] = node['connection']+1
            except Exception as e:
                error_class = e.__class__.__name__ 
                detail = e.args[0] 
                #print(error_class, detail)

        linkjson.append({"source":f"{i}", "target":f"{tag}"})

    #計算 media public 數量
    for node in nodejson:
        try:
            if node['media'] == j:
                node['publish'] += 1
        except:
            pass

dataJson = {
    "nodes":nodejson,
    "links":linkjson
}

exportJson = json.dumps(dataJson,ensure_ascii=False)
with open('China_India.json', 'w') as file:
    file.write(exportJson)