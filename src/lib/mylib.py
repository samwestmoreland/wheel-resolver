"""
Some methods for wheel fetching and selection
"""

import os
from third_party.python.packaging.utils import parse_wheel_filename
import third_party.python.packaging.tags as tags
import third_party.python.distlib.locators as locators


def is_compatible(wheel, arch):
    """
    Check whether the given python package is a wheel compatible with the
    current platform and python interpreter.
    Compatibility is based on https://www.python.org/dev/peps/pep-0425/
    """
    # Get the tag from the wheel we're checking
    _, _, _, tag = parse_wheel_filename(wheel)

    # taglist is a list (generator) of tags that are compatible
    taglist = tags.generic_tags(platforms=arch) if arch else tags.sys_tags()

    for tagliatelle in taglist:
        if tagliatelle in tag:
            return True
    return False


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


def get_url(urls, arch):
    """
    From the list of urls we got from the wheel index, return the first
    one that is compatible (either with our system or a provided one)
    """
    if arch:
        count = 0
        for _ in tags.generic_tags(platforms=[arch]):
            count += 1
        if count == 0:
            print("Didn't generate any tags for arch =", arch)
            return 1

    for url in urls:
        if is_wheel_file(url) and is_compatible(get_basename(url), arch):
            return url

    print("No compatible urls for", count, "system tags")
    print("The tags given to me for this arch were:")
    print('\n'.join(map(str, list(tags.generic_tags(platforms=[arch])))))
    print('The tags I was looking for were:')
    for url in urls:
        if is_wheel_file(url):
            _, _, _, tag = parse_wheel_filename(get_basename(url))
            print(tag)

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
