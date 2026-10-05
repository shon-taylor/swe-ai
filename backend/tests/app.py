"""Flask app for QR generation. Returns base64-encoded PNG images."""
import base64
from flask import Flask, request, jsonify
from generator import generate_qr_code

app = Flask(__name__)


@app.route("/api/generate", methods=["POST"])
def generate():
    body = request.get_json(silent=True) or {}
    text = body.get("text")
    box_size = body.get("box_size", 10)
    border = body.get("border", 4)
    error_correction = body.get("error_correction", "M")

    try:
        png_bytes = generate_qr_code(
            data=text,
            box_size=box_size,
            border=border,
            error_correction=error_correction,
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    encoded = base64.b64encode(png_bytes).decode("utf-8")
    return jsonify({"image_base64": encoded}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)


# This Flask app provides an endpoint to generate QR codes.
# The generated QR codes are returned as base64-encoded PNG images.
# Example request:
# POST /api/generate
# {
#     "text": "https://example.com",
#     "box_size": 10,
#     "border": 4,
#     "error_correction": "M"
# }
# Example response:
# {
#     "image_base64": "<base64-encoded PNG>"
# }
