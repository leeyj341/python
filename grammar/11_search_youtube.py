from pprint import pprint
import requests
key = "AIzaSyBUA3syJcKiCStjSlEnvV2xLnQfw4udznI"
url = "https://www.googleapis.com/youtube/v3/search"

# 1. 검색어를 입력하면 
# 2. 영상들을 검색
# 3. 그 영상들의 제목과 채널명

# string interpolation
search = input("검색어를 입력해주세요. : ")
q = f"q={search}"
my_type = "type=video"
part = "part=snippet"
maxResults = "maxResults=20"

url = f"https://www.googleapis.com/youtube/v3/search?key={key}&{part}&{my_type}&{q}&{maxResults}"
# print(url)

response = requests.get(url)
data = response.json()
# pprint(data) # 구조 더러워...

# 채널명, 영상 제목
for data in data['items'][:10] :
    print(data["snippet"]["title"], end="\t채널명 ")
    print(data["snippet"]["channelTitle"])

