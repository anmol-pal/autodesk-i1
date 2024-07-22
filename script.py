# Phase 1:
# Write a script that retrieves info from the API and prints out all databases, their storage type, and their used storage.
import requests
import sys

enpoint="https://6god8pgyzf.execute-api.us-west-2.amazonaws.com/databases"

r=requests.get(enpoint)
out = dict()
if r.status_code==200:
    temp = r.json()['databases']
    for t in temp:
        key=t['name']+"|"+t['storage_type']
        if t['storage_used']:
            value = float(t['storage_used'])/float(t['storage_size'])  * 100
        else:
            value=0
        out[key]= value

sorted_database = sorted(out, key=out.get, reverse=True)


data = dict()
for item in sorted_database:
    temp = item.split('|')
    name=temp[0]
    data[name]= str(temp[1])+' '+str(out[item])
# print(data)


# Update your script to allow pulling the entire list, or just a single DB based on name
print(sys.argv)
if len(sys.argv)>1:
    first = sys.argv[1]
    print(data[first])
else:
    for item in data:
        print(item, data[item])
