#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""head -- head tag

"""
from .html_tag import HtmlTag


class Head(HtmlTag):
    """Head

    Head is a HtmlTag.
    Responsibility:

    HTML の <head> 要素は、文書に関する機械可読な情報 (メタデータ)、
    たとえば題名、スクリプト、スタイルシートなどを含みます。

    メモ: <head> は機械処理のための情報を保持するためのものであり、
    人間が読むためのものではありません。
    人間が読むための情報、例えば最上位のヘッダーや著者のリストのためのものは、
    <header> 要素を参照してください。

    コンテンツカテゴリ	なし
    許可されている内容
    文書が <iframe> の srcdoc 文書である場合、
    または題名情報がより上位のプロトコル (HTML メールの件名の行など) で
    使用される場合は、0個以上のメタデータコンテンツ。

    他の場合は正確に1つの <title> 要素を含む、1個以上のメタデータコンテンツ。

    タグの省略	<head> 要素内で最初に存在するものが要素である場合、
    開始タグを省略可能。
    <head> 要素に続く最初のものが空白文字やコメントでない場合、終了タグが省略可能。
    許可されている親要素	<html> 要素の最初の子要素として配置可能。
    許可されている ARIA ロール	なし
    DOM インターフェイス
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='head', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# head.py ends here
