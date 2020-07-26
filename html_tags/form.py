#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""form -- form tag

"""
from .html_tag import HtmlTag


class Form(HtmlTag):
    """Form

    Form is a HtmlTag.
    Responsibility:

    HTML の <form> 要素は、ウェブサーバーに情報を送信するための
    対話型コントロールを含む文書の区間を表します。

    <form> 要素には、 CSS の :valid および :invalid
    疑似クラスを使用して整形することが可能です。

    コンテンツカテゴリ	フローコンテンツ, 知覚可能コンテンツ
    許可されている内容	フローコンテンツ。ただし、<form> 要素の中に別の <form> 要素を内包することは許可されていません。
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	フローコンテンツを受け入れるすべての要素
    許可されている ARIA ロール	group, presentation
    DOM インターフェイス

    accept-charset
    サーバーが受け入れる文字エンコーディングのリスト。
    リストはスペースまたはコンマで区切ることができます。
    ブラウザーは、それらがリストされている順序を優先順位として使用します。
    既定値である予約語 "UNKNOWN" は、
    form 要素を含む文書のエンコーディングと同じであることを示します。
    以前のバージョンの HTML では、
    さまざまな文字エンコーディングをスペースまたはコンマで区切ることができました。
    これは HTML5 ではあてはまらず、スペースだけが適切です。

    action
    フォーム経由で送信された情報を処理するプログラムの URI。この値は <button>, <input type="submit">, <input type="image"> の formaction 属性によって上書きすることが可能です。

    autocomplete
    input 要素が既定で、ブラウザーによる値の入力補完を受けるかを示します。
    この設定はフォームに属する要素の autocomplete 属性で上書きできます。
    以下の値が指定可能です。
    off: ユーザーは、フォームを使用するたびにすべての値を入力するか、
    もしくは独自の入力補完を使用する必要があります。
    ブラウザーが入力補完をサポートすることはありません。
    on: ブラウザーはユーザーが以前に入力した値に基づき、
    これを自動補完のための候補として使用することができます。
    ほとんどの現行ブラウザー (Firefox 38+、Google Chrome 34+、IE 11+ など) では
    autocomplete 属性を設定しても、
    ブラウザーのパスワードマネージャーがユーザーにログイン情報
    (ユーザー名やパスワード) を保存したいかを問い合わせる、
    またユーザーが同意した場合に次回以降ページを訪れた際に
    ログイン情報を自動入力することは抑制できません。
    autocomplete 属性とログインフィールドをご覧ください。
    メモ: 文書で独自の入力補完を提供するために autocomplete を
    off に設定する場合は、フォーム内で入力補完が可能なそれぞれの
    input 要素でも autocomplete を off に設定するべきです。
    詳しくは、互換性一覧表の Google Chrome に関するメモを参照してください。

    enctype
    method 属性の値が post であるとき、
    この属性はフォームをサーバーに送信する際に使用する、
    コンテンツの MIME タイプを示します。以下の値が指定可能です。
    application/x-www-form-urlencoded: 初期値。属性を指定していない場合、
    この値が使用されます。
    multipart/form-data: type 属性で "file" を指定した
    <input> 要素のために使用する値です。
    text/plain: (HTML5)
    この値は、 <button>, <input type="submit">,
    <input type="image"> の formenctype 属性によって上書きすることが可能です。

    method
    フォームを送信する際にブラウザーが使用する HTTP メソッドです。
    以下の値が指定可能です。
    post: HTTP POST メソッドに相当します。
    フォームのデータはボディに収めてサーバーに送信します。
    get: HTTP GET メソッドに相当します。
    フォームのデータは '?' をセパレーターとして action 属性の URI に追加して、
    その結果となる URI をサーバにー送信します。
    フォームが ASCII 文字列だけを含み、まったく副作用がない場合にのみ、
    このメソッドを使用してください。
    dialog: フォームが <dialog> 要素の中にある場合に使用し、
    送信するとダイアログが閉じます。
    この値は、 <button>, <input type="submit">, <input type="image"> の
    formmethod 属性によって上書きすることが可能です。

    name
    フォームの名前です。HTML 4 では推奨されていません
    （代わりに id を用いるべきです）。
    HTML 5 ではドキュメント内のフォーム間でユニークである必要があり、
    また空文字列であってはいけません。

    novalidate
    フォームを送信するときに検証しないことを示す真偽値です。
    この属性を指定していない（つまり検証される）場合は、既定の設定を <button>,
    <input type="submit">, <input type="image"> の
    formnovalidate 属性で上書きすることが可能です。

    target
    フォームを送信した後に受け取った応答の表示位置を示す名前またはキーワードです。
    これは、HTML 4 ではフレームの名前またはキーワードでした。
    HTML5 では、閲覧コンテキスト の名前またはキーワードです
    (例えば、タブ、ウィンドウ、インラインフレームなど)。
    以下のキーワードは特別な意味を持ちます:
    _self: 応答を現在と同じ HTML 4 フレーム (または HTML5 閲覧コンテキスト) に表示します。この値は、属性が指定されていない場合の既定値です。
    _blank: 応答を新しい名前のつけられていない、HTML 4 ウィンドウまたは HTML5 の閲覧コンテキストに読み込みます。
    _parent: 応答を現在のフレームの HTML 4 フレームセットの親要素または HTML5 の現在の親閲覧コンテキストに読み込みます。親要素がない場合、このオプションは _self と同じ振る舞いをします。
    _top: HTML 4 では、応答を元のウィンドウ全体に読み込み、他のフレームをすべてキャンセルします。HTML5 では、応答をトップレベルの閲覧コンテキストに読み込みます (現在の閲覧コンテキストの祖先にあたり、それ以上親のない要素です)。親要素がない場合、このオプションは _self と同じ振る舞いをします。
    iframename: 応答を、名前のついた <iframe> に読み込みます。
    HTML5: この値は、 <button>, <input type="submit">,
    <input type="image"> の formtarget 属性によって上書きすることが可能です。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        ACCEPT_CHARSET = 'accept-charset'
        ACTION = 'action'
        AUTOCOMPLETE = 'autocomplete'
        ENCTYPE = 'enctype'
        METHOD = 'method'
        NAME = 'name'
        NOVALIDATE = 'novalidate'
        TARGET = 'target'

    class AcceptCharset(object):
        """AcceptCharset

        AcceptCharset is a object.
        Responsibility:
        """
        UNKNOWN = 'unknown'

    class Enctype(object):
        """Enctype

        Enctype is a object.
        Responsibility:
        """
        DEFAULT = 'application/x-www-form-urlencoded'
        FILE = 'multipart/form-data'
        TEXT = 'text/plain'

    class Method(object):
        """Method

        Method is a object.
        Responsibility:
        """
        GET = 'get'
        POST = 'post'
        DIALOG = 'dialog'

    class Target(object):
        """Target

        Target is a object.
        Responsibility:
        """
        SELF = 'self'
        BLANK = 'blank'
        PARENT = 'parent'
        TOP = 'top'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='form', tags=[], attrs=None, **kwargs)

    def get_accept_charset(self, ):
        """Get accept-charset attribute values.

        get_accept-charset()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ACCEPT_CHARSET, None)

    def append_accept_charset(self, value):
        """Append accept-charset values.

        append_accept_charset(value)

        @Arguments:
        - `value`:

        @Return: this instance

        @Error:
        """
        self.attrs.append_value(self.AttributeNames.ACCEPT_CHARSET, value)
        return self

    def remove_accept_charset(self, value):
        """Remove accept-charset value.

        remove_accept_charset(value)

        @arguments:
        - `value`: value

        @Return: this instance

        @Error:
        """
        self.attrs.remove_value(self.AttributeNames.ACCEPT_CHARSET, klass)
        return self

    def clear_accept_charset(self, ):
        """Clear accept charset.

        clear_accept_charset()

        @Return: this instance

        @Error:
        """
        self.clear_attribute_value(self.AttributeNames.ACCEPT_CHARSET)
        return self

    def delete_accept_charset(self, ):
        """Delete accept_charset.

        delete_accept_charset()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ACCEPT_CHARSET in self.attrs:
            del self.attrs[self.AttributeNames.ACCEPT_CHARSET]
        return self

    def set_action(self, value):
        """Set action attribute.

        set_action(value)

        @Arguments:
        - `value`: action value

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.ACTION, value)

    def remove_action(self, ):
        """Remove action attribute.

        remove_action()

        @Return: this instance.

        @Error:
        """
        self.attrs.remove_attribute(self.AttributeNames.ACTION)
        return self

    def get_action(self, ):
        """Get action attribute.

        get_action()

        @Return: (str) id value if exists else None.

        @Error:
        """
        if self.AttributeNames.ACTION not in self.attrs:
            return None
        return str(self.attrs[self.AttributeNames.ACTION])

    def enable_autocomplete(self, ):
        """set on autocomplete attribute value.

        enable_contenteditable()

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.AUTOCOMPLETE, 'on')

    def disable_autocomplete(self, ):
        """Set off autocomplete attribute value.

        disable_autocomplete()

        @Return: this instance.

        @Error:
        """
        self.set_contenteditable(self.ContentEditable.AUTOCOMPLETE)
        return self

    def remove_autocomplete(self, ):
        """Remove autocomplete attribute.

        remove_autocomplete()

        @Return: this instance.

        @Error:
        """
        if self.AttributeNames.AUTOCOMPLETE in self.attrs:
            del self.attrs[self.AttributeNames.AUTOCOMPLETE]
        return self

    def set_enctype(self, value):
        """Set enctype.

        set_enctype(value)

        @Arguments:
        - `value`: enctype

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.ENCTYPE, value)

    def get_enctype(self, ):
        """Get enctype attribute value.

        get_enctype()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ENCTYPE, None)

    def remove_enctype(self, ):
        """Remove enctype attribute.

        remove_enctype()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ENCTYPE in self.attrs:
            del self.attrs[self.AttributeNames.ENCTYPE]
        return self

    def set_method(self, value):
        """Set method.

        set_method(value)

        @Arguments:
        - `value`: method

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.METHOD, value)

    def get_method(self, ):
        """Get method attribute value.

        get_method()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.METHOD, None)

    def remove_method(self, ):
        """Remove method attribute.

        remove_method()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.METHOD in self.attrs:
            del self.attrs[self.AttributeNames.METHOD]
        return self

    def set_name(self, value):
        """Set name.

        set_name(value)

        @Arguments:
        - `value`: name

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.NAME, value)

    def get_name(self, ):
        """Get name attribute value.

        get_name()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.NAME, None)

    def remove_name(self, ):
        """Remove name attribute.

        remove_name()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.NAME in self.attrs:
            del self.attrs[self.AttributeNames.NAME]
        return self

    def set_novalidate(self, ):
        """set novalidate attribute value.

        set_novalidate()

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.NOVALIDATE, None)

    def remove_novalidate(self, ):
        """Remove novalidate attribute.

        remove_novalidate()

        @Return: this instance.

        @Error:
        """
        if self.AttributeNames.NOVALIDATE in self.attrs:
            del self.attrs[self.AttributeNames.NOVALIDATE]
        return self

    def set_target(self, value):
        """Set target.

        set_target(value)

        @Arguments:
        - `value`: target

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.TARGET, value)

    def get_target(self, ):
        """Get target attribute value.

        get_target()

        @Return:

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



# for Emacs
# Local Variables:
# coding: utf-8
# End:
# form.py ends here
