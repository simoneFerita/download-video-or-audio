import pytube
import time

def download_video(url, resolution, file_format):
  yt = pytube.YouTube(url)
 
  video = yt.streams.filter(res=resolution, file_extension=file_format).first()
 
  video.download()
 
  return video.filesize, time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime())

url = input("Insert link: ")

yt = pytube.YouTube(url)

streams = yt.streams.all()
for i, stream in enumerate(streams):
  size_mb = stream.filesize / (1024 * 1024)
  print(f"{i}: {stream.resolution} {stream.mime_type} {stream.abr} kbps, {size_mb:.2f} MB")

choice = int(input("Select number: "))
selected_stream = streams[choice]
resolution = selected_stream.resolution
file_format = selected_stream.mime_type.split("/")[1]

size, timestamp = download_video(url, resolution, file_format)

size_mb = size / (1024 * 1024)

print(f"Ok! File size: {size_mb:.2f} MB, When: {timestamp}")
