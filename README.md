# Pink Hash

*It's like a pink elephant, but a hash*

Convert hashes to mnemonic phrases.

Hashes are great for many machine-specific purposes, but if you give a hash to a person (e.g., display it on a console), you're doing something wrong. Humans struggle with remembering, comparing, or typing hashes accurately. For most people, `8f776debaf8b5031643aa463ba5bf0dc` and `8f776debaf8b5013643aa463ba5bf0dc` look essentially the same.

However, humans aren’t entirely useless — they can remember vivid phrases quite well. If you tell someone not to think about a pink elephant (or a white monkey), and then Margot Robbie calls to ask them out on a date, even after spending the entire evening and night with her, they’ll still be thinking about the pink elephant.

If a hash is converted into words, people will remember it much better:
- *alter print drive* (`bip39`, `en` option by default, but we have `fr`, `es`, `pt`, `it`, `ko`, `cz`, `zh-hant` and `zh-hans` as well)
- *WELL LANE HELD* (`rfc1751`)
- *configurational candidate* (`eng1`)
- *Uniform X-ray November* (`nato`)


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
# get pink hash for stdin, default mode with bip39/en
$ echo "Hello world!" | pink 
alter print drive

# get pink hash for any file as stdin stream
$ pink < /tmp/1M
spot slogan tomato

# get 5-words pink hash with specific language: NATO/ICAO alphabet
$ pink -l nato -w 5 < /tmp/1M 
Hotel Yankee Zulu Papa Hotel

# eng1 never returns more then 2 words
$ pink -l eng1  < /tmp/1M 
paraboloidal teapot

# pink can hash many files as well
$ pink ~/*txt
/home/xenon/cookies.txt: pelican number item
/home/xenon/DNS.txt: shadow expire inhale
/home/xenon/log.txt: absurd now caution
~~~

## Python usage

Get pinkhash for a `str` with all default settings (Bip39 language as default).
~~~python
from pinkhash import PinkHash
pink = PinkHash()
print(pink.convert('Hello world!'))
~~~

~~~python
from pinkhash import PinkHash
import sys

pink = PinkHash(language_name='nato', nwords=3)
data = sys.stdin.buffer.read()
r = pink.convert(data)
print(r)
~~~

## Languages
Each method to convert hash into words in Pinkhash is called an *language*. For example, `nato` is one language and `rfc1751` is another language. Do not confuse this with a national language. Pinkhash now has built-in `eng1` language (which produces adjective+noun pair from large set of english words) but there could be another *english* language, e.g. one which uses only simple popular words, or one which builds longer phrases or one which produces poems or haiku. 

Usually (but not always) language can produce hashes of specified (`-w`) number of words, but `eng1` never produces more then 2 words.

## Contributions
Contributions are welcome! Write me to yaroslaff / gmail.com to discuss or make a ticket and/or PR.
