#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""base -- base tag

"""
from .html_tag import HtmlTag


class Base(HtmlTag):
    """Base

    Base is a HtmlTag.
    Responsibility:


    コンテンツカテゴリ	メタデータコンテンツ
    許可されている内容	なし。この要素は空要素。
    タグの省略	終了タグを用いてはならない。
    許可されている親要素	他に <base> 要素を含まない <head>。
    暗黙の ARIA ロール	対応するロールなし
    許可されている ARIA ロール	許可されている role なし
    DOM インターフェイス	HTMLBaseElement

    以下の属性のいずれかが指定されている場合、
    この要素は URL の属性値を持つ他の要素の前におかなければなりません。
    例えば <link> の href 属性などです。

    href
    文書全体を通して相対 URL に使用される基底 URL です。
    絶対 URL と相対 URL が使用できます。
    target
    キーワードまたは作者が定義した名前で既定の閲覧コンテキストを表し、
    <a> または <form> 要素が明示的に target 属性を持たない場合に、
    移動の結果を表示する先として使用されます。
    以下のキーワードは特別な意味を持ちます。
    _self (既定値): 同じ閲覧コンテキストに結果を表示します。
    _blank: 新しい無名の閲覧コンテキストに結果を表示します。
    _parent: 現在のコンテキストの親の閲覧コンテキストに結果を表示します。
    親がない場合、このオプションは _self と同じ振る舞いをします。
    _top: 最上位の閲覧コンテキスト (現在のコンテキストの祖先で、
    それ以上の親をもたない閲覧コンテキスト）に結果を表示します。
    親がない場合、このオプションは _self と同じ振る舞いをします。

    使用上の注意
    複数の <base> 要素
    複数の <base> 要素が使用された場合、最初の href と最初の target の値が使用され、他はすべて無視されます。

    ページ内アンカー
    文書内のフラグメントを指すリンク — 例えば <a href="#some-id"> — は <base> によって解決され、基底 URL にフラグメントを付けて HTTP リクエストを発行します。例を示します。

    <base href="https://example.com"> が指定された場合
    ...そこで <a href="#anchor">Anker</a> というリンクの場合
    ...リンク先は https://example.com/#anchor となります。
    Open Graph
    OpenGraph のメタタグは <base> を認識しないので、次のように常に完全 URL を使用してください。

    <meta property="og:image" content="https://example.com/thumbnail.jpg">
    例
    <base href="https://www.example.com/">
    <base target="_blank">
    <base target="_top" href="https://example.com/">
    """
    class AttributeNames(HtmlTag.AttributeNames):
        HREF = 'href'
        TARGET = 'target'

    class Target(object):
        """Target

        Target is a object.
        Responsibility:

        リンク先の URL を表示する場所、 閲覧コンテキスト (タブ、ウィンドウ、<iframe>)
        の名前で指定します。以下のキーワードは URL の読み込み先について特別な意味を持ちます。

        注: target を使用する際は、window.opener API の悪用を避けるために
        rel="noreferrer noopener" を追加してください。

        注: target="_blank" を使用して他のページにリンクすると、
        新しいページが現在のページと同じプロセスで実行されます。
        新しいページで JavaScript が実行されると、現在のページの性能が影響を受けます。
        これを避けるには、 rel="noreferrer noopener" を使用してください。
        """
        SELF = '_self'
        BLANK = '_blank'
        PARENT = '_parent'
        TOP = '_top'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='base', tags=[], attrs=None, **kwargs)

    def set_href(self, value):
        """Set href.

        set_href(value)

        @Arguments:
        - `value`: href attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.HREF, value)
        return self

    def get_href(self, ):
        """Get href attribute value.

        get_href()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.HREF, None)

    def remove_href(self, ):
        """Remove href attribute value.

        remove_href()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.HREF in self.attrs:
            del self.attrs[self.AttributeNames.HREF]
        return self

    def set_target(self, value):
        """Set target.

        set_target(value)

        @Arguments:
        - `value`: target attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.TARGET, value)
        return self

    def get_target(self, ):
        """Get target attribute value.

        get_target()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.TARGET, None)

    def remove_target(self, ):
        """Remove target attribute.

        remove_target()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.TARGET in self.attrs:
            del self.attrs[self.AttributeNames.TARGET]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# base.py ends here
