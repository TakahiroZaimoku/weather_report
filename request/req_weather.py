import requests
from datetime import datetime
from req_geography import get_coordinate

class GetWeather:
    # コンストラクタ
    def __init__(self):
        # 今日・明日・明後日の天気予報を取得するAPIのURL
        self.get_weather_info_url = "https://www.jma.go.jp/bosai/forecast/data/forecast/"
    
    # APIのレスポンスを受け取る
    def get_weather_info(self, prefecture_code):
        if not prefecture_code: return "検索ワードから近隣情報の取得に失敗しました。"
        # 今日・明日・明後日の天気予報を取得する
        response = requests.get(f"{self.get_weather_info_url}{prefecture_code}.json")
        # 取得結果判定
        if response.status_code == 200:
            json_data = response.json()
            wether_info = json_data[0].get("timeSeries")[0].get("areas")[0].get("weathers")
            result_msg = "\n".join([
                f"{day[:10].replace('-', '/')} {self.get_day_of_week(day)}: {tenki}" 
                for day, tenki in zip(json_data[0].get("timeSeries")[0].get("timeDefines"), wether_info)
            ])
            return result_msg
        else:
            return "情報が取得出来ませんでした。"
        
    # 県コードに変換する
    def change_prefecture_code(self, prefecture):
        mydict = {
            "北海": "015000",
            "青森": "020000",
            "秋田": "050000",
            "岩手": "030000",
            "宮城": "040000",
            "山形": "060000",
            "福島": "070000",
            "茨城": "080000",
            "栃木": "090000",
            "群馬": "100000",
            "埼玉": "110000",
            "東京": "130000",
            "千葉": "120000",
            "神奈": "140000",
            "長野": "200000",
            "山梨": "190000",
            "静岡": "220000",
            "愛知": "230000",
            "岐阜": "210000",
            "三重": "240000",
            "新潟": "150000",
            "富山": "160000",
            "石川": "170000",
            "福井": "180000",
            "滋賀": "250000",
            "京都": "260000",
            "大阪": "270000",
            "兵庫": "280000",
            "奈良": "290000",
            "和歌": "300000",
            "岡山": "330000",
            "広島": "340000",
            "島根": "320000",
            "鳥取": "310000",
            "徳島": "360000",
            "香川": "370000",
            "愛媛": "380000",
            "高知": "390000",
            "山口": "350000",
            "福岡": "400000",
            "大分": "440000",
            "長崎": "420000",
            "佐賀": "410000",
            "熊本": "430000",
            "宮崎": "450000",
            "鹿児": "460100",
            "沖縄": "471000",
        }
        return mydict.get(prefecture[:2], "")
    
    # 日付文字列から曜日を取得
    def get_day_of_week(self, date_str):
        # 日付文字列をdatetimeオブジェクトに変換
        date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')
        # 曜日を取得（0: 月曜日, 1: 火曜日, ..., 6: 日曜日）
        day_of_week = date_obj.weekday()
        # 曜日の名前を返す
        days = ["(月)", "(火)", "(水)", "(木)", "(金)", "(土)", "(日)"]
        return days[day_of_week]

if __name__ == "__main__":
    # インスタンス生成
    get_weather = GetWeather()
    # 引数名称の住所を取得
    coordinate = get_coordinate("大分")
    # 県コードに変換する
    prefecture_code = get_weather.change_prefecture_code(coordinate[1])
    # APIのレスポンスを受け取る
    json_data = get_weather.get_weather_info(prefecture_code)
    import pdb;pdb.set_trace()