# 2016.11.19 19:58:44 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/email/mime/nonmultipart.py
"""Base class for MIME type messages that are not multipart."""
__all__ = ['MIMENonMultipart']
from email import errors
from email.mime.base import MIMEBase

class MIMENonMultipart(MIMEBase):
    """Base class for MIME multipart/* type messages."""

    def attach(self, payload):
        raise errors.MultipartConversionError('Cannot attach additional subparts to non-multipart/*')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\Lib\email\mime\nonmultipart.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:58:44 Støední Evropa (bìžný èas)
