#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""p -- p tag

"""
from .html_tag import HtmlTag


class p(HtmlTag):
    """p

    p is a HtmlTag.
    Responsibility:

    HTML の <p> 要素は、テキストの段落を表します。
    視覚メディアにおいて、段落はふつう隣接するブロックと上下の空白や
    最初の行の字下げによって隔てられたテキストのブロックとして表現されますが、
    HTML の段落は画像やフォーム欄などの関連するコンテンツを構造的にまとめることができます。

    段落はブロックレベル要素であり、特徴的なのは </p> で閉じる前に
    他のブロックレベル要素が見つかった場合は自動的に閉じることです。
    下記の「タグの省略」をご覧ください。

    コンテンツカテゴリ	フローコンテンツ、知覚可能コンテンツ
    許可されている内容	記述コンテンツ
    タグの省略	開始タグは必須。後続する要素が <address>, <article>, <aside>, <blockquote>, <div>, <dl>, <fieldset>, <footer>, <form>, <h1>, <h2>, <h3>, <h4>, <h5>, <h6>, <header>, <hr>, <menu>, <nav>, <ol>, <pre>, <section>, <table>, <ul> または別の <p> 要素のいずれかである、または親要素内で他のコンテンツがなく親要素が <a> 要素ではない場合は終了タグを省略することが可能。
    許可されている親要素	フローコンテンツを受け入れるすべての要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='p', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# p.py ends here
