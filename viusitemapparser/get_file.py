from viusitemapparser.sitemap_file import SitemapFile
import logging
from viusitemapparser.url_functions import check_if_url
import requests
import os.path


def get_file(filename, headers=None, proxy=None):
    result_file = SitemapFile(filename)
    proxies = { 
              "http"  : proxy, 
              "https" : proxy
            }
    try:
        # If remote file: use requests
        if check_if_url(filename):
            result = requests.get(filename, headers=headers, proxies=proxies)
            if 200 >= result.status_code < 300:
                result_file.set_remote_file_from_requests(result)
            else:
                result_file.error_receiving_remote_file(f"Error receiving '{filename}' - status code {result.status_code}")
        # else local file: read it from filesystem
        else:
            if os.path.isfile(filename):
                with open(filename, 'r') as f:
                    result_file.set_local_file(f.read())
                    print(f.read())
            else:
                result_file.error_receiving_local_file(f"There is no file '{filename}'")

    except Exception as e:
        error_message = f"Unable to receive file: {e}"
        logging.error(error_message)
        result_file.error_receiving_file(error_message)
        result_file.sitemap_received = False
        return result_file

    return result_file
