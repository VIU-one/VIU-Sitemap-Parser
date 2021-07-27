

def detect(sitemap):
    if sitemap.has_lxml():
        if "sitemaps.org" in sitemap.sitemap_lxml.tag.lower() and "urlset" in sitemap.sitemap_lxml.tag.lower():
            return "xml_sitemap"
        elif "sitemaps.org" in sitemap.sitemap_lxml.tag.lower() and "sitemapindex" in sitemap.sitemap_lxml.tag.lower():
            return "xml_sitemap_index"
        elif "atom" in sitemap.sitemap_lxml.tag.lower():
            return "atom_feed"
        elif "rss" in sitemap.sitemap_lxml.tag.lower():
            return "rss_feed"
        else:
            return "invalid_file_format"
    else:
        # file has no valid format, treat it as plain_text
        return "plain_text"

