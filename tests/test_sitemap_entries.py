from unittest import TestCase

from viusitemapparser.vsp import get_sitemap_contents


def test_entries_xml_sitemap():
    sitemap, sitemap_entries = get_sitemap_contents('tests/sitemap_types/xml_sitemap.xml')
    count = 0
    result = []
    for e in sitemap_entries:
        count += 1
        result.append(e)
    assert count == 8

    TestCase().assertCountEqual(result, [
        {'loc': 'http://www.example.com/', 'lastmod': '2005-01-01', 'changefreq': 'monthly', 'priority': '0.8'},
        {'loc': 'http://www.example.com/catalog?item=12&desc=vacation_hawaii', 'changefreq': 'weekly'},
        {'loc': 'http://www.example.com/catalog?item=73&desc=vacation_new_zealand', 'lastmod': '2004-12-23',
         'changefreq': 'weekly'}, {'loc': 'http://www.example.com/catalog?item=74&desc=vacation_newfoundland',
                                   'lastmod': '2004-12-23T18:00:15+00:00', 'priority': '0.3'},
        {'loc': 'http://www.example.com/catalog?item=83&desc=vacation_usa', 'lastmod': '2004-11-23',
         'link': [{'@rel': 'alternate', '@hreflang': 'de', '@href': 'http://www.example.com/deutsch/page.html'},
                  {'@rel': 'alternate', '@hreflang': 'de-ch',
                   '@href': 'http://www.example.com/schweiz-deutsch/page.html'},
                  {'@rel': 'alternate', '@hreflang': 'en', '@href': 'http://www.example.com/english/page.html'}]},
        {'loc': 'http://www.example.com/videos/some_video_landing_page.html',
         'video': {'thumbnail_loc': 'http://www.example.com/thumbs/123.jpg', 'title': 'Grilling steaks for summer',
                   'description': 'Alkis shows you how to get perfectly done steaks every\n             time',
                   'content_loc': 'http://streamserver.example.com/video123.mp4',
                   'player_loc': 'http://www.example.com/videoplayer.php?video=123', 'duration': '600',
                   'expiration_date': '2021-11-05T19:20:30+08:00', 'rating': '4.2', 'view_count': '12345',
                   'publication_date': '2007-11-05T19:20:30+08:00', 'family_friendly': 'yes',
                   'restriction': {'@relationship': 'allow', '#text': 'IE GB US CA'},
                   'price': {'@currency': 'EUR', '#text': '1.99'}, 'requires_subscription': 'yes',
                   'uploader': {'@info': 'http://www.example.com/users/grillymcgrillerson',
                                '#text': 'GrillyMcGrillerson'}, 'live': 'no'}},
        {'loc': 'http://example.com/sample1.html',
         'image': [{'loc': 'http://example.com/image.jpg'}, {'loc': 'http://example.com/photo.jpg'}]},
        {'loc': 'http://example.com/sample2.html',
         'image': {'loc': 'http://example.com/picture.jpg', 'caption': 'A funny picture of a cat eating cabbage',
                   'geo_location': 'Lyon, France', 'title': 'Cat vs Cabbage',
                   'license': 'http://example.com/image-license'}}]
                                )


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
         'pubdate': 'Sat, 13 Dec 2003 18:30:02 GMT', 'description': 'Some text.'}])


def test_entries_rss_feed_only_relevant_fiels():
    sitemap, sitemap_entries = get_sitemap_contents('tests/sitemap_types/rss_feed.xml', only_relevant_rss_fields=True)
    count = 0
    result = []
    for e in sitemap_entries:
        count += 1
        result.append(e)
    assert count == 1

    TestCase().assertCountEqual(result, [
        {'link': 'http://example.org/2003/12/13/atom03', 'pubdate': 'Sat, 13 Dec 2003 18:30:02 GMT'}])


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


def test_entries_xml_news_sitemap():
    sitemap, sitemap_entries = get_sitemap_contents('tests/sitemap_types/xml_news_sitemap.xml')
    count = 0
    result = []
    for e in sitemap_entries:
        count += 1
        result.append(e)
    assert count == 1

    TestCase().assertCountEqual(result, [{'loc': 'http://www.example.org/business/article55.html',
                                          'news': {'publication': {'name': 'The Example Times', 'language': 'en'},
                                                   'publication_date': '2008-12-23',
                                                   'title': 'Companies A, B in Merger Talks'}}])
