#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""display_multiton -- DESCRIPTION

"""


# class DisplayMultitonMeta(type):
#     r"""DisplayMultitonMeta

#     DisplayMultitonMeta is a type.
#     Responsibility:
#     """
#     _instances = {}

#     def __call__(cls, display, *args, **kwargs):
#         if display not in cls._instances:
#             cls._instances[display] = super(
#                 DisplayMultitonMeta, cls).__call__(display, *args, **kwargs)
#         return cls._instances[display]

# @classmethod
# def get_instance(cls, display):
#     if display not in cls._instances:
#         cls._instances[display] = cls(display)
#     return cls._instances[display]


class multiton_display(object):
    r"""multiton_display

    multiton_display is a object.
    Responsibility:
    """
    __instances = {}

    def __call__(self, cls):
        def getinstance(display, *args, **kwargs):
            if cls not in multiton_display.__instances:
                multiton_display.__instances[cls] = {}
            if display not in multiton_display.__instances[cls]:
                multiton_display.__instances[cls][display] = cls(
                    display, *args, **kwargs)
            return multiton_display.__instances[cls][display]
        return getinstance

    @staticmethod
    def instances():
        r"""SUMMARY

        instances()

        @Return:

        @Error:
        """
        return multiton_display.__instances

    @staticmethod
    def get_instances(klass):
        r"""SUMMARY

        get_instances(cls)

        @Arguments:
        - `cls`:

        @Return:

        @Error:
        """
        return multiton_display.instances().get(klass, None)


# def display_multiton(cls):
#     instances = {}
#     def getinstance(display, *args, **kwargs):
#         if cls not in instances:
#             instances[cls] = {}
#         if display not in instances[cls]:
#             instances[cls][display] = cls(display, *args, **kwargs)
#         return instances[cls][display]
#     return getinstance



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# display_multiton.py ends here
