#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""param -- param tag

"""
from .html_tag import HtmlTag


class Param(HtmlTag):
    """Param

    Param is a HtmlTag.
    Responsibility:

    HTML の <param> 要素は、<object> 要素の引数を定義します。

    コンテンツカテゴリ	なし
    許可されている内容	なし。これは 空要素 です。
    タグの省略	空要素であるため開始タグは必須、また終了タグを置いてはなりません。
    許可されている親要素	<object> の子として、他のフローコンテンツより前に配置可能。
    許可されている ARIA ロール	なし
    DOM インターフェイス	HTMLParamElement

    属性
    この要素にはグローバル属性があります。

    name
    引数の名称。
    value
    引数の値
    """
    class AttributeNames(HtmlTag.AttributeNames):
        NAME = 'name'
        VALUE = 'name'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='param', tags=[], attrs=None, **kwargs)

    def set_name(self, value):
        """Set name.

        set_name(value)

        @Arguments:
        - `value`: name value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.NAME, value)

    def get_name(self, ):
        """Get name attribute value.

        get_name()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.NAME, None)

    def remove_name(self, ):
        """Remove name attribute.

        remove_name()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.NAME in self.attrs:
            del self.attrs[self.AttributeNames.NAME]
        return self

    def set_value(self, value):
        """Set value.

        set_value(value)

        @Arguments:
        - `value`: name value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.VALUE, value)

    def get_value(self, ):
        """Get value attribute value.

        get_value()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.VALUE, None)

    def remove_value(self, ):
        """Remove value attribute.

        remove_value()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.VALUE in self.attrs:
            del self.attrs[self.AttributeNames.VALUE]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# param.py ends here
