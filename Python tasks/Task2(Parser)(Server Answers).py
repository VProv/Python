import sys


def read_int(line, start):
    pos = start
    st = ""
    flag = True
    while flag:
        if '0' <= line[pos] <= '9':
            st += line[pos]
        else:
            flag = False
        pos += 1
    return st, pos


def main():
    st = "200"
    full_requests = 0
    req_with_200 = 0
    req_with_300_309 = 0
    req_over = 0
    for line in sys.stdin.readlines():
        full_requests += 1
        pos = line.find('"', line.find('"') + 1)
        request_ans, end_r = read_int(line, pos+2)
        if request_ans == "200":
            req_with_200 += 1
        elif "300" <= request_ans <= "309":
            req_with_300_309 += 1
        else:
            req_over += 1
    print(req_with_200)
    print(req_with_300_309)
    print(req_over)
    print(full_requests)

main()
