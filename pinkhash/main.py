import argparse
import sys

from . import __version__
from . import PinkHash
from .lang import language_mgr

def get_args():
    parser = argparse.ArgumentParser(
        description=f'PinkHash version {__version__}. Convert data to memorable strings',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.epilog = 'Available languages (-a) are:\n'
    for lang in language_mgr.languages.values():
        parser.epilog += f'  {lang.name}: {lang.description}\n'

    parser.add_argument('-l', '--lang', metavar='LANG', type=str, 
                        help=f'One of: {" ".join(language_mgr.languages.keys())}')
    parser.add_argument('-o', '--option', metavar='OPTION', type=str, 
                        help=f'Option of pinkhash language (for bip39)')
    parser.add_argument('-w', '--words', metavar='N_WORDS', type=int, default=3, help='Pink-hash lenght in words')
    parser.add_argument('FILE',  nargs='*', help='Files to hash')

    g = parser.add_argument_group('Hashing inbound data')

    args = parser.parse_args()
    return args

def main():
    args = get_args()

    pink = PinkHash(language_name=args.lang, option=args.option, nwords=args.words)

    if args.FILE:
        for path in args.FILE:
            with open(path, 'rb') as f:
                data = f.read()
                r = pink.convert(data)
                print(f'{path}: {r}')
    else:
        data = sys.stdin.buffer.read()
        r = pink.convert(data)
        print(r)
