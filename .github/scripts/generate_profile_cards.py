from __future__ import annotations

import json
import os
import urllib.request
from collections import Counter
from pathlib import Path
from xml.sax.saxutils import escape

OWNER = os.environ.get("GITHUB_REPOSITORY_OWNER", "YingaoWang-casia")
PROFILE_TOKEN = os.environ.get("PROFILE_STATS_TOKEN", "")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
AUTH_TOKEN = PROFILE_TOKEN or GITHUB_TOKEN
OUT_DIR = Path("profile")
COLORS = {"Python": "#3776ab", "HTML": "#e34c26", "Shell": "#89e051", "PowerShell": "#012456", "Makefile": "#427819", "Jupyter Notebook": "#da5b0b", "JavaScript": "#f1e05a", "TypeScript": "#3178c6", "CSS": "#563d7c", "C++": "#f34b7d", "C": "#555555", "Java": "#b07219", "Go": "#00add8", "Rust": "#dea584", "Markdown": "#083fa1"}


def request_json(url: str):
    headers = {"User-Agent": "profile-card-generator"}
    if AUTH_TOKEN:
        headers["Authorization"] = f"Bearer {AUTH_TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_repos():
    repos, page = [], 1
    if PROFILE_TOKEN:
        base = "https://api.github.com/user/repos?affiliation=owner,collaborator,organization_member&visibility=all&sort=updated"
    else:
        base = f"https://api.github.com/users/{OWNER}/repos?type=all&sort=updated"
    while True:
        batch = request_json(f"{base}&per_page=100&page={page}")
        if not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return repos


def fetch_languages(repos):
    totals = Counter()
    for repo in repos:
        if repo.get("fork"):
            continue
        try:
            totals.update({k: int(v) for k, v in request_json(repo["languages_url"]).items()})
        except Exception:
            pass
    return totals


def write_stats_card(repos):
    rows = [
        ("Total Stars Earned", sum(int(r.get("stargazers_count", 0)) for r in repos)),
        ("Tracked Repositories", len(repos)),
        ("Original Projects", sum(1 for r in repos if not r.get("fork"))),
        ("Repository Forks", sum(int(r.get("forks_count", 0)) for r in repos)),
        ("Private Repositories", sum(1 for r in repos if r.get("private"))),
        ("Forked Repositories", sum(1 for r in repos if r.get("fork"))),
    ]
    row_svg = "".join(
        f'<text x="34" y="{58 + i * 18}" class="label">{escape(k)}:</text><text x="245" y="{58 + i * 18}" class="value">{v}</text>'
        for i, (k, v) in enumerate(rows)
    )
    note = "all accessible repositories" if PROFILE_TOKEN else "public repositories only"
    svg = f'''<svg width="467" height="170" viewBox="0 0 467 170" fill="none" xmlns="http://www.w3.org/2000/svg" role="img">
<style>.title{{font:600 18px 'Segoe UI',Ubuntu,sans-serif;fill:#0891b2}}.label{{font:600 13px 'Segoe UI',Ubuntu,sans-serif;fill:#64748b}}.value{{font:700 13px 'Segoe UI',Ubuntu,sans-serif;fill:#0f172a}}.note{{font:500 11px 'Segoe UI',Ubuntu,sans-serif;fill:#94a3b8}}.star{{fill:#0891b2}}</style>
<rect x="0.5" y="0.5" width="466" height="169" rx="4.5" fill="#ffffff00" stroke="#e2e8f0" stroke-opacity="0"/>
<text x="25" y="32" class="title">{escape(OWNER)}'s GitHub Stats</text><path class="star" d="M388 43.5l9.4 19 21 3.1-15.2 14.8 3.6 20.9L388 91.4l-18.8 9.9 3.6-20.9-15.2-14.8 21-3.1 9.4-19z" opacity="0.16"/>
{row_svg}<text x="34" y="158" class="note">scope: {escape(note)}</text></svg>'''
    (OUT_DIR / "github-stats.svg").write_text(svg, encoding="utf-8")


def write_top_langs_card(language_totals):
    total = sum(language_totals.values()) or 1
    top = language_totals.most_common(6) or [("No language data", 1)]
    rows = "".join(
        f'<circle cx="32" cy="{62 + i * 18}" r="5" fill="{COLORS.get(name, "#0891b2")}"/><text x="45" y="{66 + i * 18}" class="label">{escape(name)}</text><text x="315" y="{66 + i * 18}" class="pct">{size / total * 100:.1f}%</text>'
        for i, (name, size) in enumerate(top)
    )
    svg = f'''<svg width="360" height="170" viewBox="0 0 360 170" fill="none" xmlns="http://www.w3.org/2000/svg" role="img">
<style>.title{{font:600 18px 'Segoe UI',Ubuntu,sans-serif;fill:#0891b2}}.label{{font:600 13px 'Segoe UI',Ubuntu,sans-serif;fill:#64748b}}.pct{{font:700 13px 'Segoe UI',Ubuntu,sans-serif;fill:#0f172a;text-anchor:end}}</style>
<rect x="0.5" y="0.5" width="359" height="169" rx="4.5" fill="#ffffff00" stroke="#e2e8f0" stroke-opacity="0"/><text x="25" y="35" class="title">Top Languages</text>{rows}</svg>'''
    (OUT_DIR / "top-languages.svg").write_text(svg, encoding="utf-8")


def main():
    OUT_DIR.mkdir(exist_ok=True)
    repos = fetch_repos()
    write_stats_card(repos)
    write_top_langs_card(fetch_languages(repos))


if __name__ == "__main__":
    main()
