"""For logs"""
import re
from collections import Counter
import json
from fileinput import FileInput

ACCESSLOG = '/home/yury/PycharmProjects/selenium_otus/otus_log/access.log'
ACCESSLOG2 = '/home/yury/PycharmProjects/selenium_otus/otus_log/access2.log'
MERGELOG = '/home/yury/PycharmProjects/selenium_otus/otus_log/access3.log'


def read_log(filename):
    """Read logs"""
    # merge two files for parsing
    if filename == MERGELOG:
        merge_log()
    # one file for parsing
    else:
        pass

    regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    with open(filename) as fo:
        log = fo.read()
        ip_list = re.findall(regexp, log)
    return ip_list


def merge_log():
    """Merge files"""
    with FileInput([ACCESSLOG, ACCESSLOG2]) as input_lines:
        with open(MERGELOG, 'w') as output_file:
            output_file.writelines(input_lines)


def count_ip(ip_list, summ=0):
    """Count ip"""
    count = Counter(ip_list)
    for i in count:
        summ += count[i]
    summ = ['The total number of requests is equal to', summ]
    list_count = list(count.items())
    list_count.sort(key=lambda ik: ik[1], reverse=True)
    max_list_ip = []
    for n in range(0, 10):
        max_list_ip.append(list_count[n])
    max_list_ip = ['Top 10 IP:', max_list_ip]
    return summ, max_list_ip


if __name__ == '__main__':
    res = count_ip(read_log(ACCESSLOG2))
    print(res)
    with open('res.json', 'w') as f:
        json.dump(res, f)
