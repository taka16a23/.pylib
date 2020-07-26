#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""blockquote -- blockquote tag

"""
from .html_tag import HtmlTag


class BlockQuote(HtmlTag):
    """BlockQuote

    BlockQuote is a HtmlTag.
    Responsibility:

    HTML の <blockquote> 要素 (HTML ブロック引用要素) は、
    内包する要素の文字列が引用文であることを示します。
    通常、字下げを伴ってレンダリングされます
    (整形方法については注意の項を参照してください)。
    cite 属性により引用元の文書の URL を、 <cite>
    要素により引用元の文書のタイトルなどを明示可能です。

    コンテンツカテゴリ	フローコンテンツ, 区分化ルート, 知覚可能コンテンツ
    許可されている内容	フローコンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	フローコンテンツを受け入れるすべての要素
    暗黙の ARIA ロール	対応するロールなし
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLQuoteElement

    使用上の注意
    引用された文字列に適用される字下げを変更するには、
    CSS の margin-left や margin-right プロパティ、または一括指定の margin
    プロパティを使用してください。

    独立したブロックというより行内の短い引用を行うには、
    <q> (Quotation) 要素を使用してください。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        """AttributeNames

        AttributeNames is a HtmlTag.AttributeNames.
        Responsibility:

        cite
        引用元の文書の URL、または引用元の情報に関するメッセージを示します。この属性は、引用文の背景や出典についての説明を指し示そうとするものです。
        """
        CITE = 'cite'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='blockquote', tags=[], attrs=None, **kwargs)

    def set_cite(self, value):
        """Set cite.

        set_cite(value)

        @Arguments:
        - `value`: cite attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.CITE, value)
        return self

    def get_cite(self, ):
        """Get cite attribute value.

        get_cite()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.CITE, None)

    def remove_cite(self, ):
        """Remove cite attribute value.

        remove_cite()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.CITE in self.attrs:
            del self.attrs[self.AttributeNames.CITE]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# blockquote.py ends here
