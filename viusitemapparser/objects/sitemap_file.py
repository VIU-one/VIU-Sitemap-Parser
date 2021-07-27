

class SitemapFile:
    sitemap_file_name = None
    sitemap_contents = None
    sitemap_headers = None
    sitemap_source_type = None      # remote or local
    sitemap_file_error = None
    sitemap_received = False
    sitemap_lxml = None
    sitemap_plain_text = None
    sitemap_type = None             # one of xml_sitemap, xml_sitemap_index, rss_feed, atom_feed, plain_text,
                                    # invalid_file_format

    def __init__(self, filename):
        self.sitemap_file_name = filename

    def set_remote_file_from_requests(self, result):
        self.sitemap_source_type = 'remote'
        self.sitemap_received = True
        self.sitemap_contents = result.text
        self.sitemap_headers = result.headers

    def set_local_file(self, file_contents):
        self.sitemap_source_type = 'local'
        self.sitemap_received = True
        self.sitemap_contents = file_contents

    def error_receiving_file(self, message):
        self.sitemap_file_error = message

    def error_receiving_remote_file(self, message):
        self.sitemap_source_type = 'remote'
        self.sitemap_file_error = message

    def error_receiving_local_file(self, message):
        self.sitemap_source_type = 'local'
        self.sitemap_file_error = message

    def get_file_status_as_dict(self):
        return {'file_name': self.sitemap_file_name,
                'file_headers': self.sitemap_headers,
                'source_type': self.sitemap_source_type,
                'file_error': self.sitemap_file_error,
                'file_received': self.sitemap_received,
                'sitemap_type': self.sitemap_type}

    def get_content(self):
        if self.sitemap_contents:
            return self.sitemap_contents.strip()
        else:
            return None

    def has_lxml(self):
        if self.sitemap_lxml:
            return True
        else:
            return False

    def set_lxml(self, lxml):
        self.sitemap_lxml = lxml

    def set_plain_text(self, content):
        self.sitemap_plain_text = content

    def set_sitemap_type(self, sitemap_type):
        self.sitemap_type = sitemap_type
