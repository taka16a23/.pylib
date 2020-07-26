#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""script -- script tag

"""
from .html_tag import HtmlTag


class Script(HtmlTag):
    """Script

    Script is a HtmlTag.
    Responsibility:

    HTML の <script> 要素は、実行できるコードを埋め込んだり
    参照したりするために使用されます。
    ふつうは JavaScript のコードの埋め込みや参照に使用されます。
    <script> 要素は WebGL の GLSL shader
    プログラミング言語等の他の言語にも使用することができます。

    コンテンツカテゴリ	メタデータコンテンツ, フローコンテンツ, 記述コンテンツ
    許可されている内容	text/javascript などの動的スクリプト
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	メタデータコンテンツを受け入れるすべての要素、または記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	なし
    DOM インターフェイス	HTMLScriptElement

    属性
    この要素にはグローバル属性があります。

    asyncHTML5
    クラシックスクリプトでは、 async 属性があると、
    クラシックスクリプトが利用可能になったらすぐに並行して読み込み、
    解析と評価を行います。

    モジュールスクリプトでは、 async 属性があると、
    スクリプトとその依存関係はすべて遅延キューで実行されるので、
    解析と並行して読み込まれ、利用可能になるとすぐに評価されます。

    この属性は、ブラウザーが解析を一時停止してスクリプトを
    読み込んで評価しなければならないようなパーサーブロック
    JavaScript を排除することを可能にします。
    defer はこの場合に同様の効果があります。

    これは論理属性です。論理属性が要素にあれば真の値を表し、
    属性がなければ偽の値を表します。

    ブラウザーの互換性の状況についてはブラウザーの互換性をご覧ください。
    asm.js 向け非同期スクリプトもご覧ください。

    crossorigin
    通常の script 要素は標準の CORS チェックに通らないスクリプトに対して、
    window.onerror に最小限の情報しか渡しません。
    別のドメインを使用するサイトに静的メディアへの
    エラーログ出力ができるようにするためには、この属性を使用してください。
    有効な値について、詳しくは CORS 設定属性をご覧ください。

    defer
    この論理属性は、スクリプトを文書の解析完了後かつ DOMContentLoaded
    が発生する前に実行することをブラウザーに示します。

    defer 属性の付いたスクリプトは、スクリプトが読み込まれて評価が完了するまで、
    DOMContentLoaded イベントの発生が抑制されます。

    この属性は、 src 属性がない場合 (すなわちインラインスクリプト) に
    使用してはいけません。そのような場合は効果がありません。

    defer 属性はモジュールスクリプトには効果がありません。 — 既定で延期が行われます。

    defer 属性のあるスクリプトは、文書に現れた順に実行されます。

    この属性により、ブラウザーが解析を一時停止してスクリプトを読み込んで
    評価しなければならないような、パーサーブロッキング JavaScript を
    排除することができるようになります。
    async はこの場合と似た効果があります。

    integrity
    この属性は、取得したリソースが予期せぬ改ざんを受けずに提供されたかを、
    ユーザーエージェントが検証するために使用できるメタデータを含みます。
    Subresource Integrity をご覧ください。

    nomodule
    この論理属性は、 ES2015 モジュールに対応するブラウザーで
    スクリプトを実行するべきではないことを示します。
    要するに、モジュール式の JavaScript コードをサポートしない
    古いブラウザー向けのフォールバックスクリプトを提供するために使用できます。

    nonce
    script-src コンテンツセキュリティポリシー内のスクリプトを
    ホワイトリストに入れるための暗号ノンス (ワンタイム番号) です。
    サーバーはポリシーを送信するたびに一意のノンス値を生成する必要があります。
    それ以外の方法でリソースのポリシーのバイパスを推測できない
    ノンスを提供することが重要です。

    referrerpolicy
    スクリプトを読み込んだり、スクリプトがリソースを読み込んだりする際に、
    どのリファラーを送信するかを示します。
    no-referrer: Referer ヘッダーは送信しません。
    no-referrer-when-downgrade (既定値): Referer ヘッダーは、
    オリジンに TLS (HTTPS) がない場合には送信しません。
    origin: 送信するリファラーを、参照しているページのオリジン
    (スキーム、ホスト、ポート番号) のみに制限します。
    origin-when-cross-origin: 異なるオリジンへの移動ではリファラーをスキーム、
    ホスト、ポート番号に制限します。
    同一オリジンへの移動では、リファラーのパスも含めます。
    same-origin: リファラーは同一オリジンには送信しますが、
    オリジン間リクエストにはリファラー情報を含めません。
    strict-origin: プロトコルのセキュリティ水準が同等 (例えば HTTPS→HTTPS)
    である場合は文書のオリジンのみをリファラーとして送信しますが、
    宛先の安全性がより低い場合 (例えば HTTPS→HTTP) には送信しません。
    strict-origin-when-cross-origin: 同一オリジンのリクエストを行う際は
    URL 全体を送信しますが、プロトコルのセキュリティ水準が同等
    (例えば HTTPS→HTTPS) である場合は文書のオリジンのみをリファラーとして送信し、
    宛先の安全性がより低い場合 (例えば HTTPS→HTTP) にはヘッダーを送信しません。
    unsafe-url: リファラーはオリジンおよびパスを含みます
    (ただし、フラグメント、パスワード、ユーザー名は含めません)。
    これはオリジンやパスの情報が TLS で保護されたリソースから
    セキュアでない生成元へ漏えいしますので、安全ではありません。
    メモ: 既定値および referrerpolicy に対応していない場合の
    代替値は空文字列 ("") です。
    referrerpolicy が <script> 要素で明示的に指定されていない場合はより高次元、
    つまり文書全体やドメイン全体のリファラーポリシーに合わせられます。
    より高次元のポリシーが利用できない場合は、空文字列は
    no-referrer-when-downgrade と同等のものとして扱われます。

    src
    この属性は外部スクリプトの URI を指定します。
    文書に直接スクリプトを埋め込む代わりに使用することができます。

    type
    スクリプトを表すタイプを指定します。
    この属性の値は、以下の種類のいずれかにします。

    省略または JavaScript の MIME タイプ:
    これはスクリプトが JavaScript であることを示します。
    HTML5 仕様書では、冗長な MIME タイプを指定せずに属性を省略するよう主張しています。
    過去のブラウザーでは埋め込まれている、
    あるいは (src 属性で) インポートされたコードのスクリプト言語を指定していました。
    JavaScript の MIME タイプは仕様書に掲載されています。
    module: コードを JavaScript モジュールとして扱います。
    スクリプトの処理は、charset および defer 属性の影響を受けません。
    module の利用についての情報は、 JavaScript モジュールをご覧ください。
    クラシックスクリプトとは異なり、モジュールスクリプトはオリジン間の
    フェッチに CORS プロトコルの使用を必要とします。
    その他の値: このタグで埋め込んだコンテンツを、
    ブラウザーによって処理されないデータブロックとして扱います。
    開発者はデータブロックを記述するために、
    JavaScript の MIME タイプではない有効な MIME タイプを使用しなければなりません。

    charset
    存在する場合、値は ASCII で大文字小文字を区別せずに "utf-8" と
    一致する文字列でなければなりません。
    charset 属性は、文書が UTF-8 でなければならないこと、
    および script 要素が文書から文字エンコーディングを継承することから、
    指定する必要はありません。

    language
    type 属性と同じように、この属性は使われているスクリプト言語
    を指定する際に用いられます。
    しかし、 type 属性とは異なり、この属性に指定可能な値が標準化されませんでした。
    代わりに type 属性を使用してください。
    """
    class CrossOrigin(object):
        """CrossOrigin

        CrossOrigin is a object.
        Responsibility:
        """
        ANONYMOUS = 'anonymous'
        USE_CREDENTIALS = 'use-credentials'

    class AttributeNames(HtmlTag.AttributeNames):
        CROSSORIGIN = 'crossorigin'
        DEFER = 'defer'
        INTEGRITY = 'integrity'
        NOMODULE = 'nomodule'
        NONCE = 'nonce'
        REFERRERPOLICY = 'referrerpolicy'
        SRC = 'src'
        TYPE = 'type'
        CHARSET = 'charset'
        LANGUAGE = 'language'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='script', tags=[], attrs=None, **kwargs)

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

    def set_defer(self, value):
        """Set defer.

        set_defer(value)

        @Arguments:
        - `value`: name value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.DEFER, value)

    def get_defer(self, ):
        """Get value attribute value.

        get_defer()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.DEFER, None)

    def remove_defer(self, ):
        """Remove value attribute.

        remove_defer()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.DEFER in self.attrs:
            del self.attrs[self.AttributeNames.DEFER]
        return self

    def set_integrity(self, value):
        """Set integrity.

        set_integrity(value)

        @Arguments:
        - `value`: name value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.INTEGRITY, value)

    def get_integrity(self, ):
        """Get integrity attribute value.

        get_defer()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.INTEGRITY, None)

    def remove_integrity(self, ):
        """Remove integrity attribute.

        remove_integrity()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.INTEGRITY in self.attrs:
            del self.attrs[self.AttributeNames.INTEGRITY]
        return self

    def enable_nomodule(self, ):
        """Enable nomodule.

        enable_nomodule()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.NOMODULE, None)

    def disable_nomodule(self, ):
        """Disable nomodule.

        disable_nomodule()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.NOMODULE in self.attrs:
            del self.attrs[self.AttributeNames.NOMODULE]
        return self

    def is_nomodule(self, ):
        """Check nomodule enabled.

        is_nomodule()

        @Return: this instance

        @Error:
        """
        return self.AttributeNames.NOMODULE in self.attrs

    def set_nonce(self, value):
        """Set nonce.

        set_nonce(value)

        @Arguments:
        - `value`: name value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.NONCE, value)

    def get_nonce(self, ):
        """Get nonce attribute value.

        get_nonce()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.NONCE, None)

    def remove_nonce(self, ):
        """Remove nonce attribute.

        remove_nonce()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.NONCE in self.attrs:
            del self.attrs[self.AttributeNames.NONCE]
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

    def set_src(self, value):
        """Set src.

        set_src(value)

        @Arguments:
        - `value`: name value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.SRC, value)

    def get_src(self, ):
        """Get src attribute value.

        get_src()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.SRC, None)

    def remove_src(self, ):
        """Remove src attribute.

        remove_src()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.SRC in self.attrs:
            del self.attrs[self.AttributeNames.SRC]
        return self

    def set_type(self, value):
        """Set type.

        set_type(value)

        @Arguments:
        - `value`: type attribute value.

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.TYPE, value)

    def get_type(self, ):
        """Get type attribute.

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

    def get_charset(self, ):
        """Get charset attribute values.

        get_charset()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.CHARSET, None)

    def append_charset(self, value):
        """Append charset values.

        append_charset(value)

        @Arguments:
        - `value`:

        @Return: this instance

        @Error:
        """
        self.attrs.append_value(self.AttributeNames.CHARSET, value)
        return self

    def remove_charset(self, value):
        """Remove charset value.

        remove_charset(value)

        @arguments:
        - `value`: value

        @Return: this instance

        @Error:
        """
        self.attrs.remove_value(self.AttributeNames.CHARSET, klass)
        return self

    def clear_charset(self, ):
        """Clear charset.

        clear_charset()

        @Return: this instance

        @Error:
        """
        self.clear_attribute_value(self.AttributeNames.CHARSET)
        return self

    def delete_charset(self, ):
        """Delete charset.

        delete_charset()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.CHARSET in self.attrs:
            del self.attrs[self.AttributeNames.CHARSET]
        return self

    def set_language(self, value):
        """Set language.

        set_language(value)

        @Arguments:
        - `value`: language attribute value.

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.LANGUAGE, value)

    def get_language(self, ):
        """Get language attribute.

        get_language()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.LANGUAGE, None)

    def remove_language(self, ):
        """Remove language attribute.

        remove_language()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.LANGUAGE in self.attrs:
            del self.attrs[self.AttributeNames.LANGUAGE]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# script.py ends here
