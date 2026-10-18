"""Tests for scanner.py, the /api/decode route, and the demo page route."""
import io
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
from generator import generate_qr_code
from scanner import decode_qr_code
from app import app


# ---------- Unit tests: decode_qr_code ----------

def test_decode_round_trip():
    png = generate_qr_code("https://example.com/hello")
    assert decode_qr_code(png) == "https://example.com/hello"


def test_decode_empty_bytes_raises():
    with pytest.raises(ValueError):
        decode_qr_code(b"")


def test_decode_garbage_bytes_raises():
    with pytest.raises(ValueError):
        decode_qr_code(b"definitely not an image")


def test_decode_image_without_qr_raises_lookup():
    import cv2
    import numpy as np

    blank = np.full((200, 200, 3), 255, dtype=np.uint8)
    ok, buf = cv2.imencode(".png", blank)
    assert ok
    with pytest.raises(LookupError):
        decode_qr_code(buf.tobytes())


# ---------- Integration tests: routes ----------

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_decode_route_success(client):
    png = generate_qr_code("round trip text")
    response = client.post(
        "/api/decode",
        data={"image": (io.BytesIO(png), "qr.png")},
        content_type="multipart/form-data",
    )
    assert response.status_code == 200
    assert response.get_json()["text"] == "round trip text"


def test_decode_route_no_file(client):
    response = client.post("/api/decode")
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_decode_route_bad_image(client):
    response = client.post(
        "/api/decode",
        data={"image": (io.BytesIO(b"not an image"), "bad.png")},
        content_type="multipart/form-data",
    )
    assert response.status_code == 400


def test_decode_route_no_qr_found(client):
    import cv2
    import numpy as np

    ok, buf = cv2.imencode(".png", np.full((200, 200, 3), 255, dtype=np.uint8))
    response = client.post(
        "/api/decode",
        data={"image": (io.BytesIO(buf.tobytes()), "blank.png")},
        content_type="multipart/form-data",
    )
    assert response.status_code == 404


def test_index_serves_demo_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"QR Toolkit" in response.data
    response.close()
