#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""slot -- slot tag

"""
from .html_tag import HtmlTag


class Slot(HtmlTag):
    """Slot

    Slot is a HtmlTag.
    Responsibility:

    HTML の <slot> 要素 — ウェブコンポーネント技術の一部 — は、
    ウェブコンポーネント内で別な DOM ツリーを構築し、
    いっしょに表示することができる独自のマークアップを
    入れることができるプレイスホルダーです。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ
    許可されている内容	透過的コンテンツ
    イベント	slotchange
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	Any element that accepts 記述コンテンツ
    許可されている ARIA ロール	なし
    DOM インターフェイス	HTMLSlotElement

    name
    スロットの名前です。
    名前付きスロットは、 <slot> 要素に name 属性が付きます。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        NAME = 'name'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='slot', tags=[], attrs=None, **kwargs)

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



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# slot.py ends here
