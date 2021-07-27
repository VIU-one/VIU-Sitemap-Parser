from unittest import TestCase

from viusitemapparser.vsp import get_sitemap_contents


def test_entries_xml_sitemap():
    sitemap, sitemap_entries = get_sitemap_contents('tests/sitemap_types/xml_sitemap.xml')
    count = 0
    result = []
    for e in sitemap_entries:
        count += 1
        result.append(e)
    assert count == 5

    TestCase().assertCountEqual(result, [
        {'loc': 'http://www.example.com/', 'lastmod': '2005-01-01', 'changefreq': 'monthly', 'priority': '0.8'},
        {'loc': 'http://www.example.com/catalog?item=12&desc=vacation_hawaii', 'changefreq': 'weekly'},
        {'loc': 'http://www.example.com/catalog?item=73&desc=vacation_new_zealand', 'lastmod': '2004-12-23',
         'changefreq': 'weekly'},
        {'loc': 'http://www.example.com/catalog?item=74&desc=vacation_newfoundland',
         'lastmod': '2004-12-23T18:00:15+00:00', 'priority': '0.3'},
        {'loc': 'http://www.example.com/catalog?item=83&desc=vacation_usa', 'lastmod': '2004-11-23',
         'link': [{'@rel': 'alternate', '@hreflang': 'de', '@href': 'http://www.example.com/deutsch/page.html'},
                  {'@rel': 'alternate', '@hreflang': 'de-ch',
                   '@href': 'http://www.example.com/schweiz-deutsch/page.html'},
                  {'@rel': 'alternate', '@hreflang': 'en', '@href': 'http://www.example.com/english/page.html'}]}])


def test_entries_xml_sitemap_index():
    sitemap, sitemap_entries = get_sitemap_contents('tests/sitemap_types/xml_sitemap_index.xml')
    count = 0
    result = []
    for e in sitemap_entries:
        count += 1
        result.append(e)
    assert count == 2

    TestCase().assertCountEqual(result, [
        {'loc': 'http://www.example.com/sitemap1.xml.gz', 'lastmod': '2004-10-01T18:23:17+00:00'},
        {'loc': 'http://www.example.com/sitemap2.xml.gz', 'lastmod': '2005-01-01'}])


def test_entries_rss_feed():
    sitemap, sitemap_entries = get_sitemap_contents('tests/sitemap_types/rss_feed.xml')
    count = 0
    result = []
    for e in sitemap_entries:
        count += 1
        result.append(e)
    assert count == 1

    TestCase().assertCountEqual(result, [
        {'title': 'Atom-Powered Robots Run Amok', 'link': 'http://example.org/2003/12/13/atom03',
         'guid': {'@isPermaLink': 'false', '#text': 'urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a'},
         'pubDate': 'Sat, 13 Dec 2003 18:30:02 GMT', 'description': 'Some text.'}])


def test_entries_rss_feed_only_relevant_fiels():
    sitemap, sitemap_entries = get_sitemap_contents('tests/sitemap_types/rss_feed.xml', only_relevant_rss_fields=True)
    count = 0
    result = []
    for e in sitemap_entries:
        count += 1
        result.append(e)
    assert count == 1

    TestCase().assertCountEqual(result, [
        {'link': 'http://example.org/2003/12/13/atom03', 'pubDate': 'Sat, 13 Dec 2003 18:30:02 GMT'}])


def test_entries_atom_feed():
    sitemap, sitemap_entries = get_sitemap_contents('tests/sitemap_types/atom_feed.xml')
    count = 0
    result = []
    for e in sitemap_entries:
        count += 1
        result.append(e)

    assert count == 1

    TestCase().assertCountEqual(result, [
        {'title': 'Atom-Powered Robots Run Amok', 'link': {'@href': 'http://example.org/2003/12/13/atom03'},
         'id': 'urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a', 'updated': '2003-12-13T18:30:02Z',
         'summary': 'Some text.'}])


def test_entries_atom_feed_only_relevant_fiels():
    sitemap, sitemap_entries = get_sitemap_contents('tests/sitemap_types/atom_feed.xml', only_relevant_atom_fields=True)
    count = 0
    result = []
    for e in sitemap_entries:
        count += 1
        result.append(e)

    assert count == 1

    TestCase().assertCountEqual(result, [
        {'link': {'@href': 'http://example.org/2003/12/13/atom03'}, 'updated': '2003-12-13T18:30:02Z'}])


def test_entries_plain_text():
    sitemap, sitemap_entries = get_sitemap_contents('tests/sitemap_types/plain_text.txt')
    count = 0
    result = []
    for e in sitemap_entries:
        count += 1
        result.append(e)

    assert count == 2

    TestCase().assertCountEqual(result,
                                ['http://www.example.com/catalog?item=1', 'http://www.example.com/catalog?item=11'])

def test_entries_error():
    sitemap, sitemap_entries = get_sitemap_contents('https://run.mocky.io/v3/90bf8eb6-d773-437d-80b1-205bc2987cf8')
    count = 0
    result = []
    for e in sitemap_entries:
        count += 1
        result.append(e)

    assert count == 0

    TestCase().assertCountEqual(result,
                                [])