"""QR code generation logic."""
import io
import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H

_ERROR_LEVELS = {
    "L": ERROR_CORRECT_L,
    "M": ERROR_CORRECT_M,
    "Q": ERROR_CORRECT_Q,
    "H": ERROR_CORRECT_H,
}

MAX_DATA_LENGTH = 2000  # practical upper bound before QR capacity/readability suffers


def generate_qr_code(data: str, box_size: int = 10, border: int = 4, error_correction: str = "M") -> bytes:
    """
    Generate a QR code PNG image as bytes from the given text/URL.

    Raises:
        ValueError: if data is empty, too long, or error_correction is invalid.
    """
    if data is None or not isinstance(data, str) or data.strip() == "":
        raise ValueError("data must be a non-empty string")

    if len(data) > MAX_DATA_LENGTH:
        raise ValueError(f"data exceeds maximum length of {MAX_DATA_LENGTH} characters")

    if error_correction not in _ERROR_LEVELS:
        raise ValueError(f"error_correction must be one of {list(_ERROR_LEVELS.keys())}")

    if box_size <= 0 or border < 0:
        raise ValueError("box_size must be positive and border must be non-negative")

    qr = qrcode.QRCode(
        error_correction=_ERROR_LEVELS[error_correction],
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return buffer.getvalue()
