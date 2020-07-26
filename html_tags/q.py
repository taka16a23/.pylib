#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""q -- q tag

"""
from .html_tag import HtmlTag


class q(HtmlTag):
    """q

    q is a HtmlTag.
    Responsibility:

    HTML の <q> 要素 は、その内容が行内の引用であることを表します。
    最近の多くのブラウザーでは、文字列を引用符で囲むように実装しています。
    この要素は、段落区切りをまたがない短い引用のためのものです。
    長文の引用には、 <blockquote> 要素を使用してください。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, 知覚可能コンテンツ
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLQuoteElement

    属性
    この要素はグローバル属性を持ちます。

    cite
    この属性の値は、引用した情報の引用元文書やメッセージの URL です。
    この属性は、引用文の文脈や参照先を説明する情報を指すためのものです。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        CITE = 'cite'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='q', tags=[], attrs=None, **kwargs)

    def set_cite(self, value):
        """Set citet attribute.

        set_cite(value)

        @Arguments:
        - `value`: cite value

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.CITE, value)

    def remove_cite(self, ):
        """Remove cite attribute.

        remove_cite()

        @Return: this instance.

        @Error:
        """
        self.attrs.remove_attribute(self.AttributeNames.CITE)
        return self

    def get_cite(self, ):
        """Get cite attribute.

        get_cite()

        @Return: (str) accept value.

        @Error:
        """
        if self.AttributeNames.CITE not in self.attrs:
            return None
        return str(self.attrs[self.AttributeNames.CITE])



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# q.py ends here
