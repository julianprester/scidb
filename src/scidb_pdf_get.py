#! /usr/bin/env python
"""PDFGetInterface: ScidbPdfGet"""

from zope.interface import implementer
from colrev.package_manager.interfaces import PDFGetInterface
import colrev.package_manager.package_settings
import colrev.ops.pdf_get

@implementer(PDFGetInterface)
class ScidbPdfGet:
    settings_class = '' #TODO

    settings_class = colrev.package_manager.package_settings.DefaultSettings

    def __init__(
        self,
        *,
        pdf_get_operation: colrev.ops.pdf_get.PDFGet,
        settings: dict,
    ) -> None:
      pass # TODO

    def get_pdf(self, record):
      """Run the pdf-get operation"""
      # TODO

