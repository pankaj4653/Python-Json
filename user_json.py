import json

people_string = '''
{
	"people": [
	{
	   "name":"John Smith",
	   "phone":"655-555-7164",
	   "emails":["johnsmith@bogusemail.com","john.smith@work-place.com"],
	   "has_license": false
	 },
	 {
	  "name":"John Doe",
	  "phone":"560-555-5153",
	  "emails":null,
	  "has_license":true
	 }
	]
}'''

data = json.loads(people_string) #Json String into a Python Object

#print(type(data))
#print(type(data['people']))

for person in data['people']:
	print(person['name'])


for person in data['people']:
	del person['phone']


for person in data['people']:
	print(person)

new_string = json.dumps(data)  # Dumps the Python Object in Json Sting Object
print(new_string)

