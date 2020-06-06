company_id=input("Enter company(NWFB/CTB) :")
stop_id=input("Enter stop id :")
route=input("Enter route number :")
import urllib.request as request
import json
src='https://rt.data.gov.hk/v1/transport/citybus-nwfb/eta/'+company_id+'/'+stop_id+'/'+route
with request.urlopen(src) as response:
    data=json.load(response)
clist=data["data"]
for etaofbus in clist:
    print("往 "+etaofbus["dest_tc"]+"   "+"預計到達時間: "+etaofbus["eta"][11:19]+"   "+"備註: "+etaofbus["rmk_tc"])
input()    