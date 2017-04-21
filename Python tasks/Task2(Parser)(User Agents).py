import sys


def main():
    os_dict = {'Windows': 0, 'Ubuntu': 0, 'OS X': 0, 'Unknown': 0}

    for line in sys.stdin.readlines():
        pos = line.rfind('"', 0, -3)
        if line.find('Windows', pos) != -1:
            os_dict['Windows'] += 1
        elif line.find('Ubuntu', pos) != -1:
            os_dict['Ubuntu'] += 1
        elif line.find('Macintosh', pos) != -1:
            os_dict['OS X'] += 1
        else:
            os_dict['Unknown'] += 1
    for os, num in sorted(os_dict.items(), key=lambda x: x[1]):
        print(os, ': ', num, sep='')

main()
