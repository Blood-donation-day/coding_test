def solution(s):
    result = [0, 0]
    while '1' != s:
        result[1] += s.count('0')
        s = s.replace('0', '')
        s = str(bin(len(s)))[2:]
        result[0] += 1
    return result