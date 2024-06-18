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

