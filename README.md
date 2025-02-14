# Dog-Image-Fetcher
This Python script fetches a random dog image from an API, allows the user to specify a save location, and provides two ways to view the image: using the default Windows image viewer or a custom Tkinter GUI.

# Dependencies

Ensure you have the following dependencies installed before running the script:

pip install requests pillow

# Running the Script

Run the script using:

python dog_image_fetcher.py

# Image Display Method

The script offers two options for displaying the downloaded image:

  1. Windows Default Viewer (uses subprocess.run() to open the image normally)

  2. Tkinter GUI (uses PIL and Tkinter to open a custom image window)

Tkinter is useful because it ensures cross-platform compatibility, while the default Windows viewer provides a familiar experience.


