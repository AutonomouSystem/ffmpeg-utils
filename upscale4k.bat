cd C:\Users\mcwee\Videos\Upscaling
C:\ffmpeg\bin\ffmpeg.exe -i input.mp4 -vf scale=3840:2160:flags=neighbor -r 60 -rc constqp -qp 19 -c:a copy output.mp4