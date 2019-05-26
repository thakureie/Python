import argparse
parentparser = argparse.ArgumentParser(add_help=False)
parentparser.add_argument('--user' , action="store")
parentparser.add_argument('--password' , action="store")

parser = argparse.ArgumentParser(parents=[parentparser])
parser.add_argument('--local-arg', action="store_true", default=False)
parser.parse_args()
