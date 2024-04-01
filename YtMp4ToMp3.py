from pytube import YouTube
import os
from moviepy.editor import VideoFileClip


# function to download video
def download_video(url, output_path):
    try:
        yt = YouTube(url)
        yd = yt.streams.get_highest_resolution()

        #  ger  the original file name without extension
        original_filename = os.path.splitext(yd.default_filename)[0]
        print("========== Details ==========")
        print("Title: ", yt.title)
        print("Views: ", yt.views)
        print("Channel Name: ", yt.author)

        # Specify the filename with extension
        video_file = yd.download(output_path=output_path, filename=original_filename)

        return video_file # return thr path to the download video file
    
    except TypeError as te:
        print(f"Error: {te}")
        return False
    except ValueError as ve:
        print(f"Error: {ve}")
        return False
    except NameError as ne:
        print(f"Error: {ne}")
        return False
    except OSError as oe:
        print(f"Error: {oe}")
        return False
    except AttributeError as ae:
        print(f"Error: {ae}")
        return False
    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
        return False
    
# function to change downloaded mp4 to mp3    
def change_to_mp3(input_file, output_file):
    try:
        clip = VideoFileClip(input_file)
        clip.audio.write_audiofile(output_file) #  video's audio is extracted and converted to an MP3 audio file.
        clip.close()
        return True
    
    except OSError as oe:
        print(f"Error: {oe}")
        return False
    except NameError as ne:
        print(f"Error: {ne}")
        return False
    except TypeError as te:
        print(f"Error: {te}")
        return False
    except ValueError as ve:
        print(f"Error: {ve}")
        return False
    except AttributeError as ae:
        print(f"Error: {ae}")
        return False
    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
        return False
    
# main function
def main():
    url = input("Enter the youtube Url: ")
    output_path = "C:\\Users\\User\\Music\\downloaded"
    
    # checks the output path and if the directory does not exists it makes output path directory
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    video_file = download_video(url, output_path)

    if video_file:
        if os.path.exists(video_file):

            # get the file name without extension
            filename_without_extension = os.path.splitext(os.path.basename(video_file))[0]
            audio_file = os.path.join(output_path, f"{filename_without_extension}.mp3")

            if change_to_mp3(video_file, audio_file):
                print("conversion completed successfully!")
                os.remove(video_file)
            else:
                print("conversion of mp4 to mp3 failed.")
        else:
            print("Downloaded video file not found")
    else:
        print("Download Failed")


if __name__ == "__main__":
    main() 