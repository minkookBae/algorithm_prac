def solution(s):
    arr = map(int, s.split())
    answer = ''
    arr = list(arr)
    answer = str(min(arr)) + " " + str(max(arr))

    return answer