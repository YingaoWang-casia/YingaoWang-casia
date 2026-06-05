import { mkdir, readFile, writeFile } from 'node:fs/promises';

const OWNER = 'YingaoWang-casia';

const BADGE_REPOS = [
  { fullName: 'Bairong-Xdynamics/TurnSense', slug: 'turnsense' },
  { fullName: 'YingaoWang-casia/CoDeTT.github.io', slug: 'codett' },
  { fullName: 'YingaoWang-casia/shushu-ProjectProof', slug: 'projectproof' },
  { fullName: 'YingaoWang-casia/shushu-InterviewProof-RAG', slug: 'interviewproof-rag' },
];

const EXTRA_TRACKED_REPOS = (process.env.TRACKED_REPOSITORIES || '')
  .split(/[\s,]+/)
  .map((repo) => repo.trim())
  .filter(Boolean);

const token = process.env.GITHUB_TOKEN;
const headers = {
  Accept: 'application/vnd.github+json',
  'X-GitHub-Api-Version': '2022-11-28',
  'User-Agent': 'YingaoWang-casia-profile-svg-generator',
  ...(token ? { Authorization: `Bearer ${token}` } : {}),
};

async function api(path) {
  const response = await fetch(`https://api.github.com${path}`, { headers });
  if (!response.ok) {
    const body = await response.text();
    throw new Error(`${response.status} ${response.statusText}: ${body}`);
  }
  return response.json();
}

async function listOwnerRepos(owner) {
  const repos = [];
  for (let page = 1; ; page += 1) {
    const batch = await api(`/users/${owner}/repos?type=owner&per_page=100&page=${page}`);
    repos.push(...batch);
    if (batch.length < 100) break;
  }
  return repos;
}

async function fetchRepo(fullName) {
  try {
    return await api(`/repos/${fullName}`);
  } catch (error) {
    console.warn(`Skipping ${fullName}: ${error.message}`);
    return null;
  }
}

async function fetchLanguages(fullName) {
  try {
    return await api(`/repos/${fullName}/languages`);
  } catch (error) {
    console.warn(`Skipping languages for ${fullName}: ${error.message}`);
    return {};
  }
}

function unique(values) {
  return [...new Set(values.filter(Boolean))];
}

function escapeXml(value) {
  return String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;');
}

function escapeRegex(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function formatCount(value) {
  if (value >= 1000) return `${(value / 1000).toFixed(value >= 10000 ? 0 : 1)}k`;
  return String(value);
}

function statsSvg({ totalStars, trackedRepos, originalProjects, repositoryForks }) {
  return `<svg width="467" height="170" viewBox="0 0 467 170" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc">
  <title id="title">${OWNER}'s GitHub Stats</title>
  <desc id="desc">GitHub repository statistics for ${OWNER}.</desc>
  <style>.title{font:600 18px 'Segoe UI',Ubuntu,sans-serif;fill:#0891b2}.label{font:600 14px 'Segoe UI',Ubuntu,sans-serif;fill:#64748b}.value{font:700 14px 'Segoe UI',Ubuntu,sans-serif;fill:#64748b}.icon{fill:none;stroke:#0891b2;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}.github{fill:#64748b}.rim{stroke:#ccfbf1;stroke-width:8;fill:none}.arc{stroke:#0891b2;stroke-width:8;fill:none;stroke-linecap:round;stroke-dasharray:175 75;transform:rotate(-90deg);transform-origin:402px 89px}</style>
  <rect x="0.5" y="0.5" width="466" height="169" rx="4.5" fill="#ffffff00" stroke="#e2e8f0" stroke-opacity="0"/>
  <text x="36" y="29" class="title">${OWNER}'s GitHub Stats</text>
  <g transform="translate(36 52)"><path class="icon" d="M8 .8l2.2 4.5 5 .7-3.6 3.5.8 5-4.4-2.3-4.4 2.3.8-5L.8 6l5-.7L8 .8z"/><text x="30" y="11" class="label">Total Stars Earned:</text><text x="250" y="11" class="value">${totalStars}</text></g>
  <g transform="translate(36 84)"><path class="icon" d="M3 4.5h10M3 8.5h10M3 12.5h10M2.5 1.8h11A1.7 1.7 0 0 1 15.2 3.5v10A1.7 1.7 0 0 1 13.5 15.2h-11A1.7 1.7 0 0 1 .8 13.5v-10A1.7 1.7 0 0 1 2.5 1.8z"/><text x="30" y="11" class="label">Tracked Repositories:</text><text x="250" y="11" class="value">${trackedRepos}</text></g>
  <g transform="translate(36 116)"><path class="icon" d="M3.5 3.5v9M12.5 3.5v9M3.5 8h9M3.5 3.5a2 2 0 1 0 0 .1M12.5 3.5a2 2 0 1 0 0 .1M3.5 12.5a2 2 0 1 0 0 .1M12.5 12.5a2 2 0 1 0 0 .1"/><text x="30" y="11" class="label">Original Projects:</text><text x="250" y="11" class="value">${originalProjects}</text></g>
  <g transform="translate(36 148)"><path class="icon" d="M3 3.5h10v9H3zM5 15h6M6.5 12.5v2.5M9.5 12.5v2.5"/><text x="30" y="11" class="label">Repository Forks:</text><text x="250" y="11" class="value">${repositoryForks}</text></g>
  <circle class="rim" cx="402" cy="89" r="48"/><circle class="arc" cx="402" cy="89" r="48"/><circle cx="402" cy="89" r="36" fill="#64748b" opacity="0.12"/>
  <g transform="translate(374 61) scale(3.5)"><path class="github" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82A7.65 7.65 0 0 1 8 3.36c.68 0 1.36.09 2 .27 1.53-1.03 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.28.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></g>
</svg>`;
}

const LANGUAGE_COLORS = {
  Python: '#3776ab',
  HTML: '#e34c26',
  CSS: '#563d7c',
  JavaScript: '#f1e05a',
  TypeScript: '#3178c6',
  Shell: '#89e051',
  Makefile: '#427819',
  PowerShell: '#012456',
  JupyterNotebook: '#da5b0b',
};

function topLanguagesSvg(languageTotals) {
  const total = Object.values(languageTotals).reduce((sum, value) => sum + value, 0) || 1;
  const rows = Object.entries(languageTotals)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 5)
    .map(([name, bytes], index) => {
      const y = 62 + index * 18;
      const pct = ((bytes / total) * 100).toFixed(1);
      const color = LANGUAGE_COLORS[name.replaceAll(' ', '')] || '#64748b';
      return `<circle cx="32" cy="${y}" r="5" fill="${color}"/><text x="45" y="${y + 4}" class="label">${escapeXml(name)}</text><text x="315" y="${y + 4}" class="pct">${pct}%</text>`;
    })
    .join('');

  return `<svg width="360" height="170" viewBox="0 0 360 170" fill="none" xmlns="http://www.w3.org/2000/svg" role="img"><style>.title{font:600 18px 'Segoe UI',Ubuntu,sans-serif;fill:#0891b2}.label{font:600 13px 'Segoe UI',Ubuntu,sans-serif;fill:#64748b}.pct{font:700 13px 'Segoe UI',Ubuntu,sans-serif;fill:#0f172a;text-anchor:end}</style><rect x="0.5" y="0.5" width="359" height="169" rx="4.5" fill="#ffffff00" stroke="#e2e8f0" stroke-opacity="0"/><text x="25" y="35" class="title">Top Languages</text>${rows}</svg>`;
}

function starBadgeSvg(repo, stars) {
  const value = formatCount(stars);
  const valueWidth = Math.max(17, value.length * 7 + 16);
  const labelWidth = 37;
  const width = labelWidth + valueWidth;
  const valueTextLength = Math.max(70, value.length * 70);

  return `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="20" role="img" aria-label="${escapeXml(repo)} stars: ${value}"><title>${escapeXml(repo)} stars: ${value}</title><g shape-rendering="crispEdges"><rect width="${labelWidth}" height="20" fill="#555"/><rect x="${labelWidth}" width="${valueWidth}" height="20" fill="#0891b2"/></g><g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110"><text x="195" y="140" transform="scale(.1)" fill="#fff" textLength="270">stars</text><text x="${(labelWidth + valueWidth / 2) * 10}" y="140" transform="scale(.1)" fill="#fff" textLength="${valueTextLength}">${escapeXml(value)}</text></g></svg>`;
}

async function updateReadmeBadges() {
  const readmePath = 'README.md';
  let readme = await readFile(readmePath, 'utf8');
  let nextReadme = readme;

  for (const { fullName, slug } of BADGE_REPOS) {
    const pattern = new RegExp(`https://img\\.shields\\.io/github/stars/${escapeRegex(fullName)}\\?style=flat-square&color=0891b2`, 'g');
    nextReadme = nextReadme.replace(pattern, `profile/badges/stars-${slug}.svg`);
  }

  if (nextReadme !== readme) {
    await writeFile(readmePath, nextReadme, 'utf8');
  }
}

async function main() {
  await mkdir('profile/badges', { recursive: true });

  const ownerRepos = await listOwnerRepos(OWNER);
  const trackedNames = unique([
    ...ownerRepos.map((repo) => repo.full_name),
    ...BADGE_REPOS.map((repo) => repo.fullName),
    ...EXTRA_TRACKED_REPOS,
  ]);

  const repos = (await Promise.all(trackedNames.map(fetchRepo))).filter(Boolean);
  const stats = {
    totalStars: repos.reduce((sum, repo) => sum + repo.stargazers_count, 0),
    trackedRepos: repos.length,
    originalProjects: repos.filter((repo) => !repo.fork).length,
    repositoryForks: repos.reduce((sum, repo) => sum + repo.forks_count, 0),
  };

  const languageTotals = {};
  for (const repo of repos) {
    const languages = await fetchLanguages(repo.full_name);
    for (const [name, bytes] of Object.entries(languages)) {
      languageTotals[name] = (languageTotals[name] || 0) + bytes;
    }
  }

  await writeFile('profile/github-stats.svg', statsSvg(stats), 'utf8');
  await writeFile('profile/stats.svg', statsSvg(stats), 'utf8');
  await writeFile('profile/top-languages.svg', topLanguagesSvg(languageTotals), 'utf8');
  await writeFile('profile/top-langs.svg', topLanguagesSvg(languageTotals), 'utf8');

  const repoStatsByName = new Map(repos.map((repo) => [repo.full_name, repo]));
  for (const { fullName, slug } of BADGE_REPOS) {
    const repo = repoStatsByName.get(fullName);
    if (repo) {
      await writeFile(`profile/badges/stars-${slug}.svg`, starBadgeSvg(fullName, repo.stargazers_count), 'utf8');
    }
  }

  await updateReadmeBadges();
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
