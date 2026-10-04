"""Unit tests for generator.py and integration tests for the /api/generate route."""
import base64
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from generator import generate_qr_code, MAX_DATA_LENGTH
from app import app


# ---------- Unit tests: generate_qr_code ----------

def test_generate_qr_code_returns_png_bytes():
    result = generate_qr_code("https://example.com")
    assert isinstance(result, bytes)
    # PNG files start with this magic header
    assert result[:8] == b"\x89PNG\r\n\x1a\n"


def test_generate_qr_code_empty_string_raises():
    with pytest.raises(ValueError):
        generate_qr_code("")


def test_generate_qr_code_whitespace_only_raises():
    with pytest.raises(ValueError):
        generate_qr_code("   ")


def test_generate_qr_code_none_raises():
    with pytest.raises(ValueError):
        generate_qr_code(None)


def test_generate_qr_code_too_long_raises():
    with pytest.raises(ValueError):
        generate_qr_code("a" * (MAX_DATA_LENGTH + 1))


def test_generate_qr_code_invalid_error_correction_raises():
    with pytest.raises(ValueError):
        generate_qr_code("test", error_correction="Z")


def test_generate_qr_code_invalid_box_size_raises():
    with pytest.raises(ValueError):
        generate_qr_code("test", box_size=0)


def test_generate_qr_code_negative_border_raises():
    with pytest.raises(ValueError):
        generate_qr_code("test", border=-1)


def test_generate_qr_code_custom_box_size_changes_output():
    small = generate_qr_code("test", box_size=4)
    large = generate_qr_code("test", box_size=20)
    assert len(large) > len(small)


@pytest.mark.parametrize("level", ["L", "M", "Q", "H"])
def test_generate_qr_code_all_error_correction_levels(level):
    result = generate_qr_code("test", error_correction=level)
    assert isinstance(result, bytes)


# ---------- Integration tests: /api/generate route ----------

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_generate_route_success(client):
    response = client.post("/api/generate", json={"text": "https://example.com"})
    assert response.status_code == 200
    data = response.get_json()
    assert "image_base64" in data
    # confirm it decodes back to valid PNG bytes
    decoded = base64.b64decode(data["image_base64"])
    assert decoded[:8] == b"\x89PNG\r\n\x1a\n"


def test_generate_route_missing_text(client):
    response = client.post("/api/generate", json={})
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_generate_route_empty_text(client):
    response = client.post("/api/generate", json={"text": ""})
    assert response.status_code == 400


def test_generate_route_no_body(client):
    response = client.post("/api/generate")
    assert response.status_code == 400


def test_generate_route_custom_params(client):
    response = client.post(
        "/api/generate",
        json={"text": "test", "box_size": 15, "border": 2, "error_correction": "H"},
    )
    assert response.status_code == 200
