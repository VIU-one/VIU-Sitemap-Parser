from urllib.parse import urlparse


def check_if_url(filename):
    try:
        result = urlparse(filename)
        return all([result.scheme, result.netloc])
    except:
        return False
