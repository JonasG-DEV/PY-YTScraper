from pytube import YouTube

url = YouTube(input("Youtube URL: "))
print("Getting youtube video...")
print("Title: "+url.title)
print("Author: "+url.author)
print("Thumbnail: "+url.thumbnail_url)
print("Video length: "+str(url.length)+" seconds")
print("Description:\n"+url.description)
print("Age restricted: "+str(url.age_restricted))
print("Rating: "+str(url.rating))
print("Views: "+str(url.views)+"\n")

destinationPath = input("Path to save: ")

url.streams.get_highest_resolution().download(destinationPath)
print("Successfully downloaded and saved video!")
