#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""img -- img tag

"""
from .html_tag import HtmlTag


class Img(HtmlTag):
    """Img

    Img is a HtmlTag.
    Responsibility:

    上記の例では、 <img> 要素のとてもシンプルな使い方を示しています。

    src 属性は必須で、埋め込みたい画像へのパスを入れます。
    alt 属性は画像のテキストによる説明で、
    必須ではありませんがアクセシビリティのために非常に有用です。
    — 読み上げソフトがこの説明を読み上げることで、
    画像が何を表すかをユーザーが知ることができます。
    また、代替テキストは、例えばネットワークエラーやコンテンツがブロックされた、
    リンク切れ等、何らかの理由で画像が読み込めなかった場合に、ページに表示されます。
    以下の例のように、様々な目的を達成するために、
    指定することができるその他の属性がたくさんあります。

    セキュリティおよびプライバシーのための Referrer/CORS 制御。
    crossorigin および referrerpolicy を参照してください。
    width と height の両方を使用して画像の固有の寸法を設定すると、
    画像を読み込む前に場所を確保し、
    コンテンツのレイアウトが移動することを防ぐことができます。
    sizes および srcset を使用したレスポンシブ画像のヒント
    (<picture> 要素、およびレスポンシブ画像のチュートリアルもご覧ください)。

    対応している画像形式
    HTML 標準では、対応しなければならない画像形式の一覧を提供していないので、ユーザーエージェントによって対応する画像形式のセットは異なります。ウェブブラウザーで対応している画像形式のガイドが利用できます。

    Abbreviation	File format	MIME type	File extension(s)	Browser compatibility
    APNG	Animated Portable Network Graphics	image/apng	.apng	Chrome, Edge, Firefox, Opera, Safari
    BMP	Bitmap file	image/bmp	.bmp	Chrome, Edge, Firefox, Internet Explorer, Opera, Safari
    GIF	Graphics Interchange Format	image/gif	.gif	Chrome, Edge, Firefox, Internet Explorer, Opera, Safari
    ICO	Microsoft Icon	image/x-icon	.ico, .cur	Chrome, Edge, Firefox, Internet Explorer, Opera, Safari
    JPEG	Joint Photographic Expert Group image	image/jpeg	.jpg, .jpeg, .jfif, .pjpeg, .pjp	Chrome, Edge, Firefox, Internet Explorer, Opera, Safari
    PNG	Portable Network Graphics	image/png	.png	Chrome, Edge, Firefox, Internet Explorer, Opera, Safari
    SVG	Scalable Vector Graphics	image/svg+xml	.svg	Chrome, Edge, Firefox, Internet Explorer, Opera, Safari
    TIFF	Tagged Image File Format	image/tiff	.tif, .tiff	None built-in; add-ons required
    WebP	Web Picture format	image/webp	.webp	Chrome, Edge, Firefox, Opera
    The abbreviation for each format links to a longer description of the format, its capabilities, and detailed browser compatibility information; including which versions introduced support and specific special features that may have been introduced later.

    画像読み込みエラー
    画像の読み込みまたは表示の間にエラーが発生した場合、かつ
    onerror イベントハンドラーが error イベントを扱うよう設定されていた場合は、
    イベントハンドラーが呼び出されます。これはいくつもの状況がありえます。

    src 属性が空 ("") または null である。
    指定された src の URL が現在ユーザーがいるページの URL と同じである。
    指定された画像が何らかの理由で読み込みが妨害され、中止された。
    指定された画像のメタデータが、寸法を受け取ることができないなどの
    理由で読み込みが中止され、かつ <img> 要素の属性に寸法が指定されていなかった場合。
    指定された画像が、ユーザーエージェントが対応している形式ではない場合。

    属性
    この要素にはグローバル属性があります。

    alt
    この属性は、画像を説明する代替文字列を定義します。
    メモ: ブラウザーは、要素から参照された画像を常に表示するとは限りません。

    視覚ブラウザー以外のブラウザー (視覚障碍者向けの物を含む) で閲覧された場合
    ユーザーが画像を非表示に設定している場合 (帯域の節約、プライバシー上の理由)
    画像が無効であったり未対応の画像形式であったりした場合
    このような場合、ブラウザーは、画像をこの要素の alt 属性で
    定義された文字列に置き換えます。
    このような理由から、 alt には可能な限り役に立つ値を指定するべきです。

    alt 属性を省略すると、画像がコンテンツの鍵となる部分であり、
    同等のテキスト表現を行うことができないことを表します。
    この属性に空文字列を設定すると (alt="")、
    この画像がコンテンツにおいて重要な箇所ではないことを示し、
    視覚ブラウザーではない場合はレンダリングを省略することがあります。
    視覚ブラウザーでは、 alt が空欄で画像の表示に失敗した場合は、
    壊れた画像のアイコンの表示が省略される場合もあります。

    この属性は画像をテキストにコピー＆ペーストした場合や、
    リンクされた画像をブックマークに保存したときにも使用されます。

    crossorigin
    これは列挙型の属性で、関連する画像の取得の際に CORS を使用しなければならないか
    どうかを示します。
    CORS が有効な画像は、「汚染」されることなく <canvas> 要素で再利用できます。
    次の値が使用できます。
    anonymous
    オリジン間リクエスト (Origin HTTP ヘッダーを持つリクエスト) を実行しますが、
    資格情報 (Cookie、 X.509 証明書、 HTTP ベーシック認証など) は送信しません。
    サーバーがそのオリジンのサイトに資格情報を付与しない
    (HTTP の Access-Control-Allow-Origin ヘッダーの設定がない) 場合は、
    画像が汚染され、その使用も制限されます。
    use-credentials
    信用情報を伴ってオリジン間リクエスト (HTTP の Origin ヘッダーを持つリクエスト)
    を送信します (Cookie、証明書、 HTTP ベーシック認証を使用します)。
    サーバーが元のサイトに信用情報を付与しない場合は
    (HTTP の Access-Control-Allow-Credentials ヘッダーに関わらず)、
    画像が汚染され、その使用も制限されます。
    この属性を指定しない場合は、リソースが CORS リクエストなしで取得され
    (HTTP の Origin: ヘッダーを送信せずに取得)、
    <canvas> 要素での汚染されない使用が妨げられます。
    この属性が無効である場合は、列挙型のキーワードに anonymous が
    指定されたものとして扱います。詳しくは CORS 設定属性を参照してください。

    decoding
    ブラウザーに画像のデコードのヒントを提供します。次のような値が使用できます。
        sync
        他のコンテンツと不可分の表示として、画像を同期的にデコードします。
        async
        他のコンテンツの表示が遅れないように、画像を非同期的にデコードします。
        auto
        既定のモードで、デコード方式を指定しません。ブラウザーはユーザーのために最良の方法を選択します。

    height
    画像固有の高さをピクセル値で指定します。

    importance
    リソースの相対的な重要性を示します。優先度のヒントは以下の値を使用して委任されます。
        auto: 設定なしを表します。
              ブラウザーはリソースの優先度を決めるために、
              独自の経験則を使用するかもしれません。
        high: リソースが高い優先度のものであることをブラウザーに示します。
        low: リソースが低い優先度のものであることをブラウザーに示します。

    intrinsicsize
    この属性はブラウザーに、画像の固有の寸法を無視し、
    この属性で指定された寸法であると見せかけるよう指示します。
    特に、画像がこれらの次元のラスターであって、画像の
    naturalWidth/naturalHeight はこの属性で指定された値が返されます。
    説明と例

    ismap
    この真偽値を持つ属性は、画像がサーバーサイドマップの一部であるかを示します。
    そうである場合は、クリック位置の正確な座標をサーバーに送信します。
    メモ: この属性は <img> 要素が、有効な href 属性を持つ
    <a> 要素の子孫である場合に限り許可されます。

    loading
    ブラウザーがどのように画像を読み込むかを示します。
    eager: 画像が現在可視ビューポートに入っているかどうかにかかわらず、
           直ちに画像を読み込みます (これが既定値です)。
    lazy: 画像がブラウザーで定義されたビューポートからの距離に達するまで、
          画像の読み込みを遅延させます。
          これは、画像が必要とされるのが合理的に確実になるまで、
          処理に必要なネットワークやストレージの帯域幅を使用しないようにするためです。
          これは一般的に、ほとんどの典型的な使用法において、
          コンテンツの性能を向上させることができます。

    referrerpolicy
    リソースを読み込む際に、どのリファラーを使用するかを示す文字列です。
    no-referrer: Referer ヘッダーを送信しないことを表します。
    no-referrer-when-downgrade: TLS (HTTPS) を使用せずにある
                                オリジンへ移動する場合は、 Referer
                                ヘッダーを送信しないことを表します。
                                これは他にポリシーが定められていない場合の、
                                ユーザーエージェントの既定の動作です。
    origin: Referer ヘッダーにそのページのオリジンのスキーム、ホスト名、
                    ポート番号を含めます。
    origin-when-cross-origin: 異なるオリジンへのナビゲーションでは、
                              リファラーをスキーム、ホスト、ポートのみに制限します。
                              同一のオリジンへのナビゲーションでは、リファラーのフルパスを含めます。
    unsafe-url: Referer ヘッダーにオリジンとパスを含めることを表します
                        (ただし、フラグメント、パスワード、ユーザー名は含めません)。
                        これはオリジンやパスの情報が TLS で保護された
                        リソースからセキュアでないオリジンへ漏えいしますので、安全ではありません。

    sizes
    ソースのサイズのセットを示す、カンマ区切りの文字列を1個以上並べたリストです。
    それぞれのソースサイズの構成は以下のとおりです。
    メディア条件。最後のアイテムでは省略しなければなりません。
    ソースサイズ値。
    メディアの状態はビューポートのプロパティで記述するものであり、
    画像のプロパティではありません。
    例えば、 (max-height: 500px) 1000px は、ビューポートの高さが
    500px 以下であれば 1000px 幅のソースを使用することを提案します。

    ソースサイズ値は、画像の表示サイズを指定するものです。
    ユーザーエージェントは srcset 属性で与えられたソースからひとつを選択するために、
    現在のソースサイズを使用します。
    そのとき、ソースは幅記述子 ('w') を使用して説明します。
    選択したソースサイズは画像の固有の寸法 (CSS スタイルが適用されていない場合の、
    画像の表示サイズ) に影響します。
    srcset 属性がない場合、あるいは幅記述子 (w) を持つ値がない場合は、
    sizes 属性の効果はありません。

    src
    画像の URL です。この属性は、 <img> 要素に必須です。
    srcset に対応するブラウザーでは src を、画素密度記述子
    1x の候補画像であるように扱います。
    ただし、この画素密度記述子が srcset で定義済みである、
    または srcset に 'w' 記述子が含まれている場合を除きます。

    srcset
    ユーザーエージェントが使用可能なソース画像のセットを示す、
    カンマ区切りで文字列を 1 個以上並べたリストです。
    各々の文字列の構成は以下のとおりです:
    画像の URL
    任意で、ホワイトスペースの後に以下のいずれかを記述:
    幅記述子。これは直後に 'w' を付加した正の整数です。
    幅記述子は実際の画素密度を計算するために、
    sizes 属性で与えられたソースサイズで割られます。
    画素密度記述子。これは直後に 'x' を付加した正の浮動小数点数です。
    記述子を指定しない場合は、ソースを既定の記述子 1x に割り当てます。

    幅記述子と画素密度記述子を同一の srcset 属性に混在させると無効になります。
    重複した記述子 (例えばひとつの srcset に2つのソースがあり、
    どちらも '2x' とする) も無効になります。

    ユーザーエージェントには、利用可能なソースからひとつを選択する裁量があります。
    これは、ユーザー設定や帯域幅の条件などに基づいて選択を適合させるような、
    かなりの裁量が与えられています。例としてはレスポンシブ画像のチュートリアルを
    ご覧ください。

    width
    画像固有の幅をピクセル値で指定します。
    usemap
    要素に関連づけられた イメージマップの部分的な URL ('#' で始まる) です。
    メモ: <img> 要素が <a> または <button> 要素の子孫である場合は、
    この属性を使用することはできません。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        ALT = 'alt'
        CROSSORIGIN = 'crossorigin'
        anonymous = 'anonymous'
        USE_CREDENTIALS = 'use-credentials'
        DECODING = 'decoding'
        SYNC = 'sync'
        ASYNC = 'async'
        AUTO = 'auto'
        HEIGHT = 'height'
        IMPORTANCE = 'importance'
        INTRINSICSIZE = 'intrinsicsize'
        ISMAP = 'ismap'
        LOADING = 'loading'
        SIZES = 'sizes'
        SRC = 'src'
        SRCSET = 'srcset'
        WIDTH = 'width'
        USEMAP = 'usemap'

    class CrossOrigin(object):
        """CrossOrigin

        CrossOrigin is a object.
        Responsibility:
        """
        ANONYMOUS = 'anonymous'
        USE_CREDENTIALS = 'use-credentials'

    class Decoding(object):
        """Decoding

        Decoding is a object.
        Responsibility:
        """
        SYNC = 'sync'
        ASYNC = 'async'
        AUTO = 'auto'

    class Importance(object):
        """Importance

        Importance is a object.
        Responsibility:
        """
        AUTO = 'auto'
        HIGH = 'high'
        LOW = 'low'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='img', tags=[], attrs=None, **kwargs)

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

    def set_decoding(self, value):
        """Set decoding attribute value.

        set_decoding(value)

        @Arguments:
        - `value`: decoding attribute value.

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.DECODING, value)

    def get_decoding(self, ):
        """Get decoding attribute value.

        get_decoding()

        @Return: decoding attribute value.

        @Error:
        """
        return self.attrs.get(self.AttributeNames.DECODING, None)

    def remove_decoding(self, ):
        """Remove decoding attribute.

        remove_decoding()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.DECODING in self.attrs:
            del self.attrs[self.AttributeNames.DECODING]
        return self

    def set_height(self, value):
        """Set height attribute value.

        set_height(value)

        @Arguments:
        - `value`: height attribute value.

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.HEIGHT, value)

    def get_height(self, ):
        """Get height attribute value.

        get_height()

        @Return: height attribute value.

        @Error:
        """
        return self.attrs.get(self.AttributeNames.HEIGHT, None)

    def remove_height(self, ):
        """Remove height attribute.

        remove_height()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.HEIGHT in self.attrs:
            del self.attrs[self.AttributeNames.HEIGHT]
        return self

    def set_importance(self, value):
        """Set importance attribute value.

        set_importance(value)

        @Arguments:
        - `value`: importance attribute value.

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.IMPORTANCE, value)

    def get_importance(self, ):
        """Get importance attribute value.

        get_importance()

        @Return: importance attribute value.

        @Error:
        """
        return self.attrs.get(self.AttributeNames.IMPORTANCE, None)

    def remove_importance(self, ):
        """Remove importance attribute.

        remove_importance()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.IMPORTANCE in self.attrs:
            del self.attrs[self.AttributeNames.IMPORTANCE]
        return self

    def set_intrinsicsize(self, value):
        """Set intrinsicsize attribute value.

        set_intrinsicsize(value)

        @Arguments:
        - `value`: intrinsicsize attribute value.

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.INTRINSICSIZE, value)

    def get_intrinsicsize(self, ):
        """Get intrinsicsize attribute value.

        get_intrinsicsize()

        @Return: intrinsicsize attribute value.

        @Error:
        """
        return self.attrs.get(self.AttributeNames.INTRINSICSIZE, None)

    def remove_intrinsicsize(self, ):
        """Remove intrinsicsize attribute.

        remove_intrinsicsize()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.INTRINSICSIZE in self.attrs:
            del self.attrs[self.AttributeNames.INTRINSICSIZE]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# img.py ends here
