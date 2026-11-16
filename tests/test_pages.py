"""Checks that every page in the app loads without crashing."""

from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).parent.parent
PAGES = [ROOT / "Home.py"] + sorted(ROOT.glob("pages/*.py"))


@pytest.mark.parametrize("page", PAGES, ids=lambda p: p.name)
def test_page_runs(page):
    app = AppTest.from_file(str(page)).run()
    assert not app.exception
