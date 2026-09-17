#!/usr/bin/env python3
"""
Glass Horizon — generative art piece.

Renders a layered, semi-transparent "horizon" made of overlapping arcs and
triangular shards, evoking sunlight refracted through broken glass over a
skyline. Deterministic given a seed, so the same seed always reproduces the
same artwork.

Usage:
    python3 generate_art.py --seed 42 --out artwork.svg
"""
from __future__ import annotations

import argparse
import math
import random

WIDTH = 1200
HEIGHT = 800

PALETTE = [
    "#0b1d3a",  # deep night blue (background)
    "#ff8c42",  # amber sun
    "#ffd166",  # warm gold
    "#06d6a0",  # glass teal
    "#118ab2",  # cool blue
    "#ef476f",  # accent rose
]


def shard_polygon(rng: random.Random, cx: float, cy: float, size: float) -> str:
    """Return an SVG points string for a jagged glass shard around (cx, cy)."""
    points = []
    n = rng.randint(4, 6)
    for i in range(n):
        angle = (2 * math.pi * i / n) + rng.uniform(-0.2, 0.2)
        r = size * rng.uniform(0.6, 1.0)
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        points.append(f"{x:.1f},{y:.1f}")
    return " ".join(points)


def build_svg(seed: int) -> str:
    rng = random.Random(seed)
    parts: list[str] = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" '
        f'viewBox="0 0 {WIDTH} {HEIGHT}">'
    )
    parts.append(f'<rect width="{WIDTH}" height="{HEIGHT}" fill="{PALETTE[0]}"/>')

    # Horizon glow: concentric translucent arcs near the bottom third.
    horizon_y = HEIGHT * 0.68
    for i in range(24, 0, -1):
        radius = i * 22
        color = rng.choice(PALETTE[1:3])
        opacity = 0.03 + (24 - i) * 0.01
        parts.append(
            f'<circle cx="{WIDTH/2:.1f}" cy="{horizon_y:.1f}" r="{radius}" '
            f'fill="{color}" fill-opacity="{opacity:.3f}"/>'
        )

    # Skyline silhouette.
    x = 0.0
    skyline = ['<path d="M0,{h}'.format(h=HEIGHT)]
    while x < WIDTH:
        building_w = rng.uniform(40, 110)
        building_h = rng.uniform(80, 260)
        top_y = horizon_y - building_h
        skyline.append(f" L{x:.1f},{top_y:.1f} L{x + building_w:.1f},{top_y:.1f}")
        x += building_w
    skyline.append(f" L{WIDTH},{HEIGHT} Z\"")
    parts.append(
        "".join(skyline) + f' fill="#04122a" fill-opacity="0.85"/>'
    )

    # Scattered glass shards catching light across the upper two-thirds.
    for _ in range(60):
        cx = rng.uniform(0, WIDTH)
        cy = rng.uniform(0, horizon_y)
        size = rng.uniform(10, 70)
        color = rng.choice(PALETTE[1:])
        opacity = rng.uniform(0.08, 0.35)
        pts = shard_polygon(rng, cx, cy, size)
        rotation = rng.uniform(0, 360)
        parts.append(
            f'<polygon points="{pts}" fill="{color}" fill-opacity="{opacity:.3f}" '
            f'transform="rotate({rotation:.1f} {cx:.1f} {cy:.1f})"/>'
        )

    parts.append("</svg>")
    return "\n".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the Glass Horizon artwork.")
    parser.add_argument("--seed", type=int, default=42, help="Random seed (deterministic).")
    parser.add_argument("--out", type=str, default="artwork.svg", help="Output SVG path.")
    args = parser.parse_args()

    svg = build_svg(args.seed)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Wrote {args.out} (seed={args.seed})")


if __name__ == "__main__":
    main()
