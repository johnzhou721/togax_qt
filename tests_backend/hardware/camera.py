# Somehow collection fails without this.
import pytest


class CameraProbe:
    pytest.skip("Location not impl'd yet on Qt", allow_module_level=True)
    pass
