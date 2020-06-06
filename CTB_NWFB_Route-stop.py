company_id=input("Enter company(NWFB/CTB) :")
route=input("Enter route number :")
direction=input("Enter inbound/outbound :")
import urllib.request as request
import json
src='https://rt.data.gov.hk/v1/transport/citybus-nwfb/route-stop/'+company_id+'/'+route+'/'+direction
with request.urlopen(src) as response:
    data=json.load(response)
clist=data["data"]
with open(company_id+route+direction+'.txt', 'w') as file:
    for busstop in clist:
        file.write(busstop["stop"]+'\n')
        print(busstop["stop"])