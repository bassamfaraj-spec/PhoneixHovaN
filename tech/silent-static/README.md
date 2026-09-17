# Silent Static (Tech)

A tiny, dependency-free Python CLI that generates randomized project
codenames and creative briefs across all five domains in this portfolio
(music, film, art, tech, sports). Deterministic when given a `--seed`.

## Usage
```bash
cd tech/silent-static
python3 -m silent_static.cli tech --seed 7
python3 -m silent_static.cli            # one brief per domain
```

## Run tests
```bash
cd tech/silent-static
python3 -m pytest tests/ -v
```

Licensed under the repository's root [LICENSE](../../LICENSE) (MIT) — free
to use, modify, and distribute with attribution.
