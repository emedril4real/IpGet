# URL IP Lookup Tool

A simple portfolio project that takes a URL or hostname and returns its IP address.

## Features
- Accepts a website URL or hostname
- Resolves the domain to an IP address using Python's socket library
- Includes a clean Flask web interface
- Easy to run locally and push to GitHub

## Project structure
- `app.py` — Flask app and lookup logic
- `templates/index.html` — web interface
- `static/styles.css` — styling
- `tests/test_app.py` — validation tests
- `requirements.txt` — dependencies

## Run locally

1. Open a terminal in this project folder.
2. Create and activate a virtual environment if needed.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the app:

```bash
python app.py
```

5. Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Example

Input:

```text
example.com
```

Result:

```text
172.66.147.243
```

Note: the exact IP may vary depending on your DNS resolver and network.

## GitHub portfolio note

This project is designed to be a simple, practical tool that demonstrates:
- Python web development
- DNS and networking basics
- Input validation and user-friendly output
- Clean project structure for GitHub showcasing

## Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-github-repository-url>
git push -u origin main
```
