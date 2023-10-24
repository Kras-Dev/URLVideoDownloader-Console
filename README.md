# URL-VideoDownloader-Console
The video downloader is a console application built in Python. It allows you to download YouTube videos and other videos with correct URL-links to the user's system.

## Installation
1. Clone the repository.
2. Go to the project directory.
3. Create a virtual environment:
 ```bash
   python -m venv venv
```
4. Activate the virtual environment:
### Windows:
```bash
   env\Scripts\activate
```
### Mac OS / Linux:
```bash
   source env/bin/activate
```
5. Install dependencies:
 ```bash
   pip install -r requirements.txt
```
## Usage
1. Run the main.py script:
 ```bash
   python main.py
 ```
2. Enter the directory path where you want to save the video and the URL of the video you want to download.
3. The script will check the entered data and start downloading the video.
   
## Notes
To download a video from YouTube, you must enter the correct video URL. The script will automatically detect whether the URL is a video from YouTube or another source.
While the video is downloading, you will see the progress as a percentage.
If the directory for saving the video does not exist, the script will display an error.
