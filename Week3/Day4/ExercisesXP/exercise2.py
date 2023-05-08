# import json
# sampleJson = """{
#    "company":{
#       "employee":{
#          "name":"emma",
#          "payable":{
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
#
#
# 1. Access the nested “salary” key from the JSON-string above.
# 2. Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# 3. Save the dictionary as JSON to a file.

import json
from os.path import dirname, join

CURRENT_DIR = dirname(__file__)
RESULT_FILE = "./result.json"
FILE_PATH = join(CURRENT_DIR, RESULT_FILE)

sampleJson = {
    "company": {
        "employee": {
            "name": "emma",
            "payable": {
                "salary": 7000,
                "bonus": 800
            }
        }
    }
}

salary = sampleJson.get("company").get("employee").get("payable").get("salary")

# sampleJson["company"]["employee"]["birth_date"] = '01-01-1990'
sampleJson["company"]["employee"]["birth_date"] = None

if __name__ == "__main__":
    print(salary)

    with open(RESULT_FILE, "w") as f:
        json.dump(sampleJson, f, indent=2)
