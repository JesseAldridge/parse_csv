#!/usr/local/bin/python3
import sys, codecs, csv, json, argparse


def csv_to_dicts(filename):
  rows = csv_to_rows(filename)
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

def csv_to_rows(filename):
  for encoding in 'utf-8', "ISO-8859-1":
    try:
      with open(filename, encoding=encoding) as f:
        reader = csv.reader(f, delimiter=',', quotechar='"', skipinitialspace=True)
        rows = [row for row in reader]
    except UnicodeDecodeError:
      pass
  return rows

parser = argparse.ArgumentParser()
parser.add_argument('--file', dest='path')
parser.add_argument('--head', dest='head', type=int)
parser.add_argument('--tail', dest='tail', type=int)
parser.set_defaults(head=None, tail=None)

args = parser.parse_args()

rows = csv_to_rows(args.path)
column_labels = rows[0]
rows = rows[1:]
if args.head:
  rows = rows[:args.head]
if args.tail:
  rows = rows[-args.tail:]

with open('out.csv', 'w') as f:
  writer = csv.writer(f, lineterminator='\n')
  writer.writerow(column_labels)
  for row in rows:
    writer.writerow(row)
