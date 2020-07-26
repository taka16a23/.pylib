#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""textarea -- textarea tag

"""
from .html_tag import HtmlTag


class TextArea(HtmlTag):
    """TextArea

    TextArea is a HtmlTag.
    Responsibility:

    HTML の <textarea> 要素は、複数行のプレーンテキスト編集コントロールを表し、
    レビューのコメントやお問い合わせフォーム等のように、
    ユーザーが大量の自由記述テキストを入力できるようにするときに便利です。

    上記の例では <textarea> の様々な機能を紹介しています。
    最初の例はもっとも単純な使い方で、アクセシビリティのために <textarea> を
    <label> 要素に結び付けるための id 属性と、
    フォームが送信された時にサーバに送信された関連データポイントの名前を設定する
    name 属性とともに、下記に説明する rows および cols 属性を伴っています。

    それ以外の例 (下記参照) は、より複雑な機能をいくつか示しています。

    rows および cols 属性で、 <textarea> が取る正確な寸法を指定することができます。
    ブラウザーの既定値が様々なので、これらを設定するのは一貫性の上で良い考えです。
    maxlength は <textarea> に含めることができる最大文字数を指定します。
    また、 minlength 属性を使用して有効とみなされる最小文字数を設定したり、
    required 属性を使用して空欄の場合に <textarea> が
    送信されないように指定することもできます。
    これによって <textarea> に他のフォーム要素よりも基本的ながら、
    単純な検証を行うことができます。
    (例えば、 <input> 要素で使用できる
    pattern 属性を使用して、正規表現による検証を行ったりすることはできません。)
    wrap はテキストが <textarea> の端まで達した時の折り返しの動作を指定します。
    <textarea> の既定の内容を入れたい場合は、開始タグと終了タグの間に入れます。
    <textarea> は value 属性には対応していません。
    <textarea> 要素は他にも、 autocomplete, autofocus, disabled,
    placeholder, readonly, required などのフォームの
    <input> と共通の属性をいくつか受け付けます。

    autocomplete
    この属性は、コントロールの値をブラウザーが自動的に補完してよいかを示します。以下の値を指定できます。
    off: ユーザーはフォームを使用するたびにフィールドへ値を明示的に入力しなければならないか、ドキュメントが独自の自動補完を提供します。ブラウザーは入力内容の自動補完を行いません。
    on: ブラウザーはユーザーが以前入力した値を元に、値の自動補完を行うことができます。
    <textarea> 要素で autocomplete 属性を指定していない場合は、ブラウザーは <textarea> 要素のフォームオーナーの autocomplete 属性の値を使用します。フォームオーナーは当該 <textarea> 要素が子孫になっている <form> 要素か、textarea 要素の form 属性で id を指定されている form 要素です。詳しくは、<form> 要素の autocomplete 属性をご覧ください。

    autofocus
    この論理属性で、ユーザーが別のコントロールに入力するなどして変更しない限り、ページ読み込み時にフォームコントロールがフォーカスを持つべきであることを指定できます。文書中のフォーム関連要素のうちのひとつだけに、この属性を指定することができます。値は、属性名と同じ autofocus のみ指定可能です。

    cols
    平均的な文字幅による、テキストコントロールの外見上の幅です。
    この属性を指定する場合は、正の整数を与えなければなりません。
    指定しない場合のデフォルト値は 20 です (HTML5)。

    disabled
    この真偽値属性は、ユーザーがそのコントロールを利用できないことを示します。(もしこの属性が指定されていない場合、コントロールはその設定を親要素、例えば fieldset 要素から継承します。もし親要素に disabled 属性を持つものがなければ、そのコントロールは利用可能です。)

    form
    <textarea> 要素が関連づけられた form 要素 (フォームオーナー) です。属性値は、同じドキュメント内の form 要素の id としなければなりません。この属性を指定しない場合は、<textarea> 要素を form 要素の子要素として配置しなければなりません。この属性により、<textarea> 要素を form 要素の子孫としてだけではなく、同一文書のどこにでも配置できるようになりました。

    maxlength
    ユーザーが入力可能な文字 (Unicode コードポイント) の最大数です。この属性を指定しない場合、ユーザーは無制限に文字を入力可能です。

    minlength
    ユーザーが入力しなければならない最小文字数 (Unicode コードポイント) です。

    name
    コントロールの名前です。

    placeholder
    コントロールに何を入力できるかに関する、ユーザーへの助言です。プレイスホルダーのテキスト内にあるキャリッジリターンやラインフィードは、ヒントを表示する際に改行として扱わなければなりません。
    メモ: プレイスホルダーはフォームに入力されるべきデータの種類の例を示すためだけに使用してください。入力欄に関連付けられた <label> 要素の代わりとして使用しないでください。全体的な説明は、ラベルとプレイスホルダー in <input>: 入力欄 (フォーム入力) 要素を参照してください。

    readonly
    この論理属性は、ユーザーがコントロールの値を変更できないことを示します。disabled 属性とは異なり、readonly 属性はユーザーがコントロールをクリックしたり選択することを妨げません。読み取り専用のコントロールの値は、フォームとともに送信可能です。

    required
    この属性は、フォームを送信する前に値を入力しなければならないことを示します。

    rows
    コントロールで見ることが可能なテキストの行数です。

    spellcheck
    <textarea> がブラウザーや OS に依存したスペルチェックを行うかどうかを指定します。以下の値が使用できます。
    true: 要素でスペルや文法チェックを行う必要があることを示します。
    default : 要素は既定の動作、おそらく親要素の spellcheck 値によって動作することを示します。
    false : 要素でスペルチェックを行うべきではないことを示します。
    wrap
    テキストの折り返しの制御法を示します。以下の値を指定可能です。
    hard : 各行の長さがコントロールの幅を超えないように、ブラウザーが自動的に改行 (CR+LF) を挿入します。cols 属性を指定しなければなりません。
    soft : ブラウザーは値に含まれる改行 (CR+LF のペア) をすべて維持しますが、改行の付加は行いません。
    off : soft に似ていますが外観を white-space: pre に変更しますので、cols を超えた部分は折り返されず、水平方向にスクロール可能になります。
    この属性を指定しない場合の既定値は soft です。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        AUTOCOMPLETE = 'autocomplete'
        AUTOFOCUS = 'autofocus'
        COLS = 'cols'
        DISABLED = 'disabled'
        FORM = 'form'
        MAXLENGTH = 'maxlength'
        MINLENGTH = 'minlength'
        NAME = 'name'
        PLACEHOLDER = 'placeholder'
        READONLY = 'readonly'
        REQUIRED = 'required'
        ROWS = 'rows'
        SPELLCHECK = 'spellcheck'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='textarea', tags=[], attrs=None, **kwargs)

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

    def set_cols(self, value):
        """Set cols attibutes value.

        set_cols(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.COLS, value)
        return self

    def get_cols(self, ):
        """Get cols attribute value.

        get_cols()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.COLS, None)

    def remove_cols(self, ):
        """Remove cols attribute value.

        remove_cols()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.COLS in self.attrs:
            del self.attrs[self.AttributeNames.COLS]
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

    def set_maxlength(self, value):
        """Set maxlength.

        set_maxlength(value)

        @Arguments:
        - `value`: maxlength value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.MAXLENGTH, value)

    def get_maxlength(self, ):
        """Get maxlength attribute value.

        get_maxlength()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.MAXLENGTH, None)

    def remove_maxlength(self, ):
        """Remove maxlength attribute.

        remove_maxlength()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.MAXLENGTH in self.attrs:
            del self.attrs[self.AttributeNames.MAXLENGTH]
        return self

    def set_minlength(self, value):
        """Set minlength.

        set_minlength(value)

        @Arguments:
        - `value`: minlength value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.MINLENGTH, value)

    def get_minlength(self, ):
        """Get minlength attribute value.

        get_minlength()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.MINLENGTH, None)

    def remove_minlength(self, ):
        """Remove minlength attribute.

        remove_minlength()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.MINLENGTH in self.attrs:
            del self.attrs[self.AttributeNames.MINLENGTH]
        return self

    def set_name(self, value):
        """Set name.

        set_name(value)

        @Arguments:
        - `value`: name value

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

    def set_placeholder(self, value):
        """Set placeholder.

        set_placeholder(value)

        @Arguments:
        - `value`: placeholder value

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.PLACEHOLDER, value)

    def get_placeholder(self, ):
        """Get placeholder attribute value.

        get_placeholder()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.PLACEHOLDER, None)

    def remove_placeholder(self, ):
        """Remove placeholder attribute.

        remove_placeholder()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.PLACEHOLDER in self.attrs:
            del self.attrs[self.AttributeNames.PLACEHOLDER]
        return self

    def set_readonly(self, ):
        """Set readonly.

        set_readonly()

        @Return: this instance

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.READONLY, None)

    def remove_readonly(self, ):
        """Remove readonly.

        remove_readonly()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.READONLY in self.attrs:
            del self.attrs[self.AttributeNames.READONLY]
        return self

    def is_readonly(self, ):
        """Check readonly enabled.

        is_readonly()

        @Return: this instance

        @Error:
        """
        return self.AttributeNames.READONLY in self.attrs

    def set_required(self, ):
        """Set required attribute.

        disable_required()

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

    def set_rows(self, value):
        """Set rows attibutes value.

        set_rows(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.ROWS, value)
        return self

    def get_rows(self, ):
        """Get rows attribute value.

        get_rows()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ROWS, None)

    def remove_rows(self, ):
        """Remove rows attribute value.

        remove_rows()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ROWS in self.attrs:
            del self.attrs[self.AttributeNames.ROWS]
        return self

    def set_spellcheck(self, value):
        """Set spellcheck value.

        set_spellcheck(value)

        @Arguments:
        - `value`: set spellcheck value. true or false

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.SPELLCHECK, value)

    def enable_spellcheck(self, ):
        """set true spellcheck attribute value.

        enable_spellcheck()

        @Return: this instance.

        @Error:
        """
        self.set_spellcheck(self.Spellcheck.TRUE)
        return self

    def disable_spellcheck(self, ):
        """Set false spellcheck attribute value.

        disable_spellcheck()

        @Return: this instance.

        @Error:
        """
        self.set_spellcheck(self.Spellcheck.FALSE)
        return self

    def remove_spellcheck(self, ):
        """Remove spellcheck attribute.

        remove_spellcheck()

        @Return: this instance.

        @Error:
        """
        if self.AttributeNames.SPELLCHECK in self.attrs:
            del self.attrs[self.AttributeNames.SPELLCHECK]
        return self

    def get_spellcheck(self, ):
        """Get Spellcheck value.

        get_spellcheck()

        @Return: this instance.

        @Error:
        """
        if self.AttributeNames.SPELLCHECK not in self.attrs:
            return None
        return str(self.attrs[self.AttributeNames.SPELLCHECK])



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# textarea.py ends here
