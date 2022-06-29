import requests
import datetime
import threading
from api.models import Opendata
import json

# import pandas

current = datetime.datetime.now()
today = current.strftime("%Y-%m-%d")
time = current.strftime("%H:%M:%S")

later = current - datetime.timedelta(minutes=60)
later_time = later.strftime("%H:%M:%S")


clean_data = []
results = []
api_data = []


def real_time_api():
    """국립수산과학원 실시간 어장 정보"""

    url = "https://www.nifs.go.kr/OpenAPI_json"
    service_key = "qPwOeIrU-2111-doc2kim-0377"
    real_time_id = "risaList"

    parameters = {
        'id': real_time_id,
        'key': service_key
    }

    response = requests.get(url, params=parameters).json()
    item = response.get('body').get('item')

    return item


def location_api():
    """국립수산과학원 측정 위치 정보"""

    url = "https://www.nifs.go.kr/OpenAPI_json"
    service_key = "qPwOeIrU-2111-doc2kim-0377"
    location_id = "risaCode"

    parameters = {
        'id': location_id,
        'key': service_key,
    }

    response = requests.get(url, params=parameters).json()

    item = response.get('body').get('item')
    return item


def results_api():
    """ gps 찾아 Naver geo coding하여 주소변환 """
    api = real_time_api()
    gps_data = location_api()

    for i in api:
        for j in gps_data:
            if i["sta_cde"] == j["sta_cde"] and i["wtr_tmp"] != None:
                i["lat"] = j["lat"]
                i["lng"] = j["lon"]
                i["ocean"] = j["gru_nam"]
                if i["lat"] != None and i["lng"] != None:
                    latlng = i["lng"] + "," + i["lat"]
                    url = "https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc"
                    service_id = "2ctgl620in"
                    service_key = "I7bVAsrjstHcpGvB7F9UmvCCrkHPXDO0hhhEw81Q"

                    parameters = {
                        'X-NCP-APIGW-API-KEY-ID': service_id,
                        'X-NCP-APIGW-API-KEY': service_key,
                        'coords': latlng,
                        'output': 'json'
                    }
                    response = requests.get(url, params=parameters)

                    if response.status_code == 200:
                        try:
                            get_json = response.json()
                            get_adress = get_json.get(
                                "results")[0].get("region")
                            area1 = get_adress.get("area1").get("name")
                            area2 = get_adress.get("area2").get("name")
                            area3 = get_adress.get("area3").get("name")
                        except IndexError:
                            continue
                        try:
                            area4 = get_adress.get("area4").get("name")
                        except IndexError:
                            area4 = None

                        i.update(
                            area1=area1,
                            area2=area2,
                            area3=area3,
                            area4=area4,
                        )
                        if i["wtr_tmp"] is None:
                            continue
                        if i["dox"] is None:
                            i["dox"] = 0
                        if i["sal"] is None:
                            i["sal"] = 0
                        if i["obs_dat"] == today and i["obs_tim"] >= later_time:
                            api_data.append(
                                {
                                    "coordinates": {
                                        "lat": i.get("lat"),
                                        "lng": i.get("lng")
                                    },
                                    "location": {
                                        "ocean": i.get("ocean"),
                                        "area1": i.get("area1"),
                                        "area2": i.get("area2"),
                                        "area3": i.get("area3"),
                                        "area4": i.get("area4")
                                    },
                                    "value": {
                                        "temp": i.get("wtr_tmp"),
                                        "oxy ": i.get("dox"),
                                        "salt": i.get("sal"),
                                        "ph": 0.0,
                                        "salt": 0.0,
                                        "ntu": 0.0,
                                    },
                                    "time": {
                                        "obs_date": i.get("obs_dat"),
                                        "obs_time": i.get("obs_tim"),
                                    }
                                }
                            )

                            data = Opendata.objects.create(
                                ocean=i.get("ocean"),
                                temp=i.get("wtr_tmp"),
                                oxy=i.get("dox"),
                                salt=i.get("sal"),
                                lat=i.get("lat"),
                                lng=i.get("lng"),
                                obs_date=i.get("obs_dat"),
                                obs_time=i.get("obs_tim"),
                                area1=i.get("area1"),
                                area2=i.get("area2"),
                                area3=i.get("area3"),
                                area4=i.get("area4"),
                            )
                            data.save()
        with open("./json_data.json", 'w') as outfile:
            json.dump(api_data, outfile, indent=4, ensure_ascii=False)


def start_timer():
    Opendata.objects.all().delete()
    print("data reset..")
    results_api()
    threading.Timer(1200, start_timer).start()
