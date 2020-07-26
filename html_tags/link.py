#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""link -- link tag

"""
from .html_tag import HtmlTag


class Link(HtmlTag):
    """Link

    Link is a HtmlTag.
    Responsibility:

    HTML 外部リソースへのリンク要素 (<link>) は、
    現在の文書と外部のリソースとの関係を指定します。
    この要素はスタイルシートへのリンクに最もよく使用されますが、
    サイトのアイコン ("favicon" スタイルのアイコンと、
    モバイル端末のホーム画面やアプリのアイコンの両方) の確立や、
    その他のことにも使用されます。

    外部スタイルシートへリンクするには、<head> の中に次のような <link>
    要素を入れてください。

    <link href="main.css" rel="stylesheet">
    この単純な例では、href 属性内にスタイルシートへのパスを提供し、
    rel 属性の値を stylesheet にしています。
    rel は "relationship" を意味し、おそらく <link> 要素の重要な機能の一つです。
    — 値はこれを含んでいる文書にどのように関係するかを示します。
    リンク種別で見られるように、様々な種類の関係があります。

    他にも見かけるであろう他の一般的な種別はたくさんあります。
    例えば、サイトのファビコンへのリンクがあります。

    <link rel="icon" href="favicon.ico">
    他にもアイコンの rel 値はいくつもあり、
    以下のように主に様々なモバイルプラットフォーム上で特殊な
    アイコンの種別を示すために使用されます。

    <link rel="apple-touch-icon-precomposed" sizes="114x114"
      href="apple-icon-114.png" type="image/png">
    sizes 属性はアイコンの寸法を表し、type はリンクされようとしているリソースの
    MIME タイプが入ります。
    これらはブラウザーが利用できる最も適切なアイコンを選択するための
    有益なヒントを提供します。

    media 属性でメディア種別やクエリを指定することもできます。
    このリソースはメディアの条件が真になった場合のみ読み込まれます。

    <link href="print.css" rel="stylesheet" media="print">
    <link href="mobile.css" rel="stylesheet" media="screen and (max-width: 600px)">
    <link> 要素には、興味深いパフォーマンスやセキュリティの機能も
    いくつか追加されています。以下の例を見てみましょう。

    <link rel="preload" href="myFont.woff2" as="font"
      type="font/woff2" crossorigin="anonymous">
    rel が preload の値であることは、ブラウザーがこのリソースを
    先読みすることを指示しており (詳しくは rel="preload" による
    コンテンツの先読みを参照)、as 属性がコンテンツが読み込まれるされる
    特定のクラスを示します。
    crossorigin 属性はリソースが CORS リクエストによって読み込まれるかどうかを
    示します。

    その他の有用なメモです。

    <link> 要素はリンク種別が body-ok であるかどうかによって、
    <head> 要素または <body> 要素のどちらかに置くことができます。
    例えば stylesheet リンク種別は body-ok であり、<link rel="stylesheet"> を
    body 要素内に置くことができます。
    しかし、これは従うべき良い方法ではありません。
    <link> 要素は <head> に入れて本文から離した方が分かりやすくなります。
    サイトにファビコンを設定するために <link> を使用する場合で、
    サイトがセキュリティの強化のためにコンテンツセキュリティポリシー (CSP)
    を使用している場合、ファビコンにポリシーが適用されます。
    ファビコンが読み込まれないという問題が発生したら、
    Content-Security-Policy ヘッダーの img-src
    ディレクティブがアクセスを禁止していないかどうか確認してください。
    HTML および XHTML の仕様では <link>
    要素向けのイベントハンドラーを定義していますが、
    それらがどのように使用されるかは不明確です。
    XHTML 1.0 では <link> のような空要素では、
    <link /> のように末尾のスラッシュが必要です。
    WebTV は rel に next の値を使用して、
    一連の文書の次のページを先読みすることに対応しています。

    属性
    この要素にはグローバル属性があります。

    as
    この属性は、rel="preload" または rel="prefetch" を <link>
    要素に設定した場合に限り使用されます。
    これは <link> によって読み込まれるコンテンツのタイプを指定する属性であり、
    リクエストのマッチング、正しいコンテンツセキュリティポリシーの適用、
    正しい Accept リクエストヘッダーの設定のために必要です。
    更には、rel="preload" ではリクエストの優先度づけの信号としても使います。
    下記の表はこの属性と適用される要素やリソースの妥当な値の一覧です。

    値

    適用先
    audio	<audio> 要素
    document	<iframe> と <frame> 要素
    embed	<embed> 要素
    fetch
    fetch, XHR

    This value also requires <link> to contain the crossorigin attribute.

    font	CSS @font-face
    image	<img> と <picture> 要素に srcset か imageset 属性を付けたもの、SVG <image> 要素、CSS *-image ルール
    object	<object> 要素
    script	<script> 要素、Worker importScripts
    style	<link rel=stylesheet> 要素、CSS @import
    track	<track> 要素
    video	<video> 要素
    worker	Worker, SharedWorker

    crossorigin
    この列挙型の属性は、関連リソースを取得する際に CORS を
    使用しなければならないかを示します。
    CORS が有効な画像は、汚染されることなく <canvas> 要素で再利用できます。
    次の値が使用できます。

    anonymous
    オリジン間リクエスト (つまり、HTTP の Origin ヘッダーを持つリクエスト) が
    実行されます。ただし、信用情報は送信されません
    (Cookie、X.509 証明書、HTTP ベーシック認証は利用されません)。
    サーバーが元のサイトに信用情報を付与しない
    (HTTP の Access-Control-Allow-Origin ヘッダーの設定がない) 場合、
    リソースが汚染され、その使用も制限されます。

    use-credentials
    オリジン間リクエスト (つまり、HTTP の Origin ヘッダーを持つリクエスト) が
    実行され、信用情報が送信されます
    (Cookie、証明書、HTTP ベーシック認証が利用されます)。
    サーバーが元のサイトに信用情報を付与しない場合
    (HTTP の Access-Control-Allow-Credentials ヘッダーに関わらず)、
    画像が汚染され、その使用も制限されます。
    この属性が存在しない場合、リソースは CORS リクエストなしで
    (Origin HTTP ヘッダーを送信せずに) 取得され、汚染されない使用が妨げられます。
    これが無効な場合、列挙型のキーワード anonymous が指定されたものとして扱われます。
    それ以上の情報は CORS 設定属性 を参照してください。

    disabled
    rel="stylesheet" の場合のみ、disabled は論理属性であり、
    指定されたスタイルシートを読み込んで文書に適用するかどうかを示します。
    disabled が HTML に読み込み時点で指定されていた場合、
    そのスタイルシートはページ読み込み処理の間に読み込まれません。
    代わりに、そのスタイルシートは disabled 属性が false に変更されたか
    削除された場合にオンデマンドで読み込まれます。

    いったんスタイルシートが読み込まれると、disabled プロパティの値を変更しても、
    StyleSheet.disabled プロパティの値と関係がなくなります。
    このプロパティの値を変更すると、単に文書に適用されるスタイルシートを
    有効化したり無効化したりするだけになります。

    これは StyleSheet の disabled プロパティとは異なります。
    これを true にすると文書の document.styleSheets の一覧から
    スタイルシートが削除され、false に戻したときに自動的にスタイルシートが
    再読み込みされません。

    href
    この属性は、リンクしたリソースの URL を指定します。
    URL は絶対・相対のどちらでもかまいません。

    hreflang
    この属性は、リンク先のリソースの言語を示します。
    これは単なる助言です。許容される値は BCP47 で定めています。
    この属性は、href 属性が提供されている場合にのみ使用します。

    importance
    リソースの相対的な重要性を示します。
    優先度のヒントは以下の値を使用して委任されます。
        auto: 設定なしを表します。ブラウザーはリソースの優先度を決めるために、
              独自の経験則を使用するかもしれません。
        high: リソースが高い優先度のものであることをブラウザーに示します。
        low: リソースが低い優先度のものであることをブラウザーに示します。
    メモ: importance 属性は <link> 要素に rel="preload" または rel="prefetch" がある場合にのみ使用されます。

    integrity
    この属性は、取得したリソースが予期せぬ改ざんを受けずに提供されたかを、
    ユーザーエージェントが検証するために使用できるメタデータである、
    ブラウザーに取得させたリソース (ファイル) の暗号学的ハッシュを
    BASE64 でエンコードしたデータを含みます。
    Subresource Integrity をご覧ください。

    media
    この属性は、リンク先のリソースが適用されるメディアを指定します。
    この値はメディアクエリーでなければなりません。
    この属性は主に外部のスタイルシートから、
    実行中のデバイスに最適なものをユーザーエージェントが
    選択できるようにリンクするときに役立ちます。
    メモ:

    HTML 4 では、単純なホワイトスペースで区切られたメディアリテラルの
    リストのみ記述できます。
    これはメディアタイプとグループ で、print, screen, aural, braille などの
    使用可能な値が定義されています。
    HTML5 ではこれがあらゆるメディアクエリに拡張され、
    HTML 4 で使用できる値の上位互換となっています。
    CSS3 メディアクエリに対応していないブラウザーは、
    リンクを適切に理解するとは限りません。
    HTML 4 で定義されたメディアクエリーのセットに制限されるので、
    フォールバックリンクを設定することを忘れないでください。

    referrerpolicy
    リソースを読み込む際にどのリファラーを使用するかを示す文字列です。
    no-referrer は、Referer ヘッダーを送信しないことを表します。
    no-referrer-when-downgrade は、TLS (HTTPS) を使用せずに生成元へナビゲートする場合は Referer ヘッダーを送信しないことを表します。これは他にポリシーが定められていない場合の、ユーザーエージェントの既定の動作です。
    origin は、ページの生成元 (大まかにいえばスキーム、ホスト、ポート) をリファラーとすることを表します。
    origin-when-cross-origin は、異なるオリジンへの移動ではリファラーをスキーム、ホスト、ポートに制限します。同一オリジンへの移動では、リファラーのパスも含めます。
    unsafe-url は、リファラーに生成元とパスを含めることを表します (ただし、フラグメント、パスワード、ユーザー名は含めません)。これは生成元やパスの情報が TLS で保護されたリソースからセキュアでない生成元へ漏えいしますので、安全ではありません。
    rel
    この属性は現在の文書に対する、リンクされた文書の関係を示します。属性値は、空白で区切られたリンク種別の値のリストでなければなりません。
    sizes
    この属性は、リソースに含まれる映像メディア向けのアイコンのサイズを定義します。これは、rel の値が icon 又は Apple の apple-touch-icon のような標準外の種別が含まれている場合にのみ指定することができます。以下の値を指定できます。
    any: image/svg+xml のようなベクター画像であるため、どのようなサイズにも調整可能であることを示します。
    ホワイトスペースで区切られたサイズのリスト。サイズはそれぞれ <幅のピクセル値>x<高さのピクセル値> または <幅のピクセル値>X<高さのピクセル値> という形式です。それぞれのサイズがリソースに含まれていることが必要です。
    メモ: ほとんどのアイコン形式は 1 個のアイコンのみ保存可能です。よってほとんどの場合、sizes 属性はエントリーが 1 個だけになります。アップルの ICN はもちろん、マイクロソフトの ICO 形式も使用できます。ICO の方が一般的であり、複数ブラウザーの対応 (特に IE の古いバージョン) が重要である場合はこの形式を使用してください。

    title
    title 属性は、<link> 要素では特別な意味があります。
    <link rel="stylesheet"> で使用すると、
    優先スタイルシートか代替スタイルシートか を定義します。
    間違って使用すると スタイルシートが無視されます。

    type
    この属性は、リンク先コンテンツの種類を定義します。
    この属性の値は text/html や text/css などの MIME タイプにします。
    この属性の一般的な使用法は、参照されるスタイルシートのタイプ (text/css など)
    の定義ですが、CSS はウェブ上の唯一のスタイルシート言語であるため、
    type 属性を省略できるばかりでなく、それが実際に推奨される習慣になっています。
    また rel="preload" リンク種別で、ブラウザーが対応するファイルタイプのみ
    ダウンロードさせるためにも使用します。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        AS = 'as'
        CROSSORIGIN = 'crossorigin'
        DISABLED = 'disabled'
        HREF = 'href'
        HREFLANG = 'hreflang'
        IMPORTANCE = 'importance'
        INTEGRITY = 'integrity'
        MEDIA = 'media'
        REFERRERPOLICY = 'referrerpolicy'
        TITLE = 'title'
        TYPE = 'type'

    class CrossOrigin(object):
        """CrossOrigin

        CrossOrigin is a object.
        Responsibility:
        """
        ANONYMOUS = 'anonymous'
        USE_CREDENTIALS = 'use-credentials'

    class Referrerpolicy(object):
        """Referrerpolicy

        Referrerpolicy is a object.
        Responsibility:
        """
        NO_REFERRER = 'no-referrer'
        NO_REFERRER_WHEN_DOWNGRADE = 'no-referrer-when-downgrade'
        ORIGIN = 'origin'
        ORIGIN_WHEN_CROSS_ORIGIN = 'origin-when-cross-origin'
        UNSAFE_URL = 'unsafe-url'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='img', tags=[], attrs=None, **kwargs)

    def set_as(self, value):
        """Set as attibutes value.

        set_attribute(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.AS, value)
        return self

    def get_as(self, ):
        """Get as attribute value.

        get_as()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.AS, None)

    def remove_as(self, ):
        """Remove as attribute value.

        remove_as()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.AS in self.attrs:
            del self.attrs[self.AttributeNames.AS]
        return self

    def set_crossorigin(self, value):
        """Set crossorigin attribute value.

        set_crossorigin(value)

        @Arguments:
        - `value`: crossorigin attribute value.

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.FORM, value)

    def get_crossorigin(self, ):
        """Get crossorigin attribute value.

        get_crossorigin()

        @Return: crossorigin attribute value.

        @Error:
        """
        return self.attrs.get(self.AttributeNames.CROSSORIGIN, None)

    def remove_crossorigin(self, ):
        """Remove crossorigin attribute.

        remove_crossorigin()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.CROSSORIGIN in self.attrs:
            del self.attrs[self.AttributeNames.CROSSORIGIN]
        return self

    def set_disabled(self, ):
        """Set disabled attribute.

        disable_attribute()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.DISABLED in self.attrs:
            del self.attrs[self.AttributeNames.DISABLED]
        return self

    def remove_disabled(self, ):
        """Remove disabled attribute.

        remove_disabled()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.DISABLED, '')

    def is_disabled(self, ):
        """Check has disabled attribute.

        is_disabled()

        @Return: True if enable button

        @Error:
        """
        return self.AttributeNames.DISABLED not in self.attrs

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

    def set_integrity(self, value):
        """Set as integrity value.

        set_integrity(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.INTEGRITY, value)
        return self

    def get_integrity(self, ):
        """Get integrity attribute value.

        get_integrity()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.INTEGRITY, None)

    def remove_integrity(self, ):
        """Remove integrity attribute value.

        remove_integrity()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.INTEGRITY in self.attrs:
            del self.attrs[self.AttributeNames.INTEGRITY]
        return self

    def set_media(self, value):
        """Set as media value.

        set_media(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.MEDIA, value)
        return self

    def get_media(self, ):
        """Get media attribute value.

        get_media()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.MEDIA, None)

    def remove_media(self, ):
        """Remove media attribute value.

        remove_media()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.MEDIA in self.attrs:
            del self.attrs[self.AttributeNames.MEDIA]
        return self

    def set_referrerpolicy(self, value):
        """Set referrerpolicy.

        set_referrerpolicy(value)

        @Arguments:
        - `value`: value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.REFERRERPOLICY, value)

    def get_referrerpolicy(self, ):
        """Get referrerpolicy attribute value.

        get_referrerpolicy()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.REFERRERPOLICY, None)

    def remove_referrerpolicy(self, ):
        """Remove referrerpolicy attribute.

        remove_referrerpolicy()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.REFERRERPOLICY in self.attrs:
            del self.attrs[self.AttributeNames.REFERRERPOLICY]
        return self

    def set_title(self, value):
        """Set title value.

        set_title(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.TITLE, value)
        return self

    def get_title(self, ):
        """Get title attribute value.

        get_title()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.TITLE, None)

    def remove_title(self, ):
        """Remove integrity attribute value.

        remove_title()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.TITLE in self.attrs:
            del self.attrs[self.AttributeNames.TITLE]
        return self

    def set_type(self, value):
        """Set type value.

        set_type(value)

        @Arguments:
        - `value`: attribute value

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
        """Remove type attribute value.

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
# link.py ends here
