from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

BASE_SEARCH_URL = "/api/"


class TestWikiSearch:
    def test_get_invalid_term(self):
        resp = client.get(f"{BASE_SEARCH_URL}search_term/Noam_Polak?k=1")
        assert resp.json() == []

    def test_get_valid_term_one_result(self):
        term = "Tabby cat"
        k = 1
        resp = client.get(f"{BASE_SEARCH_URL}search_term/{term}?k={k}")
        json_res = resp.json()
        assert len(json_res) == 1
        assert json_res[0]["title"] == "Tabby cat"

    def test_get_valid_term_many_results(self):
        term = "python"
        k = 3
        resp = client.get(f"{BASE_SEARCH_URL}search_term/{term}?k={k}")
        json_res = resp.json()
        assert len(json_res) == 3
        assert term in resp.json()[0]["title"].lower()
