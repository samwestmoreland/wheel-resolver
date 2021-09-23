"""
Some methods for wheel fetching and selection
"""

import os
from third_party.python.packaging.utils import parse_wheel_filename
import third_party.python.packaging.tags as tags
import third_party.python.distlib.locators as locators
# from wheel_inspect import inspect_wheel


def is_compatible_with(system, wheel):
    _, _. _, tag = parse_wheel_filename(wheel)
    count = 0
    for systag in tags.generic_tags(None, None, system):
        count += 1
        if systag in tag:
            return True


def is_compatible(wheel):
    """
    Check whether the given python package is a wheel compatible with the
    current platform and python interpreter.
    Compatibility is based on https://www.python.org/dev/peps/pep-0425/
    """
    _, _, _, tag = parse_wheel_filename(wheel)
    count = 0
    for systag in tags.sys_tags():
        count += 1
        if systag in tag:
            # print('match with sys_tag:', systag)
            # print('tag', count, 'of', num_sys_tags)
            return True


def get_basename(url):
    """
    Return the url basename,
    i.e. https://www.example.com/foo/bar.whl -> bar.whl
    """
    return os.path.basename(url)


def is_wheel_file(url):
    """ Return whether or not this is a .whl file """
    basename = os.path.basename(url)
    _, ext = os.path.splitext(basename)
    return ext == '.whl'


def get_url(urls):
    """
    From the list of urls we got from the wheel index, return the first
    one that is compatible (either with our system or a provided one)
    """
    for url in urls:
        if is_wheel_file(url) and is_compatible(get_basename(url)):
            return url

    return 1


def get_download_urls(package, version=None):
    """
    Return all downloadable urls from wheel index that match
    the provided package name and version requirement
    """
    if package is None:
        return None

    mylocator = locators.PyPIJSONLocator('https://pypi.org/pypi')
    # Populate requirement
    requirement = None
    if version is not None:
        requirement = package + '==' + version
    else:
        requirement = package
    dist = mylocator.locate(requirement)
    if dist is not None:
        return dist.download_urls
    return 1
