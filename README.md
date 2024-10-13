# Pink Hash

*It's like a pink elephant, but a hash*

Convert hashes to mnemonic phrases.

Hashes are great for many machine-specific purposes, but if you give a hash to a person (e.g., display it on a console), you're doing something wrong. Humans struggle with remembering, comparing, or typing hashes accurately. For most people, `8f776debaf8b5031643aa463ba5bf0dc` and `8f776debaf8b5013643aa463ba5bf0dc` look essentially the same.

However, humans aren’t entirely useless — they can remember vivid phrases quite well. If you tell someone not to think about a pink elephant or a white monkey, and then Margot Robbie calls to ask them out on a date, even after spending the entire evening and night with her, they’ll still be thinking about the pink elephant.

`WELL LANE HELD` (rfc1751), `configurational candidate` (eng1) or `Uniform Xray November` (nato) is much easier for numan to remember.

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

# eng1 never returns more then 2 words
$ pink -a eng1  < /tmp/1M 
paraboloidal teapot

# can hash files
$ pink ~/*txt
/home/xenon/cookies.txt: JOEL HESS DRAW
/home/xenon/DNS.txt: NOAH BABY DIRE
/home/xenon/log.txt: AID HERO LIE
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

## Languages
Each method to convert hash into words in Pinkhash is called an *language*. For example, `nato` is one language and `rfc1751` is another language. Do not confuse this with national language. Pinkhash now has built-in `eng1` language (which produces adjective+noun pair from large set of english words) but there could be another *english* language, e.g. one which uses only simple popular words or one which produces poems or haiku.

## Contributions
Contributions are welcome! Write me to yaroslaff / gmail.com to discuss or make a ticket and/or PR.
