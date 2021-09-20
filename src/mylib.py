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


def is_compatible_with_this_system(wheel):
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


def get_url(urls):
    for url in urls:
        basename = os.path.basename(url)
        _, ext = os.path.splitext(basename)
        if ext == '.whl':
            # _, _, _, tagliatelles = parse_wheel_filename(basename)
            # for tag in tagliatelles:
            #     print('tag:', tag)

            if is_compatible_with_this_system(basename):
                return url

    return 1


def get_download_urls(package, version=None):
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
