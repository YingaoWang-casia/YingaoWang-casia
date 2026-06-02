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
EXTRA_REPOSITORIES = ["Bairong-Xdynamics/TurnSense"]
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

    seen = {repo.get("full_name") for repo in repos}
    for full_name in EXTRA_REPOSITORIES:
        if full_name not in seen:
            try:
                repo = request_json(f"https://api.github.com/repos/{full_name}")
                repos.append(repo)
                seen.add(full_name)
            except Exception:
                pass
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
    values = {
        "stars": sum(int(r.get("stargazers_count", 0)) for r in repos),
        "repos": len(repos),
        "projects": sum(1 for r in repos if not r.get("fork")),
        "forks": sum(int(r.get("forks_count", 0)) for r in repos),
    }
    svg = f'''<svg width="467" height="170" viewBox="0 0 467 170" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc">
  <title id="title">{escape(OWNER)}'s GitHub Stats</title>
  <desc id="desc">GitHub repository statistics for {escape(OWNER)}.</desc>
  <style>.title{{font:600 18px 'Segoe UI',Ubuntu,sans-serif;fill:#0891b2}}.label{{font:600 14px 'Segoe UI',Ubuntu,sans-serif;fill:#64748b}}.value{{font:700 14px 'Segoe UI',Ubuntu,sans-serif;fill:#64748b}}.icon{{fill:none;stroke:#0891b2;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}}.github{{fill:#64748b}}.rim{{stroke:#ccfbf1;stroke-width:8;fill:none}}.arc{{stroke:#0891b2;stroke-width:8;fill:none;stroke-linecap:round;stroke-dasharray:175 75;transform:rotate(-90deg);transform-origin:374px 89px}}</style>
  <rect x="0.5" y="0.5" width="466" height="169" rx="4.5" fill="#ffffff00" stroke="#e2e8f0" stroke-opacity="0"/>
  <text x="36" y="29" class="title">{escape(OWNER)}'s GitHub Stats</text>
  <g transform="translate(36 52)"><path class="icon" d="M8 .8l2.2 4.5 5 .7-3.6 3.5.8 5-4.4-2.3-4.4 2.3.8-5L.8 6l5-.7L8 .8z"/><text x="30" y="11" class="label">Total Stars Earned:</text><text x="270" y="11" class="value">{values['stars']}</text></g>
  <g transform="translate(36 84)"><path class="icon" d="M3 4.5h10M3 8.5h10M3 12.5h10M2.5 1.8h11A1.7 1.7 0 0 1 15.2 3.5v10A1.7 1.7 0 0 1 13.5 15.2h-11A1.7 1.7 0 0 1 .8 13.5v-10A1.7 1.7 0 0 1 2.5 1.8z"/><text x="30" y="11" class="label">Tracked Repositories:</text><text x="270" y="11" class="value">{values['repos']}</text></g>
  <g transform="translate(36 116)"><path class="icon" d="M3.5 3.5v9M12.5 3.5v9M3.5 8h9M3.5 3.5a2 2 0 1 0 0 .1M12.5 3.5a2 2 0 1 0 0 .1M3.5 12.5a2 2 0 1 0 0 .1M12.5 12.5a2 2 0 1 0 0 .1"/><text x="30" y="11" class="label">Original Projects:</text><text x="270" y="11" class="value">{values['projects']}</text></g>
  <g transform="translate(36 148)"><path class="icon" d="M3 3.5h10v9H3zM5 15h6M6.5 12.5v2.5M9.5 12.5v2.5"/><text x="30" y="11" class="label">Repository Forks:</text><text x="270" y="11" class="value">{values['forks']}</text></g>
  <circle class="rim" cx="374" cy="89" r="48"/><circle class="arc" cx="374" cy="89" r="48"/><circle cx="374" cy="89" r="36" fill="#64748b" opacity="0.12"/>
  <g transform="translate(346 61) scale(3.5)"><path class="github" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82A7.65 7.65 0 0 1 8 3.36c.68 0 1.36.09 2 .27 1.53-1.03 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.28.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></g>
</svg>'''
    (OUT_DIR / "github-stats.svg").write_text(svg, encoding="utf-8")


def write_top_langs_card(language_totals):
    total = sum(language_totals.values()) or 1
    top = language_totals.most_common(6) or [("No language data", 1)]
    rows = "".join(
        f'<circle cx="32" cy="{62 + i * 18}" r="5" fill="{COLORS.get(name, "#0891b2")}"/><text x="45" y="{66 + i * 18}" class="label">{escape(name)}</text><text x="315" y="{66 + i * 18}" class="pct">{size / total * 100:.1f}%</text>'
        for i, (name, size) in enumerate(top)
    )
    svg = f'''<svg width="360" height="170" viewBox="0 0 360 170" fill="none" xmlns="http://www.w3.org/2000/svg" role="img"><style>.title{{font:600 18px 'Segoe UI',Ubuntu,sans-serif;fill:#0891b2}}.label{{font:600 13px 'Segoe UI',Ubuntu,sans-serif;fill:#64748b}}.pct{{font:700 13px 'Segoe UI',Ubuntu,sans-serif;fill:#0f172a;text-anchor:end}}</style><rect x="0.5" y="0.5" width="359" height="169" rx="4.5" fill="#ffffff00" stroke="#e2e8f0" stroke-opacity="0"/><text x="25" y="35" class="title">Top Languages</text>{rows}</svg>'''
    (OUT_DIR / "top-languages.svg").write_text(svg, encoding="utf-8")


def main():
    OUT_DIR.mkdir(exist_ok=True)
    repos = fetch_repos()
    write_stats_card(repos)
    write_top_langs_card(fetch_languages(repos))


if __name__ == "__main__":
    main()
