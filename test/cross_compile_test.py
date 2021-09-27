import unittest
import src.lib.mylib as ml


class CrossCompileTest(unittest.TestCase):
    """ Test cross compilation """

    def test_darwin_tag(self):
        urls = ml.get_download_urls('tensorflow')
        # result = ml.get_url(urls, "darwin_amd64")
        result = ml.get_url(urls, "macosx_10_11_x86_64")
        self.assertNotEqual(result, 1)
        self.assertIn('.whl', ml.get_basename(result))
        self.assertIn('tensorflow', ml.get_basename(result))

    def test_freebsd_tag(self):
        package = 'six'
        urls = ml.get_download_urls(package)
        archs = ["manylinux"]
        result = ml.get_url(urls, archs)

        # Assert we get a url back from get_url
        self.assertNotEqual(result, 1)

        # Assert that the url we get back is for a .whl file
        self.assertIn('.whl', ml.get_basename(result))
        self.assertIn(package, ml.get_basename(result))
