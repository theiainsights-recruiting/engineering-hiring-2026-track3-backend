"""Companies-for-theme endpoint with per-customer entitlements."""

import logging

from fastapi import Depends, FastAPI, HTTPException

from .auth import Customer, get_customer
from .store import fetch_companies_for_theme, theme_exists

logger = logging.getLogger(__name__)

app = FastAPI()

_response_cache: dict[str, dict] = {}


@app.get("/v1/themes/{tiic_id}/companies")
async def companies_for_theme(
    tiic_id: str, customer: Customer = Depends(get_customer)
) -> dict:
    cached = _response_cache.get(tiic_id)
    if cached is not None:
        return cached

    if not theme_exists(tiic_id):
        raise HTTPException(status_code=404)

    rows = await fetch_companies_for_theme(tiic_id)
    visible = [r for r in rows if r["sector"] in customer.entitled_sectors]
    if not visible:
        # 404, not 403: we don't reveal which themes exist outside a
        # customer's entitlement (API guidelines §4).
        raise HTTPException(status_code=404)

    payload = {
        "tiic_id": tiic_id,
        "count": len(visible),
        "companies": visible,
    }
    _response_cache[tiic_id] = payload
    logger.debug("cached %s (%d companies)", tiic_id, len(visible))
    return payload
