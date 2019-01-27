#!/usr/bin/python
import argparse
parser = argparse.ArgumentParser(description="Sum The ineteger at command line")
parser.add_argument('integers', nargs='+', type = int, help = "an integer to summed")
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help="sum the integers(default: Find the max)")
args = parser.parse_args()
print(args.accumulate(args.integers))
