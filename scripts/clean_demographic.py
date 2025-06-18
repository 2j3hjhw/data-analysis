import csv
import sys
from pathlib import Path


def clean_demographic(input_path: str, output_path: str) -> None:
    """Clean demographic CSV and write result to `output_path`."""
    with open(input_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        if fieldnames is None:
            raise ValueError("Input file has no header")
        seen = set()
        with open(output_path, 'w', newline='', encoding='utf-8') as out:
            writer = csv.DictWriter(out, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                uid = row.get('USERID')
                if uid in seen:
                    continue  # drop duplicate USERID
                seen.add(uid)
                cleaned = {}
                for k, v in row.items():
                    if isinstance(v, str):
                        v = v.replace('\n', ' ').replace('\r', ' ')
                        if v.strip().lower() == 'unknown':
                            v = ''
                    cleaned[k] = v
                writer.writerow(cleaned)


def main(argv: list[str]) -> None:
    input_path = argv[1] if len(argv) > 1 else 'demographic.csv'
    output_path = argv[2] if len(argv) > 2 else 'demographic_clean.csv'
    clean_demographic(input_path, output_path)


if __name__ == '__main__':
    main(sys.argv)
