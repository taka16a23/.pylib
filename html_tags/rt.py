#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""rt -- rt tag

"""
from .html_tag import HtmlTag


class Rt(HtmlTag):
    """Rt

    Rt is a HtmlTag.
    Responsibility:

    HTML のルビ文字列 (<rt>) 要素は、ルビによる注釈（振り仮名）のルビ文字列の部分を定義し、
    東アジアの組版において発音、翻訳、音写などの情報を提供するために使用します。
    <rt> 要素は常に <ruby> 要素の中で使用されます。

    コンテンツカテゴリ	なし
    許可されている内容	記述コンテンツ
    タグの省略	<rt> 要素の直後に <rt> 要素または <rp> 要素がある場合、または親要素内に他のコンテンツがない場合は終了タグを省略可能。
    許可されている親要素	<ruby> 要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='rt', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# rt.py ends here
