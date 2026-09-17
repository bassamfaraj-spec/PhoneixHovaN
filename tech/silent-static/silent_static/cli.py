"""Command-line interface for Silent Static."""
from __future__ import annotations

import argparse
import sys

from .generator import DOMAINS, generate_brief


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="silent-static",
        description="Generate randomized creative project codenames and briefs.",
    )
    parser.add_argument(
        "domain",
        nargs="?",
        choices=DOMAINS,
        help="Creative domain. If omitted, one brief per domain is printed.",
    )
    parser.add_argument(
        "--seed", type=int, default=None,
        help="Seed for reproducible output.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    domains = [args.domain] if args.domain else list(DOMAINS)
    for i, domain in enumerate(domains):
        seed = None if args.seed is None else args.seed + i
        brief = generate_brief(domain, seed=seed)
        print(brief)
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
