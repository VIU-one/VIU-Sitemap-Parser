from distutils.core import setup
import os

setup(
    name='VIU Sitemap parser',
    version=os.environ.get('RELEASE_NUMBER', '0.1'),
    packages=['viu-sitemap-parser'],
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown"
)
