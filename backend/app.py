"""Flask app for QR generation and decoding, plus the demo frontend."""
import base64
from flask import Flask, request, jsonify, send_from_directory
from generator import generate_qr_code
from scanner import decode_qr_code

# Serve the demo page from ../frontend so one command runs the whole MVP
app = Flask(__name__, static_folder="../frontend", static_url_path="/static")


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


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


@app.route("/api/decode", methods=["POST"])
def decode():
    upload = request.files.get("image")
    if upload is None:
        return jsonify({"error": "no image uploaded (expected form field 'image')"}), 400

    try:
        text = decode_qr_code(upload.read())
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except LookupError as e:
        return jsonify({"error": str(e)}), 404

    return jsonify({"text": text}), 200


if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=5000)
