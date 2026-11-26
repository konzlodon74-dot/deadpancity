# deadpancity
[![make.fun](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/konzlodon74-dot/deadpancity/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/konzlodon74-dot/deadpancity/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
Bounty: https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c

> Tomorrow in New Brindlewick: 18°C, drizzle until noon, wind 12 knots, then the fog lifts just enough to confirm it never really left.

## How it works
`main.py` holds the forecast in a `SENTENCE` constant and asserts it is non-blank, unpadded, single-line, and within the character limit. It then creates `/output` if needed and writes the sentence as UTF-8 bytes with no trailing newline to `/output/entry.txt`.

## Run
```bash
python3 main.py
```
