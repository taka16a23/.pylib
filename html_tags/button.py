#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""button -- button tag

"""
from .html_tag import HtmlTag


class Button(HtmlTag):
    """Button

    Button is a HtmlTag.
    Responsibility:

    HTML の <button> 要素はクリックできるボタンを表し、フォームや、
    文書で単純なボタン機能が必要なあらゆる場所で使用することができます。
    既定では、 HTML のボタンは ユーザーエージェント が実行されているホストの
    プラットフォームのスタイルと似ていますが、
    CSS を使用してボタンの外見を変更することができます。

    <button> 要素は <input> 要素よりもずっと簡単に整形できます。
    <input> が value 属性に文字列を設定することしかできないのに対し、
    内部に HTML コンテンツを追加できますし (<em>、 <strong> や <img> さえも)、
    複雑な描画のために ::after や ::before 疑似要素を使用することもできます。

    ボタンがサーバーにデータを送信するためのものでない場合は、
    button に type 属性を設定することを忘れないでください。
    さもないと、フォームデータを送信して (存在しない) レスポンスを読み込み、
    文書の現在の状態を破棄してしまうおそれがあります。

    Internet Explorer 7 には <button type="submit" name="myButton" value="foo">Click me</button>
    でフォームデータを送信したとき、 POST データが myButton=foo ではなく
    myButton=Click me として送信されるバグがあります。
    この問題は Internet Explorer 6 ではもっと悪く、ボタンを介してフォームデータを送信すると、
    Internet Explorer 7 と同様の方法でフォーム内のすべてのボタンが送信されるバグもあります。
    このバグは Internet Explorer 8 で修正されました。

    Firefox の既定の動作は他のブラウザーと異なり、ページを再読み込みしても
    <button> を動的に無効化した状態を維持します。
    autocomplete 属性の値を off にすると、この機能が無効になります。
    バグ 654072 をご覧ください。

    Android 版 Firefox のバージョン35より前では、すべてのボタンに既定でグラデーションの
    background-image を設定していました (バグ 763671 をご覧ください)。
    これは background-image: none を使用して無効化できます。

    Example
    <button name="button">クリックしてね</button>
    """
    class AttributeNames(HtmlTag.AttributeNames):
        """AttributeNames

        AttributeNames is a HtmlTag.AttributeNames.
        Responsibility:

        autofocus
        論理属性で、ページ読み込み時に (ユーザーが例えば他のコントロールに入力するなどして
        動作を上書きしない限り)、入力フォーカスを持つべきボタンであることを指定します。
        文書中のフォーム関連要素のうちの一つだけにこの属性を指定することができます。

        autocomplete
        <button> 要素におけるこの属性は、 Firefox 独自の非標準属性です。
        Firefox の既定の動作は他のブラウザーと異なり、ページを再読み込みしても
        <button> を動的に無効化した状態を維持します。
        autocomplete="off" に設定すると、この機能が無効になります。 バグ 654072 をご覧ください。

        disabled
        論理属性で、ユーザーがボタンを操作することを抑止します。
        この属性が設定されていない場合、ボタンを内包する親要素の設定値を継承します。
        例えば、ボタンの祖先となる <fieldset> 要素などにも disabled 属性が
        指定されていないのであれば、この子要素であるボタンは使用可能のままであるということです。
        Firefox の動作は他のブラウザーと異なり、ページを再読み込みしても
        <button> を動的に無効化した状態を維持します。
        この機能は autocomplete 属性で制御できます。

        form
        ボタンに関連付けられた <form> 要素 (フォームオーナー) です。
        属性値は同一文書内の <form> 要素の id 属性と同一の値にしなくてはなりません。
        この属性を設定しなかった場合は、祖先に <form> 要素が存在すれば、
        その要素に関連付けられます。この属性によって <form> 要素の子孫にするだけでなく、
        同一文書内にある任意の <form> 要素に <button>
        要素を関連付けることが可能になりました。

        formaction
        ボタンによって送信された情報を処理する URL です。
        指定した場合は、そのボタンの属するフォームの action 属性よりも優先されます。

        formenctype
        ボタンを送信ボタンとして使用する場合、ブラウザーがフォーム情報をサーバーに送信する
        ために使用するフォームデータのエンコード方法を指定します。
        以下の値が指定可能です。
        application/x-www-form-urlencoded: 初期値。
        属性を指定していない場合、この値が使用されます。
        multipart/form-data: <input> 要素の type 属性に file を指定して使用する 場合に使用。
        text/plain: デバッグ目的で仕様書に追加されました。
        実用的なフォーム送信で使用するべきではありません。
        この属性が指定されている場合、button 属性が紐付けられた
        form 要素 (form owner)の enctype 属性より、ボタンのそれが優先されます。

        formnovalidate
        ボタンが送信ボタンである場合に、ブラウザーがフォーム情報を送信するために使用する
        HTTP メソッドです。以下の値が指定可能です。
        post: フォームのデータは、サーバーへ送信する際に
        HTTP リクエストの本文に含められます。
        フォームにパスワードなどの公開するべきではない情報が含まれている場合は、
        このメソッドを使用してください。
        get: フォームのデータは、セパレーターとして '?' を使用してフォームの
        action の URL に追加され、その結果となる URL をサーバーへ送信します。
        検索フォームのように、まったく副作用がない場合にのみ、このメソッドを使用してください。
        この属性が指定された場合、これはボタンのフォームオーナーの method 属性より
        優先して使用されます。
        example
        <button type="submit" formmethod="post">Submit using POST</button>

        formnovalidate
        論理属性で、ボタンが送信ボタンである場合に、
        フォームデータ送信時に内容を検証しないように指定するものです。
        この属性が指定された場合、ボタンの属するフォームオーナーの novalidate 属性
        より優先して使用されます。

        formtarget
        ボタンが送信ボタンである場合、フォームの送信後に受信したレスポンスを表示する場所
        を示すユーザー定義の名前、もしくはアンダースコアから始まる標準化されたキーワードです。
        これは、閲覧コンテキスト (タブ、ウィンドウ、インラインフレーム) の
        name またはそれを表すキーワードです。
        この属性が指定された場合、ボタンの属するフォームオーナーの
        target 属性より優先されます。以下のキーワードは特別な意味を持ちます。
        _self: 同じ閲覧コンテキストにレスポンスデータを読み込みます。
               これは、属性が指定されていない場合の既定値です。
        _blank: 新しい無名の閲覧コンテキスト — 普通は、ブラウザーの設定に従い、
                新しいタブまたはウィンドウ — にレスポンスデータを読み込みます。
        _parent: 現在のコンテキストの親の閲覧コンテキストにレスポンスデータを読み込みます。
                 親要素がない場合、このオプションは _self と同じ振る舞いをします。
        _top: 最上位の閲覧コンテキスト (現在のコンテキストの祖先で、
              それ以前の祖先をもたない閲覧コンテキスト) にレスポンスデータを読み込みます。
              親要素がない場合、このオプションは _self と同じ振る舞いをします。

        name
        フォームデータの一部としてボタンの value との組み合わせで送信される、
        ボタンの名前です。

        type
        ボタンの種別。以下の値を指定可能です。
        submit: 自身が属するフォームのデータをサーバーに送信するボタンとなります。
        これは type 属性が指定されていない場合、
        もしくは属性値が動的に空にされたり不正な値にされた場合の既定の動作です。
        reset: <input type="reset"> と同様に、
        すべてのコントロールを初期値にリセットするボタンです。
        button: ボタンには既定の動作がなく、押されても何も行いません。
        クライアントサイドスクリプトを要素のイベントに関連付けることで、
        イベントが発生したときに実行させます。

        value
        ボタンの初期値です。
        フォームデータと一緒に送信する際に、ボタンの name と関連付けられる値を定義します。
        この値は、フォームに送信する際にサーバーに引数として渡されます。
        """
        AUTOFOCUS = 'autofocus'
        AUTOCOMPLETE = 'autocomplete'
        DISABLED = 'disabled'
        FORM = 'form'
        FORMACTION = 'formaction'
        FORMENCTYPE = 'formenctype'
        FORMMETHOD = 'formmethod'
        FORMNOVALIDATE = 'formnovalidate'
        FORMTARGET = 'formtarget'
        NAME = 'name'
        TYPE = 'type'
        VALUE = 'value'

    class AutoComplete(object):
        """AutoComplete

        AutoComplete is a object.
        Responsibility:
        """
        ON = 'on'
        OFF = 'off'

    class FormTarget(object):
        """FormTarget

        FormTarget is a object.
        Responsibility:
        """
        SELF = '_selef'
        BLANK = '_blank'
        PARENT = '_parent'
        TOP = '_top'

    class Type(object):
        """Type

        Type is a object.
        Responsibility:
        """
        SUBMIT = 'submit'
        RESET = 'reset'
        BUTTON = 'button'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='button', tags=[], attrs=None, **kwargs)

    def enable_autofocus(self, ):
        """Enable autofocus.

        enable_autofocus()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.AUTOFOCUS, '')

    def disable_autofocus(self, ):
        """Disable autofocus.

        disable_autofocus()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.AUTOFOCUS in self.attrs:
            del self.attrs[self.AttributeNames.AUTOFOCUS]
        return self

    def is_autofocus(self, ):
        """Check autofocus enabled.

        is_autofocus()

        @Return: this instance

        @Error:
        """
        return self.AttributeNames.AUTOFOCUS in self.attrs

    def set_autocomplete(self, value):
        """Set autocomplete attribute value.

        set_autocomplete(value)

        @Arguments:
        - `value`: autocomplete attribute value
                   'on' or 'off'

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.AUTOCOMPLETE, value)

    def get_autocomplete(self, ):
        """Get autocomplete attribute value.

        get_autocomplete()

        @Return: autocomplete attribute value

        @Error:
        """
        return self.attrs.get(self.AttributeNames.AUTOCOMPLETE, None)

    def enable_autocomplete(self, ):
        """Enable autocomplete attribute value to On.

        enable_autocomplete()

        @Return: this instance

        @Error:
        """
        self.set_autocomplete(self.AutoComplete.ON)
        return self

    def disable_autocomplete(self, ):
        """Disable autocomplete attribute value to OFF.

        disable_autocomplete()

        @Return: this instance

        @Error:
        """
        self.set_autocomplete(self.AutoComplete.OFF)
        return self

    def remove_autocomplete(self, ):
        """Remove autocomplete attribute.

        remove_autocomplete()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.AUTOCOMPLETE in self.attrs:
            del self.attrs[self.AttributeNames.AUTOCOMPLETE]
        return self

    def disable_button(self, ):
        """Disable button as set disable attribute.

        disable_button()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.DISABLED in self.attrs:
            del self.attrs[self.AttributeNames.DISABLED]
        return self

    def enable_button(self, ):
        """Enable button as remove enable attribute.

        enable_button()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.DISABLED, '')

    def is_enable_button(self, ):
        """Check enabled button.

        is_enable_button()

        @Return: True if enable button

        @Error:
        """
        return self.AttributeNames.DISABLED not in self.attrs

    def set_form(self, value):
        """Set form.

        set_form(value)

        @Arguments:
        - `value`: form value as form id

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.FORM, value)

    def get_form(self, ):
        """Get form attribute value.

        get_form()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.FORM, None)

    def remove_form(self, ):
        """Remove form attribute.

        remove_form()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.FORM in self.attrs:
            del self.attrs[self.AttributeNames.FORM]
        return self

    def set_formaction(self, value):
        """Set formaction.

        set_formaction(value)

        @Arguments:
        - `value`: formaction attribute value.

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.FORMACTION, value)

    def get_formaction(self, ):
        """Get formaction attribute.

        get_formaction()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.FORMACTION, None)

    def remove_formaction(self, ):
        """Remove formaction attribute.

        remove_formaction()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.FORMACTION in self.attrs:
            del self.attrs[self.AttributeNames.FORMACTION]
        return self

    def set_formenctype(self, value):
        """Set formenctype.

        set_formaenctype(value)

        @Arguments:
        - `value`: formenctype attribute value.

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.FORMENCTYPE, value)

    def get_formenctype(self, ):
        """Get formenctype attribute.

        get_formenctype()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.FORMENCTYPE, None)

    def remove_formenctype(self, ):
        """Remove formenctype attribute.

        remove_formenctype()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.FORMENCTYPE in self.attrs:
            del self.attrs[self.AttributeNames.FORMENCTYPE]
        return self

    def set_formmethod(self, value):
        """Set formmethod.

        set_formmethod(value)

        @Arguments:
        - `value`: formmethod attribute value.

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.FORMMETHOD, value)

    def get_formmethod(self, ):
        """Get formmethod attribute.

        get_formmethod()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.FORMMETHOD, None)

    def remove_formmethod(self, ):
        """Remove formmethod attribute.

        remove_formmethod()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.FORMMETHOD in self.attrs:
            del self.attrs[self.AttributeNames.FORMMETHOD]
        return self

    def set_formtarget(self, value):
        """Set formtarget.

        set_formtarget(value)

        @Arguments:
        - `value`: formtarget attribute value.

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.FORMTARGET, value)

    def get_formtarget(self, ):
        """Get formtarget attribute.

        get_formtarget()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.FORMTARGET, None)

    def remove_formtarget(self, ):
        """Remove formtarget attribute.

        remove_formtarget()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.FORMTARGET in self.attrs:
            del self.attrs[self.AttributeNames.FORMTARGET]
        return self

    def set_name_attribute(self, value):
        """Set name.

        set_name_attribute(value)

        @Arguments:
        - `value`: name attribute value.

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.NAME, value)

    def get_name_attribute(self, ):
        """Get name attribute.

        get_name_attribute()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.NAME, None)

    def remove_name_attribute(self, ):
        """Remove name attribute.

        remove_name_attribute()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.NAME in self.attrs:
            del self.attrs[self.AttributeNames.NAME]
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

    def set_value(self, value):
        """Set value.

        set_value(value)

        @Arguments:
        - `value`: value attribute value.

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.VALUE, value)

    def get_value(self, ):
        """Get value attribute.

        get_value()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.VALUE, None)

    def remove_value(self, ):
        """Remove value attribute.

        remove_value()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.VALUE in self.attrs:
            del self.attrs[self.AttributeNames.VALUE]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# button.py ends here
