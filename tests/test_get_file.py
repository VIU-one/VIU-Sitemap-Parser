from viusitemapparser.get_file import get_file

# Testurls viu mock.io
# 200 XML Sitemap
xml_sitemap_200 = 'https://viusitemaps.free.beeceptor.com/page_200'

# 404
xml_sitemap_404 = 'https://viusitemaps.free.beeceptor.com/page_404'

# 501
xml_sitemap_501 = 'https://viusitemaps.free.beeceptor.com/page_501'

# DNS Error
xml_sitemap_dns_error = 'http://adsljashlsadkjdsalkjdsalaskdjaslkdjaslkdj.de'

# local file exists
xml_sitemap_local_file_exists = 'tests/sitemap_types/xml_sitemap.xml'

# local file exists not
xml_sitemap_local_file_exists_not = 'tests/sitemap_types/no_xml_sitemap.xml'

# Todo: 302 to xml sitemaps

# Todo: 302 to 404

# Todo: Server Timeout Error


def test_get_file():
    # Test remote file
    # 2xx
    res = get_file(xml_sitemap_200)

    res_dict = res.get_file_status_as_dict()

    assert res.sitemap_file_error is None
    assert res.sitemap_received is True
    assert res_dict.get("source_type") == 'remote'

    # 4xx
    res = get_file(xml_sitemap_404)

    res_dict = res.get_file_status_as_dict()
    assert res.sitemap_file_error is not None
    assert res.sitemap_received is False
    assert res_dict.get("source_type") == 'remote'

    # 5xx
    res = get_file(xml_sitemap_501)

    res_dict = res.get_file_status_as_dict()
    assert res.sitemap_file_error is not None
    assert res.sitemap_received is False
    assert res_dict.get("source_type") == 'remote'

    # DNS Error
    res = get_file(xml_sitemap_dns_error)

    assert res.sitemap_file_error is not None
    assert res.sitemap_received is False

    # Test local file

    # exists
    res = get_file(xml_sitemap_local_file_exists)

    assert res.sitemap_file_error is None
    assert res.sitemap_received is True

    # exists not
    res = get_file(xml_sitemap_local_file_exists_not)

    assert res.sitemap_file_error is not None
    assert res.sitemap_received is False

