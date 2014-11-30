import argparse
from read import read

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="subparser_name")
    add_parser = subparser.add_parser('add')
    add_parser.add_argument("-p", "--pmid", dest="pmid", required=1, help="pmid")
    args = parser.parse_args()
    print read(args.pmid)
