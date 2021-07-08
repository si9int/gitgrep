#!/usr/bin/env python3
# BY SI9INT | 07-2021 | H4CK TH3 W0RLD
import requests, json, math, sys


RESULT = {
    'repos': [],
    'files': []
}


def fetch_data(res):
    for r in res['hits']['hits']:
        repo = 'https://github.com/' + r['repo']['raw']

        if repo not in RESULT['repos']:
            RESULT['repos'].append(repo)

        try:
            raw = 'https://raw.githubusercontent.com/{a}/{b}/{c}'.format(a=r['repo']['raw'], b=r['branch']['raw'], c=r['path']['raw'])

            if raw not in RESULT['files']:
                RESULT['files'].append(raw)
        except KeyError:
            raw = 'https://raw.githubusercontent.com/{a}/master/{b}'.format(a=r['repo']['raw'], b=r['path']['raw'])

            if raw not in RESULT['files']:
                RESULT['files'].append(raw)


if __name__ == '__main__':
    try:
        domain = sys.argv[1]
    except IndexError:
        print('[X] Usage: python3 grepgit.py <domain> <optional|-json>')
        exit(0)

    first = json.loads(requests.get('https://grep.app/api/search?q=rewe.de').text)
    total = int(math.ceil(first['hits']['total']/10))

    fetch_data(first)

    for t in range(1, total+1):
        fetch_data(json.loads(requests.get('https://grep.app/api/search?q={a}&page={b}'.format(a=domain, b=t)).text))

    try:
        if sys.argv[2] == '-json':
            print(json.dumps(RESULT))
    except IndexError:
        print('[-] Printing repositories for', domain, '\n')

        for r in RESULT['repos']:
            print(r)

        print('\n[-] Printing raw-data', domain, '\n')

        for r in RESULT['files']:
            print(r)
