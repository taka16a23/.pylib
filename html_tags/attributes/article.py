#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""article -- article tag

"""
from .html_tag import HtmlTag


class Article(HtmlTag):
    """Article

    Article is a HtmlTag.
    Responsibility:

    HTML の <article> 要素は文書、ページ、アプリケーション、
    サイトなどの中で自己完結しており、
    (集合したものの中で) 個別に配信や再利用を行うことを意図した構成物を表します。
    例えば、フォーラムの投稿、雑誌や新聞の記事、ブログの記事などが含まれます。

    ある文書に複数の記事を含めることができます。
    たとえば、読者がスクロールするたびに各記事のテキストを次々と表示するブログでは、
    各記事は <article> 要素に含まれ、おそらくその中に1つ以上の <section> があります。

    コンテンツカテゴリ	フローコンテンツ, 区分コンテンツ, 知覚可能コンテンツ
    許可されている内容	フローコンテンツ
    タグの省略          不可。開始と終了タグの両方が必要。
    許可されている親要素	フローコンテンツを受け入れるすべての要素。なお、 <article> 要素を <address> 要素の子孫にしてはいけません。
    許可されている ARIA ロール	application, document, feed, main, presentation, region
    DOM インターフェイス

    使用上の注意
    それぞれの <article> は、子要素として見出し (<h1>-<h6> 要素)
    を含むなどの方法で識別できるようにするべきです。
    <article> 要素を入れ子にした場合、内側の要素は外側の要素に関する記事を表します。
    例えばブログ投稿へのコメントは、ブログ投稿を表す
    <article> 内へ入れ子にした <article> 要素にできます。
    <article> 要素の著者情報は <address> 要素で提供できますが、
    入れ子にされた <article> 要素には適用されません。
    <article> 要素の発行日時は、 <time> 要素の datetime 属性で示すことができます。
    なお、 <time> 要素の pubdate 属性は W3C HTML5 標準から外されました。
    """
    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='article', tags=[], attrs=None, **kwargs)



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# article.py ends here
