#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""bdo -- bdo tag

"""
from .html_tag import HtmlTag


class Bdo(HtmlTag):
    """Bdo

    Bdo is a HtmlTag.
    Responsibility:

    HTML の双方向文字列上書き要素 (<bdo>) は、現在の文字列の方向を上書きし、
    中の文字列が異なる方向に描画されるようにします。

    文字列の文字は指定された方向の開始位置から描画されます。
    それぞれの文字の向きには影響を与えません (ですから、例えば、文字は裏返しにはなりません)。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, 知覚可能コンテンツ
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    暗黙の ARIA ロール	対応するロールなし
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement。Gecko 1.9.2 (Firefox 4)
    以前では、Firefox はこの要素に対し HTMLSpanElement インターフェイスを実装しています。

    dir
    この要素の書字方向。以下の値を指定可能です。
    ltr: テキストを左から右へ (Left to Right) 向かわせることを意味する指定。
    rtl: テキストを右から左へ (Right to Left) 向かわせることを意味する指定。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        DIR = 'dir'

    class Dir(object):
        """Dir

        Dir is a object.
        Responsibility:
        """
        LTR = 'ltr'
        RTL = 'rtl'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='bdo', tags=[], attrs=None, **kwargs)

    def set_dir(self, value):
        """Set dir.

        set_dir(value)

        @Arguments:
        - `value`: dir attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.DIR, value)
        return self

    def get_dir(self, ):
        """Get dir attribute value.

        get_dir()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.DIR, None)

    def remove_dir(self, ):
        """Remove dir attribute value.

        remove_dir()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.DIR in self.attrs:
            del self.attrs[self.AttributeNames.DIR]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# bdo.py ends here
