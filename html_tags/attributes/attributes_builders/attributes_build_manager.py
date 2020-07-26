#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""attributes_build_manager -- attributes build manager

"""
from checker.typecheck import typecheck

from .base_attributes_builder import BaseAttributesBuilder


class AttributesBuildManager(object):
    """AttributesBuildManager

    AttributesBuildManager is a object.
    Responsibility:
    """
    def __init__(self, builders=[]):
        self.builders = list(builders)

    def append_builder(self, builder):
        """SUMMARY

        append_builder(builder)

        @Arguments:
        - `builder`: (BaseAttributesBuilder) attributes builder

        @Return:

        @Error:
        """
        typecheck(builder, 'builder', (BaseAttributesBuilder, ))
        self.builders.append(builder)
        return self

    def remove_builder(self, builder):
        """Remove builder.

        remove_builder(builder)

        @Arguments:
        - `builder`:

        @Return: (BaseAttributesBuilder) attributes builder

        @Error:
        """
        self.builders.remove(builder)
        return self

    def has_builder(self, builder):
        """Check hold builder.

        has_builder(builder)

        @Arguments:
        - `builder`: (BaseAttributesBuilder) attributes builder

        @Return:

        @Error:
        """
        return builder in self.builders

    def clear_builders(self, ):
        """Clear builders.

        clear_builders()

        @Return: this instance

        @Error:
        """
        self.builders.clear()
        return self

    def build(self, attrs):
        """Build attributs.

        build(attrs)

        @Arguments:
        - `attrs`: attributes

        @Return: this instance

        @Error:
        """
        for builder in self.builders:
            builder.build_attributes(attrs)
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# attributes_build_manager.py ends here
