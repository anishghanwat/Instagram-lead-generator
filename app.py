from flask import Flask, render_template, request, jsonify
from instagram_lead_generator import search_instagram_accounts, parse_results
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

print("Starting Flask application...")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    logger.info(f"Route '/' accessed with method: {request.method}")
    results = []
    if request.method == 'POST':
        logger.info("POST request received")
        logger.info(f"Form data: {request.form}")
        location = request.form.get('location')
        niche = request.form.get('niche')

        logger.info(f"Searching for: Location: {location}, Niche: {niche}")
        search_results = search_instagram_accounts(location, niche)
        logger.info(f"Raw search results: {search_results}")
        if search_results:
            results = parse_results(search_results)
            logger.info(f"Parsed results: {results}")
        else:
            results = [{"error": "Failed to retrieve results. Please try again later."}]
            logger.error("Failed to retrieve results")
    else:
        logger.info("GET request received")
    
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)

# Remove this line to avoid the duplicate print
# print("Flask application script completed")
