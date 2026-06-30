from datetime import datetime
from typing import Literal, Protocol

import numpy as np

__author__: str
__version__: str


# timeframes
TIMEFRAME_M1: Literal[1]
TIMEFRAME_M2: Literal[2]
TIMEFRAME_M3: Literal[3]
TIMEFRAME_M4: Literal[4]
TIMEFRAME_M5: Literal[5]
TIMEFRAME_M6: Literal[6]
TIMEFRAME_M10: Literal[10]
TIMEFRAME_M12: Literal[12]
TIMEFRAME_M15: Literal[15]
TIMEFRAME_M20: Literal[20]
TIMEFRAME_M30: Literal[30]
TIMEFRAME_H1: Literal[16385]
TIMEFRAME_H2: Literal[16386]
TIMEFRAME_H3: Literal[16387]
TIMEFRAME_H4: Literal[16388]
TIMEFRAME_H6: Literal[16390]
TIMEFRAME_H8: Literal[16392]
TIMEFRAME_H12: Literal[16396]
TIMEFRAME_D1: Literal[16408]
TIMEFRAME_W1: Literal[32769]
TIMEFRAME_MN1: Literal[49153]
# tick copy flags
COPY_TICKS_ALL: Literal[-1]
COPY_TICKS_INFO: Literal[1]
COPY_TICKS_TRADE: Literal[2]
# tick flags
TICK_FLAG_BID: Literal[0x02]
TICK_FLAG_ASK: Literal[0x04]
TICK_FLAG_LAST: Literal[0x08]
TICK_FLAG_VOLUME: Literal[0x10]
TICK_FLAG_BUY: Literal[0x20]
TICK_FLAG_SELL: Literal[0x40]
# position type, ENUM_POSITION_TYPE
POSITION_TYPE_BUY: Literal[0]
POSITION_TYPE_SELL: Literal[1]
# position reason, ENUM_POSITION_REASON
POSITION_REASON_CLIENT: Literal[0]
POSITION_REASON_MOBILE: Literal[1]
POSITION_REASON_WEB: Literal[2]
POSITION_REASON_EXPERT: Literal[3]
# order types, ENUM_ORDER_TYPE
ORDER_TYPE_BUY: Literal[0]
ORDER_TYPE_SELL: Literal[1]
ORDER_TYPE_BUY_LIMIT: Literal[2]
ORDER_TYPE_SELL_LIMIT: Literal[3]
ORDER_TYPE_BUY_STOP: Literal[4]
ORDER_TYPE_SELL_STOP: Literal[5]
ORDER_TYPE_BUY_STOP_LIMIT: Literal[6]
ORDER_TYPE_SELL_STOP_LIMIT: Literal[7]
ORDER_TYPE_CLOSE_BY: Literal[8]
# order state, ENUM_ORDER_STATE
ORDER_STATE_STARTED: Literal[0]
ORDER_STATE_PLACED: Literal[1]
ORDER_STATE_CANCELED: Literal[2]
ORDER_STATE_PARTIAL: Literal[3]
ORDER_STATE_FILLED: Literal[4]
ORDER_STATE_REJECTED: Literal[5]
ORDER_STATE_EXPIRED: Literal[6]
ORDER_STATE_REQUEST_ADD: Literal[7]
ORDER_STATE_REQUEST_MODIFY: Literal[8]
ORDER_STATE_REQUEST_CANCEL: Literal[9]
# ENUM_ORDER_TYPE_FILLING
ORDER_FILLING_FOK: Literal[0]
ORDER_FILLING_IOC: Literal[1]
ORDER_FILLING_RETURN: Literal[2]
# ENUM_ORDER_TYPE_TIME
ORDER_TIME_GTC: Literal[0]
ORDER_TIME_DAY: Literal[1]
ORDER_TIME_SPECIFIED: Literal[2]
ORDER_TIME_SPECIFIED_DAY: Literal[3]
# ENUM_ORDER_REASON
ORDER_REASON_CLIENT: Literal[0]
ORDER_REASON_MOBILE: Literal[1]
ORDER_REASON_WEB: Literal[2]
ORDER_REASON_EXPERT: Literal[3]
ORDER_REASON_SL: Literal[4]
ORDER_REASON_TP: Literal[5]
ORDER_REASON_SO: Literal[6]
DEAL_TYPE_BUY: Literal[0]
DEAL_TYPE_SELL: Literal[1]
DEAL_TYPE_BALANCE: Literal[2]
DEAL_TYPE_CREDIT: Literal[3]
DEAL_TYPE_CHARGE: Literal[4]
DEAL_TYPE_CORRECTION: Literal[5]
DEAL_TYPE_BONUS: Literal[6]
DEAL_TYPE_COMMISSION: Literal[7]
DEAL_TYPE_COMMISSION_DAILY: Literal[8]
DEAL_TYPE_COMMISSION_MONTHLY: Literal[9]
DEAL_TYPE_COMMISSION_AGENT_DAILY: Literal[10]
DEAL_TYPE_COMMISSION_AGENT_MONTHLY: Literal[11]
DEAL_TYPE_INTEREST: Literal[12]
DEAL_TYPE_BUY_CANCELED: Literal[13]
DEAL_TYPE_SELL_CANCELED: Literal[14]
DEAL_DIVIDEND: Literal[15]
DEAL_DIVIDEND_FRANKED: Literal[16]
DEAL_TAX: Literal[17]
# ENUM_DEAL_ENTRY
DEAL_ENTRY_IN: Literal[0]
DEAL_ENTRY_OUT: Literal[1]
DEAL_ENTRY_INOUT: Literal[2]
DEAL_ENTRY_OUT_BY: Literal[3]
# ENUM_DEAL_REASON
DEAL_REASON_CLIENT: Literal[0]
DEAL_REASON_MOBILE: Literal[1]
DEAL_REASON_WEB: Literal[2]
DEAL_REASON_EXPERT: Literal[3]
DEAL_REASON_SL: Literal[4]
DEAL_REASON_TP: Literal[5]
DEAL_REASON_SO: Literal[6]
DEAL_REASON_ROLLOVER: Literal[7]
DEAL_REASON_VMARGIN: Literal[8]
DEAL_REASON_SPLIT: Literal[9]
# ENUM_TRADE_REQUEST_ACTIONS, Trade Operation Types
TRADE_ACTION_DEAL: Literal[1]
TRADE_ACTION_PENDING: Literal[5]
TRADE_ACTION_SLTP: Literal[6]
TRADE_ACTION_MODIFY: Literal[7]
TRADE_ACTION_REMOVE: Literal[8]
TRADE_ACTION_CLOSE_BY: Literal[10]
# ENUM_SYMBOL_CHART_MODE
SYMBOL_CHART_MODE_BID: Literal[0]
SYMBOL_CHART_MODE_LAST: Literal[1]
# ENUM_SYMBOL_CALC_MODE
SYMBOL_CALC_MODE_FOREX: Literal[0]
SYMBOL_CALC_MODE_FUTURES: Literal[1]
SYMBOL_CALC_MODE_CFD: Literal[2]
SYMBOL_CALC_MODE_CFDINDEX: Literal[3]
SYMBOL_CALC_MODE_CFDLEVERAGE: Literal[4]
SYMBOL_CALC_MODE_FOREX_NO_LEVERAGE: Literal[5]
SYMBOL_CALC_MODE_EXCH_STOCKS: Literal[32]
SYMBOL_CALC_MODE_EXCH_FUTURES: Literal[33]
SYMBOL_CALC_MODE_EXCH_OPTIONS: Literal[34]
SYMBOL_CALC_MODE_EXCH_OPTIONS_MARGIN: Literal[36]
SYMBOL_CALC_MODE_EXCH_BONDS: Literal[37]
SYMBOL_CALC_MODE_EXCH_STOCKS_MOEX: Literal[38]
SYMBOL_CALC_MODE_EXCH_BONDS_MOEX: Literal[39]
SYMBOL_CALC_MODE_SERV_COLLATERAL: Literal[64]
# ENUM_SYMBOL_TRADE_MODE
SYMBOL_TRADE_MODE_DISABLED: Literal[0]
SYMBOL_TRADE_MODE_LONGONLY: Literal[1]
SYMBOL_TRADE_MODE_SHORTONLY: Literal[2]
SYMBOL_TRADE_MODE_CLOSEONLY: Literal[3]
SYMBOL_TRADE_MODE_FULL: Literal[4]
# ENUM_SYMBOL_TRADE_EXECUTION
SYMBOL_TRADE_EXECUTION_REQUEST: Literal[0]
SYMBOL_TRADE_EXECUTION_INSTANT: Literal[1]
SYMBOL_TRADE_EXECUTION_MARKET: Literal[2]
SYMBOL_TRADE_EXECUTION_EXCHANGE: Literal[3]
# ENUM_SYMBOL_SWAP_MODE
SYMBOL_SWAP_MODE_DISABLED: Literal[0]
SYMBOL_SWAP_MODE_POINTS: Literal[1]
SYMBOL_SWAP_MODE_CURRENCY_SYMBOL: Literal[2]
SYMBOL_SWAP_MODE_CURRENCY_MARGIN: Literal[3]
SYMBOL_SWAP_MODE_CURRENCY_DEPOSIT: Literal[4]
SYMBOL_SWAP_MODE_INTEREST_CURRENT: Literal[5]
SYMBOL_SWAP_MODE_INTEREST_OPEN: Literal[6]
SYMBOL_SWAP_MODE_REOPEN_CURRENT: Literal[7]
SYMBOL_SWAP_MODE_REOPEN_BID: Literal[8]
# ENUM_DAY_OF_WEEK
DAY_OF_WEEK_SUNDAY: Literal[0]
DAY_OF_WEEK_MONDAY: Literal[1]
DAY_OF_WEEK_TUESDAY: Literal[2]
DAY_OF_WEEK_WEDNESDAY: Literal[3]
DAY_OF_WEEK_THURSDAY: Literal[4]
DAY_OF_WEEK_FRIDAY: Literal[5]
DAY_OF_WEEK_SATURDAY: Literal[6]
# ENUM_SYMBOL_ORDER_GTC_MODE
SYMBOL_ORDERS_GTC: Literal[0]
SYMBOL_ORDERS_DAILY: Literal[1]
SYMBOL_ORDERS_DAILY_NO_STOPS: Literal[2]
# ENUM_SYMBOL_OPTION_RIGHT
SYMBOL_OPTION_RIGHT_CALL: Literal[0]
SYMBOL_OPTION_RIGHT_PUT: Literal[1]
# ENUM_SYMBOL_OPTION_MODE
SYMBOL_OPTION_MODE_EUROPEAN: Literal[0]
SYMBOL_OPTION_MODE_AMERICAN: Literal[1]
# ENUM_ACCOUNT_TRADE_MODE
ACCOUNT_TRADE_MODE_DEMO: Literal[0]
ACCOUNT_TRADE_MODE_CONTEST: Literal[1]
ACCOUNT_TRADE_MODE_REAL: Literal[2]
# ENUM_ACCOUNT_STOPOUT_MODE
ACCOUNT_STOPOUT_MODE_PERCENT: Literal[0]
ACCOUNT_STOPOUT_MODE_MONEY: Literal[1]
# ENUM_ACCOUNT_MARGIN_MODE
ACCOUNT_MARGIN_MODE_RETAIL_NETTING: Literal[0]
ACCOUNT_MARGIN_MODE_EXCHANGE: Literal[1]
ACCOUNT_MARGIN_MODE_RETAIL_HEDGING: Literal[2]
# ENUM_BOOK_TYPE
BOOK_TYPE_SELL: Literal[1]
BOOK_TYPE_BUY: Literal[2]
BOOK_TYPE_SELL_MARKET: Literal[3]
BOOK_TYPE_BUY_MARKET: Literal[4]
# order send/check return codes
TRADE_RETCODE_REQUOTE: Literal[10004]
TRADE_RETCODE_REJECT: Literal[10006]
TRADE_RETCODE_CANCEL: Literal[10007]
TRADE_RETCODE_PLACED: Literal[10008]
TRADE_RETCODE_DONE: Literal[10009]
TRADE_RETCODE_DONE_PARTIAL: Literal[10010]
TRADE_RETCODE_ERROR: Literal[10011]
TRADE_RETCODE_TIMEOUT: Literal[10012]
TRADE_RETCODE_INVALID: Literal[10013]
TRADE_RETCODE_INVALID_VOLUME: Literal[10014]
TRADE_RETCODE_INVALID_PRICE: Literal[10015]
TRADE_RETCODE_INVALID_STOPS: Literal[10016]
TRADE_RETCODE_TRADE_DISABLED: Literal[10017]
TRADE_RETCODE_MARKET_CLOSED: Literal[10018]
TRADE_RETCODE_NO_MONEY: Literal[10019]
TRADE_RETCODE_PRICE_CHANGED: Literal[10020]
TRADE_RETCODE_PRICE_OFF: Literal[10021]
TRADE_RETCODE_INVALID_EXPIRATION: Literal[10022]
TRADE_RETCODE_ORDER_CHANGED: Literal[10023]
TRADE_RETCODE_TOO_MANY_REQUESTS: Literal[10024]
TRADE_RETCODE_NO_CHANGES: Literal[10025]
TRADE_RETCODE_SERVER_DISABLES_AT: Literal[10026]
TRADE_RETCODE_CLIENT_DISABLES_AT: Literal[10027]
TRADE_RETCODE_LOCKED: Literal[10028]
TRADE_RETCODE_FROZEN: Literal[10029]
TRADE_RETCODE_INVALID_FILL: Literal[10030]
TRADE_RETCODE_CONNECTION: Literal[10031]
TRADE_RETCODE_ONLY_REAL: Literal[10032]
TRADE_RETCODE_LIMIT_ORDERS: Literal[10033]
TRADE_RETCODE_LIMIT_VOLUME: Literal[10034]
TRADE_RETCODE_INVALID_ORDER: Literal[10035]
TRADE_RETCODE_POSITION_CLOSED: Literal[10036]
TRADE_RETCODE_INVALID_CLOSE_VOLUME: Literal[10038]
TRADE_RETCODE_CLOSE_ORDER_EXIST: Literal[10039]
TRADE_RETCODE_LIMIT_POSITIONS: Literal[10040]
TRADE_RETCODE_REJECT_CANCEL: Literal[10041]
TRADE_RETCODE_LONG_ONLY: Literal[10042]
TRADE_RETCODE_SHORT_ONLY: Literal[10043]
TRADE_RETCODE_CLOSE_ONLY: Literal[10044]
TRADE_RETCODE_FIFO_CLOSE: Literal[10045]
# functio error codes, last_error()
RES_S_OK: Literal[1]
RES_E_FAIL: Literal[-1]
RES_E_INVALID_PARAMS: Literal[-2]
RES_E_NO_MEMORY: Literal[-3]
RES_E_NOT_FOUND: Literal[-4]
RES_E_INVALID_VERSION: Literal[-5]
RES_E_AUTH_FAILED: Literal[-6]
RES_E_UNSUPPORTED: Literal[-7]
RES_E_AUTO_TRADING_DISABLED: Literal[-8]
RES_E_INTERNAL_FAIL: Literal[-10000]
RES_E_INTERNAL_FAIL_SEND: Literal[-10001]
RES_E_INTERNAL_FAIL_RECEIVE: Literal[-10002]
RES_E_INTERNAL_FAIL_INIT: Literal[-10003]
RES_E_INTERNAL_FAIL_CONNECT: Literal[-10004]
RES_E_INTERNAL_FAIL_TIMEOUT: Literal[-10005]


class AccountInfo(Protocol):
    login: int
    trade_mode: int
    leverage: int
    limit_orders: int
    margin_so_mode: int
    trade_allowed: bool
    trade_expert: bool
    margin_mode: int
    currency_digits: int
    fifo_close: bool
    balance: float
    credit: float
    profit: float
    equity: float
    margin: float
    margin_free: float
    margin_level: float
    margin_so_call: float
    margin_so_so: float
    margin_initial: float
    margin_maintenance: float
    assets: float
    liabilities: float
    commission_blocked: float
    name: str
    server: str
    currency: str
    company: str


class BookInfo(Protocol):
    type: int
    price: float
    volume: int
    volume_dbl: float


class TerminalInfo(Protocol):
    community_account: bool
    community_connection: bool
    connected: bool
    dlls_allowed: bool
    trade_allowed: bool
    tradeapi_disabled: bool
    email_enabled: bool
    ftp_enabled: bool
    notifications_enabled: bool
    mqid: bool
    build: int
    maxbars: int
    codepage: int
    ping_last: int
    community_balance: float
    retransmission: float
    company: str
    name: str
    language: str
    path: str
    data_path: str
    commondata_path: str


class Tick(Protocol):
    time: int
    bid: float
    ask: float
    last: float
    volume: float
    time_msc: int
    flags: int
    volume_real: float


class TradeOrder(Protocol):
    ticket: int
    time_setup: int
    time_setup_msc: int
    time_done: int
    time_done_msc: int
    time_expiration: int
    type: int
    type_time: int
    type_filling: int
    state: int
    magic: int
    position_id: int
    position_by_id: int
    reason: int
    volume_initial: float
    volume_current: float
    price_open: float
    sl: float
    tp: float
    price_current: float
    price_stoplimit: float
    symbol: str
    comment: str
    external_id: str


class TradePosition(Protocol):
    ticket: int
    time: int
    time_msc: int
    time_update: int
    time_update_msc: int
    type: int
    magic: int
    identifier: int
    reason: int
    volume: float
    price_open: float
    sl: float
    tp: float
    price_current: float
    swap: float
    profit: float
    symbol: str
    comment: str
    external_id: str


class TradeDeal(Protocol):
    ticket: int
    order: int
    time: int
    time_msc: int
    type: int
    entry: int
    magic: int
    position_id: int
    reason: int
    volume: float
    price: float
    commission: float
    swap: float
    profit: float
    fee: float
    symbol: str
    comment: str
    external_id: str


class TradeRequest(Protocol):
    action: int
    magic: int
    symbol: str
    volume: float
    price: float
    deviation: int
    type: int
    type_filling: int
    type_time: int
    comment: str
    sl: float
    tp: float
    position: int
    stoplimit: float
    expiration: int
    order: int


class MqlTradeCheckResult(Protocol):
    retcode: int  # Reply code
    balance: float  # Balance after the execution of the deal
    equity: float  # Equity after the execution of the deal
    profit: float  # Floating profit
    margin: float  # Margin requirements
    margin_free: float  # Free margin
    margin_level: float  # Margin level
    comment: str  # Comment to the reply code (description of the error)
    request: TradeRequest  # The original trading request


class SymbolInfo(Protocol):
    custom: bool
    chart_mode: int
    select: bool
    visible: bool
    session_deals: int
    session_buy_orders: int
    session_sell_orders: int
    volume: float
    volumehigh: float
    volumelow: float
    time: int
    digits: int
    spread: float
    spread_float: bool
    ticks_bookdepth: int
    trade_calc_mode: int
    trade_mode: int
    start_time: int
    expiration_time: int
    trade_stops_level: int
    trade_freeze_level: int
    trade_exemode: int
    swap_mode: int
    swap_rollover3days: int
    margin_hedged_use_leg: bool
    expiration_mode: int
    filling_mode: int
    order_mode: int
    order_gtc_mode: int
    option_mode: int
    option_right: int
    bid: float
    bidhigh: float
    bidlow: float
    ask: float
    askhigh: float
    asklow: float
    last: float
    lasthigh: float
    lastlow: float
    volume_real: float
    volumehigh_real: float
    volumelow_real: float
    option_strike: float
    point: float
    trade_tick_value: float
    trade_tick_value_profit: float
    trade_tick_value_loss: float
    trade_tick_size: float
    trade_contract_size: float
    trade_accrued_interest: float
    trade_face_value: float
    trade_liquidity_rate: float
    volume_min: float
    volume_max: float
    volume_step: float
    volume_limit: float
    swap_long: float
    swap_short: float
    margin_initial: float
    margin_maintenance: float
    session_volume: float
    session_turnover: float
    session_interest: float
    session_buy_orders_volume: float
    session_sell_orders_volume: float
    session_open: float
    session_close: float
    session_aw: float
    session_price_settlement: float
    session_price_limit_min: float
    session_price_limit_max: float
    margin_hedged: float
    price_change: float
    price_volatility: float
    price_theoretical: float
    price_greeks_delta: float
    price_greeks_theta: float
    price_greeks_gamma: float
    price_greeks_vega: float
    price_greeks_rho: float
    price_greeks_omega: float
    price_sensitivity: float
    basis: str
    category: str
    currency_base: str
    currency_profit: str
    currency_margin: str
    bank: str
    description: str
    exchange: str
    formula: str
    isin: bool
    name: str
    page: str
    path: str


class OrderSendResult(Protocol):
    retcode: int
    deal: int
    order: int
    volume: float
    price: float
    bid: float
    ask: float
    comment: str
    request_id: int
    retcode_external: int
    request: TradeRequest


def initialize(path=None, *, login: int = None, password: str = None, server: str = None, timeout: int = 60_000, portable: bool = False) -> bool:
    """
    Establish a connection with the MetaTrader 5 terminal.
    https://www.mql5.com/en/docs/python_metatrader5/mt5initialize_py
    """


def login(login: int, *, password: str = None, server: str = None, timeout: int = 60_000) -> bool:
    """
    Connect to a trading account using specified parameters.
    https://www.mql5.com/en/docs/python_metatrader5/mt5initialize_py
    """


def shutdown() -> None:
    """
    Close the previously established connection to the MetaTrader 5 terminal.
    https://www.mql5.com/en/docs/python_metatrader5/mt5shutdown_py
    """


def version() -> tuple[int, int, str] | None:
    """
    Return the MetaTrader 5 terminal version.
    https://www.mql5.com/en/docs/python_metatrader5/mt5version_py
    """


def last_error() -> tuple[int, str] | None:
    """
    Return data on the last error.
    https://www.mql5.com/en/docs/python_metatrader5/mt5lasterror_py
    """


def account_info() -> AccountInfo | None:
    """
    Get info on the current trading account.

    https://www.mql5.com/en/docs/python_metatrader5/mt5accountinfo_py
    """


def terminal_info() -> TerminalInfo | None:
    """
    Get the connected MetaTrader 5 client terminal status and settings.

    https://www.mql5.com/en/docs/python_metatrader5/mt5terminalinfo_py
    """


def symbols_total() -> int:
    """
    Get the number of all financial instruments in the MetaTrader 5 terminal.

    https://www.mql5.com/en/docs/python_metatrader5/mt5symbolstotal_py
    """


def symbols_get(*, group: str = None) -> tuple[SymbolInfo, ...] | None:
    """
    Get all financial instruments from the MetaTrader 5 terminal.

    https://www.mql5.com/en/docs/python_metatrader5/mt5symbolsget_py
    """


def symbol_info(symbol: str) -> SymbolInfo | None:
    """
    Get data on the specified financial instrument.

    https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfo_py
    """


def symbol_info_tick(symbol: str) -> Tick | None:
    """
    Get the last tick for the specified financial instrument.

    https://www.mql5.com/en/docs/python_metatrader5/mt5symbolinfotick_py
    """


def symbol_select(symbol, enable: bool = None) -> bool:
    """
    Select a symbol in the MarketWatch window or remove a symbol from the window.

    https://www.mql5.com/en/docs/python_metatrader5/mt5symbolselect_py
    """


def market_book_add(symbol: str) -> bool:
    """
    Subscribes the MetaTrader 5 terminal to the Market Depth change events for a specified symbol.

    https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookadd_py
    """


def market_book_get(symbol: str) -> tuple[BookInfo, ...] | None:
    """
    Returns a tuple from BookInfo featuring Market Depth entries for the specified symbol.

    https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookget_py
    """


def market_book_release(symbol: str) -> bool:
    """
    Cancels subscription of the MetaTrader 5 terminal to the Market Depth change events for a specified symbol.

    https://www.mql5.com/en/docs/python_metatrader5/mt5marketbookrelease_py
    """


def copy_rates_from(symbol: str, timeframe: int, date_from: datetime, count: int) -> np.ndarray | None:
    """
    Get bars from the MetaTrader 5 terminal starting from the specified date.

    https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrom_py
    """


def copy_rates_from_pos(symbol: str, timeframe: int, start_pos: int, count: int) -> np.ndarray | None:
    """
    Get bars from the MetaTrader 5 terminal starting from the specified index.

    https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrompos_py
    """


def copy_rates_range(symbol: str, timeframe: int, date_from: datetime, date_to: datetime) -> np.ndarray | None:
    """
    Get bars in the specified date range from the MetaTrader 5 terminal.

    https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesrange_py
    """


def copy_ticks_from(symbol: str, date_from: datetime, count: int, flags: Literal[-1, 1, 2]) -> np.ndarray | None:
    """
    Get ticks from the MetaTrader 5 terminal starting from the specified date.

    https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py
    """


def copy_ticks_range(symbol: str, date_from: datetime, date_to: datetime, flags: Literal[-1, 1, 2]) -> np.ndarray | None:
    """
    Get ticks for the specified date range from the MetaTrader 5 terminal.

    https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksrange_py
    """


def orders_total() -> int:
    """
    Get the number of active orders.

    https://www.mql5.com/en/docs/python_metatrader5/mt5orderstotal_py
    """


def orders_get(*, symbol: str = None, group: str = None, ticket: int = None) -> tuple[TradeOrder, ...] | None:
    """
    Get active orders with the ability to filter by symbol or ticket.

    https://www.mql5.com/en/docs/python_metatrader5/mt5ordersget_py
    """


def order_calc_margin(action: int, symbol: str, volume: float, price: float) -> float | None:
    """
    Return margin in the account currency to perform a specified trading operation.

    https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcmargin_py
    """


def order_calc_profit(action: int, symbol: str, volume: float, price_open: float, price_close: float) -> float | None:
    """
    Return profit in the account currency for a specified trading operation.

    https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcprofit_py
    """


def order_check(request: TradeRequest) -> MqlTradeCheckResult:
    """
    Check funds sufficiency for performing a required trading operation. Check result are returned as the MqlTradeCheckResult structure.

    https://www.mql5.com/en/docs/python_metatrader5/mt5ordercheck_py
    """


def order_send(request: TradeRequest) -> OrderSendResult:
    """
    Send a request to perform a trading operation from the terminal to the trade server.

    https://www.mql5.com/en/docs/python_metatrader5/mt5ordersend_py
    """


def positions_total() -> int:
    """
    Get the number of open positions.

    https://www.mql5.com/en/docs/python_metatrader5/mt5positionstotal_py
    """


def positions_get(*, symbol: str = None, group: str = None, ticket: int = None) -> tuple[TradePosition, ...] | None:
    """
    Get open positions with the ability to filter by symbol or ticket.

    https://www.mql5.com/en/docs/python_metatrader5/mt5positionsget_py
    """


def history_orders_total(date_from: datetime, date_to: datetime) -> int:
    """
    Get the number of orders in trading history within the specified interval.

    https://www.mql5.com/en/docs/python_metatrader5/mt5historyorderstotal_py
    """


def history_orders_get(date_from: datetime, date_to: datetime, *, group: str = None, ticket: int = None, position: int = None) -> tuple[TradeOrder, ...] | None:
    """
    Get orders from trading history with the ability to filter by ticket or position.

    https://www.mql5.com/en/docs/python_metatrader5/mt5historyordersget_py
    """


def history_deals_total(date_from: datetime, date_to: datetime) -> int:
    """
    Get the number of deals in trading history within the specified interval.

    https://www.mql5.com/en/docs/python_metatrader5/mt5historydealstotal_py
    """


def history_deals_get(date_from: datetime, date_to: datetime, *, group: str = None, ticket: int = None, position: int = None) -> tuple[TradeDeal, ...] | None:
    """
    Get deals from trading history within the specified interval with the ability to filter by ticket or position.

    https://www.mql5.com/en/docs/python_metatrader5/mt5historydealsget_py
    """
