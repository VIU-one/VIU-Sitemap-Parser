from distutils.core import setup
import os

version = os.environ.get('RELEASE_NUMBER', None)

if not version:
    version = os.environ.get('RUN_ID', '0.1')

setup(
    name='viu_sitemap_parser',
    version=version,
    packages=['viusitemapparser'],
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown"
)