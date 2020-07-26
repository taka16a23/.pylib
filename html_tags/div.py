#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""div -- div tag

"""
from .html_tag import HtmlTag


class Div(HtmlTag):
    """Div

    Div is a HtmlTag.
    Responsibility:

    HTML の コンテンツ分割要素 (<div>) は、フローコンテンツの汎用コンテナーです。
    CSS を用いてスタイル付けがされるまでは、コンテンツやレイアウトには影響を与えません。

    <div> 要素は「純粋」なコンテナーとして、本質的には何も表しません。
    その代わり、 class や id を使用してスタイル付けしやすくしたり、
    文書内で異なる言語で書かれた部分を
    (lang 属性を使用して) 示したりするために使用します。

    コンテンツカテゴリ	フローコンテンツ, 知覚可能コンテンツ
    許可されている内容	フローコンテンツ。
    または (WHATWG HTML において) 親要素が <dl> である場合: 1つ以上の <dt> 要素と、それに続く1つ以上の <dd> 要素、さらに任意で <script> 要素や <template> 要素が混在。
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	フローコンテンツ を受け入れるすべての要素。
    または (WHATWG HTML において) <dl> 要素。
    許可されている ARIA ロール	すべて
    DOM インターフェイス

    使用上の注意
    <div> 要素は、他に適切な意味的要素（<article> や <nav> など）が
    ない場合に限り使用してください。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='div', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# div.py ends here
