import xml.etree.ElementTree as ET
import logging


def parse_file(file_content):

    try:
        lxml = ET.fromstring(file_content)
        return lxml
    except Exception as e:
        logging.exception(e)
