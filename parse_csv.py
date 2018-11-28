#!/usr/bin/python
import sys, codecs, csv, json


def parse_csv(filename):
  # Read the passed csv file into a list of objects.

  for encoding in 'utf-8', "ISO-8859-1":
    try:
      with open(filename, encoding=encoding) as f:
        reader = csv.reader(f, delimiter=',', quotechar='"', skipinitialspace=True)
        rows = [row for row in reader]
    except UnicodeDecodeError:
      pass
  dicts = []
  if rows:
    keys = rows[0]
    keys = [key.strip().lower().replace(' ', '_') for key in keys]
    for row in rows[1:]:
      d = {}
      dicts.append(d)
      for key, val in zip(keys, row):
        d[key] = val
  return dicts

path = sys.argv[1]
rows = parse_csv(path)
print(rows)
