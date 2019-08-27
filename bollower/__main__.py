from collections import defaultdict
from csv import DictReader
from random import choice
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', type=argparse.FileType('r'), default='-')
    parser.add_argument('--sentence')
    parser.add_argument('--n', type=int, default=3)

    args = parser.parse_args()
    reader = DictReader(args.csv)

    columns = defaultdict(list)
    for row in reader:
        for (k,v) in row.items():
            if v:
                columns[k].append(v)

    print(columns.keys())

    for n in range(args.n):
        s = args.sentence
        for k in columns.keys():
            s = s.replace(k, choice(columns[k]))

        print(s)

if __name__ == '__main__':
    main()
