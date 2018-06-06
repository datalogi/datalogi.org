"""
    datalogi.py
    ~~~~~~~~~~~

    This script generates the static pages for https://datalogi.org,
    a danish nonprofit established to further the danish language.
"""

import json
from pathlib import Path
import shutil

from jinja2 import Environment, FileSystemLoader, select_autoescape


build_dir = Path('./build/')
source_dir = Path('./src/')
static_dir = Path(source_dir, 'static')

try:
    shutil.rmtree(build_dir)
except FileNotFoundError:
    pass

shutil.copytree(static_dir, build_dir)
Path(build_dir, 'leksikon').mkdir(parents=True)


with open(Path(source_dir, 'data.json'), 'r', encoding='utf-8') as f:
    lexicon = json.load(f)

env = Environment(
    loader=FileSystemLoader([source_dir]),
    autoescape=select_autoescape(['html']),
)


lexicon_template = env.get_template('leksikon_template.html')
for entry in lexicon:
    with open(Path(build_dir, 'leksikon', entry['word'] + '.html'), 'w+') as f:
        f.write(lexicon_template.render(
            entry_name=entry['word'],
            conjugation=entry['conjugation'],
            translation=entry['translation'],
            definition=entry['definition'],
            origin=entry['origin'],
            related_words=entry['related_words'],
        ))


with open(Path(build_dir, 'leksikon.html'), 'w+') as f:
    f.write(env.get_template('leksikon.html').render(
        entries=[entry['word'] for entry in lexicon]))


with open(Path(build_dir, 'ordbog.html'), 'w+') as f:
    entry_template = r'%s: "%s"'
    danish = []
    english = []
    for entry in lexicon:
        danish.append(entry_template % (entry['word'], entry['translation']))
        english.append(entry_template % (entry['translation'], entry['word']))
    f.write(env.get_template('ordbog.html').render(
        danish_to_english=', '.join(danish),
        english_to_danish=', '.join(english),
    ))


no_input_files = ['forslag', 'index', 'medlemskab']
for filename in no_input_files:
    with open(Path(build_dir, filename + '.html'), 'w+') as f:
        f.write(env.get_template(filename + '.html').render())
