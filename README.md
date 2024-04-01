# YouTube Audio Downloader

I created this script so i can download my favorite music froom youtube. I updated the youtube downloader to just download its audio. i think there might be better
way to create this script but i used the previous library and updated it.
This Python script allows you to download audio from YouTube videos. It utilizes the `pytube` library to fetch the video and the `moviepy` library to convert the downloaded video file into an MP3 audio file.

## Prerequisites

Before running the script, make sure you have Python installed on your system. You'll also need to install the required libraries. You can install them using pip:

```bash
pip install pytube moviepy
```

## Usage

1. Clone the repository or download the `youtube_audio_downloader.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory where `youtube_audio_downloader.py` is located.
4. Run the script using the following command:

   ```bash
   python youtube_audio_downloader.py
   ```

5. Enter the YouTube URL of the video you want to download audio from when prompted.
6. The audio file will be downloaded to the specified output directory in MP3 format.

## Example

```bash
Enter the YouTube URL: https://www.youtube.com/watch?v=YOUR_VIDEO_ID
```

## Features

- Downloads the audio from a YouTube video in MP3 format.
- Provides details such as video title, views, and channel name.
- Automatically converts the downloaded video file to MP3 audio.

## Disclaimer

Please use this code only if you understand its purpose and how it works. The author takes no responsibility for any issues that may arise from your use of this code. It is important to exercise caution and review the code before usage.

## Function Details

### 1. `download_video(url, output_path)`

   This function downloads the video from the provided YouTube URL and returns the path to the downloaded video file. It handles various exceptions such as `TypeError`, `ValueError`, `NameError`, `OSError`, `AttributeError`, and `FileNotFoundError`.

### 2. `change_to_mp3(input_file, output_file)`

   This function converts the downloaded video file (MP4 format) to an MP3 audio file. It uses `moviepy` to extract the audio from the video. It also handles exceptions like `OSError`, `NameError`, `TypeError`, `ValueError`, `AttributeError`, and `FileNotFoundError`.

## Author

- [XiranXibi](https://github.com/NoahXiren)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

Feel free to customize this `README.md` with additional details or sections as needed. Replace `"YOUR_VIDEO_ID"` in the example with an actual YouTube video ID. This template aims to provide clear instructions and information about your script for users.
