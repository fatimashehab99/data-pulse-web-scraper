# Web Scraping Flask API

This project is a Flask-based web scraping API that collects product data from a given URL and stores the data in Google Cloud Storage (GCS). The project includes robust error handling and various utility functions to extract specific elements from the HTML content.

## Features

- Web scraping using BeautifulSoup and requests
- Collects product data such as title, tags, type, domain, description, image, currency, prices, vendor, date, ID, and items
- Stores collected data in a GCS bucket
- Handles various error scenarios gracefully
- Easily extensible and maintainable
  
## Error Handling

The API handles various error scenarios, such as invalid URLs, connection errors, timeouts, and HTTP errors, and returns appropriate error messages.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Sample of the JSON data 

```json
{
    "post_title": "Palladio Liquid Blush",
    "post_tags": [
        "Makeup"
    ],
    "post_url": "https://feel22.com/products/palladio-liquid-blush?variant=45138684608650",
    "post_type": "product",
    "domain": "Feel22",
    "description": "Get Palladio Liquid Blush delivered from Feel22 to your home anywhere in Lebanon and discover our wide range of Perfumes, Skincare And Beauty products. Shop Online Now!",
    "post_image": "http://feel22.com/cdn/shop/files/BundlesPackshotsCarla-2024-06-12T121131.993_1024x1024.png?v=1718183192",
    "post_currency": "USD",
    "post_discount_price": "$0 USD",
    "post_base_price": "$12.17 USD\n",
    "post_vendor": "Palladio",
    "post_date": "2024-06-18",
    "post_id": "8193553858698",
    "post_items": [
        "Sunny Coral",
        "Rose Cloud",
        "Dainty",
        "Dusty Rose",
        "Cool Pink",
        "Deep Fuchsia"
    ],
    "ip": "172.69.87.193",
    "user_id": "user123",
    "device": "Mobile"
}
