import re

#
# Complete the 'maxValue' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING t as parameter.
#

occurrences_dict = {}


def count_occurrences(s, t):
    return len(s) * len(re.findall(f'(?={s})', t))


def max_value(t):
    maximum = -1
    visited = {}
    for i in range(1, len(t) + 1):
        for j in range(len(t) - i + 1):
            ss = t[j: j+i]
            if ss in visited:
                continue
            local_max = count_occurrences(ss, t)
            visited[ss] = True
            maximum = max(maximum, local_max)
    return maximum


if __name__ == '__main__':
    print(max_value("abcdabcdddaddd"))
