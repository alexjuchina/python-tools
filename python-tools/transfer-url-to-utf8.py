import urllib
url="https://ems-chn.jasper.com/event/search?options=%7B%22eventTable%22:%7B%7D,%22searchParams%22:%7B%22query%22:%22%22,%22service%22:%5B%22*gomez*%22%5D%7D%7D"
_de_code= urllib.unquote(url)
de_code = urllib.unquote(_de_code).decode("utf8")
print de_code