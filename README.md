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


🔎 How the solution is achieved
1. Community 🌐

The script connects to the web community via HTTP requests to fetch shared images.
We use the requests library to download the image content.

2. Respect 🙏

Not every connection works. We wrap everything in try/except and use response.raise_for_status() to respect HTTP status codes (404, 500, etc.).

3. Sharing 📂

We organize images into a Fetched_Images/ folder so they can be easily shared later.
We use os.makedirs("Fetched_Images", exist_ok=True) to create it safely.

4. Practicality 🛠️

We extract filenames from the URL using urllib.parse.urlparse. If no name is found, we generate a fallback like downloaded_image.jpg.


Respect: Handle errors gracefully without crashing


Sharing: Organize the fetched images for later sharing

Practicality: Create a tool that serves a real need
