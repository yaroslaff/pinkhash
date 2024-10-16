# Pink Hash

*It's like a pink elephant, but a hash*

Convert hashes to mnemonic phrases.

Hashes are great for many machine-specific purposes, but if you give a hash to a person (e.g., display it on a console), you're doing something wrong. Humans struggle with remembering, comparing, or typing hashes accurately. For most people, `8f776debaf8b5031643aa463ba5bf0dc` and `8f776debaf8b5013643aa463ba5bf0dc` look essentially the same.

However, humans aren’t entirely useless — they can remember vivid phrases quite well. If you tell someone not to think about a pink elephant (or a white monkey), and then Margot Robbie calls to ask them out on a date, even after spending the entire evening and night with her, they’ll still be thinking about the pink elephant.

If a hash is converted into words, people will remember it much better:
- `alter print drive` *// bip39 with `en` option by default, but we have `fr`, `es`, `pt`, `it`, `ko`, `cz`, `zh-hant` and `zh-hans` as well*
- `WELL LANE HELD` *// rfc1751*
- `configurational candidate` *// eng1*
- `Uniform X-ray November` *// nato*


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

# or in French...
$ echo "Hello world!" | pink  -o fr
agacer offrir déposer

# Nato alphabet, 5 words
$ echo "Hello world!" | pink  -l nato -w 5
Lima Quebec Whiskey Xray Sierra

# eng1 always returns 2 words, no matter how many we ask
$ echo "Hello world!" | pink  -l eng1 -w 42
peripatetic viola
~~~

How to get pinkhash for files:
~~~shell
# pink can hash many files
$ pink *txt
cookies.txt: pelican number item
DNS.txt: shadow expire inhale
log.txt: absurd now caution
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
Each method to convert hash into words in Pinkhash is called an *language*. For example, `nato` is one language and `rfc1751` is another language. Do not confuse this with a national language. Pinkhash now has built-in `eng1` language (which produces adjective+noun pair from large set of english words) but in future there could be another *english* language, e.g. one which uses only simple popular words, or one which builds longer phrases or one which produces poems or haiku. 

Usually (but not always) language can produce hashes of specified (`-w`) number of words, but `eng1` never produces more then 2 words. Also pinkhash will not produce more words then needed to cover only lower 64bits of sha1 hash of input.

`BIP-39` language (based on [BIP-0039](https://github.com/bitcoin/bips/tree/master/bip-0039)) has 10 *options* (wordlists), choose it with `-o`. See all options with `-h`/`--help`.

## Disclaimer
While pinkhash uses `RFC1751` and `BIP-0039`, it's not strictly following it! Pinkhash has it's own algorithms and just uses wordlists from these standards. Do not use pinkhash where you need strict standard compliance.

Mnemonical pink hashes are NOT cryptographically strong.

## Contributions
Contributions are welcome! Write me to yaroslaff / gmail.com to discuss or make a ticket and/or PR.
