# The GPS That Only Turns Left at Puns

[![Dad Joke Showdown](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![Rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/nemesisbug/gps-dad-joke/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5/leaderboard)
[![Reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/nemesisbug/gps-dad-joke/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

Entry for the [Dad Joke Showdown](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5) on make.fun.

## The joke

> I asked my GPS to tell me a joke. It said, 'Turn left at the next pun — you've been driving straight for years.'

A GPS that navigates by wordplay: it can only turn left at puns, and
it has been driving straight for years. The setup is a straight-faced
question, the punchline turns on "pun" and "straight" at once, and it
reads out loud the way a dad would say it across the dinner table.

## How it works

`main.py` (Python 3.13, standard library only) writes the joke to
`/output/entry.txt` — 112 characters, inside the 1–200 character gate,
and refuses to write anything outside the gate. Verified locally:
`/output/entry.txt` holds exactly the joke above, no trailing newline.

Run it locally:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
