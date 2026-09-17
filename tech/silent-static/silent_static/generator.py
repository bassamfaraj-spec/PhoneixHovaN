"""Core generation logic for Silent Static."""
from __future__ import annotations

import random
from dataclasses import dataclass

ADJECTIVES = [
    "Velvet", "Amber", "Obsidian", "Glass", "Neon", "Crimson", "Lunar",
    "Rogue", "Silent", "Copper", "Fractal", "Wild", "Hollow", "Radiant",
    "Feral", "Iron", "Paper", "Static", "Violet", "Solar",
]

NOUNS = [
    "Comet", "Recursion", "Bloom", "Marathon", "Orchard", "Static", "Horizon",
    "Cipher", "Ember", "Tide", "Echo", "Vault", "Signal", "Garden", "Engine",
    "Compass", "Lantern", "Current", "Anthem", "Drift",
]

DOMAINS = ("music", "film", "art", "tech", "sports")

_PROMPTS: dict[str, list[str]] = {
    "music": [
        "Write a {tempo} BPM {genre} track about {theme}.",
        "Compose a one-minute instrumental interlude built entirely around {theme}.",
        "Write lyrics for a duet where two voices disagree about {theme}.",
    ],
    "film": [
        "Write a 5-page short film script about {theme}, single location only.",
        "Pitch a film trilogy where each installment reframes {theme}.",
        "Write a cold open (no dialogue) that visually establishes {theme}.",
    ],
    "art": [
        "Design a generative art series exploring {theme} through color and repetition.",
        "Sketch a triptych: past, present, and future versions of {theme}.",
        "Create a poster series where typography alone conveys {theme}.",
    ],
    "tech": [
        "Prototype a small tool that helps people track {theme}.",
        "Design an API for a service centered on {theme}.",
        "Build a CLI game whose core mechanic is a metaphor for {theme}.",
    ],
    "sports": [
        "Invent a two-team sport whose central rule enforces {theme}.",
        "Design a solo endurance event themed around {theme}.",
        "Create a spectator sport where scoring literally visualizes {theme}.",
    ],
}

_THEMES = [
    "signals that outlast their senders", "borrowed time", "quiet rebellion",
    "the weight of unfinished things", "second chances", "collective memory",
    "the space between strangers", "slow-burning courage", "found light",
    "letting go of control",
]

_GENRES = ["synthwave", "folk", "jazz-fusion", "ambient", "punk", "orchestral pop"]


@dataclass(frozen=True)
class CreativeBrief:
    domain: str
    codename: str
    prompt: str

    def __str__(self) -> str:  # pragma: no cover - trivial formatting
        return f"[{self.domain.upper()}] {self.codename}: {self.prompt}"


def generate_codename(rng: random.Random | None = None) -> str:
    """Return a random two-word codename, e.g. 'Amber Recursion'."""
    rng = rng or random.Random()
    return f"{rng.choice(ADJECTIVES)} {rng.choice(NOUNS)}"


def generate_brief(domain: str, seed: int | None = None) -> CreativeBrief:
    """Generate a full creative brief (codename + prompt) for a domain.

    Deterministic when a seed is provided: the same domain + seed always
    returns the same brief.
    """
    if domain not in DOMAINS:
        raise ValueError(f"Unknown domain {domain!r}. Choose from {DOMAINS}.")

    rng = random.Random(seed)
    codename = generate_codename(rng)
    template = rng.choice(_PROMPTS[domain])
    prompt = template.format(
        theme=rng.choice(_THEMES),
        tempo=rng.choice([90, 100, 108, 120, 128, 140]),
        genre=rng.choice(_GENRES),
    )
    return CreativeBrief(domain=domain, codename=codename, prompt=prompt)
