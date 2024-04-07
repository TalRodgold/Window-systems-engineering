from typing import Optional
import requests
import os
import tempfile
from consts import *

def delete_file(file_path: str):
    try:
        os.remove(file_path)
        print(f"File deleted successfully: {file_path}")
    except Exception as e:
        print(f"Error deleting file: {e}")


def get_imagga(image_path: str) -> list[str]:
    # Opening the image file
    with open(image_path, 'rb') as file:
        # Creating a files dictionary to upload the image
        files = {
            'image': file
        }
        try:
            # Sending POST request to Imagga API
            response = requests.post(IMAGGA_API, files=files, headers=IMAGGA_AUTH_HEADER)

            # Checking if the request was successful
            if response.status_code == 200:
                # Parsing the JSON response
                data = response.json()

                # Extracting tags from the response
                tags = data['result']['tags']

                # Printing the tags
                resault = []
                for tag in tags:
                    if float(tag['confidence']) > IMAGGA_CONFIDENCE:
                        resault.append(tag['tag']['en'])
                return resault
            else:
                raise("Error:", response.status_code, response.text)
        except Exception as e:
            print("Error occurred:", str(e))


def download_image(url: str) -> Optional[str]:
    try:
        # Send a GET request to the URL to fetch the image data
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        # Create the directory if it doesn't exist
        save_dir = TMP_FILE_PATH
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


def main(image_url: str):
        
    downloaded_image_path = download_image(image_url)
    if downloaded_image_path:
        resault = get_imagga(downloaded_image_path)
        for i in resault:
            print(i)
        delete_file(downloaded_image_path)
    else:
        print("Failed to download image.")

if __name__ == "__main__":
    main("https://i0.wp.com/post.medicalnewstoday.com/wp-content/uploads/sites/3/2022/07/what_to_know_apples_green_red_1296x728_header-1024x575.jpg?w=1155&h=1528")