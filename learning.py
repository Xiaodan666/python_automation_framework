from datetime import datetime


def covert_time_to_timestamp(t):
    try:
        res = datetime.strptime(t, "%Y-%m-%dT%H:%M:%S.%f").timestamp() * 1000
    except ValueError as e:
        res = datetime.strptime(t, "%Y-%m-%dT%H:%M:%S").timestamp() * 1000
    return res


def bubbling_record(li):
    l = len(li)
    for i in range(1, l):
        for j in range(l - i):
            pr = li[j]
            af = li[j + 1]
            pre = covert_time_to_timestamp(pr["updateTime"])
            aft = covert_time_to_timestamp(af["updateTime"])
            if pre > aft:
                temp = li[j]
                li[j] = li[j + 1]
                li[j + 1] = temp
    return li


if __name__ == '__main__':
    li = [{'updateTime':'2022-08-16T08:54:50.123'},{'updateTime':'2022-08-15T08:54:50.123'},{'updateTime':'2022-08-17T08:54:50.123'}]
    print(bubbling_record(li))

