# this function is used to append the json data to cloud storage file
import json

from google.cloud import storage


def append_json_to_gcs(bucket_name, file_name, data):
    try:
        storage_client = storage.Client()  # Initialize a client
        bucket = storage_client.bucket(bucket_name)  # Get the bucket
        blob = bucket.blob(file_name)  # Get the blob (file) in the bucket
    except Exception as e:
        return f"Error initializing GCS client or accessing bucket/blob: {e}"

    try:
        if blob.exists():  # Check if the blob exists
            existing_data = json.loads(blob.download_as_text())  # Download the existing data
            # If the existing data is a dictionary, convert it to a list of dictionaries
            if isinstance(existing_data, dict):
                existing_data = [existing_data]
        else:  # If the file does not exist, start with an empty list
            existing_data = []
    except Exception as e:
        return f"Error checking blob existence or downloading existing data: {e}"

    try:
        existing_data.append(data)  # Append the new data
        updated_json_data = json.dumps(existing_data, indent=4)  # Convert the updated data to JSON string
    except Exception as e:
        return f"Error appending new data or converting to JSON: {e}"

    try:
        # Upload the JSON string to the blob
        blob.upload_from_string(updated_json_data, content_type='application/json')
    except Exception as e:
        return f"Error uploading updated data to GCS: {e}"

    return f"Data appended to {file_name} in bucket {bucket_name}."
