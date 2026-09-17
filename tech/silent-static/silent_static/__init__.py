"""Silent Static — a deterministic creative-prompt generator.

Given a domain (music, film, art, tech, sports) and an optional seed, it
produces a randomized project codename plus a short creative brief. Used to
kick off new work across the PhoneixHovaN portfolio without ever staring at
a blank page.
"""

from .generator import DOMAINS, generate_brief, generate_codename

__all__ = ["DOMAINS", "generate_brief", "generate_codename"]
__version__ = "0.1.0"
