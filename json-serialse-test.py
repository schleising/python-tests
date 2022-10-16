import json
import random
import string

letters = string.ascii_uppercase

toBeSaved = {str(key): random.choice(letters) for key in range(100)}

with open('output.txt', 'w', encoding='utf8') as jsonFile:
    json.dump(toBeSaved, jsonFile)

with open('output.txt', 'r', encoding='utf8') as jsonFile:
    loadedData = json.load(jsonFile)

print('Successfully Verified') if all([val == toBeSaved[key] for key, val in loadedData.items()]) else print('Verification Failure')
