import requests
import os
import tempfile

def download_image(url):
    try:
        # Send a GET request to the URL to fetch the image data
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        # Create the directory if it doesn't exist
        save_dir = os.path.join("PyOneDark_Qt_Widgets_Modern_GUI", "gui", "connect_to_cloud_services")
        os.makedirs(save_dir, exist_ok=True)

        # Create a temporary file with .jpg extension in the specified directory
        temp_file = tempfile.NamedTemporaryFile(suffix=".jpg", dir=save_dir, delete=False)
        temp_path = temp_file.name

        # Write the image data to the temporary file
        with open(temp_path, "wb") as file:
            file.write(response.content)

        return temp_path  # Return the path to the downloaded image
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None

# Example usage:
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Red_Apple.jpg/1200px-Red_Apple.jpg"
downloaded_image_path = download_image(image_url)
if downloaded_image_path:
    print(f"Image downloaded successfully to: {downloaded_image_path}")
else:
    print("Failed to download image.")
