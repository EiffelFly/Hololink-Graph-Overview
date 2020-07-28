import pandas as pd
import json


nodejson = []
nodevalidator = []
linkjson = []
linkvalidator = []

data = pd.read_csv('Hololink_Tags_chinaIndia.csv')

for i,j,k,z in zip(data['title'], data['media'], data['url'],data['tags']):

    tagAmount = 0

    if i not in nodevalidator:
        nodejson.append({"id":f"{i}", "url":f"{k}", "level":"article", "tagAmount":0})
        nodevalidator.append(i)

    if j not in nodevalidator:
        nodejson.append({"id":f"{j}","level":"media", "publish":0})
        nodevalidator.append(j)

    tags = z.split(',')


    for tag in tags:
        tag = tag.strip()
        if tag not in nodevalidator:
            nodejson.append({"id":f"{tag}","level":"tag" ,"connection":0})
            nodevalidator.append(tag)
        
        for node in nodejson:
            try:
                if node['id'] == tag:
                    node['connection'] = node['connection']+1
            except Exception as e:
                error_class = e.__class__.__name__ 
                detail = e.args[0] 
                #print(error_class, detail)

        #計算 article tag 數量
        tagAmount += 1



        linkjson.append({"source":f"{i}", "target":f"{tag}"})

    #計算 media publish 數量
    for node in nodejson:
        try:
            if node['level'] == "media" and node['id'] == j:
                node["publish"] += 1
            if node['id'] == i:
                node["tagAmount"] = tagAmount
        except:
            pass

    


dataJson = {
    "nodes":nodejson,
    "links":linkjson
}

exportJson = json.dumps(dataJson,ensure_ascii=False)
with open('China_India.json', 'w', encoding='utf-8') as file:
    file.write(exportJson)