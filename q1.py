#1

def clock_angle(hour: int, minute: int) -> float:
    
    #hourに12~23が与えられた場合、0~11の数字に直す。
    if hour > 11:
        hour -= 12
    
    #12時の位置を基準とした各針の角度計算
    s = hour * 30 + minute * 0.5
    l = minute * 6 

    angle = s - l

    if angle < 0:
        angle = - angle
    elif angle > 180:
        angle = 360 - angle

    print(angle)

# clock_angle(11, 30)
# clock_angle(6, 30)
# clock_angle(1, 30) 
# clock_angle(12, 30) 
# clock_angle(12, 0) 
# clock_angle(11, 5) 
# clock_angle(11, 0)
# clock_angle(1, 0)
# clock_angle(22, 0)
# clock_angle(22, 30)
# clock_angle(2, 30)


def astrology(birthday: str) -> str:
    ymd = birthday.split("/")
    y = int(ymd[0])
    m = int(ymd[1])
    d = int(ymd[2])

    sign = ""
    zodiac = ""

    if m == 3 and d >= 21 or m == 4 and d < 20:
        sign = "Aries"
    if m == 4 and d >= 20 or m == 5 and d < 21:
        sign = "Taurus"
    if m == 5 and d >= 21 or m == 6 and d < 22:
        sign = "Gemini"
    if m == 6 and d >= 22 or m == 7 and d < 23:
        sign = "Cancer"
    if m == 7 and d >= 23 or m == 8 and d < 23:
        sign = "Leo"
    if m == 8 and d >= 23 or m == 9 and d < 23:
        sign = "Virgo"
    if m == 9 and d >= 23 or m == 10 and d < 24:
        sign = "Libra"
    if m == 10 and d >= 24 or m == 11 and d < 23:
        sign = "Scorpio"
    if m == 11 and d >= 23 or m == 12 and d < 22:
        sign = "Sagittarius"
    if m == 12 and d >= 22 or m == 1 and d < 20:
        sign = "Capricorn"
    if m == 1 and d >= 20 or m == 2 and d < 19:
        sign = "Aquarius"
    if m == 2 and d >= 19 or m == 3 and d < 21:
        sign = "Pisces"

    # 十二支 
    # 誕生年を12で割った余りで干支を判定
    num = y % 12
    zodiacs = ["申", "酉", "戌", "亥", "子", "丑", "寅", "卯", "辰", "巳", "午", "未"]
    
    zodiac = zodiacs[num]
    
    print(birthday, sign, zodiac)




astrology("1998/07/03")

    

