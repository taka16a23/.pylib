#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""rp -- rp tag

"""
from .html_tag import HtmlTag


class Rp(HtmlTag):
    """Rp

    Rp is a HtmlTag.
    Responsibility:

    HTML のルビ代替表示用括弧 (<rp>) 要素は、
    <ruby> 要素によるルビの表示に対応していない
    ブラウザー向けの代替表示用括弧を提供するために使用します。
    <rp> 要素は、注釈の文字列を <rt> 要素を囲む開き括弧と閉じ
    括弧をそれぞれ囲む必要があります。

    コンテンツカテゴリ	なし
    許可されている内容	テキスト
    タグの省略	要素の直後に <rt> または他の <rp> 要素が続くとき、または親要素内にそれ以上のコンテンツがない場合は、終了タグを省略可。
    許可されている親要素	<ruby> 要素。 <rp> 要素は <rt> 要素の直前または直後に配置しなければなりません。
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement

    使用上のメモ
    ルビは日本語のふりがなや台湾語の注音符号など、東アジア言語で発音を示すものです。
    <rp> 要素は <ruby> 要素に対応していない場合に使用されます。
    <rp> 要素の内容物で、ルビの存在を示すために何を表示すべきか（通常は括弧）を指定します。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='rp', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# rp.py ends here
