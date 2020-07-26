#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""br -- br tag

"""
from .html_tag import HtmlTag


class br(HtmlTag):
    """br

    br is a HtmlTag.
    Responsibility:

    HTML の <br> 要素 は、文中に改行（キャリッジリターン）を生成します。
    詩や住所など、行の分割が重要な場合に有用です。

    上記の例に見られるように、 <br> 要素はテキストを改行したい場所にそれぞれ含められます。
    <br> の後のテキストは、テキストブロックの次の行の先頭から再開されます。

    メモ: 段落の間を開けるために <br> を使わないでください。
    それぞれを <p> 要素で囲み、 CSS の margin プロパティで間隔を制御してください。

    上記の例に見られるように、 <br> 要素はテキストを改行したい場所にそれぞれ含められます。
    <br> の後のテキストは、テキストブロックの次の行の先頭から再開されます。

    メモ: 段落の間を開けるために <br> を使わないでください。
    それぞれを <p> 要素で囲み、 CSS の margin プロパティで間隔を制御してください。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='br', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# br.py ends here
