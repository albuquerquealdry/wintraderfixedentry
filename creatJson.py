import json



def writeJson(jsonFile):
    with open("jsonteste.json", 'w') as f:
        json.dump(jsonFile, f)


file_json = {
            "result": "",
            "Balance" : "",
            "Hour": "",
            "ID" : ""
}
