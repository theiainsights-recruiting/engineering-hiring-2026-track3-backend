"""Data access layer.

In-memory fixtures standing in for the production store; the real service
reads Postgres through the same interface.
"""

_THEMES: set[str] = {"cloud-computing", "battery-materials", "nuclear-energy"}

_COMPANIES: dict[str, list[dict]] = {
    "cloud-computing": [
        {"company_id": "C001", "name": "Example Corp", "sector": "information-technology"},
        {"company_id": "C009", "name": "Grid Example", "sector": "utilities"},
    ],
    "battery-materials": [
        {"company_id": "C002", "name": "Lithium Example", "sector": "materials"},
    ],
    "nuclear-energy": [
        {"company_id": "C003", "name": "Fission Example", "sector": "industrials"},
    ],
}

_API_KEYS: dict[str, dict] = {
    "key-alpha": {
        "customer_id": "alpha",
        "entitled_sectors": ["information-technology", "materials", "industrials", "utilities"],
    },
    "key-bravo": {"customer_id": "bravo", "entitled_sectors": ["information-technology"]},
}


def theme_exists(tiic_id: str) -> bool:
    # The theme catalogue (~2,000 ids) is held in memory from startup, so
    # this is a set lookup, not I/O; only per-theme rows go to the store.
    return tiic_id in _THEMES


async def fetch_companies_for_theme(tiic_id: str) -> list[dict]:
    return list(_COMPANIES.get(tiic_id, []))


async def lookup_api_key(key: str) -> dict | None:
    return _API_KEYS.get(key)
