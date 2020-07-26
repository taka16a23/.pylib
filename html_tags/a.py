#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""a -- html a tag

"""
from .html_tag import HtmlTag


class a(HtmlTag):
    """a tag.

    a is a HtmlTag.
    Responsibility:

    HTML の <a> 要素 (アンカー要素) は、 href 属性を用いて、
    別のウェブページ、ファイル、メールアドレス、同一ページ内の場所、
    または他の URL へのハイパーリンクを作成します。
    <a> の内容は、リンク先を示すものであるべきです。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        """AttributeNames

        AttributeNames is a HtmlTag.AttributeNames.
        Responsibility:

        リンクされた URL に移動するのではなく、保存するようユーザーに促します。
        値があってもなくても利用できます。
        値を定義すると、ファイル名として提案します。
        / および \ はアンダースコアに変換されます。
        ファイルシステムがファイル名に禁止している文字は他にもあるかもしれませんので、
        ブラウザーは必要に応じてファイル名を調整します。
        値がない場合は、ブラウザーは様々なソースから生成されたファイル名/拡張子を提案します。
        HTTP の Content-Disposition ヘッダー
        URL のパスの最後の部分
        メディア種別 (Content-Type ヘッダー、
        data: URL の先頭、
        blob: URL の Blob.type から)

        ハイパーリンクが指す先の URL です。
        リンクは HTTP ベースの URL に限定されません。
        ブラウザーが対応するあらゆるプロトコルを使用することができます。

        ページの節を示すフラグメント URL
        メディアファイルの一部を示すメディアフラグメント
        電話番号を示す tel: URL
        メールアドレスを示す mailto: URL
        ウェブブラウザーがその他の URL スキームに対応していない可能性がある場合、
        ウェブサイトは registerProtocolHandler() を使用することができます。

        リンク先の URL における自然言語のヒントです。
        組み込まれている機能はありません。
        許容される値は、 lang グローバル属性と同じです。

        空白で区切られた URL のリストです。
        リンクをたどるときに、ブラウザーは POST
        リクエストを指定された URL に、 PING を本文として送信します。
        通常、トラッキングに使用されます。

        リンクをたどるときにどれだけのリファラーを送信するかです。
        有効な値とその効果については Referrer-Policy を参照してください。

        リンク先の URL との関係を示す、空白で区切られたリンク種別のリストです。

        リンク先の URL を表示する場所、 閲覧コンテキスト (タブ、ウィンドウ、<iframe>)
        の名前で指定します。以下のキーワードは URL の読み込み先について特別な意味を持ちます。
        _self: 現在の閲覧コンテキストです。 (既定値)
        _blank: ふつうは新しいタブですが、新しいウィンドウを使用するようにブラウザーを設定できます。
        _parent: 現在の親の閲覧コンテキストです。親がない場合は、 _self と同じ振る舞いをします。
        _top: 最上位の閲覧コンテキスト (現在のコンテキストの祖先である "最上位" のコンテキスト) です。親の閲覧コンテキストがない場合は、 _self と同じ動作をします。

        注: target を使用する際は、window.opener API の悪用を避けるために
        rel="noreferrer" を追加してください。

        注: target="_blank" を使用して他のページにリンクすると、
        新しいページが現在のページと同じプロセスで実行されます。
        新しいページで JavaScript が実行されると、現在のページの性能が影響を受けます。
        これを避けるには、 rel="noreferrer noopener" を使用してください。

        リンク先 URL の MIME タイプの形式を表すヒントです。組み込まれている機能はありません。
        """
        DOWNLOAD = 'download'
        HREF = 'href'
        HREFLANG = 'hreflang'
        PING = 'ping'
        REFERRERPOLICY = 'referrerpolicy'
        REL = 'rel'
        TARGET = 'target'
        TYPE = 'type'

    class RefererPolicy(object):
        """RefererPolicy

        RefererPolicy is a object.
        Responsibility:
        """
        NO_REFERRER = 'no-referrer'
        """いずれの場合もリファラーを送信しない。"""
        NO_REFERRER_WHEN_DOWNGRADE = 'no-referrer-when-downgrade'
        """httpsからhttpに移動する時はリファラーを送信しない。ブラウザのデフォルトの挙動。"""
        SAME_ORIGIN = 'same-origin'
        """同一オリジン間の移動時にだけ、リファラーを送信する。"""
        ORIGIN = 'origin'
        """スキーム、ホスト、ポートのみをリファラーに含める。パスは含めない。"""
        STRICT_ORIGIN = 'strict-origin'
        """httpsからhttpに移動する時はリファラーを送信しない。それ以外では、originと同じ。"""
        ORIGIN_WHEN_CROSS_ORIGIN = 'origin-when-cross-origin'
        """同一オリジン間の移動時には、完全なリファラーを送信する。それ以外では、originと同じ。httpからhttpsへのアクセスはドメインが同じでもクロスオリジンとみなされる。"""
        STRICT_ORIGIN_WHEN_CROSS_ORIGIN = 'strict-origin-when-cross-origin'
        """httpsからhttpに移動する時はリファラーを送信しない。同一オリジン間の移動時には、完全なリファラーを送信する。それ以外では、originと同じ。httpからhttpsへのアクセスはドメインが同じでもクロスオリジンとみなされる。"""
        UNSAFE_URL = 'unsafe-url'
        """いずれの場合も完全なリファラーを送信する。"""

    class Rel(object):
        """Rel

        Rel is a object.
        Responsibility:
        """

        ALTERNATE = 'alternate'
        """Provides a link to an alternate representation of the document
        (i.e. print page, translated or mirror)"""

        AUTHOR = 'AUTHOR'
        """Provides a link to the author of the document"""

        BOOKMARK = 'bookmark'
        """Permanent URL used for bookmarking"""

        EXTERNAL = 'external'
        """Indicates that the referenced document is not part of the same site
        as the current document"""

        HELP = 'help'
        """Provides a link to a help document"""

        LICENSE = 'license'
        """Provides a link to licensing information for the document"""

        NEXT = 'next'
        """Provides a link to the next document in the series"""

        NOFOLLOW = 'nofollow'
        """Links to an unendorsed document, like a paid link.
        ("nofollow" is used by Google, to specify that the Google search spider should not follow that link)
        """

        NOREFERRER = 'noreferrer'
        """Requires that the browser should not send an HTTP
        referer header if the user follows the hyperlink"""

        NOOPENER = 'noopener'
        """Requires that any browsing context created by following the hyperlink
        must not have an opener browsing context"""

        PREV = 'prev'
        """The previous document in a selection"""

        SEARCH = 'search'
        """Links to a search tool for the document"""

        TAG = 'tag'
        """A tag (keyword) for the current document"""

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
        """現在の閲覧コンテキストです。 (既定値)"""

        BLANK = '_blank'
        """ふつうは新しいタブですが、新しいウィンドウを使用するようにブラウザーを設定できます。"""

        PARENT = '_parent'
        """現在の親の閲覧コンテキストです。親がない場合は、 _self と同じ振る舞いをします。"""

        TOP = '_top'
        """最上位の閲覧コンテキスト (現在のコンテキストの祖先である "最上位" のコンテキスト) です。親の閲覧コンテキストがない場合は、 _self と同じ動作をします。"""

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='a', tags=[], attrs=None, **kwargs)

    def set_download(self, value):
        """Set download.

        set_download(value)

        @Arguments:
        - `value`: download attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.DOWNLOAD, value)
        return self

    def get_download(self, ):
        """Get Download attribute value.

        get_download()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.DOWNLOAD, None)

    def remove_download(self, ):
        """Remove download attribute.

        remove_download()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.DOWNLOAD in self.attrs:
            del self.attrs[self.AttributeNames.DOWNLOAD]
        return self

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

    def set_hreflang(self, value):
        """Set hreflang.

        set_hreflang(value)

        @Arguments:
        - `value`: hreflang attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.HREFLANG, value)
        return self

    def get_hreflang(self, ):
        """Get hreflang attribute value.

        get_hreflang()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.HREFLANG, None)

    def remove_hreflang(self, ):
        """Remove hreflang attribute value.

        remove_hreflang()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.HREFLANG in self.attrs:
            del self.attrs[self.AttributeNames.HREFLANG]
        return self

    def get_ping(self, ):
        """Get ping attribute values.

        get_ping()

        @Return: (AttrValue) ping attribute value.

        @Error:
        """
        return self.attrs.get(self.AttributeNames.PING, None)

    def append_ping(self, value):
        """Append ping values.

        append_ping(value)

        @Arguments:
        - `value`: ping attribute value

        @Return: this instance

        @Error:
        """
        self.attrs.append_value(self.AttributeNames.PING, value)
        return self

    def remove_ping(self, value):
        """Remove ping value.

        remove_ping(value)

        @Arguments:
        - `value`: ping attribute value

        @Return: this instance

        @Error:
        """
        self.attrs.remove_value(self.AttributeNames.PING, value)
        return self

    def clear_ping(self, ):
        """Clear ping.

        clear_ping()

        @Return: this instance

        @Error:
        """
        self.clear_attribute_value(self.AttributeNames.PING)
        return self

    def delete_ping(self, ):
        """Delete ping.

        delete_ping()

        @Return: this instance

        @Error:
        """
        self.set_attribute_none(self.AttributeNames.PING)
        return self

    def set_refererpolicy(self, value):
        """Set refererpolicy.

        set_refererpolicy(value)

        @Arguments:
        - `value`: refererpolicy attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.REFERRERPOLICY, value)
        return self

    def get_refererpolicy(self, ):
        """Get refererpolicy attribute value.

        get_refererpolicy()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.REFERRERPOLICY, None)

    def remove_refererpolicy(self, ):
        """Remove refererpolicy attribute.

        remove_refererpolicy()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.REFERRERPOLICY in self.attrs:
            del self.attrs[self.AttributeNames.REFERRERPOLICY]
        return self

    def get_rel(self, ):
        """Get rel attribute values.

        get_rel()

        @Return: (AttrValue) rel attribute value.

        @Error:
        """
        return self.attrs.get(self.AttributeNames.REL, None)

    def append_rel(self, value):
        """Append rel values.

        append_rel(value)

        @Arguments:
        - `value`: rel attribute value

        @Return: this instance

        @Error:
        """
        self.attrs.append_value(self.AttributeNames.REL, value)
        return self

    def remove_rel(self, value):
        """Remove rel value.

        remove_rel(value)

        @Arguments:
        - `value`: rel attribute value

        @Return: this instance

        @Error:
        """
        self.attrs.remove_value(self.AttributeNames.REL, value)
        return self

    def clear_rel(self, ):
        """Clear rel.

        clear_rel()

        @Return: this instance

        @Error:
        """
        self.clear_attribute_value(self.AttributeNames.REL)
        return self

    def delete_rel(self, ):
        """Delete rel.

        delete_rel()

        @Return: this instance

        @Error:
        """
        self.set_attribute_none(self.AttributeNames.REL)
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

    def set_type(self, value):
        """Set type.

        set_type(value)

        @Arguments:
        - `value`: type attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.TYPE, value)
        return self

    def get_type(self, ):
        """Get type attribute value.

        get_type()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.TYPE, None)

    def remove_type(self, ):
        """Remove type attribute.

        remove_type()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.TYPE in self.attrs:
            del self.attrs[self.AttributeNames.TYPE]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# a.py ends here
