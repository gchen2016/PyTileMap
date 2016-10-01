
import sys
import sip

import qtpy


__all__ = [
    'getQVariantValue',
    'wheelAngleDelta',
]


try:
    if qtpy.PYQT5:
        QVARIANT_API = 2
    else:
        QVARIANT_API = sip.getapi('QVariant')
except ValueError:
    QVARIANT_API = 1


if QVARIANT_API == 1:
    def getQVariantValue(variant):
        return variant.toPyObject()
else:
    def getQVariantValue(variant):
        return variant

if qtpy.PYQT5:
    def wheelAngleDelta(wheelEvent):
        return wheelEvent.angleDelta().y()
else:
    def wheelAngleDelta(wheelEvent):
        return wheelEvent.delta()
