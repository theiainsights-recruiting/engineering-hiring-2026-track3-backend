"""API-key authentication."""

from dataclasses import dataclass

from fastapi import Header, HTTPException

from .store import lookup_api_key


@dataclass(frozen=True)
class Customer:
    customer_id: str
    entitled_sectors: frozenset[str]


async def get_customer(x_api_key: str = Header()) -> Customer:
    record = await lookup_api_key(x_api_key)
    if record is None:
        raise HTTPException(status_code=401)
    return Customer(
        customer_id=record["customer_id"],
        entitled_sectors=frozenset(record["entitled_sectors"]),
    )
