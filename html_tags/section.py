#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""section -- section tag

"""
from .html_tag import HtmlTag


class Section(HtmlTag):
    """Section

    Section is a HtmlTag.
    Responsibility:

    HTML の <section> 要素は、 HTML 文書の中で単独のセクション (区間) を表します。
    セクションを表現するより意味的に具体的な要素がない場合に使用します。
    必ずではありませんが、通常はセクションには見出しがあります。

    例えば、ナビゲーションメニューは <nav> 要素で表しますが、検索結果の一覧や地図の表示やコントロールには具体的な要素がないので、 <section> の中に入れることができます。

    メモ: 要素の内容が個別の記事をまとめたものであれば、
    <article> 要素がより適しているかもしれません。

    コンテンツカテゴリ	フローコンテンツ, 区分コンテンツ, 知覚可能コンテンツ
    許可されている内容	フローコンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	フローコンテンツを受け入れるすべての要素。ただし、 <section> 要素は <address> 要素の子孫要素として配置してはならない。
    許可されている ARIA ロール	alert, alertdialog, application, banner, complementary, contentinfo, dialog, document, feed, log, main, marquee, navigation, search, status, tabpanel
    DOM インターフェイス	HTMLElement
    属性
    この要素にはグローバル属性のみがあります。

    使用上の注意
    それぞれの <section> は識別可能であるべき、特に <section>
    の子要素に見出し (<h1>-<h6> 要素) を含めるべきです。
    <section> 要素の内容が単独で配信して意味がある場合は、
    代わりに <article> 要素を使用してください。
    <section> 要素を単なる汎用コンテナーとして使用しないでください。
    このような場合、特にスタイル付けのみの目的で区切るのは <div> の役割です。
    大まかに言えば、 section は文書のアウトラインに論理的に
    現れるものに使用してください。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='section', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# section.py ends here
