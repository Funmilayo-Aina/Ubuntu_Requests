# Ubuntu_Requests
Python Libraries

## Python Libraries Assignment
#### **Description**

#### Ubuntu-Inspired Image Fetcher Assignment

--The Wisdom of Ubuntu: "I am because we are"

In the spirit of Ubuntu, which emphasizes community and sharing, your task is to create a program that connects to the global community of the internet, respectfully fetches shared resources, and organizes them for later appreciation.

##### Your Task

* Create a Python script that:

Prompts the user for a URL containing an image

Creates a directory called "Fetched_Images" if it doesn't exist

Downloads the image from the provided URL

Saves it to the Fetched_Images directory with an appropriate filename

Handles errors gracefully, respecting that not all connections succeed

#### Requirements

Use the requests library to fetch the image

Check for HTTP errors and handle them appropriately

Create the directory if it doesn't exist using os.makedirs() with exist_ok=True

Extract the filename from the URL or generate one if not available

Save the image in binary mode

**Ubuntu Principles to Implement**

Community: Your program should connect to the wider web community



The script connects to the web community via HTTP requests to fetch shared images.
 requests library is used to download the image content.

2. Respect 🙏

Not every connection works. Everything  was trackded with with try/except.
Errors were handled gracefully without crashing

3. Sharing 📂

The organized imagesin the Fetched_Images/ folder can be shared by Ubuntu community later.

os.makedirs("Fetched_Images", exist_ok=True)  was used to fetch and to create images safely.

4. Practicality 🛠️

Filenames were extracted from the URL using urllib.parse.urlparse. If no name is found, a fallback generated like downloaded_image.jpg.

The shared images will reduce the burden of image files sharing in the Ubuntu community.
