@echo off
:: clear any mp4, mp3s in directory

if not exist *.mp4 if not exist *.mp3 (
    echo No mp4 or mp3 files found.
    exit
)

rem clear all .mp4 files in the current directory

for %%f in (*.mp4) do (
    del "%%f"
    echo File deleted: %%f
)


rem clear all .mp3 files in the current directory

for %%f in (*.mp3) do (
    del "%%f"
    echo File deleted: %%f
)
