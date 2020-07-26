#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""map -- map tag

"""
from .html_tag import HtmlTag


class Map(HtmlTag):
    """Map

    Map is a HtmlTag.
    Responsibility:

    HTML の <map> 要素はイメージマップ (クリック可能なリンク領域)
    を定義するために <area> 要素とともに使用します。

    コンテンツカテゴリ	フローコンテンツ、記述コンテンツ、知覚可能コンテンツ
    許可されている内容	透過的要素
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	なし
    DOM インターフェイス	HTMLMapElement

    属性
    この要素はグローバル属性を持ちます。

    name
    name 属性は、マップを参照可能にするための名前を与えます。
    この属性は指定しなければならず、値は空文字列ではなく空白文字を
    含まないものにしなければなりません。name 属性の値は、同一文書内の別の
    map 要素の name 属性の値と compatibility-caseless 方式で一致してはいけません。
    id 属性も指定した場合は、両方の属性の値を同一にしなければなりません。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='map', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# map.py ends here
