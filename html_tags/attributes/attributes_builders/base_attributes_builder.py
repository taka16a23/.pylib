#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""base_attributes_builder -- base attributes builder

"""


class BaseAttributesBuilder(object):
    """BaseAttributesBuilder

    BaseAttributesBuilder is a object.
    Responsibility:
    """
    def build_attributes(self, attrs):
        raise NotImplementedError()
        typecheck(attrs, 'attrs', (dict, UserDict, ), )
        attrs['data-toggle'] = 'tooltip'
        attrs['data-placement'] = self.placement
        attrs['data-original-title'] = self.message
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# base_attributes_builder.py ends here
