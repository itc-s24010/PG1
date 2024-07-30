def number_to_day(num=0):
        '''任意の整数が与えられたら今日、昨日、明日、それ以外を判定して返す
        戻り値
            昨日(numが-1の場合)
            今日(numが0の場合)
            明日(numが1の場合)
            今日より1日を超えて離れた日(numが上記以外の場合)
        '''
        if num == 0:
            day = "今日"
        elif num == 1:
            day = "明日"
        elif num == -1:
            day = "昨日"
        else:
            day = "今日より1日を超えて離れた日"
        return day
        
def perrin(m=100)
    '''mより小さなペラン数列をリストで返す

    ペラン数列:3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17, 22, 29, 39, 
    '''
    a, b, c, = 3, 0, 2
    result = []
    while a < m:
        result.append(a)
        a, b, c, = b, c, a+b
    return result
