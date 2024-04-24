import os
import subprocess

def get_file_path(prompt):
    while True:
        file_path = input(prompt)
        if os.path.isfile(file_path):
            return file_path
        print("Invalid file path. Please try again.")

def add_audio(video_file, audio_file, output_file, video_volume=1, audio_volume=0.20):
    command = f'ffmpeg -i "{video_file}" -i "{audio_file}" -c:v copy -filter_complex "[0:a]volume={video_volume}[v_audio];[1:a]volume={audio_volume}[m_audio];[v_audio][m_audio]amix=inputs=2[aout]" -map 0:v -map "[aout]" -c:a aac -shortest "{output_file}"'
    subprocess.call(command, shell=True)

def combine_mp3s(output_file):
    mp3_files = [f for f in os.listdir() if f.endswith(".mp3")]
    with open("concat.txt", "w") as f:
        for file in mp3_files:
            f.write(f"file '{file}'\n")
    command = f'ffmpeg -f concat -safe 0 -i concat.txt -c copy "{output_file}"'
    subprocess.call(command, shell=True)
    os.remove("concat.txt")

def fade_out(input_file, output_file, start_time=25, duration=9, curve='tri'):
    command = f'ffmpeg -i "{input_file}" -af "afade=t=out:st={start_time}:d={duration}:curve={curve}" -c:v copy "{output_file}"'
    subprocess.call(command, shell=True)

def montage(output_file):
    mp4_files = [f for f in os.listdir() if f.endswith(".mp4")]
    with open("montage.txt", "w") as f:
        for file in mp4_files:
            f.write(f"file '{file}'\n")
    command = f'ffmpeg -f concat -safe 0 -i montage.txt -c copy "{output_file}"'
    subprocess.call(command, shell=True)
    os.remove("montage.txt")

def upscale(input_file, output_file):
    command = f'ffmpeg -i "{input_file}" -c:v hevc_nvenc -preset slow -rc vbr -cq 19 -r 120 -s 3840x2160 -pix_fmt yuv420p "{output_file}"'
    subprocess.call(command, shell=True)

def download_youtube_mp3(output_file):
    video_type = input("Enter 1 for single video or 2 for playlist: ")
    link = input("Enter the YouTube link: ")
    if video_type == "1":
        command = f'yt-dlp -x --audio-format mp3 --audio-quality 0 -o "{output_file}" "{link}"'
    elif video_type == "2":
        command = f'yt-dlp -x --audio-format mp3 --audio-quality 0 -o "%(playlist_index)s.%(ext)s" "{link}"'
    else:
        print("Invalid option. Please enter 1 or 2.")
        return
    subprocess.call(command, shell=True)

def trim(input_file, output_file, start_time, end_time):
    command = f'ffmpeg -hwaccel cuda -i "{input_file}" -ss {start_time} -to {end_time} -c:v hevc_nvenc -preset slow -rc vbr -cq 17 -b:v 5M -maxrate 5M -bufsize 10M -r 120 -c:a aac -b:a 192k -strict -2 "{output_file}"'
    subprocess.call(command, shell=True)

def clear_files():
    mp4_files = [f for f in os.listdir() if f.endswith(".mp4")]
    mp3_files = [f for f in os.listdir() if f.endswith(".mp3")]
    for file in mp4_files + mp3_files:
        os.remove(file)
    print("MP4 and MP3 files cleared.")

def rename_mp4():
    counter = 1
    for file in os.listdir():
        if file.endswith(".mp4"):
            new_name = f"{counter}.mp4"
            os.rename(file, new_name)
            print(f"Renamed {file} to {new_name}")
            counter += 1

def main():
    print("Video Processing Script")
    print("=======================")

    while True:
        print("\nSelect an operation:")
        print("1. Add Audio")
        print("2. Combine MP3s")
        print("3. Fade Out")
        print("4. Montage")
        print("5. Upscale")
        print("6. Download YouTube MP3")
        print("7. Trim")
        print("8. Clear Files")
        print("9. Rename MP4")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == "1":
            video_file = get_file_path("Enter the path to the video file: ")
            audio_file = get_file_path("Enter the path to the audio file: ")
            output_file = input("Enter the output file name: ")
            add_audio(video_file, audio_file, output_file)
        elif choice == "2":
            output_file = input("Enter the output file name: ")
            combine_mp3s(output_file)
        elif choice == "3":
            input_file = get_file_path("Enter the path to the input file: ")
            output_file = input("Enter the output file name: ")
            fade_out(input_file, output_file)
        elif choice == "4":
            output_file = input("Enter the output file name: ")
            montage(output_file)
        elif choice == "5":
            input_file = get_file_path("Enter the path to the input file: ")
            output_file = input("Enter the output file name: ")
            upscale(input_file, output_file)
        elif choice == "6":
            output_file = input("Enter the output file name (for single video): ")
            download_youtube_mp3(output_file)
        elif choice == "7":
            input_file = get_file_path("Enter the path to the input file: ")
            output_file = input("Enter the output file name: ")
            start_time = input("Enter the start time (e.g., 00:00:10): ")
            end_time = input("Enter the end time (e.g., 00:01:30): ")
            trim(input_file, output_file, start_time, end_time)
        elif choice == "8":
            clear_files()
        elif choice == "9":
            rename_mp4()
        elif choice == "10":
            print("Exiting the script.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
