![example workflow](https://github.com/VIU-one/VIU-Sitemap-Parser/actions/workflows/workflow_deploy_main.yaml/badge.svg)
[![codecov](https://codecov.io/gh/VIU-one/VIU-Sitemap-Parser/branch/main/graph/badge.svg?token=ALXIxDH3q7)](https://codecov.io/gh/VIU-one/VIU-Sitemap-Parser)

# VIU-Sitemap-Parser
Parse XML/Plaintext/RSS Sitemaps

**Intent for creating that package**

We've searched for a python based Sitemap parser which supports all main types of sitemap formats. It should also be as flexible as possible by declaring sitemaps etc.
We haven't found one that fits our requirements, so we created this one.

It's not a big project - so we try to leave the code as simple as possible.

The result contains all information we found (e.g. HREF Lang etc.) They are not normalized and for each sitemap format different. See examples.

**Installation**

```pip install VIU-Sitemap-parser```

**Usage - single files**
```
from viusitemapparser.vsp import get_sitemap_contents

sitemap, sitemap_entries = get_sitemap_contents('https://run.mocky.io/v3/d8cb86d5-0400-4860-a053-78996f9ee6b2')

Add Headers (optional):
sitemap, sitemap_entries = get_sitemap_contents('https://run.mocky.io/v3/d8cb86d5-0400-4860-a053-78996f9ee6b2', headers={'User-Agent': 'Mozilla/5.0'})
```


Variable "sitemap" contains a dict with information about the sitemap itself - e.g.
```
{'file_name': 'https://run.mocky.io/v3/d8cb86d5-0400-4860-a053-78996f9ee6b2', 
'file_headers': {'Content-Type': 'text/xml; charset=UTF-8', 'Date': 'Tue, 27 Jul 2021 15:05:03 GMT', 'Content-Length': '939', 'Sozu-Id': '01FBM7YVDJEWJP4670MWBRFXBW'}, 
'source_type': 'remote',        # remote or local 
'file_error': None,             # If there was an error getting the file (e.g. 404 you will get the information about it here)
'file_received': True,          # Final boolean if we get an file to check
'sitemap_type': 'xml_sitemap'   # one of xml_sitemap, xml_sitemap_index, rss_feed, atom_feed, plain_text,
                                # invalid_file_format 
}
```


"sitemap_entries" is an iterator over the lines in the sitemap file.
The content of the lines is different by sitemap_type. 

Here is an example if you just want the URLs out of the Sitemap files.
The names are equal to the names in the Sitemap file.

```
for entry in sitemap_entries:
    if sitemap.get("sitemap_type") == 'xml_sitemap':
        print(entry.get('loc'))
    elif sitemap.get("sitemap_type") == 'xml_sitemap_index':
        print(entry.get('loc'))
    elif sitemap.get("sitemap_type") == 'rss_feed':
        print(entry.get('link'))
    elif sitemap.get("sitemap_type") == 'atom_feed':
        print(entry.get('link'))
    elif sitemap.get("sitemap_type") == 'plain_text':
        print(entry)
```

Take a look on https://github.com/VIU-one/VIU-Sitemap-Parser/blob/main/tests/test_sitemap_entries.py to see how the response of different formats looks.

**Usage - with iterator over sitemap_index files**

TODO

**Alternatives**

https://github.com/mediacloud/ultimate-sitemap-parser

**More about the Sitemaps format**

https://www.sitemaps.org/

https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap?hl=de

https://developers.google.com/search/blog/2014/10/best-practices-for-xml-sitemaps-rssatom

Video in Sitemaps: https://developers.google.com/search/docs/advanced/sitemaps/video-sitemaps

Images in Sitemaps: https://developers.google.com/search/docs/advanced/sitemaps/image-sitemaps

HREF Lang in Sitemaps: https://developers.google.com/search/docs/advanced/crawling/localized-versions#sitemap

Google News Sitemaps: https://developers.google.com/search/docs/advanced/sitemaps/news-sitemap?hl=de