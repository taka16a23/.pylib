#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""col -- col tag

"""
from .html_tag import HtmlTag


class Col(HtmlTag):
    """Col

    Col is a HtmlTag.
    Responsibility:

    HTML の <col> 要素は、表内の列を定義して、
    すべての一般セルに共通の意味を定義するために使用します。
    この要素は通常、 <colgroup> 要素内にみられます。

    この要素では CSS を使用して列にスタイルを設定できますが、
    列に対して効果があるプロパティは限定されています
    (CSS 2.1 仕様書 をご覧ください)。

    コンテンツカテゴリ	なし
    許可されている内容	なし。これは空要素です。
    タグの省略	開始タグは必須ですが、空要素ですので終了タグを置いてはいけません。
    許可されている親要素	<colgroup> のみ。ただし開始タグが必須ではないため暗黙的に定義されることがあります。 <colgroup> 要素は span 属性を持っていてはいけません。
    許可されている ARIA ロール	なし
    DOM インターフェイス
    """

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='col', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# col.py ends here
