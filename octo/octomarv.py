from os.path import basename
from urllib.parse import urlparse
from urllib.request import urlopen, Request
from collections import OrderedDict
from binascii import hexlify
from email.message import Message
import json
import os

CONF_PATH = '/home/marwan/.marv/prusa.json'


def parse_conf():
    return json.loads(open(CONF_PATH).read(), object_pairs_hook=OrderedDict)


def call_api(path, host=None, method='GET', data=None, extra_headers=()):
    conf = parse_conf()
    host = host if host else conf['default']
    apikey = conf['keys'][host]
    url = 'http://' + host + path
    headers = dict({'X-Api-Key': apikey}, **dict(extra_headers))
    request = Request(url, data, headers, method=method)
    response = urlopen(request)
    content = response.read()
    content_type = response.info().get_content_type()
    return json.loads(content.decode()) if content_type == 'application/json' else content


def get_version(host=None):
    return call_api('/api/version', host=host)


def get_status(host=None):
    return call_api('/api/printer', host=host)


def list_files(host=None):
    return call_api('/api/files', host=host)


def delete_file(resource):
    parts = urlparse(resource)
    return call_api(parts.path, parts.netloc, 'DELETE')


def delete_all_files(host=None):
    results = list_files(host)
    count = len(results['files'])
    for i, row in enumerate(results['files']):
        print('DELETING', i, 'of', count, row['refs']['resource'])
        delete_file(row['refs']['resource'])


def get_mime_header(header, value, **kwargs):
    msg = Message()
    msg.add_header(header, value, **kwargs)
    return msg.as_string().replace('\n\n', '\r\n').encode()


def get_multipart_form_data(name, path):
    filename = basename(path)
    data = open(path, 'rb').read()
    boundary = hexlify(os.urandom(16))
    header = get_mime_header('Content-Disposition', 'form-data', name=name, filename=filename)
    parts = [b'--' + boundary, header, data, b'--' + boundary + b'--']
    body = b'\r\n'.join(parts) + b'\r\n'
    content_type = 'multipart/form-data; boundary=%s' % boundary.decode()
    return body, content_type


def upload_file(filename, host=None):
    body, content_type = get_multipart_form_data('file', filename)
    extra_headers = {'Content-Type': content_type}
    return call_api('/api/files/local', host=host, method='POST', data=body, extra_headers=extra_headers)


def print_file(resource):
    parts = urlparse(resource)
    body = b'{"command": "select", "print": true}'
    extra_headers = {'Content-Type': 'application/json'}
    return call_api(parts.path, parts.netloc, 'POST', data=body, extra_headers=extra_headers)


def set_tool_temp_target(temp=215, name='tool0', host=None):
    request = dict(command='target', targets={name: temp})
    body = json.dumps(request).encode()
    extra_headers = {'Content-Type': 'application/json'}
    return call_api('/api/printer/tool', host, 'POST', data=body, extra_headers=extra_headers)


def set_bed_temp_target(temp=60, host=None):
    request = dict(command='target', target=temp)
    body = json.dumps(request).encode()
    extra_headers = {'Content-Type': 'application/json'}
    return call_api('/api/printer/bed', host, 'POST', data=body, extra_headers=extra_headers)
