import unittest
import src.lib.mylib as ml


class CrossCompileTest(unittest.TestCase):
    """ Test cross compilation """

    def test_darwin_tag(self):
        urls = ml.get_download_urls('tensorflow')
        result = ml.get_url(urls, "darwin_amd64")
        self.assertNotEqual(result, 1)
        self.assertIn('.whl', ml.get_basename(result))
        self.assertIn('tensorflow', ml.get_basename(result))

    def test_freebsd_tag(self):
        urls = ml.get_download_urls('tensorflow')
        result = ml.get_url(urls, "freebsd_amd64")
        self.assertNotEqual(result, 1)
        self.assertIn('.whl', ml.get_basename(result))
        self.assertIn('tensorflow', ml.get_basename(result))
