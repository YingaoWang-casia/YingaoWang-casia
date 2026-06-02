from __future__ import annotations

import json
import os
import urllib.request
from collections import Counter
from pathlib import Path
from xml.sax.saxutils import escape

OWNER = os.environ.get("GITHUB_REPOSITORY_OWNER", "YingaoWang-casia")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT_DIR = Path("profile")

COLORS = {
    "Python": "#3776ab",
    "Jupyter Notebook": "#da5b0b",
    "JavaScript": "#f1e05a",
    "TypeScript": "#3178c6",
    "HTML": "#e34c26",
    "CSS": "#563d7c",
    "Shell": "#89e051",
    "PowerShell": "#012456",
    "Makefile": "#427819",
    "C++": "#f34b7d",
    "C": "#555555",
    "Java": "#b07219",
    "Go": "#00add8",
    "Rust": "#dea584",
    "Markdown": "#083fa1",
}


def request_json(url: str):
    headers = {"User-Agent": "profile-card-generator"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_owner_repos():
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{OWNER}/repos?type=owner&sort=updated&per_page=100&page={page}"
        batch = request_json(url)
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
            langs = request_json(repo["languages_url"])
        except Exception:
            continue
        totals.update({name: int(size) for name, size in langs.items()})
    return totals


def write_stats_card(repos):
    public_repos = [repo for repo in repos if not repo.get("private")]
    total_stars = sum(int(repo.get("stargazers_count", 0)) for repo in public_repos)
    total_forks = sum(int(repo.get("forks_count", 0)) for repo in public_repos)
    original_repos = sum(1 for repo in public_repos if not repo.get("fork"))
    forked_repos = sum(1 for repo in public_repos if repo.get("fork"))

    rows = [
        ("Total Stars Earned", total_stars),
        ("Public Repositories", len(public_repos)),
        ("Original Projects", original_repos),
        ("Repository Forks", total_forks),
        ("Forked Repositories", forked_repos),
    ]

    row_svg = []
    for index, (label, value) in enumerate(rows):
        y = 66 + index * 22
        row_svg.append(
            f'<text x="34" y="{y}" class="label">{escape(label)}:</text>'
            f'<text x="245" y="{y}" class="value">{value}</text>'
        )

    svg = f'''<svg width="467" height="170" viewBox="0 0 467 170" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc">
  <title id="title">{escape(OWNER)} GitHub Stats</title>
  <desc id="desc">Total stars and repository statistics for {escape(OWNER)}.</desc>
  <style>
    .title {{ font: 600 18px 'Segoe UI', Ubuntu, sans-serif; fill: #0891b2; }}
    .label {{ font: 600 14px 'Segoe UI', Ubuntu, sans-serif; fill: #64748b; }}
    .value {{ font: 700 14px 'Segoe UI', Ubuntu, sans-serif; fill: #0f172a; }}
    .star {{ fill: #0891b2; }}
  </style>
  <rect x="0.5" y="0.5" width="466" height="169" rx="4.5" fill="#ffffff00" stroke="#e2e8f0" stroke-opacity="0"/>
  <text x="25" y="35" class="title">{escape(OWNER)}'s GitHub Stats</text>
  <path class="star" d="M388 43.5l9.4 19 21 3.1-15.2 14.8 3.6 20.9L388 91.4l-18.8 9.9 3.6-20.9-15.2-14.8 21-3.1 9.4-19z" opacity="0.16"/>
  {''.join(row_svg)}
</svg>
'''
    (OUT_DIR / "stats.svg").write_text(svg, encoding="utf-8")


def write_top_langs_card(language_totals):
    total = sum(language_totals.values())
    top = language_totals.most_common(6)
    if not top:
        top = [("No language data", 1)]
        total = 1

    rows = []
    for index, (name, size) in enumerate(top):
        pct = size / total
        y = 66 + index * 18
        color = COLORS.get(name, "#0891b2")
        rows.append(f'<circle cx="32" cy="{y - 4}" r="5" fill="{color}"/>')
        rows.append(f'<text x="45" y="{y}" class="label">{escape(name)}</text>')
        rows.append(f'<text x="315" y="{y}" class="pct">{pct * 100:.1f}%</text>')

    svg = f'''<svg width="360" height="170" viewBox="0 0 360 170" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc">
  <title id="title">{escape(OWNER)} Top Languages</title>
  <desc id="desc">Top programming languages by repository byte count for {escape(OWNER)}.</desc>
  <style>
    .title {{ font: 600 18px 'Segoe UI', Ubuntu, sans-serif; fill: #0891b2; }}
    .label {{ font: 600 13px 'Segoe UI', Ubuntu, sans-serif; fill: #64748b; }}
    .pct {{ font: 700 13px 'Segoe UI', Ubuntu, sans-serif; fill: #0f172a; text-anchor: end; }}
  </style>
  <rect x="0.5" y="0.5" width="359" height="169" rx="4.5" fill="#ffffff00" stroke="#e2e8f0" stroke-opacity="0"/>
  <text x="25" y="35" class="title">Top Languages</text>
  {''.join(rows)}
</svg>
'''
    (OUT_DIR / "top-langs.svg").write_text(svg, encoding="utf-8")


def main():
    OUT_DIR.mkdir(exist_ok=True)
    repos = fetch_owner_repos()
    write_stats_card(repos)
    write_top_langs_card(fetch_languages(repos))


if __name__ == "__main__":
    main()
