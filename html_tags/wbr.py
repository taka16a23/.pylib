#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""wbr -- wbr tag

"""
from .html_tag import HtmlTag


class Wbr(HtmlTag):
    """Wbr

    Wbr is a HtmlTag.
    Responsibility:

    HTML の <wbr> 要素は、改行可能位置 — テキスト内でブラウザーが任意で
    改行してよい位置を表しますが、この改行規則は必要のない場合は改行を行いません。

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ
    許可されている内容	なし
    タグの省略	この要素は空要素です。開始タグは必須であり、終了タグを記述してはなりません。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement

    メモ
    UTF-8 エンコードを使用するページでは、
    <wbr> 要素は U+200B ZERO-WIDTH SPACE コードポイントのように作用します。
    特に、この要素は Unicode bidi BN コードポイントのように作用するため、
    双方向性には影響を与えません。 <div dir=rtl>123,<wbr>456</div> が
    2 行に分かれないときは 456,123 ではなく 123,456 と表示されます。

    同じ理由で、 <wbr> 要素は改行位置でハイフンを生成しません。
    行末にのみハイフンを表示させるには、代わりにソフトハイフンの文字実体参照
    (&shy;) を使用してください。

    この要素は Internet Explorer 5.5 で最初に実装され、
    HTML5 で公式に定義されました。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='wbr', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# wbr.py ends here
