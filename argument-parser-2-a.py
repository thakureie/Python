#!/usr/bin/python
import argparse
parser = argparse.ArgumentParser(description="Calculate X to the Y exponent")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v" , "--vervbose" , action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x"  , type=int, help="The base")
parser.add_argument("y", type=int, help="The exponent")
args = parser.parse_args()
answers = args.x**args.y
addition = args.x + args.y


if args.quiet:
	print(answers)
	print("SUM:", addition)
	print("{} plus {} is equal to {} ".format(args.x, args.y, addition))
elif args.vervbose:
	print("{} to the power of {} is euqal to {}".format(args.x, args.y, answers))

else:
	print("{}^{} == {}".format(args.x, args.y, answers))

