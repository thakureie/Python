import argparse

argparse_parent_base = argparse.ArgumentParser(add_help=False)

argparse_parent_base.add_argument('--user', action="store")
argparse_parent_base.add_argument('--password', action="store")
parser = argparse.ArgumentParser(parents=[argparse_parent_base])

parser.add_argument('--local-arg',
                    action="store_true",
                    default=False)

print(parser.parse_args())
