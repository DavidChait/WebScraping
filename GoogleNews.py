from pygooglenews import GoogleNews

gn = GoogleNews()

results = gn.search("Canadian Election")

newsitems = results['entries']
for item in newsitems:
    print(item.title)
    print(item.link, "\n")

















