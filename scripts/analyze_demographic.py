import csv
import sys
from collections import Counter


def gender_distribution(rows):
    counts = Counter(row['GENDER'] for row in rows if row['GENDER'])
    total = sum(counts.values())
    return {k: (v, v / total * 100) for k, v in counts.items()}


def age_distribution(rows):
    bins = [0, 20, 30, 40, 50, 60, 100]
    labels = ['<20', '20-29', '30-39', '40-49', '50-59', '60+']
    counts = Counter({label: 0 for label in labels})
    total = 0
    for row in rows:
        birth = row['BIRTHDAY']
        if birth.isdigit():
            age = 2025 - int(birth)
            total += 1
            for i in range(len(bins) - 1):
                if bins[i] <= age < bins[i + 1]:
                    counts[labels[i]] += 1
                    break
    return {k: (v, v / total * 100) for k, v in counts.items()}


def read_rows(path):
    with open(path, encoding='utf-8') as f:
        return list(csv.DictReader(f))


def main(argv):
    path = argv[1] if len(argv) > 1 else 'demographic_clean.csv'
    rows = read_rows(path)
    g = gender_distribution(rows)
    a = age_distribution(rows)
    print('Gender Distribution:')
    for gender, (count, pct) in g.items():
        print(f'  {gender}: {count} ({pct:.2f}%)')
    print('\nAge Distribution:')
    for label, (count, pct) in a.items():
        print(f'  {label}: {count} ({pct:.2f}%)')


if __name__ == '__main__':
    main(sys.argv)
