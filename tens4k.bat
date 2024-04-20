cd C:\Users\mcwee\Videos\Upscaling
C:\ffmpeg\bin\ffmpeg.exe -i 1.mp4 -vf scale=3840:2160:flags=lanczos -c:a copy -c:v hevc_nvenc -preset slow -rc vbr -b:v 400M -cq 1 2.mp4