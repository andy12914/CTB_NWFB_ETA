company_id=input("請輸入巴士公司(NWFB/CTB) :")
stop_id=input("請輸入巴士站編號 :")
route=input("請輸入路線號碼 :")
import urllib.request as request
import json
import time
times=0
while True:
    src='https://rt.data.gov.hk/v1/transport/citybus-nwfb/eta/'+company_id+'/'+stop_id+'/'+route
    with request.urlopen(src) as response:
        data=json.load(response)
    print()    
    print("資料更新時間: "+data["generated_timestamp "][11:19])
    clist=data["data"]
    for etaofbus in clist:
        print("往 "+etaofbus["dest_tc"]+"   "+"預計到達時間: "+etaofbus["eta"][11:19]+"   "+"備註: "+etaofbus["rmk_tc"])
    print()
    time.sleep(5)
input()