#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""area -- area tag

"""
from .html_tag import HtmlTag


class Area(HtmlTag):
    """Area tag

    Area is a HtmlTag.
    Responsibility:

    HTML の <area> 要素は画像のホットスポット領域を定義し、
    また任意で領域とハイパーテキストリンクの関連づけを行います。
    この要素は <map> 要素内だけで使用します

    コンテンツカテゴリ	フローコンテンツ、記述コンテンツ
    許可されている内容	なし。これは空要素です。
    タグの省略	開始タグは必須。終了タグを記述してはなりません。
    許可されている親要素	記述コンテンツを受け入れるすべての要素。 <area> 要素は祖先が <map> でなければなりませんが、直接の親要素である必要はありません。
    暗黙の ARIA ロール	href 属性がある場合は link、そうでなければ対応するロールなし
    許可されている ARIA ロール	なし
    DOM インターフェイス

    alt
    画像を表示しないブラウザーが代わりに表示するテキスト文字列です。
    テキストの内容は、代替テキストを表示しない場合に画像が提供する選択肢と同じものをユーザーに与えるような表現にすべきです。 HTML4 では、この属性は必須ですが空文字列 ("") でもかまいません。
    HTML5 では、この属性は href 属性を使用する場合にのみ必須です。

    coords
    ホットスポット領域の座標を指定する値のセットです。
    値の数と意味は shape 属性で指定した値に依存します。
      rect すなわち長方形の場合は、 coords の値は2つの x,y の組で、左、上、右、下を表します。
      circle すなわち円の場合は、 x,y,r であり、 x,y は円の中心を指定する組、r は半径の値です。
      poly すなわち多角形の場合は、多角形の各頂点の x,y の組のセットです。
      x1,y1,x2,y2,x3,y3, などのようになります。
    HTML4 での値はピクセル数、またはパーセント記号 (%) を付加した場合はパーセント値です。 HTML5 での値は CSS ピクセル数です。

    download HTML5
    この属性がある場合は、作者はハイパーリンクをリソースのダウンロードに使用すると考えていることを示します。
    download 属性の詳しい説明は <a> をご覧ください。

    href
    この領域のハイパーリンクの宛先です。この値は有効な URL です。HTML4 では、この属性か nohref 属性を与えなければなりません。HTML5 では、この属性を省略できます。省略した場合、 area 要素はハイパーリンクを提供しません。
    hreflang HTML5
    リンク先のリソースの言語を示します。許容される値は BCP47 で定めています。この属性は、href 属性を与える場合にのみ使用してください。

    ping
    ハイパーリンクがフォローされたときに、ブラウザーから (バックグラウンドで) 本文を PING とした POST リクエストが送信される URL を空白で区切ったリストを含めます。ふつうは追跡用に使用します。

    referrerpolicy
    リソースを読み込む際にどのリファラーを使用するかを示す文字列です:
    "no-referrer" は、Referer: ヘッダーを送信しないことを表します。
    "no-referrer-when-downgrade" は、TLS (HTTPS) を使用せずに生成元へナビゲートする場合は Referer: ヘッダーを送信しないことを表します。これは他にポリシーが定められていない場合の、ユーザーエージェントの既定の動作です。
    "origin" は、ページの生成元 (大まかにいえばスキーム、ホスト、ポート) をリファラーとすることを表します。
    "origin-when-cross-origin" は、異なる生成元へのナビゲートではリファラーをスキーム、ホスト、ポートに制限します。同一生成元へのナビゲートでは、リファラーのパスも含めます。
    "unsafe-url" は、リファラーに生成元とパスを含めることを表します (ただし、フラグメント、パスワード、ユーザー名は含めません)。これは生成元やパスの情報が TLS で保護されたリソースからセキュアでない生成元へ漏えいしますので、安全ではありません。

    rel HTML5
    href 属性を含むアンカーで、この属性は、対象オブジェクトとリンクオブジェクトの関係を指定します。属性値は、空白で区切られたリンク種別の値のリストです。値とそれらの意味は、ドキュメントの作者に意味づけを示す何らかの権威により登録されます。値が与えられない場合の既定の関係は、空 (void) です。この属性は、href 属性を与える場合にのみ使用してください。

    shape
    関連づけたホットスポットの形状です。HTML5 および HTML4 の仕様では
    長方形の領域を定義する値 rect、
    円形の領域を定義する値 circle、
    多角形を定義する値 poly、
    定義済みの領域以外すべての領域を示す値 default を定めています。
    多くのブラウザー、特に Internet Explorer 4 以降では circ、polygon、rectangle を
    shape の有効な値としてサポートします。
    これらの値は  (非標準) です。

    target
    この属性は、リンク先のリソースをどこに表示するかを指定します。
    これは、HTML4 ではフレームの名前またはキーワードでした。
    HTML5 では、閲覧コンテキスト の名前またはキーワードです (例えば、タブ、ウィンドウ、インラインフレームなど)。
    以下のキーワードは特別な意味を持ちます:
    _self: レスポンスを現在のものと同じ HTML4 フレーム
           (または HTML5 の閲覧コンテキスト) に読み込みます。
           この値は、属性が指定されていない場合の既定値です。
    _blank: レスポンスを新しい名前の付けられていない
           HTML4 ウィンドウまたは HTML5 の閲覧コンテキストに読み込みます。
    _parent: レスポンスを現在のフレームの HTML4 フレームセットの親要素または
           HTML5 の現在の親閲覧コンテキストに読み込みます。
           親要素がない場合、このオプションは _self と同じ振る舞いをします。
    _top:  HTML4 では、レスポンスをすべて元のウィンドウに読み込み、
           他のフレームをすべてキャンセルします。
           HTML5 では、レスポンスを最上位の閲覧コンテキストに読み込みます
           (現在の閲覧コンテキストの祖先にあたり、それ以上親のない要素です)。
           親要素がない場合、このオプションは _self と同じ振る舞いをします。
    この属性は、href 属性を与える場合にのみ使用してください。
    注: 新しいブラウザー (例えば Firefox 79 以降) では、
    target="_blank" を <area> 要素に設定すると、暗黙に同じ動作をする
    rel を rel="noopener" と設定します。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        ALT = 'alt'
        COORDS = 'coords'
        DOWNLOAD = 'download'
        HREF = 'href'
        PING = 'ping'
        REFERRERPOLICY = 'referrerpolicy'
        REL = 'rel'
        SHAPE = 'shape'
        TARGET = 'target'

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

    class Shape(object):
        """Shape

        Shape is a object.
        Responsibility:
        """
        RECT = 'rect'
        CIRCLE = 'circle'
        POLY = 'poly'

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
        super(HtmlTag, self).__init__(name='area', tags=[], attrs=None, **kwargs)

    def set_alt(self, value):
        """Set alt attribute value.

        set_alt(value)

        @Arguments:
        - `value`: alt attribute value.

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.ALT, value)

    def get_alt(self, ):
        """Get alt attribute value.

        get_autocapitalize()

        @Return:

        @Error:
        """
        if self.AttributeNames.ALT not in self.attrs:
            return None
        return str(self.attrs[self.AttributeNames.ALT])

    def remove_alt(self, ):
        """Remove alt attribute value.

        remove_alt()

        @Return: this instance.

        @Error:
        """
        if self.AttributeNames.ALT in self.attrs:
            del self.attrs[self.AttributeNames.ALT]
        return self

    def set_coords(self, value):
        """Set coords attribute value.

        set_coords(value)

        @Arguments:
        - `value`: coords attribute value.

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.COORDS, value)

    def get_coords(self, ):
        """Get coords attribute value.

        get_coords()

        @Return:

        @Error:
        """
        if self.AttributeNames.COORDS not in self.attrs:
            return None
        return str(self.attrs[self.AttributeNames.COORDS])

    def remove_coords(self, ):
        """Remove coords attribute value.

        remove_coords()

        @Return: this instance.

        @Error:
        """
        if self.AttributeNames.COORDS in self.attrs:
            del self.attrs[self.AttributeNames.COORDS]
        return self

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

    def set_shape(self, value):
        """Set shape attribute value.

        set_shape(value)

        @Arguments:
        - `value`: shape attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.SHAPE, value)
        return self

    def get_shape(self, ):
        """Get shape attribute value.

        get_shape()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.SHAPE, None)

    def remove_shape(self, ):
        """Remove shape attribute.

        remove_shape()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.SHAPE in self.attrs:
            del self.attrs[self.AttributeNames.SHAPE]
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
# area.py ends here
