from viusitemapparser.vsp import process_sitemap


def test_detect_filetype():

    sitemap = process_sitemap('tests/sitemap_types/xml_sitemap.xml')
    assert sitemap.sitemap_type == 'xml_sitemap'

    sitemap = process_sitemap('tests/sitemap_types/xml_sitemap_index.xml')
    assert sitemap.sitemap_type == 'xml_sitemap_index'

    sitemap = process_sitemap('tests/sitemap_types/atom_feed.xml')
    assert sitemap.sitemap_type == 'atom_feed'

    sitemap = process_sitemap('tests/sitemap_types/plain_text.xml')
    assert sitemap.sitemap_type == 'plain_text'

    sitemap = process_sitemap('tests/sitemap_types/rss_feed.xml')
    assert sitemap.sitemap_type == 'rss_feed'

    sitemap = process_sitemap('tests/sitemap_types/xml_invalid.xml')
    assert sitemap.sitemap_type == 'invalid_file_format'
