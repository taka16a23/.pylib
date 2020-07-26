#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""rb -- rb tag

"""
from .html_tag import HtmlTag


class Rb(HtmlTag):
    """Rb

    Rb is a HtmlTag.
    Responsibility:

    HTML ルビベース (<rb>) 要素は、 <ruby> 表記のベースとなるテキストの部分を
    区切るために使用されます。つまり、修飾される文字列です。
    一つの <rb> 要素がベーステキストの不可分な区間を隔てるように囲みます。

    コンテンツカテゴリ	なし
    許可されている内容	<ruby> 要素の子と同様。
    タグの省略	終了タグを省略できるのは、要素に <rt>, <rtc>, <rp> 要素、または他の <rb> 要素が続く場合、または親要素に残りのコンテンツがない場合です。
    許可されている親要素	<ruby> 要素。
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLElement

    使用上のメモ
    ルビ表記は、日本語の振り仮名や台湾語の注音符号のように、
    東アジアの文字の発音を示すためのものです。
    <rb> 要素はルビベース文字の区間を区切るために使用されます。
    <rb> 要素は空要素ではありませんが、
    ソースコード上ではそれぞれの要素の開始タグだけを含めるのが一般的で、
    その方がマークアップが複雑ではなく読みやすくなります。
    ブラウザーは表示する際に完全な要素に補完します。
    修飾をしたいそれぞれのベース区間/<rb> 要素ごとに一つずつ <rt> 要素を置く必要があります。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='rb', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# rb.py ends here
