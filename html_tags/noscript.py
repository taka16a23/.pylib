#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""noscript -- noscript tag

"""
from .html_tag import HtmlTag


class NoScript(HtmlTag):
    """NoScript

    NoScript is a HtmlTag.
    Responsibility:

    HTML の <noscript> 要素は、このページ上のスクリプトの種類に対応していない場合や、
    スクリプトの実行がブラウザーで無効にされている場合に表示する HTML の部分を定義します。

    コンテンツカテゴリー	メタデータコンテンツ、フローコンテンツ、記述コンテンツ
    許可されている内容	スクリプトの実行が無効かつ <head> 要素の子孫である場合: 任意の順序で、0個以上の <link> 要素、0個以上の<style> 要素、0個以上の <meta> 要素。
    スクリプトの実行が無効かつ <head> 要素の子孫ではない場合: 任意の透過的コンテンツ、ただし <noscript> 要素を入れ子にしてはならない。
    上記以外の場合: フローコンテンツ、記述コンテンツ。
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	祖先要素に <noscript> が存在しない場合に、記述コンテンツ を受け入れるすべての要素。または、祖先要素に <noscript> が存在しない場合に、<head> 要素 (HTML 文書に限る)。
    許可されている ARIA ロール	なし
    DOM インターフェイス	HTMLElement
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='noscript', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# noscript.py ends here
