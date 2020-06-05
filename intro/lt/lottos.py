import requests
import random

def lotto(number = 1000) :
    response = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=913')
    # print(response.json())
    # print(type(response.json()))
    data = response.json()
    winner = []
    # print(dir(winner))
    for i in range(1, 7) :
        winner.append(data[f"drwtNo{i}"])
    # print(winner)

    win_rate = {
        "1st" : 0,
        "2nd" : 0,
        "3rd" : 0,
        "4th" : 0,
        "fail" : 0
    }

    if number.isdecimal == True :
        for i in range(number) :
            lotto = random.sample(range(1,46), 6)
            # print(lotto)

            matched = 0
            for num in lotto :
                if num in winner :
                    matched += 1

            # 1. matched = 6 1등
            # 2. matched = 5 3등
            # 3. matched = 4 4등
            # 4. 그 외는 fail

            if matched == 6 :
                win_rate["1st"] += 1
            elif matched == 5 :
                if data["bnusNo"] in lotto :
                    win_rate["2nd"] += 1
                else :
                    win_rate["3rd"] += 1
            elif matched == 4 :
                win_rate["4th"] += 1
            else :
                win_rate["fail"] += 1

        return win_rate
    else :
        return "정수형이 아닙니다."

