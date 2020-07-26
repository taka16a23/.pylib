#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""span -- span tag

"""
from .html_tag import HtmlTag


class Span(HtmlTag):
    """Span

    Span is a HtmlTag.
    Responsibility:

    HTML の <span> 要素は、記述コンテンツの汎用的な行内コンテナーであり、
    何かを表すものではありません。
    スタイル付けのため (class または id 属性を使用して)、
    または lang のような属性値を共有したりするために
    要素をグループ化する用途で使用することができます。
    他に適切な意味的要素がない時にのみ使用してください。
    <span> は <div> 要素ととても似ていますが、
    <div> がブロックレベル要素であるのに対し、 <span> はインライン要素です。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素、またはフローコンテンツを受け入れるすべての要素。
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLSpanElement (HTML5 より前は HTMLElemen
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='span', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# span.py ends here
