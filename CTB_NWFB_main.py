def company(company_id):
    import urllib.request as request
    import json
    src='https://rt.data.gov.hk/v1/transport/citybus-nwfb/company/'+company_id
    with request.urlopen(src) as response:
        data=json.load(response)
    company=data["data"]     
    print("公司編號: "+company["co"])
    print("公司名稱: "+company["name_tc"])
    print("公司網站: "+company["url"])
def route(company_id, route):
    import urllib.request as request
    import json
    src='https://rt.data.gov.hk/v1/transport/citybus-nwfb/route/'+company_id+'/'+route
    with request.urlopen(src) as response:
        data=json.load(response)
    route=data["data"]   
    print("公司編號: "+route["co"])
    print("路線號碼: "+route["route"])
    print("起點站: "+route["orig_tc"]+"  "+route["orig_en"])
    print("終點站: "+route["dest_tc"]+"  "+route["dest_en"])
def stop(stop_id):
    import urllib.request as request
    import json
    src='https://rt.data.gov.hk/v1/transport/citybus-nwfb/stop/'+stop_id
    with request.urlopen(src) as response:
        data=json.load(response)
    stop=data["data"]
    print("停站名稱: "+stop["name_tc"]+"  "+stop["name_en"])
def route_stop(company_id, route, direction):
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
def ETA(company_id, stop_id, route):
    import urllib.request as request
    import json
    src='https://rt.data.gov.hk/v1/transport/citybus-nwfb/eta/'+company_id+'/'+stop_id+'/'+route
    with request.urlopen(src) as response:
        data=json.load(response)
    print()    
    print("資料更新時間: "+data["generated_timestamp "][11:19])
    clist=data["data"]
    for etaofbus in clist:
        print("往 "+etaofbus["dest_tc"]+"   "+"預計到達時間: "+etaofbus["eta"][11:19]+"   "+"備註: "+etaofbus["rmk_tc"])
def stop_ETA(company_id, route, direction):
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

while True:
    print("""1.公司數據
2.巴士路線數據 
3.巴士站數據
4.個別路線的巴士站數據
5.預計到達時間數據
6.個別路線的巴士站及預計到達時間數據
7.離開
""")
    print()
    choice=input("請輸入查詢的選項 :")
    print()
    if choice=="1":
        company_id=input("請輸入巴士公司(NWFB/CTB) :")
        company(company_id)
        input()
    elif choice=="2":
        company_id=input("請輸入巴士公司(NWFB/CTB) :")
        route=input("請輸入路線號碼 :")
        route(company_id, route)
        input()
    elif choice=="3":
        stop_id=input("請輸入巴士站編號 :")
        stop(stop_id)
        input()
    elif choice=="4":
        company_id=input("請輸入巴士公司(NWFB/CTB) :")
        route=input("請輸入路線號碼 :")
        direction=input("輸入inbound/outbound :")
        route_stop(company_id, route, direction)
        input()
    elif choice=="5":
        company_id=input("請輸入巴士公司(NWFB/CTB) :")
        stop_id=input("請輸入巴士站編號 :")
        route=input("請輸入路線號碼 :")
        ETA(company_id, stop_id, route)
        input()
    elif choice=="6":
        company_id=input("請輸入巴士公司(NWFB/CTB) :")
        route=input("請輸入路線號碼 :")
        direction=input("輸入inbound/outbound :")
        stop_ETA(company_id, route, direction)
        input()
    elif choice=="7":
        exit()
    else:
        print("輸入錯誤，請重新輸入")
        input()    