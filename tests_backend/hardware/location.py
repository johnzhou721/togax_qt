# Somehow collection fails without this.
import pytest


class LocationProbe:
    pytest.skip("LocationProbe not impl'd yet on Qt", allow_module_level=True)
    pass
