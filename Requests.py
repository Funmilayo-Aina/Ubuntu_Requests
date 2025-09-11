import requests
import os
from urllib.parse import urlparse
import hashlib

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get multiple URLs from user (comma-separated)
    urls = input("Enter the URLs of the images you want to fetch (comma-separated): ").split(",")
    urls = [u.strip() for u in urls if u.strip()]
    
    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)
    
    # Keep track of downloaded file hashes to avoid duplicates
    downloaded_hashes = set()
    
    for url in urls:
        try:
            print(f"\nFetching: {url}")
            
            # Precaution: Skip base64 or invalid schemes
            if url.startswith("data:") or not url.startswith(("http://", "https://")):
                print("✗ Skipped (invalid or unsafe URL scheme).")
                continue
            
            # Fetch with timeout and respect server
            response = requests.get(url, timeout=10, stream=True)
            response.raise_for_status()  # Raise exception for HTTP errors
            
            # Check important headers before saving
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print("✗ Skipped (content is not an image).")
                continue
            
            # Generate hash of content to check duplicates
            file_hash = hashlib.md5(response.content).hexdigest()
            if file_hash in downloaded_hashes:
                print("✗ Skipped (duplicate image).")
                continue
            downloaded_hashes.add(file_hash)
            
            # Extract filename from URL or generate one
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            
            if not filename or "." not in filename:
                # Guess extension from Content-Type if missing
                ext = content_type.split("/")[-1] if "/" in content_type else "jpg"
                filename = f"image_{file_hash[:8]}.{ext}"
            
            # Save the image
            filepath = os.path.join("Fetched_Images", filename)
            with open(filepath, 'wb') as f:
                f.write(response.content)
                
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")
            print("✓ Connection strengthened. Community enriched.")
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error: {e}")
        except Exception as e:
            print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    main()
