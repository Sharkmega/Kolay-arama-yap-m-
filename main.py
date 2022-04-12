import webbrowser

search = input('Ne aramak istiyorsunuz: ')
url = 'https://www.google.com/search?q=' + search
webbrowser.get().open(url)
print(search + "için bulduklarım <3")