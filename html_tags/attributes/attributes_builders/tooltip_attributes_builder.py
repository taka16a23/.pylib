#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""tooltip_attributes_builder -- tooltip attributes builder

"""
from collections import UserDict

from checker.typecheck import typecheck

from material.forms.tooltip import ToolTip
from .base_attributes_builder import BaseAttributesBuilder


class TooltipAttributesBuilder(BaseAttributesBuilder):
    """TooltipAttributesBuilder

    TooltipAttributesBuilder is a BaseAttributesBuilder.
    Responsibility:
    """
    @classmethod
    def create(cls, message='', placement=ToolTip.Placement.TOP):
        tooltip = ToolTip(message=message, placement=placement)
        instance = TooltipAttributesBuilder(tooltip)
        return instance

    def __init__(self, tooltip):
        self.tooltip = tooltip

    def get_message(self, ):
        """Get message of tooltip.

        get_message()

        @Return: (str) tooltip message

        @Error:
        """
        return self.message

    def set_message(self, message):
        """Set message of tooltip.

        set_message(message)

        @Arguments:
        - `message`: (str) tooltip message

        @Return: this instance

        @Error:
        """
        self.tooltip.set_message(message)
        return self

    def get_placement(self, ):
        """Get tooltip placement.

        get_placement()

        @Return: (str) placement for tooltip

        @Error:
        """
        return self.tooltip.get_placement()

    def set_placement(self, placement):
        """Set placement for tooltip.

        set_placement(placement)

        @Arguments:
        - `placement`: placement for tooltip

        @Return: this instance

        @Error:
        """
        self.tooltip.set_placement(placement)
        return self

    def build_attributes(self, attrs):
        """Build attributes for tooltip.

        build_attributes(attrs)

        @Arguments:
        - `attrs`: (dict or UserDict)

        @Return: this instance

        @Error: TypeError
        """
        typecheck(attrs, 'attrs', (dict, UserDict, ), )
        attrs['data-toggle'] = 'tooltip'
        attrs['data-placement'] = self.tooltip.get_placement()
        attrs['data-original-title'] = self.tooltip.get_message()
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# tooltip_attributes_builder.py ends here
