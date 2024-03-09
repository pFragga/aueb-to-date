#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import sys


def show_usage() -> None:
    print('Usage:\n\t[python] ./aueb-to-date.py [filename.pdf]',
          file=sys.stderr)


def make_request(uri: str) -> requests.Response:
    r = requests.get(uri)
    if r.status_code != 200:
        print(f'Request for {uri} failed.\nStatus code: {r.status_code}',
              file=sys.stderr)
        return None
    return r


def strip_fname(uri: str) -> str:
    return uri.split('/')[-1]


if __name__ == '__main__':
    if len(sys.argv) > 2:
        show_usage()
        exit()

    # NOTE: this url is subject to change.
    url = 'https://www.aueb.gr/el/content/'\
          'orologio-programma-didaskalias-earinoy-examinoy-2023-2024'
    req = make_request(url)
    if req is None:
        exit(1)

    soup = BeautifulSoup(req.text, 'html.parser')
    doc_spans = soup.find_all('span', attrs={'class': 'file'})

    # The first span always contains the lastest schedule in pdf format.
    latest = doc_spans[0]

    # Each 'file' span contains one 'img' tag and one 'a' tag. The 'a' tag
    # contains the the link to the pdf file we want.
    href = latest.find_next('a').attrs.get('href')

    req = make_request(href)
    if req is None:
        exit(1)

    filename = sys.argv[1] if len(sys.argv) == 2 else href.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(req.content)
