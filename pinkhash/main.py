import argparse
import sys

from . import __version__
from . import PinkHash
from .alphabet import alphabet_mgr

def get_args():
    parser = argparse.ArgumentParser(
        description=f'PinkHash version {__version__}. Convert data to memorable strings',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.epilog = 'Available alphabets (-a) are:\n'
    for ab in alphabet_mgr.alphabets.values():
        parser.epilog += f'  {ab.name}: {ab.description}\n'

    parser.add_argument('-a', '--alphabet', metavar='Alphabet', type=str, 
                        help=f'One of: {" ".join(alphabet_mgr.alphabets.keys())}')
    parser.add_argument('-w', '--words', metavar='N_WORDS', type=int, default=3, help='Pink-hash lenght in words')

    g = parser.add_argument_group('Hashing inbound data')

    args = parser.parse_args()
    return args

def main():
    args = get_args()

    pink = PinkHash(alphabet_name=args.alphabet, nwords=args.words)

    data = sys.stdin.buffer.read()

    r = pink.convert(data)
    print(r)

    print()
