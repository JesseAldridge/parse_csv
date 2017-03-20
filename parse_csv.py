#!/usr/bin/python
import sys, codecs, csv, json


def parse_csv(filename):
  # Read the passed csv file into a list of objects.

  with codecs.open(filename, encoding='utf-8') as f:
    reader = csv.reader(utf_8_encoder(f), delimiter=',', quotechar='"', skipinitialspace=True)
    rows = [row for row in reader]
  dicts = []
  if rows:
    keys = rows[0]
    keys = [key.strip().lower().replace(' ', '_') for key in keys]
    for row in rows[1:]:
      d = {}
      dicts.append(d)
      for key, val in zip(keys, row):
        d[key] = val.decode('utf8')
  return dicts

def utf_8_encoder(f):
    for line in f:
      yield line.encode('utf-8')

if __name__ == '__main__':
  path = '/Users/Jesse/Desktop/Daily Log - Sheet1.csv'
  print json.dumps(parse_csv(path), indent=2)
  # print json.dumps(parse_csv(sys.argv[1]), indent=2)
