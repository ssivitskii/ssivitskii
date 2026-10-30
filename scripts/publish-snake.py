"""Publish only generated contribution SVGs, preserving output-branch history."""

import base64
import json
import os
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


def api(endpoint, payload=None, method=None):
    request = Request(
        'https://api.github.com/repos/' + os.environ['GH_REPO'] + '/' + endpoint,
        data=json.dumps(payload).encode() if payload is not None else None,
        method=method or ('POST' if payload is not None else 'GET'),
        headers={
            'Accept': 'application/vnd.github+json',
            'Authorization': 'Bearer ' + os.environ['GH_TOKEN'],
            'X-GitHub-Api-Version': '2022-11-28',
            'Content-Type': 'application/json',
        },
    )
    with urlopen(request, timeout=60) as response:
        return json.load(response)


def main():
    entries = []
    for name in ('github-snake.svg', 'github-snake-dark.svg'):
        path = Path('dist') / name
        source = path.read_text()
        ET.fromstring(source)
        # Keep the generator's initial contribution grid when motion is reduced.
        source = source.replace(
            '</svg>',
            '<style>@media (prefers-reduced-motion: reduce) {'
            '* { animation: none !important; }}</style></svg>',
        )
        ET.fromstring(source)
        blob = api('git/blobs', {
            'content': base64.b64encode(source.encode()).decode(),
            'encoding': 'base64',
        })
        entries.append({'path': name, 'mode': '100644', 'type': 'blob', 'sha': blob['sha']})

    try:
        previous = api('git/ref/heads/output')['object']['sha']
    except HTTPError as error:
        if error.code != 404:
            raise
        previous = None

    tree = api('git/trees', {'tree': entries})
    if previous and api('git/commits/' + previous)['tree']['sha'] == tree['sha']:
        print('Contribution SVGs are unchanged.')
        return

    commit = api('git/commits', {
        'message': 'Update contribution snake',
        'tree': tree['sha'],
        'parents': [previous] if previous else [],
        'author': {
            'name': 'github-actions[bot]',
            'email': '41898282+github-actions[bot]@users.noreply.github.com',
        },
    })
    if previous:
        api('git/refs/heads/output', {'sha': commit['sha'], 'force': False}, 'PATCH')
    else:
        api('git/refs', {'ref': 'refs/heads/output', 'sha': commit['sha']})
    print('Published contribution SVGs:', commit['sha'])


if __name__ == '__main__':
    main()
