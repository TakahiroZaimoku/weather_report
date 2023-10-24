import requests

# 国土地理院APIを使用して、住所から緯度経度を取得する関数。
def get_coordinate(place_name, prefecture= ""):
    if not place_name: return "地名を入力してください。"
    url = "https://msearch.gsi.go.jp/address-search/AddressSearch"
    params = {"q": place_name}
    r = requests.get(url, params=params)
    data = r.json()
    if "error" in data:
        print(data["error"])
        return "", ""
    if not data:
        return "", ""
    else:
        # レスポンスと施設名が一致する緯度経度を返す
        for row in data:
            if row["properties"]["title"].startswith(place_name):
                coordinate = row["geometry"]["coordinates"]
                title = row["properties"]["title"] 
                return coordinate, title
        # レスポンス値と都道府県が一致する緯度経度を返す
        for row in data:
            if row["properties"]["title"].startswith(prefecture):
                coordinate = row["geometry"]["coordinates"]
                title = row["properties"]["title"]
                return coordinate ,title
        # 見つからない場合
        return "", ""

if __name__ == "__main__":
    place_name = "須磨水族館"
    result = get_coordinate(place_name)
    import pdb;pdb.set_trace()