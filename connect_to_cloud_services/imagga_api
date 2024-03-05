# import requests

# # API credentials
# api_key = 'acc_f7fdd2eb8b0f369'
# api_secret = 'fa10d16de4c930c643cfb106f4b3d0f2'

# # API endpoint
# endpoint = 'https://api.imagga.com/v2/tags'

# # Image URL
# image_url = 'images_to_test\fruits.jpg'

# # Basic authentication header
# auth_header = {
#     'Authorization': 'Basic YWNjX2Y3ZmRkMmViOGIwZjM2OTpmYTEwZDE2ZGU0YzkzMGM2NDNjZmIxMDZmNGIzZDBmMg=='
# }

# # Request parameters
# params = {
#     'image_url': image_url
# }

# try:
#     # Sending GET request to Imagga API
#     response = requests.get(endpoint, params=params, headers=auth_header)
    
#     # Checking if the request was successful
#     if response.status_code == 200:
#         # Parsing the JSON response
#         data = response.json()
        
#         # Extracting tags from the response
#         tags = data['result']['tags']
        
#         # Printing the tags
#         print("Tags for the image:")
#         for tag in tags:
#             print(tag['tag']['en'], "-", tag['confidence'])
#     else:
#         print("Error:", response.status_code, response.text)
# except Exception as e:
#     print("Error occurred:", str(e))

import requests

# API credentials
api_key = 'acc_f7fdd2eb8b0f369'
api_secret = 'fa10d16de4c930c643cfb106f4b3d0f2'

# API endpoint
endpoint = 'https://api.imagga.com/v2/tags'

# Local image file path
image_path = 'connect_to_cloud_services\images_to_test\\fruits.jpg'  # Provide the path to your local image file

# Basic authentication header
auth_header = {
    'Authorization': 'Basic YWNjX2Y3ZmRkMmViOGIwZjM2OTpmYTEwZDE2ZGU0YzkzMGM2NDNjZmIxMDZmNGIzZDBmMg=='
}

# Opening the image file
with open(image_path, 'rb') as file:
    # Creating a files dictionary to upload the image
    files = {
        'image': file
    }

    try:
        # Sending POST request to Imagga API
        response = requests.post(endpoint, files=files, headers=auth_header)

        # Checking if the request was successful
        if response.status_code == 200:
            # Parsing the JSON response
            data = response.json()

            # Extracting tags from the response
            tags = data['result']['tags']

            # Printing the tags
            print("Tags for the image:")
            for tag in tags:
                if float(tag['confidence']) > 20:
                    print(tag['tag']['en'], "-", tag['confidence'])
        else:
            print("Error:", response.status_code, response.text)
    except Exception as e:
        print("Error occurred:", str(e))
