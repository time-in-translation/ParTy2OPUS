# -*- coding: utf-8 -*-

import glob
import os
import shutil

import click
from preprocess_corpora.alignment.align import sentence_align
from preprocess_corpora.preprocessing.tag import treetag_single
from preprocess_corpora.core.constants import LANGUAGES

from constants import ISO3TO2


@click.command()
@click.argument('folder_in', type=click.Path(exists=True))
@click.argument('folder_out', type=click.Path(exists=True))
@click.argument('languages', nargs=-1, type=click.Choice(LANGUAGES))
@click.option('--tag', is_flag=True)
def process(folder_in, folder_out, languages, tag=False):
    click.echo('Fetching files...')
    for dir in [f.path for f in os.scandir(folder_in) if f.is_dir()]:
        if os.path.basename(os.path.normpath(dir)) not in ['.git', 'Originals']:
            process_folder(os.path.join(dir, 'XML'), folder_out, languages, tag)

    # Create alignment files
    if len(languages) > 1:
        click.echo('Starting sentence alignment...')
        sentence_align([folder_out, *languages])

    click.echo('Finished!')

def process_folder(folder_in, folder_out, languages, tag=False):
    for file_in in glob.glob(os.path.join(folder_in, '*.xml')):
        # Fetch the title
        title = folder_in.split('/')[-2]

        # Find iso2 from iso3
        iso3 = os.path.splitext(file_in)[0].split('_')[1]
        iso2 = ISO3TO2.get(iso3)
        if not iso2:
            click.echo(f'iso2 alternative for language {iso3} in title {title} not found, skipping...')
            continue

        if iso2 in languages:
            # Create folders in output directory
            iso2_folder = os.path.join(folder_out, iso2)
            if not os.path.exists(iso2_folder):
                os.mkdir(iso2_folder)

            # Copy the files to the output directory
            file_out = os.path.join(iso2_folder, title + '.xml')
            shutil.copy(file_in, file_out)

            # Use TreeTagger to add part-of-speech tags to supported languages
            if tag:
                treetag_single(file_out, iso2)

if __name__ == "__main__":
    process()
