# dntrader

A static blog/notes site built with Jekyll and hosted on GitHub Pages.

## Setup

1. Push this repository to GitHub
2. Go to **Settings → Pages**
3. Under "Source", select the branch to deploy (e.g. `main`)
4. Your site will be live at `https://<username>.github.io/dnr/`

GitHub Pages will automatically build the Jekyll site on each push — no CI/CD config needed.

## Structure

- `_config.yml` — Jekyll site configuration
- `_posts/` — Blog posts in markdown (named `YYYY-MM-DD-title.md`)
- `_layouts/` — HTML layout templates (optional)
- `_includes/` — Reusable HTML/JS snippets (e.g. calculators)
- `assets/` — Images, styles, scripts, and other static files

## Writing Posts

Create a markdown file in `_posts/` with this naming convention:

```
_posts/2026-02-18-my-first-post.md
```

Each post needs front matter at the top:

```yaml
---
layout: post
title: "My First Post"
date: 2026-02-18
---

Your content here in markdown.
```

## Interactive Calculators

Embed form-based calculators directly in posts using HTML and inline JavaScript. Jekyll allows raw HTML inside markdown files.

Example usage in a post:

```html
<div id="calculator">
  <input type="number" id="input-val" placeholder="Enter value">
  <button onclick="calculate()">Calculate</button>
  <p>Result: <span id="result"></span></p>
</div>

<script>
function calculate() {
  const val = document.getElementById('input-val').value;
  document.getElementById('result').textContent = val * 2;
}
</script>
```

For reusable calculators, put the HTML/JS in `_includes/` and use `{% include calculator.html %}` in any post.

## Page Layout

Two-column layout with responsive design:

```
┌──────────────────────────────────────────────┐
│  dntrader                           [Posts]  │
├─────────────────┬────────────────────────────┤
│                 │                            │
│  Sidebar (30%)  │   Main Content (70%)       │
│                 │                            │
│  - Recent posts │   - Post body / content    │
│  - Categories   │   - Embedded calculators   │
│  - Quick links  │                            │
│                 │                            │
├─────────────────┴────────────────────────────┤
│  Footer                                      │
└──────────────────────────────────────────────┘
```

- Header: site title + "Posts" nav link
- Main area: post content with inline calculators
- Sidebar: recent posts, categories, quick links
- Footer: copyright / links
- Mobile: sidebar collapses below main content

### Layouts

- `default` — Base layout with header, sidebar, footer
- `post` — Extends default, adds post title, date, and content area
- `home` — Homepage with recent posts listing

## Local Preview

```sh
gem install bundler jekyll
bundle exec jekyll serve
```

Then visit `http://localhost:4000`.
