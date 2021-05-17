# W2NVShellMessage
A quote from Welcome to Night Vale to show when bash is launched.


# TODO
- write `init` arg to buid `conf` file, show current values
- write `fetch` method for first time run or if `conf` changed
- `fetch`: Download transcripts from [here](https://nightvale.fandom.com/wiki/Category:Year_1_transcripts) according to `conf`, add to list, pickle the list.
- if run without args, pickle load list, print random item from list.