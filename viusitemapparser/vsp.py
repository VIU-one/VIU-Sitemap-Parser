from viusitemapparser.detect_filetype import detect
from viusitemapparser.parse_file import parse_file
from viusitemapparser.get_file import get_file
from viusitemapparser.get_sitemap_entries import entries


def process_sitemap(filename, headers=None):
    sitemap = get_file(filename, headers=headers)
    lxml_obj = parse_file(sitemap.get_content())
    if lxml_obj:
        sitemap.set_lxml(lxml_obj)
    else:
        sitemap.set_plain_text(sitemap.get_content())

    sitemap_type = detect(sitemap)
    sitemap.set_sitemap_type(sitemap_type)

    return sitemap


def get_sitemap_contents(filename, only_relevant_rss_fields=False, only_relevant_atom_fields=False, headers=None):
    sitemap = process_sitemap(filename, headers)
    sitemap_entries = entries(sitemap, only_relevant_rss_fields=only_relevant_rss_fields,
                              only_relevant_atom_fields=only_relevant_atom_fields)
    return sitemap.get_file_status_as_dict(), sitemap_entries
