import requests
import json
import re
import os

def getWhs():
    auth_token = "zlhKTvKaZthfwpwjhpCWwSpzpPL6FtqFumMNhJQ65fXeNF6DDKfBLtkXVwi42Ms2"
    pagination_count = 200
    pagination_cursor = ""

    url = "https://api.segmentapis.com/warehouses?pagination.count=" + str(pagination_count)
    headers = {'Authorization': 'Bearer ' + auth_token}
    dir_name = "warehouses"
    os.makedirs(dir_name, exist_ok = True)

    next_page = bool(1)
    while next_page:
        new_url = url
        if pagination_cursor != "":
            new_url = new_url + "&pagination.cursor=" + pagination_cursor

        response = requests.get(new_url, headers=headers)
        response_json = json.loads(response.text)
        warehouses = response_json["data"]["warehouses"]
        
        for warehouse in warehouses:
            if("name" in warehouse["metadata"] and warehouse["metadata"]["name"] != ""):
                whs_name = warehouse["metadata"]["name"] + "_" + warehouse["id"]
            else:
                whs_name = warehouse["id"]
            
            with open(dir_name + "/" + whs_name + ".json", 'w') as outfile:
                json.dump(warehouse, outfile, indent = 4)

        pagination_cursor = response_json["data"]["pagination"]["next"]
        if pagination_cursor == None:
            next_page = bool(0)

def main():
    getWhs()

if __name__ == "__main__":
    main()