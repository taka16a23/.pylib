#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""cite -- cite tag

"""
from .html_tag import HtmlTag


class Cite(HtmlTag):
    """Cite

    Cite is a HtmlTag.
    Responsibility:

    HTML の引用元要素 (<cite>) は、引用された創作物の参照を表し、
    作品のタイトルを含む必要があります。
    参照は、引用メタデータに関する利用場面に合わせた慣習に応じて
    省略形が用いられることがあります。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, 知覚可能コンテンツ
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement。Gecko 1.9.2 (Firefox 4) 以前では、この要素には HTMLSpanElement インターフェイスが実装されています。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='cite', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# cite.py ends here
