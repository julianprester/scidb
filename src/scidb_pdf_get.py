#! /usr/bin/env python
"""PDFGetInterface: ScidbPdfGet"""
import colrev.ops.pdf_get
import colrev.package_manager.package_settings
from colrev.package_manager.interfaces import PDFGetInterface
from zope.interface import implementer


@implementer(PDFGetInterface)
class ScidbPdfGet:
    settings_class = ""  # TODO

    settings_class = colrev.package_manager.package_settings.DefaultSettings

    def __init__(
        self,
        *,
        pdf_get_operation: colrev.ops.pdf_get.PDFGet,
        settings: dict,
    ) -> None:
        pass  # TODO

    def get_pdf(self, record):
        """Run the pdf-get operation"""
        # TODO
