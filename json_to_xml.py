import json
import os
import sys


def json_to_xml(json_file):
    file = open(json_file, 'r')
    data = json.load(file)
    users = []
    for obj in data:
        if obj["type"] == 2:
            users.append(obj["filter"])
    file.close()
    users.sort()

    path = os.path.dirname(json_file)
    xml_file = open(os.path.join(path, "user.xml"), "w")
    xml_file.write("<filters>\n")
    for user in users:
        xml_file.write(f"<item enabled=\"true\">u={user}</item>\n")
    xml_file.write("</filters>")
    xml_file.close()


if __name__ == "__main__":
    json_to_xml(sys.argv[1])
