#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""colgroup -- colgroup tag

"""
from .html_tag import HtmlTag


class ColGroup(HtmlTag):
    """ColGroup

    ColGroup is a HtmlTag.
    Responsibility:

    HTML の <colgroup> 要素は、表内の列のグループを定義します。

    コンテンツカテゴリ	なし
    許可されている内容	span 属性を与えた場合: なし。これは空要素です。
    span 属性を与えない場合: 0 個以上の <col> 要素。
    タグの省略	最初の子要素が <col> 要素であり、かつ終了タグを省略した <colgroup> 要素が前にない場合は、開始タグを省略できます。
    空白またはコメントが後にない場合は、終了タグを省略できます。
    許可されている親要素	<table> 要素。<colgroup> は省略可能な <caption> 要素より後、かつ <thead>, <th>, <tbody>, <tfoot>, <tr> の各要素より前に置かなければなりません。
    許可されている ARIA ロール	なし
    DOM インターフェイス
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='colgroup', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# colgroup.py ends here
