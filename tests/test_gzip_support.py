from viusitemapparser.get_file import get_file
from viusitemapparser.vsp import get_sitemap_contents
import os


def test_gzip_local_files():
    """Test that gzipped local files are properly decompressed"""
    # Test gzipped XML sitemap
    xml_gz_path = 'tests/sitemap_types/xml_sitemap.xml.gz'
    xml_path = 'tests/sitemap_types/xml_sitemap.xml'

    # Compare gzipped vs non-gzipped content
    result_gz = get_file(xml_gz_path)
    result_normal = get_file(xml_path)

    assert result_gz.sitemap_received is True
    assert result_gz.sitemap_file_error is None
    assert result_gz.sitemap_source_type == 'local'

    # Content should be identical after decompression
    assert result_gz.get_content() == result_normal.get_content()

    # Test gzipped plain text sitemap
    txt_gz_path = 'tests/sitemap_types/plain_text.txt.gz'
    txt_path = 'tests/sitemap_types/plain_text.txt'

    result_txt_gz = get_file(txt_gz_path)
    result_txt_normal = get_file(txt_path)

    assert result_txt_gz.sitemap_received is True
    assert result_txt_gz.sitemap_file_error is None
    assert result_txt_gz.get_content() == result_txt_normal.get_content()


def test_gzip_full_processing():
    """Test that gzipped files work through the complete processing pipeline"""
    # Test XML sitemap processing
    xml_gz_path = 'tests/sitemap_types/xml_sitemap.xml.gz'
    xml_path = 'tests/sitemap_types/xml_sitemap.xml'

    # Process both files
    sitemap_gz, entries_gz = get_sitemap_contents(xml_gz_path)
    sitemap_normal, entries_normal = get_sitemap_contents(xml_path)

    # Should have same sitemap type
    assert sitemap_gz['sitemap_type'] == sitemap_normal['sitemap_type']
    assert sitemap_gz['sitemap_type'] == 'xml_sitemap'

    # Should have same entries
    entries_gz_list = list(entries_gz)
    entries_normal_list = list(entries_normal)

    assert len(entries_gz_list) == len(entries_normal_list)

    for entry_gz, entry_normal in zip(entries_gz_list, entries_normal_list):
        assert entry_gz == entry_normal

    # Test plain text processing
    txt_gz_path = 'tests/sitemap_types/plain_text.txt.gz'
    txt_path = 'tests/sitemap_types/plain_text.txt'

    sitemap_txt_gz, entries_txt_gz = get_sitemap_contents(txt_gz_path)
    sitemap_txt_normal, entries_txt_normal = get_sitemap_contents(txt_path)

    assert sitemap_txt_gz['sitemap_type'] == sitemap_txt_normal['sitemap_type']
    assert sitemap_txt_gz['sitemap_type'] == 'plain_text'

    entries_txt_gz_list = list(entries_txt_gz)
    entries_txt_normal_list = list(entries_txt_normal)

    assert entries_txt_gz_list == entries_txt_normal_list


def test_gzip_error_handling():
    """Test error handling for invalid gzipped files"""
    # Test non-existent gzipped file
    result = get_file('tests/sitemap_types/nonexistent.xml.gz')
    assert result.sitemap_received is False
    assert result.sitemap_file_error is not None
    assert 'no file' in result.sitemap_file_error.lower()

    # Test invalid gzipped file (create a fake .gz file)
    fake_gz_path = 'tests/sitemap_types/fake.xml.gz'
    with open(fake_gz_path, 'w') as f:
        f.write('This is not gzipped content')

    try:
        result = get_file(fake_gz_path)
        assert result.sitemap_received is False
        assert result.sitemap_file_error is not None
        assert 'decompressing' in result.sitemap_file_error.lower()
    finally:
        # Clean up
        if os.path.exists(fake_gz_path):
            os.remove(fake_gz_path)


def test_gzip_detection_functions():
    """Test the internal gzip detection functions"""
    from viusitemapparser.get_file import _is_gzipped_url, _is_gzipped_content, _decompress_gzip

    # Test URL detection
    assert _is_gzipped_url('sitemap.xml.gz') is True
    assert _is_gzipped_url('sitemap.XML.GZ') is True
    assert _is_gzipped_url('sitemap.xml') is False
    assert _is_gzipped_url('sitemap.txt') is False

    # Test content detection (gzip magic bytes)
    gzip_magic = b'\x1f\x8b\x08'  # gzip magic bytes
    assert _is_gzipped_content(gzip_magic) is True
    assert _is_gzipped_content(b'regular content') is False

    # Test decompression
    import gzip
    original_content = "Hello, world!"
    compressed_content = gzip.compress(original_content.encode('utf-8'))
    decompressed = _decompress_gzip(compressed_content)
    assert decompressed == original_content

    # Test invalid gzip content
    invalid_compressed = b'invalid gzip content'
    result = _decompress_gzip(invalid_compressed)
    assert result is None


if __name__ == '__main__':
    test_gzip_local_files()
    test_gzip_full_processing()
    test_gzip_error_handling()
    test_gzip_detection_functions()
    print("All gzip tests passed!")
