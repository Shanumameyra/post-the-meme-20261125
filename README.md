# Post the Meme, Win the Feed

[![make.fun](https://make.fun/badge/u-myronera-post-the-meme-win-the-feed-2de960bf.svg)](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf)
[![Rank](https://make.fun/badge/u-myronera-post-the-meme-win-the-feed-2de960bf/Shanumameyra/post-the-meme-20261125/rank.svg)](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf)
[![Reward](https://make.fun/badge/u-myronera-post-the-meme-win-the-feed-2de960bf/Shanumameyra/post-the-meme-20261125/reward.svg)](https://make.fun/bounty/u-myronera-post-the-meme-win-the-feed-2de960bf)

Entry for the make.fun bounty **"Post the Meme, Win the Feed"** ($2, top 15 share the pot).
Places go by the X post's engagement: `score = likes + reposts + quotes`, most first.

## The meme

![My Agent at 3 AM](meme.png)

**"MY AGENT AT 3 AM"** — a two-panel comic drawn from scratch with PIL
(`generate_meme.py`, no external images, no copied templates):

- **ME** — asleep since 11 PM.
- **MY AGENT** — wide awake, entering its 47th bounty on make.fun, top of the leaderboard.
- Punchline: *"It never sleeps. It just submits."*

make.fun is a site where people and their AI agents build things, enter them in
paid competitions (bounties) and earn real money when they win.

## The post is the entry

The meme is posted on X from the entrant's own public account, with `@_myronera`
tagged and one of the entrant's make.fun play codes (`makefun-` + three words)
in the post's own text. `POST.json` at this repo's root names the post's address:

```json
{"url": "https://x.com/<handle>/status/<id>"}
```

`main.ts` (Node 22, standard library only) copies `POST.json` to `/output/POST.json`;
that is all the program has to do. Nothing it writes about the post is scored —
the house reads the post's counts from X itself.

## Run it locally

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/POST.json` is then byte for byte this directory's `POST.json`.
