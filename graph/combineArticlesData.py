import json

nodevalidator = []
d3node = []
d3link = []


with open('test_data1.json', encoding='utf-8') as file:
    data = json.load(file)

    article_title = data['article']
    article_galaxy = data['galaxy']
    article_url = data['url']
    article_basestoneNum = data['basestoneNum']
    article_stellarNum = data['stellarNum']

    if article_title not in nodevalidator:
        d3node.append({"id":f"{article_title}", "url":f"{article_url}", "level":"article", "basestoneNum":f"{article_basestoneNum}", "stellarNum":f"{article_stellarNum}"})

    for value in data['nodes']:
        key_title = value['title']
        key_group = value['group']
        if key_title not in nodevalidator:
            if key_group == "basestone":
                d3node.append({"id":f"{key_title}", "level":"basestone", "connection":1})
            elif key_group == "stellar":
                d3node.append({"id":f"{key_title}", "level":"stellar", "connection":1})
        else:
            for node in d3node:
                if node['id'] == key_title:
                    if node['level'] == key_group:
                        node['connection'] += 1

        d3link.append({"source":f"{article_title}", "target":f"{key_title}"})
        
    datajson = {
        "nodes":d3node,
        "links":d3link
    }   

exportJson = json.dumps(datajson,ensure_ascii=False)
with open('testford3.json', 'w', encoding='utf-8') as file:
    file.write(exportJson)