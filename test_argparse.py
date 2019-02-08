import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--head', dest='head')
parser.add_argument('--tail', dest='tail')
parser.set_defaults(head=None, tail=None)

args = parser.parse_args()
print args.head, args.tail
