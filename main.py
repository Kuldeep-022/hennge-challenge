import sys

def calculate_sum(ys):
    if not ys:
        return 0
    y = ys[0]
    power = 0 if y > 0 else y ** 4
    return power + calculate_sum(ys[1:])

def parse_ints(strs, acc):
    if not strs:
        return acc
    acc.append(int(strs[0]))
    return parse_ints(strs[1:], acc)

def process_test_case():
    x_line = sys.stdin.readline().strip()
    if not x_line:
        return False
    x = int(x_line)
    ys_line = sys.stdin.readline().strip()
    if not ys_line:
        return False
    ys_strs = ys_line.split()
    ys = parse_ints(ys_strs, [])
    if len(ys) != x:
        print(-1)
    else:
        sum_val = calculate_sum(ys)
        print(sum_val)
    return True

def process_cases(n):
    if n <= 0:
        return
    if not process_test_case():
        return
    process_cases(n - 1)

def main():
    first_line = sys.stdin.readline().strip()
    if not first_line:
        return
    n = int(first_line)
    process_cases(n)

if __name__ == "__main__":
    main()