import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest

from silent_static.generator import DOMAINS, generate_brief, generate_codename
from silent_static.cli import main


def test_generate_codename_format():
    codename = generate_codename()
    parts = codename.split(" ")
    assert len(parts) == 2
    assert all(part.isalpha() for part in parts)


def test_generate_brief_all_domains():
    for domain in DOMAINS:
        brief = generate_brief(domain, seed=1)
        assert brief.domain == domain
        assert brief.codename
        assert brief.prompt
        assert "{" not in brief.prompt  # template fully substituted


def test_generate_brief_deterministic_with_seed():
    a = generate_brief("music", seed=42)
    b = generate_brief("music", seed=42)
    assert a == b


def test_generate_brief_varies_across_distinct_seeds():
    # Same seed always yields the same codename regardless of domain (the
    # RNG is seeded fresh each call), so distinct seeds are required for
    # distinct output -- this mirrors how the CLI offsets the seed per
    # domain when generating one brief per domain.
    briefs = {generate_brief(d, seed=99 + i).codename for i, d in enumerate(DOMAINS)}
    assert len(briefs) >= 3


def test_generate_brief_unknown_domain_raises():
    with pytest.raises(ValueError):
        generate_brief("cooking", seed=1)


def test_cli_single_domain(capsys):
    exit_code = main(["tech", "--seed", "7"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "[TECH]" in captured.out


def test_cli_all_domains(capsys):
    exit_code = main(["--seed", "1"])
    captured = capsys.readouterr()
    lines = [line for line in captured.out.strip().splitlines() if line]
    assert exit_code == 0
    assert len(lines) == len(DOMAINS)
