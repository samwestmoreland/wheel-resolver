import unittest
import logging
import src.lib.mylib as ml
import third_party.python.packaging.tags as tags


class CrossCompileTest(unittest.TestCase):

    def test_try_platform(self):
        interpreter = "py3"
        gentags = tags.generic_tags(interpreter=interpreter,
                                    abis=None,
                                    platforms=["macosx"])
        # self.assertEqual(sum(1 for _ in gentags), 0)
        self.assertEqual(list(gentags), [])
        # for tag in gentags:
        #     self.assertEqual(tag, None)
