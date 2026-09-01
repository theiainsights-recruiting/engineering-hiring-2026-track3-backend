"""API key -> entitled TIIC levels."""

ENTITLEMENTS: dict[str, dict] = {
    "key-alpha": {
        "customer_id": "alpha",
        "levels": ["sector", "industry", "sub_industry", "major_theme", "micro_theme"],
    },
    "key-bravo": {
        "customer_id": "bravo",
        "levels": ["sector", "industry"],
    },
    "key-charlie": {
        "customer_id": "charlie",
        "levels": ["major_theme", "micro_theme"],
    },
}
