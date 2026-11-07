# dheevatsa personal site

Static site for GitHub Pages. No build step.

| File | What it is | How it changes |
|---|---|---|
| `index.html` | Page layout and styles | Rarely |
| `data.js` | **Latest** items and **Publications** | Edit by hand (GitHub's pencil icon) |
| `citations.js` | Scholar totals and per-year counts | Weekly by the GitHub Action; can edit by hand |
| `photo.jpg` | Photo in the dark band | Replace any time (landscape, ~1600px wide) |

## Common edits
- **New post/talk in Latest:** add a line at the top of `LATEST` in `data.js`. Only the first 3 show.
- **New paper:** add a line at the top of `PUBLICATIONS` in `data.js` (same format as the others).
- **Citations now:** Actions tab → "Refresh Scholar citations" → Run workflow.

## Preview locally
Open `index.html` in a browser, or run `python3 -m http.server` in this folder and visit http://localhost:8000.
