from viusitemapparser.sitemap_file import SitemapFile
import logging
from viusitemapparser.url_functions import check_if_url
import requests
import os.path
import gzip


def _is_gzipped_url(url):
    """Check if URL suggests gzipped content based on file extension"""
    return url.lower().endswith('.gz')


def _is_gzipped_content(content_bytes):
    """Check if binary content is gzipped by checking magic bytes"""
    return content_bytes.startswith(b'\x1f\x8b')


def _decompress_gzip(content_bytes):
    """Decompress gzipped content and return as string"""
    try:
        decompressed = gzip.decompress(content_bytes)
        return decompressed.decode('utf-8')
    except gzip.BadGzipFile as e:
        logging.error(f"Invalid gzip file format: {e}")
        return None
    except Exception as e:
        logging.error(f"Error decompressing gzip content: {e}")
        return None


def get_file(filename, headers=None, proxy=None):
    result_file = SitemapFile(filename)
    proxies = {
              "http": proxy,
              "https": proxy
            }
    try:
        # If remote file: use requests
        if check_if_url(filename):
            result = requests.get(filename, headers=headers, proxies=proxies)
            if 200 <= result.status_code < 300:
                # Check if content is a gzipped file (not server compression)
                # Note: requests automatically handles Content-Encoding: gzip, so we don't need to check that
                is_gzipped_file = _is_gzipped_url(filename) or _is_gzipped_content(result.content)

                if is_gzipped_file:
                    # Handle gzipped content
                    decompressed_content = _decompress_gzip(result.content)
                    if decompressed_content is not None:
                        result_file.set_remote_file_content(decompressed_content, result.headers)
                    else:
                        result_file.error_receiving_remote_file(f"Error decompressing gzipped content from '{filename}'")
                else:
                    # Handle regular text content
                    result_file.set_remote_file_from_requests(result)
            else:
                result_file.error_receiving_remote_file(f"Error receiving '{filename}' - status code {result.status_code}")
        # else local file: read it from filesystem
        else:
            if os.path.isfile(filename):
                if _is_gzipped_url(filename):
                    # Handle gzipped local file
                    with open(filename, 'rb') as f:
                        content_bytes = f.read()
                        decompressed_content = _decompress_gzip(content_bytes)
                        if decompressed_content is not None:
                            result_file.set_local_file(decompressed_content)
                        else:
                            result_file.error_receiving_local_file(f"Error decompressing gzipped file '{filename}'")
                else:
                    # Handle regular text file
                    with open(filename, 'r') as f:
                        result_file.set_local_file(f.read())
            else:
                result_file.error_receiving_local_file(f"There is no file '{filename}'")

    except Exception as e:
        error_message = f"Unable to receive file: {e}"
        logging.error(error_message)
        result_file.error_receiving_file(error_message)
        result_file.sitemap_received = False
        return result_file

    return result_file
