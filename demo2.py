import requests
from PIL import Image, ImageTk
from io import BytesIO
import os
import pathlib
import subprocess
import tkinter as tk

class DogImageFetcher:
    def __init__(self):
        self.api_url = "https://dog.ceo/api/breeds/image/random"
        self.save_path = "doggy.jpg"

    def fetch_image_url(self):
        """Fetches the URL of a random dog image."""
        try:
            custom_url = input("Do you have a custom API URL? (yes/no): ").strip().lower()
            api = input("Enter your custom API URL: ") if custom_url == "yes" else self.api_url
            
            response = requests.get(api, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data.get("message")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching image URL: {e}")
            return None

    def get_save_location(self):
        """Prompts user for a save location, defaulting to the current directory."""
        custom_location = input("Do you have a preferred save location? (yes/no): ").strip().lower()
        
        if custom_location == "yes":
            path = input("Enter full path to save the image: ").strip()
            save_path = pathlib.Path(path)
            if not save_path.parent.exists():
                print("Invalid path. Saving locally instead.")
                return self.save_path
            return str(save_path)
        return self.save_path

    def download_and_save_image(self, image_url, save_path):
        """Downloads the image and saves it."""
        try:
            response = requests.get(image_url, timeout=10)
            response.raise_for_status()
            
            image = Image.open(BytesIO(response.content))
            image.save(save_path)
            print(f"Image saved at {save_path}")
            return save_path
        except requests.exceptions.RequestException as e:
            print(f"Error downloading image: {e}")
        except Exception as e:
            print(f"Error saving image: {e}")
        return None

    def open_image_windows(self, image_path):
        """Opens image with the default Windows image viewer."""
        try:
            if os.path.exists(image_path):
                subprocess.run(["start", image_path], shell=True, check=True)
                print("Displaying image...")
            else:
                print("File not found.")
        except Exception as e:
            print(f"Error opening image: {e}")

    def open_image_tkinter(self, image_path):
        """Opens image in a Tkinter window."""
        print("Displaying image...")
        window = tk.Tk()
        window.title("Here is your dog!")
        image = Image.open(image_path)
        image.thumbnail((800, 600))
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(window, image=photo)
        label.pack()
        window.mainloop()

if __name__ == "__main__":
    fetcher = DogImageFetcher()
    image_url = fetcher.fetch_image_url()
    
    if image_url:
        save_location = fetcher.get_save_location()
        saved_image_path = fetcher.download_and_save_image(image_url, save_location)
        
        if saved_image_path:
            while True:
                viewer_choice = input("View image with Windows viewer (1) or Swaply Special (2)? ")
                if viewer_choice == "1":
                    fetcher.open_image_windows(saved_image_path)
                    break
                elif viewer_choice == "2":
                    fetcher.open_image_tkinter(saved_image_path)
                    break
                else:
                    print("Invalid choice. Please choose 1 or 2.")
