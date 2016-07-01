#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""window_spec -- DESCRIPTION

"""


class WindowSpec(object):
    r"""WindowSpec

    WindowSpec is a object.
    Responsibility:
    """
    def is_satisfied_window(self, window):
        r"""SUMMARY

        is_satisfied_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        return False


class WindowSpec(object):
    r"""WindowSpec

    WindowSpec is a object.
    Responsibility:
    """
    def is_satisfied_window(self, window):
        r"""SUMMARY

        is_satisfied_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        return False

    def __call__(self, window):
        return self.is_satisfied_window(window)


class WindowAnySpec(WindowSpec):
    r"""WindowAnySpec

    WindowAnySpec is a WindowSpec.
    Responsibility:
    """
    def is_satisfied_window(self, window):
        r"""SUMMARY

        is_satisfied_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        return True


class WindowIDSpec(WindowSpec):
    r"""WindowIDSpec

    WindowIDSpec is a WindowSpec.
    Responsibility:
    """
    def __init__(self, id):
        r"""

        @Arguments:
        - `id`:
        """
        self._id = id

    def get_id(self, ):
        r"""SUMMARY

        get_id()

        @Return:

        @Error:
        """
        return self._id

    id = property(get_id)

    def is_satisfied_window(self, window):
        r"""SUMMARY

        is_satisfied_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        return self.id == window.get_id()


class WindowTitleSpec(WindowSpec):
    r"""WindowTitleSpec

    WindowTitleSpec is a WindowSpec.
    Responsibility:
    """
    def __init__(self, title):
        r"""

        @Arguments:
        - `title`:
        """
        self._title = title

    def is_satisfied_window(self, window):
        r"""SUMMARY

        is_satisfied_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        return self._title == window.get_title()


class WindowWMClassSpec(WindowSpec):
    r"""WindowWMClassSpec

    WindowWMClassSpec is a WindowSpec.
    Responsibility:
    """
    def __init__(self, wmclass):
        r"""

        @Arguments:
        - `wmclass`:
        """
        self._wmclass = wmclass

    def is_satisfied_window(self, window):
        r"""SUMMARY

        is_satisfied_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        return self._wmclass in window.wmclass


class WindowSpecs(WindowSpec):
    r"""WindowSpecs

    WindowSpecs is a WindowSpec.
    Responsibility:
    """
    def __init__(self, specs):
        r"""

        @Arguments:
        - `specs`:
        """
        WindowSpec.__init__(self, )
        self._specs = []
        for spec in specs:
            self.add_spec(spec)

    def is_satisfied_window(self, window):
        r"""SUMMARY

        is_satisfied_window(window)

        @Arguments:
        - `window`:

        @Return:

        @Error:
        """
        for spec in self._specs:
            if spec.is_satisfied_window(window):
                return True
        return False

    def add_spec(self, spec):
        r"""SUMMARY

        add_spec(spec)

        @Arguments:
        - `spec`:

        @Return:

        @Error:
        """
        self._specs.append(spec)

    def remove_spec(self, spec):
        r"""SUMMARY

        remove_spec(spec)

        @Arguments:
        - `spec`:

        @Return:

        @Error:
        """
        self._specs.remove(spec)

    def has_spec(self, spec):
        r"""SUMMARY

        has_spec(spec)

        @Arguments:
        - `spec`:

        @Return:

        @Error:
        """
        return spec in self._specs



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# window_spec.py ends here
