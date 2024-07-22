# Phase 1:
# Write a script that retrieves info from the API and prints out all databases, their storage type, and their used storage.
import requests

enpoint="https://6god8pgyzf.execute-api.us-west-2.amazonaws.com/databases"

r=requests.get(enpoint)
if r.status_code==200:
    temp = r.json()['databases']
    for t in temp:
        print(t['name'],t['storage_type'], t['storage_used'])
