#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""dl -- dl tag

"""
from .html_tag import HtmlTag


class DL(HtmlTag):
    """DL

    DL is a HtmlTag.
    Responsibility:

    HTML の <dl> 要素は、説明リストを表します。
    この要素は、一連の用語（<dt> 要素を使用して指定）
    と説明（<dd> 要素によって提供）をリスト化したものです。
    一般的な使用例として、用語集の作成やメタデータ（キーと値のペアのリスト）
    の表示が挙げられます。

    コンテンツカテゴリー	フローコンテンツ、<dl> 要素の子要素が 1 つの名前と値のグループの場合は知覚可能コンテンツ
    許可されている内容
    1 個以上の <dt> 要素とそれに続く 1 個以上の <dd> 要素、任意で <script> 要素や <template> 要素が混在するもの。
    または 1 個以上の <div> 要素、任意で <script> 要素や <template> 要素が混在するもの。

    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	フローコンテンツを受け入れるすべての要素
    許可されている ARIA ロール	group, presentation
    DOM インターフェイス

    メモ
    単なる字下げの目的でこの要素 (あるいは <ul> 要素) を使用するのは誤りです。
    そのように機能しますが、これは悪い慣習であり説明リストの意味を不明瞭にします。

    用語の説明のインデントを変更するには、CSS の margin プロパティを使用します。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='dl', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dl.py ends here
