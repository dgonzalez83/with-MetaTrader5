# with-MetaTrader5

A Python toolkit for connecting to and automating the [MetaTrader 5](https://www.metatrader5.com/) trading terminal on Windows.

It uses the official [`MetaTrader5`](https://pypi.org/project/MetaTrader5/) package to talk to a running MT5 terminal, loads account credentials from a `.env` file, and ships a local type stub (`MetaTrader5.pyi`) documenting the full API surface.

## Requirements

- **Windows** — the `MetaTrader5` package is Windows-only.
- A running **MetaTrader 5 terminal** with a (demo or live) trading account.
- **Python 3.13+**
- [**uv**](https://docs.astral.sh/uv/) for dependency and project management.

## Installation

```bash
git clone https://github.com/dgonzalez83/with-MetaTrader5.git
cd with-MetaTrader5
uv sync                 # install dependencies from the lockfile
```

## Configuration

Account credentials are loaded from a `.env` file at the project root. Copy the
example file and fill in your details:

```bash
cp .env.example .env
```

```dotenv
MT5_LOGIN=your_account_number
MT5_PASSWORD=your_password
MT5_SERVER=your_broker_server
```

> **Note:** `MT5_LOGIN` is your numeric account number. Never commit real
> credentials — keep `.env` out of version control.

## Usage

Make sure the MetaTrader 5 terminal is running and logged in, then run:

```bash
uv run main.py
```

This connects to the configured account and prints the package version,
terminal info, and MT5 version before shutting the connection down again:

```python
import os

import MetaTrader5 as mt5
from dotenv import load_dotenv

load_dotenv()

login = int(os.getenv("MT5_LOGIN"))
password = os.getenv("MT5_PASSWORD")
server = os.getenv("MT5_SERVER")

if not mt5.initialize(login=login, server=server, password=password):
    print("initialize() failed, error code =", mt5.last_error())
    quit()

print(mt5.terminal_info())
print(mt5.version())

mt5.shutdown()
```

## Development

```bash
uv add <pkg>            # add a runtime dependency
uv add --dev <pkg>      # add a dev dependency
uv run pytest          # run the test suite
```

### Type stubs

`MetaTrader5.pyi` is a local type stub (~800 lines) covering the `MetaTrader5`
package's constants, named tuples, and functions. Consult it for accurate
signatures and return types instead of guessing the runtime API.

## License

Released under the [MIT License](LICENSE.txt) — Copyright (c) 2026 Daniel Gonzalez.
