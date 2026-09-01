"""Starter — restructure freely."""

import json
from pathlib import Path

from fastapi import FastAPI

from entitlements import ENTITLEMENTS

app = FastAPI()

DATA = json.loads(Path(__file__).with_name("data.json").read_text())


# TODO: GET /companies/{company_id}/classifications?level=<optional>
