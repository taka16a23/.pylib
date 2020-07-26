#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""tag -- Tag class

"""
from collections import deque

from .attributes.attributes import Attributes
from checker.typecheck import typecheck


class Tag(object):
    """Tag

    Tag is a object.
    Responsibility:
    """
    def __init__(self, name, tags=[], attrs=None, **kwargs):
        # tag name
        self.tag_name = name
        self.tags = deque(tags)
        self.attrs = Attributes()
        if attrs is not None:
            self.attrs.update(attrs)
        self.attrs.update(**kwargs)

    def get_tag_name(self, ):
        """Get tag name.

        get_name()

        @Return: tag name

        @Error:
        """
        return self.tag_name

    def set_tag_name(self, name):
        """Set tag name.

        set_name(name)

        @Arguments:
        - `name`: tag name

        @Return: this instance

        @Error:
        """
        self.tag_name = name
        return self

    def get_attrs(self, ):
        return self.attrs

    def clear_attrs(self, ):
        """Clear attributes.

        clear_attrs()

        @Return: this instance

        @Error:
        """
        self.attrs.clear()
        return self

    def set_attr_value(self, name, value):
        """Set attribute value.

        set_attr_value(name, value)

        @Arguments:
        - `name`: attribute name
        - `value`: value

        @Return: this instance

        @Error:
        """
        self.attrs.set_value(name, value)
        return self

    def append_attribute_value(self, name, value):
        """Append atrribute value.

        append_attribute_value(name, value)

        @Arguments:
        - `name`: attribute name
        - `value`: value of attribute

        @Return: this instance

        @Error:
        """
        self.attrs.append_value(name, value)
        return self

    def remove_attribute_value(self, name, value):
        """Remove attribute value.

        remove_attribute_value(name, value)

        @Arguments:
        - `name`: attribute name
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self.attrs.remove_value(name, value)
        return self

    def clear_attribute_value(self, name):
        """Clear attribute value.

        clear_attribute_value(name)

        @Arguments:
        - `name`: attribute name

        @Return: this instance

        @Error:
        """
        if name in self.attrs:
            self.attrs[name].clear()
        return self

    def remove_attirbute(self, name):
        """Remove attribute.

        remove_attirbute(name)

        @Arguments:
        - `name`: attribute name

        @Return: this instance

        @Error:
        """
        if name in self.attrs:
            del self.attrs[name]
        return self

    def set_attribute_none(self, name):
        """Set attribute none.

        set_attribute_none(name)

        @Arguments:
        - `name`:

        @Return: this instance

        @Error:
        """
        self.attrs.set_none(name)
        return self

    def get_attribute_value(self, name, default=None):
        """Get attribute value.

        get_attribute_value(name)

        @Arguments:
        - `name`: attribute name
        - `default`: default

        @Return:

        @Error:
        """
        return self.attrs.get(name, default)

    def contains_attribute_value(self, name, value):
        """Contain value.

        contains_attribute_value(name, value)

        @Arguments:
        - `name`: attribute name
        - `value`: attribute value

        @Return:

        @Error:
        """
        return self.attrs.contains_value(name, value)

    def update_attribute(self, attr, **kwargs):
        """Update attributes.

        update_attribute(attr)

        @Arguments:
        - `attr`:
        - `kwargs`:

        @Return: this instance

        @Error:
        """
        self.attrs.update(attr, **kwargs)
        return self

    def setdefault_attribute(self, name, default=None):
        """Set default attribute.

        setdefault_attribute(name, default=None)

        @Arguments:
        - `name`: name of attribute
        - `default`:

        @Return: this instance

        @Error:
        """
        self.attrs.setdefault(name, default)
        return self

    def append_tag(self, tag):
        """Append tag to holding list.

        append_tag(tag)

        @Arguments:
        - `tag`: Tag instance

        @Return: this instance

        @Error:
        """
        typecheck(tag, 'tag', self.__class__)
        self.tags.append(tag)
        return self

    def clear_tags(self, ):
        """Clear tags.

        clear_tags()

        @Return: this instance

        @Error:
        """
        self.tags.clear()
        return self

    def count_tags(self, ):
        """Count tags.

        count_tags()

        @Return: (int) count tags on this instance.

        @Error:
        """
        return len(self.tags)

    def extend_tags(self, tags):
        """Extend tags.

        extend_tags(tags)

        @Arguments:
        - `tags`: tag list

        @Return: this instance

        @Error:
        """
        for tag in tags:
            typecheck(tag, 'tag', self.__class__)
        self.tags.extend(tags)
        return self

    def pop_tag(self, ):
        """Pop holding tags.

        pop_tag()

        @Return: Tag instance

        @Error:
        """
        return self.tags.pop()

    def remove_tag(self, tag):
        """Remove tag.

        remove_tag(tag)

        @Arguments:
        - `tag`: Tag instance

        @Return: this instance

        @Error:
        """
        self.tags.remove(tag)
        return self

    def list_tags(self, ):
        """list Tags.

        list_tags()

        @Return: tag list

        @Error:
        """
        return self.tags



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# tag.py ends here
