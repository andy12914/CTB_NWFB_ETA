company_id=input("請輸入巴士公司(NWFB/CTB) :")
route=input("請輸入路線號碼 :")
direction=input("輸入inbound/outbound :")
print(direction+" :")
import urllib.request as request
import json
src='https://rt.data.gov.hk/v1/transport/citybus-nwfb/route-stop/'+company_id+'/'+route+'/'+direction
with request.urlopen(src) as response:
    data=json.load(response)
clist=data["data"]
for busstop in clist:
    stop_id=busstop["stop"]
    src='https://rt.data.gov.hk/v1/transport/citybus-nwfb/stop/'+stop_id
    with request.urlopen(src) as response:
        data=json.load(response)
    stop=data["data"]
    print(busstop["stop"]+"  "+stop["name_tc"])
input()