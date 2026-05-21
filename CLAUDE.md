# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Personal academic homepage for Jianxiang He (何建翔), built on a Jekyll + GitHub Pages template. Deployed automatically to `Jacksonha7.github.io` on every push to `main`.

## Local Development

```bash
# Install Ruby dependencies (one-time)
bundle install

# Serve locally with live-reload
bundle exec jekyll serve
# → http://localhost:4000
```

No build step needed for GitHub Pages — push to `main` and GitHub builds it automatically.

## Key Files

| File | Purpose |
|---|---|
| `index.md` | Homepage: hero, about, education, research interests, news |
| `publications.md` | Full publications list |
| `_config.yml` | Site metadata (name, email, Scholar URL, social links) |
| `_layouts/` | Page templates (Liquid) |
| `_includes/` | Reusable HTML fragments (nav, head, footer) |
| `assets/css/main.css` | Global styles (compiled from LESS) |

## Content Architecture

The site uses inline `<style>` blocks and raw HTML inside Markdown files rather than separate CSS. This is intentional — each page is self-contained.

**index.md** is pure HTML+CSS embedded in Markdown. It controls:
- Hero section (name, tagline, badges, contact)
- About, Education timeline, Research Interests cards
- News & Publications summary
- Google Scholar citation widget (JavaScript fetch from Semantic Scholar API)

**publications.md** contains the full paper list with status badges (`status-submitted`, `status-review`, `status-published`).

## Owner Info

- **Name:** Jianxiang He / 何建翔  
- **Google Scholar:** https://scholar.google.com/citations?user=6ZJXY_EAAAAJ&hl=zh-CN  
- **PhD (incoming):** MBZUAI, advised by Prof. Xiaojun Chang (常晓军)  
- **Research interests:** VLA, Embodied AI, World Models, Multimodal LLM
