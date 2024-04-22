
import os
import subprocess

def add_audio(video, audio, output, video_volume=1, audio_volume=0.20):
    command = f'ffmpeg -i "{video}" -i "{audio}" -c:v copy -filter_complex "[0:a]volume={video_volume}[v_audio];[1:a]volume={audio_volume}[m_audio];[v_audio][m_audio]amix=inputs=2[aout]" -map 0:v -map "[aout]" -c:a aac -shortest "{output}"'
    subprocess.call(command, shell=True)

def combine_mp3s():
    count = 1
    with open("concat.txt", "w") as f:
        f.write("This is a dummy line to keep the concat.txt file non-empty.\n")
    
    while os.path.exists(f"{count}.mp3"):
        with open("concat.txt", "a") as f:
            f.write(f"file '{os.getcwd()}\\{count}.mp3'\n")
        count += 1
    
    with open("concat.txt", "r") as f:
        lines = f.readlines()
    with open("concat.txt", "w") as f:
        for line in lines:
            if line.strip() != "This is a dummy line to keep the concat.txt file non-empty.":
                f.write(line)
    
    command = 'ffmpeg -f concat -safe 0 -i concat.txt -c copy combined.mp3'
    subprocess.call(command, shell=True)
    os.remove("concat.txt")

def montage():
    with open("mylist.txt", "w") as f:
        for file in os.listdir():
            if file.endswith(".mp4"):
                f.write(f"file '{file}'\n")
    
    command = 'ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.mp4'
    subprocess.call(command, shell=True)
    os.remove("mylist.txt")

def tens4k():
    if not os.path.exists("output.mp4"):
        print("File output.mp4 not found in the current directory.")
        return
    
    command = 'ffmpeg -i output.mp4 -vf scale=3840:2160:flags=lanczos -c:a copy -c:v hevc_nvenc -preset slow -rc vbr -b:v 400M -cq 1 upscale.mp4'
    subprocess.call(command, shell=True)

def youtube_mp3():
    video_type = input("Enter 1 for single video or 2 for playlist: ")
    link = input("Enter link: ")
    
    if video_type == "1":
        command = f'yt-dlp -x --audio-format mp3 --audio-quality 0 -o "1.mp3" "{link}"'
    elif video_type == "2":
        command = f'yt-dlp -x --audio-format mp3 --audio-quality 0 -o "1.mp3" "{link}"'
    else:
        print("Invalid option. Please enter 1 or 2.")
        return
    
    subprocess.call(command, shell=True)

def trim_mp4():
    if not os.path.exists("1.mp4"):
        print("File 1.mp4 not found in the current directory.")
        return
    
    start_time = input("Enter start timestamp (e.g., 00:02:13): ")
    end_time = input("Enter end timestamp (e.g., 00:02:52): ")
    
    command = f'ffmpeg -i 1.mp4 -ss {start_time} -to {end_time} -c:v libx264 -c:a aac -strict -2 2.mp4'
    subprocess.call(command, shell=True)
    print(f"Error level: {subprocess.call(command, shell=True)}")

def trim_mp3():
    if not os.path.exists("1.mp3"):
        print("File 1.mp3 not found in the current directory.")
        return
    
    start_time = input("Enter start timestamp (e.g., 00:25:02): ")
    end_time = input("Enter end timestamp (e.g., 00:29:40): ")
    
    command = f'ffmpeg -i 1.mp3 -ss {start_time} -to {end_time} -c:v copy -c:a copy 2.mp3'
    subprocess.call(command, shell=True)
    print(f"Error level: {subprocess.call(command, shell=True)}")

def clear_files():
    mp4_files = [f for f in os.listdir() if f.endswith(".mp4")]
    mp3_files = [f for f in os.listdir() if f.endswith(".mp3")]
    
    if not mp4_files and not mp3_files:
        print("No mp4 or mp3 files found.")
        return
    
    for file in mp4_files + mp3_files:
        os.remove(file)
        print(f"File deleted: {file}")

def rename_mp4():
    count = 1
    for file in os.listdir():
        if file.endswith(".mp4"):
            if os.path.exists(f"{count}.mp4"):
                print(f"A file with the name {count}.mp4 already exists in this directory.")
                print("Please move or rename the existing file before running this script.")
                return
            os.rename(file, f"{count}.mp4")
            print(f"File renamed to {count}.mp4")
            count += 1
    
    if count == 1:
        print("No .mp4 files found in the current directory.")

def main():
    while True:
        print("\n1. Add Audio")
        print("2. Combine MP3s")
        print("3. Montage")
        print("4. Tens4k")
        print("5. YouTube MP3")
        print("6. Trim MP4")
        print("7. Trim MP3")
        print("8. Clear Files")
        print("9. Rename MP4")
        print("10. Exit")
        
        choice = input("Enter your choice (1-10): ")
        
        if choice == "1":
            video = input("Enter video file: ")
            audio = input("Enter audio file: ")
            output = input("Enter output file: ")
            add_audio(video, audio, output)
        elif choice == "2":
            combine_mp3s()
        elif choice == "3":
            montage()
        elif choice == "4":
            tens4k()
        elif choice == "5":
            youtube_mp3()
        elif choice == "6":
            trim_mp4()
        elif choice == "7":
            trim_mp3()
        elif choice == "8":
            clear_files()
        elif choice == "9":
            rename_mp4()
        elif choice == "10":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
