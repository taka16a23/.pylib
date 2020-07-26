#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""dd -- dd tag

"""
from .html_tag import HtmlTag


class DD(HtmlTag):
    """DD

    DD is a HtmlTag.
    Responsibility:

    HTML の <dd> 要素は、定義リスト要素 (<dl>) 内で、
    先行する用語 (<dt>) の説明、定義、値などを示します。

    コンテンツカテゴリ	なし
    許可されている内容	フローコンテンツ
    タグの省略	開始タグは必須。 <dd> 要素の直後に他の <dd> 要素または <dt> 要素がある場合、もしくは親要素内で後続する内容物がない場合は、終了タグが省略可能となる。
    許可されている親要素	<dl> 要素または (WHATWG HTML において) <dl> 要素内にある <div> 要素
    前の兄弟要素	<dt> 要素または別の <dd> 要素
    許可されている ARIA ロール	なし
    DOM インターフェイス
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='dd', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# dd.py ends here
