# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A Python project for interacting with the MetaTrader 5 trading terminal via the
`MetaTrader5` package. The terminal connection requires Windows and a running MT5
terminal; the `MetaTrader5` package is Windows-only.

## Tooling

This project is managed with **uv** (note `uv.lock` and `pyproject.toml`). Always
use uv rather than pip/python directly:

```bash
uv sync                 # install dependencies from the lockfile
uv add <pkg>            # add a runtime dependency
uv add --dev <pkg>      # add a dev dependency (e.g. pytest lives here)
uv run main.py          # run a script in the project environment
uv run pytest           # run the test suite
uv run pytest path::test_name   # run a single test
```

Python is pinned to 3.13 (`.python-version`, `requires-python >=3.13`).

## Credentials

MT5 account credentials are loaded from a `.env` file at the project root via
`python-dotenv`, with keys `MT5_LOGIN`, `MT5_PASSWORD`, `MT5_SERVER`. `MT5_LOGIN`
must be parsed as an `int` for `mt5.initialize()`. The `.env` file is currently
**not** listed in `.gitignore` — keep real credentials out of commits.

## MetaTrader5.pyi

`MetaTrader5.pyi` is a local type stub (~800 lines) for the `MetaTrader5`
package — it documents the full API surface (constants, named tuples, and
functions) used to talk to the terminal. Consult it for accurate signatures and
return types rather than guessing the runtime API.
