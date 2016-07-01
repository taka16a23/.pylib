#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""get_full_property -- DESCRIPTION

"""


class GetPropertyCookie(object):
    r"""PropertyCookie

    PropertyCookie is a object.
    Responsibility:
    """
    def __init__(self, requestor, cookie):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self.requestor = requestor
        self._cookie = cookie
        self._reply = None

    def raw_reply(self, ):
        """SUMMARY

        raw_reply()

        @Return:

        @Error:
        """
        if self._reply is None:
            self._reply = self._cookie.reply()
        return self._reply

    def reply(self, ):
        """SUMMARY

        get_result()

        @Return:

        @Error:
        """
        reply = self.raw_reply()
        if reply.bytes_after:
            self.requestor.set_offset(self.requestor.get_length())
            self.requestor.set_length(reply.bytes_after)
            after_reply = self.requestor.request().reply()
            reply.value += after_reply.value
            reply.value_len += after_reply.value_len
            reply.bytes_after = after_reply.bytes_after
        return reply


class GetFullProperty(object):
    r"""GetProperty

    GetProperty is a object.
    Responsibility:
    """
    class Builder(object):
        r"""Builder

        Builder is a object.
        Responsibility:
        """
        def __init__(self, display, window, property, type):
            r"""

            @Arguments:
            - `display`:
            - `window`:
            - `property`:
            - `type`:
            """
            self.display = display
            self.window = window
            self.property = property
            self.type = type
            self.delete = False
            self.offset = 0
            self.length = 20

        def set_display(self, display):
            """SUMMARY

            set_display(display)

            @Arguments:
            - `display`:

            @Return:

            @Error:
            """
            self.display = display
            return self

        def set_delete(self, delete):
            """SUMMARY

            set_delete(delete)

            @Arguments:
            - `delete`:

            @Return:

            @Error:
            """
            self.delete = delete
            return self

        def set_window(self, window):
            """SUMMARY

            set_window(window)

            @Arguments:
            - `window`:

            @Return:

            @Error:
            """
            self.window = window
            return self

        def set_property(self, property):
            """SUMMARY

            set_property(property)

            @Arguments:
            - `property`:

            @Return:

            @Error:
            """
            self.property = property
            return self

        def set_type(self, type):
            """SUMMARY

            set_type(type)

            @Arguments:
            - `type`:

            @Return:

            @Error:
            """
            self.type = type
            return self

        def set_offset(self, offset):
            """SUMMARY

            set_offset(offset)

            @Arguments:
            - `offset`:

            @Return:

            @Error:
            """
            self.offset = offset
            return self

        def set_length(self, length):
            """SUMMARY

            set_length(length)

            @Arguments:
            - `length`:

            @Return:

            @Error:
            """
            self.length = length
            return self

        def build(self, ):
            """SUMMARY

            build()

            @Return:

            @Error:
            """
            return GetFullProperty(
                self.display, self.delete, self.window, self.property,
                self.type, self.offset, self.length)

    def __init__(self, display, delete, window, property, type, offset, length):
        r"""

        @Arguments:
        - `delete`:
        - `property`:
        - `type`:
        - `offset`:
        - `length`:
        """
        self.display = display
        self.delete = delete
        self.window = window
        self.property = property
        self.type = type
        self.offset = offset
        self.length = length

    def get_display(self, ):
        """SUMMARY

        get_display()

        @Return:

        @Error:
        """
        return self.display

    def set_display(self, display):
        """SUMMARY

        set_display(display)

        @Arguments:
        - `display`:

        @Return:

        @Error:
        """
        self.display = display

    def get_delete(self, ):
        """SUMMARY

        get_delete()

        @Return:

        @Error:
        """
        return self.delete

    def set_delete(self, delete):
        """SUMMARY

        set_delete(delete)

        @Arguments:
        - `delete`:

        @Return:

        @Error:
        """
        self.delete = delete

    def get_window(self, ):
        """SUMMARY

        get_window()

        @Return:

        @Error:
        """
        return self.window

    def set_window(self, window):
        """SUMMARY

        set_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        self.window = window

    def get_property(self, ):
        """SUMMARY

        get_property()

        @Return:

        @Error:
        """
        return self.property

    def set_property(self, property):
        """SUMMARY

        set_property(property)

        @Arguments:
        - `property`:

        @Return:

        @Error:
        """
        self.property = property

    def get_type(self, ):
        """SUMMARY

        get_type()

        @Return:

        @Error:
        """
        return self.type

    def set_type(self, type):
        """SUMMARY

        set_type(type)

        @Arguments:
        - `type`:

        @Return:

        @Error:
        """
        self.type = type

    def get_offset(self, ):
        """SUMMARY

        get_offset()

        @Return:

        @Error:
        """
        return self.offset

    def set_offset(self, offset):
        """SUMMARY

        set_offset(offset)

        @Arguments:
        - `offset`:

        @Return:

        @Error:
        """
        self.offset = offset

    def get_length(self, ):
        """SUMMARY

        get_length()

        @Return:

        @Error:
        """
        return self.length

    def set_length(self, length):
        """SUMMARY

        set_length(length)

        @Arguments:
        - `length`:

        @Return:

        @Error:
        """
        self.length = length

    def request(self, ):
        """SUMMARY

        reply()

        @Return:

        @Error:
        """
        cookie = self.display.core.GetProperty(
            self.delete, self.window, self.property,
            self.type, self.offset, self.length)
        return GetPropertyCookie(self, cookie)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# get_full_property.py ends here
