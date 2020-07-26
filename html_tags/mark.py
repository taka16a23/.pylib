#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""mark -- mark tag

"""
from .html_tag import HtmlTag


class Mark(HtmlTag):
    """Mark

    Mark is a HtmlTag.
    Responsibility:

    HTML の文字列マーク要素 (<mark>) は、周囲の文脈の中でマークを付けた
    部分の関連性や重要性のために、参照や記述の目的で目立たせたり強調したりする
    文字列を表します。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, 知覚可能コンテンツ
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement

    使用上のメモ
    <mark> のよくある利用方法は以下のようなものです。

    引用 (<q>) またはブロック引用 (<blockquote>) の中で使用される場合は、
    ふつう原文で特にマークされていなくても特別な関心事となる文字列、
    または原文の筆者が特に重要だと考えていなかったことでも、
    特別に精査が必要な部分を示します。
    本の中で興味のある部分が見つかったときに、
    蛍光ペンを使ってマークするようなものだと考えてください。
    それ以外に、 <mark> はユーザーの現在の行動に関する文書中の部分を示します。
    これは例えば、検索操作で検索された語を示す場合などに使用されます。
    <mark> を (ソースコードなどの) 構文の強調には使用しないで下さい。
    <span> 要素とそれに適用する適切な CSS を使用してください。
    <mark> 要素と <strong> 要素を混同しないよう注意してください。
    <mark> は関連性のあるコンテンツを表すために使用されますが、
    <strong> は重要性のある文字列の区間を表します。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='mark', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# mark.py ends here
