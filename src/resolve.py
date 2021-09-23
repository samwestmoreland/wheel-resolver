"""
Main
"""

import sys
import src.lib.mylib as ml
import third_party.python.argparse as argparse

# my_platform_tag = util.get_platform()
# print('my os:', my_platform_tag)


def main():
    """ main function """
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--package',
            type=str,
            help='the package to resolve')
    parser.add_argument(
            '--version',
            type=str,
            help='the version of the package to be resolved')
    parser.add_argument(
            '--arch',
            type=str,
            help='specify architecture')
    parser.add_argument(
            '--os',
            type=str,
            help='specify operating system')

    args = parser.parse_args()

    # Fetch all available wheel urls from index
    urls = ml.get_download_urls(args.package, args.version)
    if urls == 1:
        print("couldn't find any matching urls in the index")
        sys.exit(1)

    result = ml.get_url(urls)

    if result is None:
        print("error")
        sys.exit(1)
    elif result == 1:
        print("none of the urls found are \
               compatible with the specified system")
        sys.exit(1)
    else:
        print(result)


main()


###############################
# num_sys_tags = 0
# for tag in tags.sys_tags():
#     print(tag)
#     num_sys_tags += 1

# print()
#
# print('macos tags')
# for tag in tags.generic_tags(None, None, tags.mac_platforms((11, 2))):
#     print(tag)
#
# print()
