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

def fade_out(input_file, output_file, start_time=25, duration=9, curve='tri'):
    command = f'ffmpeg -i {input_file} -af "afade=t=out:st={start_time}:d={duration}:curve={curve}" -c:v copy {output_file}'
    subprocess.call(command, shell=True)

def montage():
    counter = 0
    with open("mylist.txt", "w") as f:
        for file in os.listdir():
            if file.endswith(".mp4"):
                command = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{file}"'
                duration = subprocess.check_output(command, shell=True).decode().strip()
                f.write(f"file '{file}'\n")
                f.write(f"duration {duration}\n")
                counter += 1
    
    command = 'ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.mp4'
    subprocess.call(command, shell=True)
    os.remove("mylist.txt")

def tens4k():
    if not os.path.exists("output.mp4"):
        print("File output.mp4 not found in the current directory.")
        return
    
    command = 'ffmpeg -i output.mp4 -c:v hevc_nvenc -preset slow -rc vbr -cq 19 -r 120 -s 3840x2160 -pix_fmt yuv420p upscale.mp4'
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
    
    command = f'ffmpeg -hwaccel cuda -i 1.mp4 -ss {start_time} -to {end_time} -c:v hevc_nvenc -preset slow -rc vbr -cq 17 -b:v 5M -maxrate 5M -bufsize 10M -r 120 -c:a aac -b:a 192k -strict -2 2.mp4'
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
    counter = 1
    for file in os.listdir():
        if file.endswith(".mp4"):
            command = f'ffmpeg -i "{file}" -c:v libx265 -crf 17 -preset slower -c:a aac -b:a 128k -ar 48000 -s 1920x1080 -r 120 -pix_fmt yuv420p -f mp4 -y "{counter}.mp4"'
            subprocess.call(command, shell=True)
            counter += 1

def main():
    while True:
        print("\n1. Add Audio")
        print("2. Combine MP3s")
        print("3. Fade Out")
        print("4. Montage")
        print("5. Tens4k")
        print("6. YouTube MP3")
        print("7. Trim MP4")
        print("8. Trim MP3")
        print("9. Clear Files")
        print("10. Rename MP4")
        print("11. Exit")
        
        choice = input("Enter your choice (1-11): ")
        
        if choice == "1":
            video = input("Enter video file: ")
            audio = input("Enter audio file: ")
            output = input("Enter output file: ")
            add_audio(video, audio, output)
        elif choice == "2":
            combine_mp3s()
        elif choice == "3":
            input_file = input("Enter input file: ")
            output_file = input("Enter output file: ")
            fade_out(input_file, output_file)
        elif choice == "4":
            montage()
        elif choice == "5":
            tens4k()
        elif choice == "6":
            youtube_mp3()
        elif choice == "7":
            trim_mp4()
        elif choice == "8":
            trim_mp3()
        elif choice == "9":
            clear_files()
        elif choice == "10":
            rename_mp4()
        elif choice == "11":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
