import pandas as pd
import sys, argparse
import csv


#def main(argv):
delimiter_bool = False
parser = argparse.ArgumentParser()
parser.add_argument("--in-delimiter", action='store', dest='in_delimiter', required=False)
parser.add_argument("--in-quote", dest='in_quote', required=False)

namespace, extra = parser.parse_known_args()
#inpprint(namespace)

if len(extra) != 2:
    parser.print_help()
    sys.exit(2)
input_file = extra[0]
output_file = extra[1]

#if namespace.in_delimiter:
#    print(namespace.in_delimiter)

with open(input_file, 'r') as f:
    if not namespace.in_quote:
        namespace.in_quote = csv.Sniffer().sniff(f.read(1024)).quotechar
        #print(namespace.in_quote)
        f.seek(0)
    if not namespace.in_delimiter:
        #print(namespace.in_delimiter)
        namespace.in_delimiter = csv.Sniffer().sniff(f.read(1024)).delimiter
        f.seek(0)
    f.close()

if not namespace.in_quote: namespace.in_quote = '"'
if not namespace.in_delimiter: namespace.in_delimiter = "|"

df = pd.read_csv(input_file, delimiter=namespace.in_delimiter, quotechar=namespace.in_quote, dtype=str)
df.to_csv(output_file, index=False)
