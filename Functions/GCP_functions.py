from google.cloud import storage
import json


from google.cloud import storage
import json

def append_json_to_gcs(bucket_name, file_name, data):
    try:
        storage_client = storage.Client()  # Initialize a client
        bucket = storage_client.bucket(bucket_name)  # Get the bucket
        blob = bucket.blob(file_name)  # Get the blob (file) in the bucket
    except Exception as e:
        return f"Error initializing GCS client or accessing bucket/blob: {e}"

    try:
        if blob.exists():  # Check if the blob exists
            existing_data = blob.download_as_text()  # Download the existing data
            if existing_data.strip():  # If the file is not empty
                existing_data += '\n'  # Add a newline to separate JSON objects
        else:
            existing_data = ""
    except Exception as e:
        return f"Error checking blob existence or downloading existing data: {e}"

    try:
        new_data = json.dumps(data)  # Convert the new data to JSON string
        updated_data = existing_data + new_data  # Concatenate the existing data with the new data
    except Exception as e:
        return f"Error appending new data or converting to JSON: {e}"

    try:
        blob.upload_from_string(updated_data, content_type='application/json')
    except Exception as e:
        return f"Error uploading updated data to GCS: {e}"

    return f"Data appended to {file_name} in bucket {bucket_name}."

