from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from google.cloud import storage
import Functions.data_collector_functions as data_collector
import Functions.GCP_functions as GCP_functions
import logging

app = Flask(__name__)




@app.route('/collect', methods=['POST'])
def collectData():
    # logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info('Starting the web scraping process.')

    global response
    url = (request.get_json())["url"]

    # throw an exception incase the url not found
    if not url:
        return jsonify({'error': 'URL parameter is missing'}), 400
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        html = response.text
        soup = BeautifulSoup(html, 'lxml')

        post_title = (data_collector.getPostTitle(soup))["post_title"]  # get post title
        post_tags = (data_collector.getPostTitle(soup))["post_tags"]  # get post tags

        # get post type
        post_type = data_collector.getPostType(soup)
        # the post type must be a product
        if post_type != "product":
            return jsonify({'error': 'The post type must be of type product'}), 400

        domain = data_collector.getDomain(soup)  # get domain
        description = data_collector.getPostDescription(soup)  # get description
        post_image = data_collector.getPostImage(soup)  # get post image
        post_currency = data_collector.getPostCurrency(soup)  # get post currency

        post_discount_price = data_collector.getPostPrice(soup)["post_discount_price"]  # get post discount price
        post_base_price = data_collector.getPostPrice(soup)["post_base_price"]  # get post base  price

        post_vendor = data_collector.getPostVendor(soup)  # get post vendor
        post_date = datetime.now().date().isoformat()  # get post date
        post_id = data_collector.getPostId(soup)  # get post id
        post_items = data_collector.getPostItems(soup)  # get post items
        data = {
            "post_title": post_title,
            "post_tags": post_tags,
            "post_url": url,
            "post_type": post_type,
            "domain": domain,
            "description": description,
            "post_image": post_image,
            "post_currency": post_currency,
            "post_discount_price": post_discount_price,
            "post_base_price": post_base_price,
            "post_vendor": post_vendor,
            "post_date": post_date,
            "post_id": post_id,
            "post_items": post_items,
            "ip": "172.69.87.193",
            "user_id": "user123",
            "device": "Mobile"
        }
        return {"message": GCP_functions.append_json_to_gcs("data-pulse", "data/logs.json", data)}
    # exception incase the url is wrong or any http exceptions
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f'HTTP error occurred: {http_err}'}), response.status_code
    except requests.exceptions.ConnectionError as conn_err:
        return jsonify({'error': f'Connection error occurred: {conn_err}'}), 500
    except requests.exceptions.Timeout as timeout_err:
        return jsonify({'error': f'Timeout error occurred: {timeout_err}'}), 500
    except requests.exceptions.RequestException as req_err:
        return jsonify({'error': f'Invalid URL or request error occurred: {req_err}'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
