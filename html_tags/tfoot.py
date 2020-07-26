#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""tfoot -- tfoot tag

"""
from .html_tag import HtmlTag


class Tfoot(HtmlTag):
    """Tfoot

    Tfoot is a HtmlTag.
    Responsibility:

    HTML の <tfoot> 要素は、表のの列を総括する行のセットを定義します。

    コンテンツカテゴリ	なし
    許可されている内容	0 個以上の <tr> 要素
    タグの省略	開始タグは必須。親 <table> 要素内に以降のコンテンツがない場合は終了タグを省略可能。
    許可されている親要素	<table> 要素。<tfoot> は <caption>, <colgroup>, <thead>, <tbody>, <tr> の各要素の後方に配置しなければなりません。これは HTML5 の要件です。
    HTML 4 <tfoot> 要素は <tbody> 要素および <tr> 要素の後方に配置してはなりません。これは HTML5 の規範的要件とまさに矛盾することに注意してください。
    暗黙の ARIA ロール	rowgroup
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLTableSectionElement
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='tfoot', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# tfoot.py ends here
