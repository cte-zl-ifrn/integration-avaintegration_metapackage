from importlib.metadata import version
from unittest import TestCase


class TestVersion(TestCase):

    def test_module_version(self):
        import avaintegration_metapackage

        self.assertEqual(
            version("avaintegration-metapackage"),
            avaintegration_metapackage.version,
        )
