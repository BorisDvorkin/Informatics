import json
import xmltodict
with open("Schedule.xml", encoding="utf-8") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
    json_data = json.dumps(data_dict)
    with open("data.json", "w") as json_file:
        json_file.write(json_data)
