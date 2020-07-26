#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: __init__.py


"""
from material.forms.tags.attributes.attr_value import AttrValue
from material.forms.tags.attributes.attributes import Attributes
from material.forms.tags.attributes.only_one_attr_value import OnlyOneAttrValue
from material.forms.tags.attributes.attributes_builders import TooltipAttributesBuilder
from material.forms.tags.attributes.attributes_builders import AttributesBuildManager
from material.forms.tags.tag import Tag


__all__ = ['AttrValue', 'Attributes', 'OnlyOneAttrValue',
           'TooltipAttributesBuilder', 'AttributesBuildManager',
           'Tag',
]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# __init__.py ends here
