import json

jsonString = """{"people":[{"Id":"1","FirstName":"Colby","LastName":"Joines","Email":"joinescolby23@gmail.com"}]}"""


jsonObj = json.loads(jsonString)

print(jsonObj)