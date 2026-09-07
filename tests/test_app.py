"""Endpoint tests for GET /v1/themes/{tiic_id}/companies."""

from fastapi.testclient import TestClient

from api.app import app

client = TestClient(app)

URL = "/v1/themes/{}/companies"


def test_missing_or_unknown_key_is_401():
    assert client.get(URL.format("cloud-computing")).status_code == 401
    r = client.get(URL.format("cloud-computing"), headers={"X-API-Key": "nope"})
    assert r.status_code == 401


def test_unknown_theme_is_404():
    r = client.get(URL.format("no-such-theme"), headers={"X-API-Key": "key-alpha"})
    assert r.status_code == 404


def test_no_entitled_sectors_in_theme_is_404():
    # bravo buys information-technology only; battery-materials is all materials.
    r = client.get(URL.format("battery-materials"), headers={"X-API-Key": "key-bravo"})
    assert r.status_code == 404


def test_happy_path_returns_only_entitled_sectors():
    r = client.get(URL.format("cloud-computing"), headers={"X-API-Key": "key-bravo"})
    assert r.status_code == 200
    body = r.json()
    assert body["tiic_id"] == "cloud-computing"
    assert body["count"] == len(body["companies"]) == 1
    assert {c["sector"] for c in body["companies"]} == {"information-technology"}
