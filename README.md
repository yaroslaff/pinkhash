# Pink Hash

*It's like a pink elephant, but a hash*

Convert hashes to mnemonic phrases.

Hashes are great for many machine-specific purposes, but if you give a hash to a person (e.g., display it on a console), you're doing something wrong. Humans struggle with remembering, comparing, or typing hashes accurately. For most people, `8f776debaf8b5031643aa463ba5bf0dc` and `8f776debaf8b5013643aa463ba5bf0dc` look essentially the same.

However, humans aren’t entirely useless — they can remember vivid phrases quite well. If you tell someone not to think about a pink elephant or a white monkey, and then Margot Robbie calls to ask them out on a date, even after spending the entire evening and night with her, they’ll still be thinking about the pink elephant.

`WELL LANE HELD` or `Uniform Xray November` is much easier for numan to remember.


## Examples
~~~shell
$ echo -n pinkhash | md5sum
8f776debaf8b5031643aa463ba5bf0dc  -

$ echo -n pinkhash | pink -a nato
Uniform Xray November

$ echo -n pinkhash | pink
WELL LANE HELD
~~~

## Installation

recommended way (you may want to `apt install pipx` for this):
~~~
pipx install pinkhash
~~~

or older way:
~~~
pip install pinkhash
~~~

## CLI Usage
~~~shell
# get pink hash for any file as stdin stream
$ pink < /tmp/1M

# get 5-words pink hash with NATO alphabet
$ pink -a nato -w 5 < /tmp/1M 
Hotel Yankee Zulu Papa Hotel
~~~

## Python usage

Get pinkhash for a `str` with all default settings (RFC1751 alphabet).
~~~python
from pinkhash import PinkHash
pink = PinkHash()
print(pink.convert('Hello world!'))
~~~

~~~python
from pinkhash import PinkHash
import sys

pink = PinkHash(alphabet_name='nato', nwords=3)
data = sys.stdin.buffer.read()
r = pink.convert(data)
print(r)
~~~

