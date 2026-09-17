# PhoneixHovaN — Multi-Domain Creative Portfolio

An original body of creative and technical work spanning music, film, visual
art, technology, and sports. Every project ships under a randomized working
codename and the same permissive license, so anything here is free to use,
remix, perform, build on, and redistribute.

## Projects

| Domain | Codename | What it is |
|---|---|---|
| 🎵 Music | [Neon Echo](/Users/bassamfaraj/PhoneixHovaN-1/music/neon-echo) | Original synthwave/alt-pop song: full lyrics, chords, and production notes. |
| 🎬 Film | [Copper Comet](/Users/bassamfaraj/PhoneixHovaN-1/film/copper-comet) | Original ~9-minute short-film screenplay. |
| 🎨 Art | [Glass Horizon](/Users/bassamfaraj/PhoneixHovaN-1/art/glass-horizon) | Generative art piece (Python script rendering seeded SVG artworks). |
| 💻 Tech | [Silent Static](/Users/bassamfaraj/PhoneixHovaN-1/tech/silent-static) | A working, tested CLI that generates randomized codenames + creative briefs across all five domains. |
| 🏅 Sports | [Wild Marathon](/Users/bassamfaraj/PhoneixHovaN-1/sports/wild-marathon) | An original invented team sport with a full rulebook. |

Each project folder has its own `README.md` with details, and its own
primary content file (song, script, art generator, code, or rulebook).

## License

This project is licensed under the MIT License. See
[LICENSE](/Users/bassamfaraj/PhoneixHovaN-1/LICENSE). The MIT license covers
**every** project in this repository — music, film, art, code, and sport
rules alike.

## Distribution

You may use, modify, perform, remix, and distribute anything in this
repository under the terms of the MIT License. See
[DISTRIBUTION.md](/Users/bassamfaraj/PhoneixHovaN-1/DISTRIBUTION.md) for
domain-specific notes on how to credit and release each type of work.
When redistributing, include the copyright and license notice from the
license file.

## Generating more ideas

Want a new randomized project name and brief in any of these five domains?
```bash
cd tech/silent-static
python3 -m silent_static.cli          # one brief per domain
python3 -m silent_static.cli music --seed 123   # a specific domain, reproducible
```
