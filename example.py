from pinkhash import PinkHash, PinkHashError
import sys

try:
    pink = PinkHash(language_name="bip39", option="en", nwords=3)
except PinkHashError as e:
    print(e, file=sys.stderr)
    sys.exit(1)

data = sys.stdin.buffer.read()
r = pink.convert(data)
print(r)
