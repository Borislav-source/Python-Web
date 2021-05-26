from urllib import parse


def validate_url(url):
    print(parse.urlparse(url))


tests = [
    'http://softuni.bg/',
    'https://softuni.bg:447/search?Query=pesho&Users=true#go',
    'http://google:443/',
]

for el in tests:
    validate_url(el)