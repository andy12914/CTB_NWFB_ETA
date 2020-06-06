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
    etasrc='https://rt.data.gov.hk/v1/transport/citybus-nwfb/eta/'+company_id+'/'+stop_id+'/'+route
    with request.urlopen(etasrc) as response:
        etadata=json.load(response)
    eta=etadata["data"]
    print(busstop["stop"]+" "+stop["name_tc"])
    for etaofbus in eta:
        print("往 "+etaofbus["dest_tc"]+"   "+"預計到達時間: "+etaofbus["eta"][11:19]+"   "+"備註: "+etaofbus["rmk_tc"])
    print()
input()