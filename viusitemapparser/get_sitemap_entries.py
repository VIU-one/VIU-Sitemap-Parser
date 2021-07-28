from collections import defaultdict
from viusitemapparser.url_functions import check_if_url


def etree_to_dict(t):
    prefix, has_namespace, postfix = t.tag.partition('}')
    if has_namespace:
        t.tag = postfix  # strip all namespaces
    t.tag = t.tag.lower()
    d = {t.tag: {} if t.attrib else None}
    children = list(t)

    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        d = {t.tag: {k: v[0] if len(v) == 1 else v for k, v in dd.items()}}

    if t.attrib:
        d[t.tag].update(('@' + k, v) for k, v in t.attrib.items())

    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
              d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d


def entries(sitemap, only_relevant_rss_fields=False, only_relevant_atom_fields=False):
    if sitemap.sitemap_type == 'xml_sitemap':
        for url in sitemap.sitemap_lxml:
            yield etree_to_dict(url).get("url")

    elif sitemap.sitemap_type == 'xml_sitemap_index':
        for sitemap_index in sitemap.sitemap_lxml:
            yield etree_to_dict(sitemap_index).get("sitemap")

    elif sitemap.sitemap_type == 'rss_feed':
        for channel in sitemap.sitemap_lxml:
            for item in channel:
                row_res = etree_to_dict(item).get("item")
                if item and row_res:
                    if only_relevant_rss_fields:
                        yield {'link': row_res.get('link'),
                               'pubdate': row_res.get('pubdate')}
                    else:
                        yield row_res

    elif sitemap.sitemap_type == 'atom_feed':
        for entry in sitemap.sitemap_lxml:
            row_res = etree_to_dict(entry).get("entry")
            if entry and row_res:
                if only_relevant_atom_fields:
                    yield {'link': row_res.get('link'),
                           'updated': row_res.get('updated')}
                else:
                    yield row_res

    elif sitemap.sitemap_type == 'plain_text':
        if sitemap.sitemap_plain_text:
            for line in sitemap.sitemap_plain_text.splitlines():
                line = line.strip()
                # only yield line if it's a valid url
                if line:
                    if check_if_url(line):
                        yield line
