from pydoc import __version__
from unittest import TestCase


class TestVersion(TestCase):

    def test_module_version(self):
        import avaintegration_metapackage

        self.assertEqual("6.0.4.13", avaintegration_metapackage.version)
