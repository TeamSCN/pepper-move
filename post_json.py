import urllib.request, json

if __name__ == '__main__':
    url = "http://192.168.1.140:8000"
    method = "POST"
    headers = {"Content-Type" : "application/json"}

    # PythonオブジェクトをJSONに変換する
    obj = {'0':{"x" : 0.0, 'y':0.0, 'theta':0.0}, 'stop_flg': 0, 'photo_flg':1, 'dest_x':0.0, 'dest_y':0.0}
    json_data = json.dumps(obj).encode("utf-8")

    # httpリクエストを準備してPOST
    request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
