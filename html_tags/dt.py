#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""dt -- dt tag

"""
from .html_tag import HtmlTag


class DT(HtmlTag):
    """DT

    DT is a HtmlTag.
    Responsibility:

    HTML の <dt> 要素は、説明又は定義リストの中で用語を表す部分であり、
    <dl> の子要素としてのみ用いることができます。
    普通は <dd> 要素が続きます。しかし、複数の <dt> 要素が続くと、
    複数の用語がすぐ後に続く <dd> 要素で定義されていることを表します。

    後に続く <dd> (詳細説明) 要素は、 <dt> を用いて指定した用語について、
    定義やその他の関連する文字列を表します。

    コンテンツカテゴリ	なし
    許可されている内容	フローコンテンツ。ただし <header>、<footer>、区分コンテンツ、見出しコンテンツを除く。
    タグの省略	開始タグは必須。他の <dt> または <dd> 要素が後続する場合、もしくは親要素である <dl> 要素内に後続する要素がない場合に、終了タグが省略可能となる。
    許可されている親要素	<dl> または (WHATWG HTML において) <dl> の中にある <div> の内部における、 <dt> または <dd> の前。
    許可されている ARIA ロール	なし
    DOM インターフェイス	HTMLElement。 Gecko 1.9.2 (Firefox 4) 以前では、 Firefox はこの要素に対し HTMLSpanElement インターフェイスを実装していました。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='dt', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dt.py ends here
