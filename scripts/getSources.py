import requests
import json
import re
import os

def getSrcs():
    auth_token = "zlhKTvKaZthfwpwjhpCWwSpzpPL6FtqFumMNhJQ65fXeNF6DDKfBLtkXVwi42Ms2"
    pagination_count = 200
    pagination_cursor = ""

    url = "https://api.segmentapis.com/sources?pagination.count=" + str(pagination_count)
    headers = {'Authorization': 'Bearer ' + auth_token}
    dir_name = "sources"
    os.makedirs(dir_name, exist_ok = True)

    next_page = bool(1)
    while next_page:
        new_url = url
        if pagination_cursor != "":
            new_url = new_url + "&pagination.cursor=" + pagination_cursor

        response = requests.get(new_url, headers=headers)
        response_json = json.loads(response.text)
        sources = response_json["data"]["sources"]
        
        for source in sources:
            if("name" in source and source["name"] != ""):
                source_name = re.sub(r'[^A-Za-z0-9_-]','-',source["name"]) + "_" + source["id"]
            else:
                source_name = source["id"]
            
            with open(dir_name + "/" + source_name + ".json", 'w') as outfile:
                json.dump(source, outfile, indent = 4)

        pagination_cursor = response_json["data"]["pagination"]["next"]
        if pagination_cursor == None:
            next_page = bool(0)

def main():
    getSrcs()

if __name__ == "__main__":
    main()