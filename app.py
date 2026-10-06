import socket
from urllib.parse import urlparse

from flask import Flask, render_template, request

app = Flask(__name__)


def clean_url(raw_url: str) -> str:
    """Normalize the input so it can be resolved as a hostname."""
    value = raw_url.strip()
    if not value:
        raise ValueError("Please enter a valid URL or hostname.")

    if "://" not in value:
        value = f"https://{value}"

    parsed = urlparse(value)
    host = parsed.hostname or parsed.netloc

    if not host:
        raise ValueError("Please enter a valid URL or hostname.")

    return host


def get_ip_address(url: str) -> str:
    """Return the IPv4 address for a given domain name."""
    host = clean_url(url)
    try:
        return socket.gethostbyname(host)
    except socket.gaierror as exc:
        raise ValueError(f"Could not find an IP address for '{host}'.") from exc


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        user_url = request.form.get("url", "")
        try:
            result = get_ip_address(user_url)
        except ValueError as exc:
            error = str(exc)

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
