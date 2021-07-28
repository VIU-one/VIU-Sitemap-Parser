from viusitemapparser.url_functions import check_if_url


def test_url_functions():
    assert check_if_url('https://www.test.de') is True
    assert check_if_url('https://www.test.de/path') is True
    assert check_if_url('https://www.test.de/?param=value') is True
    assert check_if_url('https://www.test.de/?param=') is True
    assert check_if_url('http://www.test1234.com') is True
    assert check_if_url('www.test1234.com') is False
    assert check_if_url('/folder') is False
    assert check_if_url('/folder/folder') is False
    assert check_if_url('/folder/folder/folder') is False
    assert check_if_url(None) is False
