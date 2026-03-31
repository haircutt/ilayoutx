"""ilayoutx root module."""

# from ilayoutx._ilayoutx import __version__
try:
    from ilayoutx._ilayoutx import __version__
except ImportError:
    __version__ = "0.0.0"
from ilayoutx import (
    layouts,
    packing,
    routing,
    experimental,
)



    __version__ = "0.0.0"
__all__ = (
    __version__,
    layouts,
    packing,
    routing,
    experimental,
)
