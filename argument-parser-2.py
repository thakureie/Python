import argparse,os,sys

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
group.add_argument("-u", "--uptime", action="store_true")
parser.add_argument("x", nargs='?',type=int, help="the base")
parser.add_argument("y", nargs='?',type=int, help="the exponent")
parser.add_argument("z", nargs='?', type=str, help="The Uptime of system")
args = parser.parse_args()
#answer = args.x**args.y
#z = args.x+args.y

if args.quiet:
    answer = args.x**args.y
    print(answer)
    os.system('uname -a')
elif args.verbose:
    answer = args.x**args.y
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
    os.system('uptime')
    A = os.sys.platform
    print(A)
elif args.uptime:
    os.system("uptime")
else:
    answer = args.x**args.y
    print("{}^{} == {}".format(args.x, args.y, answer))
