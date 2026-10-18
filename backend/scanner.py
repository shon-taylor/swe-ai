"""QR code decoding logic."""
import cv2
import numpy as np


def decode_qr_code(image_bytes: bytes) -> str:
    """
    Decode a QR code from raw image bytes (PNG/JPEG/etc.) and return its text.

    Raises:
        ValueError: if the bytes are empty or can't be read as an image.
        LookupError: if the image is valid but no QR code could be found/decoded.
    """
    if not image_bytes:
        raise ValueError("image data is empty")

    arr = np.frombuffer(image_bytes, dtype=np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("could not read image data")

    text, _, _ = cv2.QRCodeDetector().detectAndDecode(img)
    if not text:
        raise LookupError("no QR code found in image")
    return text
