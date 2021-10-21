import requests
import json
import re
import os

def getDests():
    auth_token = "zlhKTvKaZthfwpwjhpCWwSpzpPL6FtqFumMNhJQ65fXeNF6DDKfBLtkXVwi42Ms2"
    pagination_count = 200
    pagination_cursor = ""

    url = "https://api.segmentapis.com/destinations?pagination.count=" + str(pagination_count)
    headers = {'Authorization': 'Bearer ' + auth_token}
    dir_name = "destinations"
    os.makedirs(dir_name, exist_ok = True)

    next_page = bool(1)
    while next_page:
        new_url = url
        if pagination_cursor != "":
            new_url = new_url + "&pagination.cursor=" + pagination_cursor

        response = requests.get(new_url, headers=headers)
        response_json = json.loads(response.text)
        destinations = response_json["data"]["destinations"]
        
        for destination in destinations:
            if("name" in destination and destination["name"] != ""):
                dest_name = re.sub(r'[^A-Za-z0-9_-]','-',destination["name"]) + "_" + destination["id"]
            else:
                dest_name = destination["id"]
            
            with open(dir_name + "/" + dest_name + ".json", 'w') as outfile:
                json.dump(destination, outfile, indent = 4)

        pagination_cursor = response_json["data"]["pagination"]["next"]
        if pagination_cursor == None:
            next_page = bool(0)

def main():
    getDests()

if __name__ == "__main__":
    main()