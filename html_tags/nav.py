#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""nav -- nav tag

"""
from .html_tag import HtmlTag


class Nav(HtmlTag):
    """Nav

    Nav is a HtmlTag.
    Responsibility:

    HTML の <nav> 要素は、現在の文書内の他の部分や他の文書へのナビゲーションリンクを
    提供するためのセクションを表します。
    ナビゲーションセクションの一般的な例としてメニュー、目次、索引などがあります。

    コンテンツカテゴリ	フローコンテンツ、区分コンテンツ、知覚可能コンテンツ
    許可されている内容	フローコンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	フローコンテンツを受け入れるすべての要素
    許可されている ARIA ロール	なし
    DOM インターフェイス	HTMLElement

    使用上の注意
    すべてのリンクを <nav> 要素に入れる必要はありません。
    <nav> はナビゲーションリンクの主要なブロックのみに用います。
    <footer> にもよくリンクのリストが設置されますが、
    <nav> 要素の中に入れる必要はありません。
    <nav> 要素は文書内に複数設定することができます。
    例えば、サイトナビゲーションを一つ、ページ内ナビゲーションを一つなどです。
    このような場合、アクセシビリティを強化するために、
    aria-labelledby を使用することができます。例をご覧ください。
    スクリーンリーダーのような障碍者向けのユーザーエージェントは、
    この要素を使用してナビゲーション用のコンテンツを初期読み上げから
    省略するかを判断するために使用することがあります。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='nav', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# nav.py ends here
