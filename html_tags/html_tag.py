#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""html_tag -- html tag

"""
from .tag import Tag
from .attributes.only_one_attr_value import OnlyOneAttrValue


class HtmlTag(Tag):
    """HtmlTag

    HtmlTag is a Tag.
    Responsibility:
    """
    class AttributeNames(object):
        """AttributeNames

        AttributeNames is a object.
        Responsibility:

        accesskey グローバル属性は、現在の要素のショートカットキーを
        生成するためのヒントを与えます。 この属性は空白で区切った表示可能な文字
        (キーボードから生成できるアクセント付き文字やその他の文字を含む) から成ります。

        input や textarea に対して、iOS の Safari の英語入力モードで入力する際、
        最初の 1文字目を入力する際に入力パネルが自動的に大文字入力モードになることがあります。
        autocapitalize は、この機能を制御する際に用います。
        mode には下記のいずれかを指定します。
        off        :  自動大文字化機能をオフにします。
        none       :  自動大文字化機能をオフにします。
        on         :  自動大文字化機能をオンにします。
        sentences  : 文章毎に自動大文字化機能をオンにします。
        words      : 単語毎に自動大文字化機能をオンにします。
        characters : 文字毎に自動大文字化機能をオンにします。

        <input type="text" autocapitalize="off">

        class グローバル属性 は、要素のクラスを空白区切りで並べたリストです。
        クラスは CSS の クラスセレクター や JavaScript の
        DOM メソッド document.getElementsByClassName といった関数により、
        特定の要素を選択したり特定の要素にアクセスしたりすることを可能にします。

        この属性は、以下の値のうち一つを取る必要があります。
        true または 空文字列: 要素が編集可能であることを示す
        false: 要素は編集不可であることを示す
        この属性を設定しなかった場合の既定値は、親要素から継承された値です。
        この属性は列挙型であり、論理型ではありません。
        これは値 true、false または空文字列のいずれかを明示的に使用することが必須であり、
        <label contenteditable>Example Label</label>
        といった省略形は認められないということです。
        正しい使用法は <label contenteditable="true">Example Label</label> です。

        draggable は以下の値を取ることができます。

        true: 要素がドラッグ可能であることを示す
        false: 要素はドラッグ不可であることを示す
        この属性は列挙型であり、論理型ではありません。
        true または false の値が必須であり、
        <img draggable> のような省略形は認められません。
        正しい使用法は <img draggable="false"> です。

        この属性が設定されなかった場合の既定値は auto であり、
        ブラウザーの既定のドラッグ動作であることを意味します。
        テキストの選択範囲、画像、リンクのみがドラッグ可能です。
        他の要素では、ドラッグ＆ドロップできるようにするためには
        ondragstart イベントを設定する必要があります
        (こちらの包括的なサンプルにあるように)

        hidden 属性は、別の表現方法で表示することが正当であるはずのコンテンツを隠すために使用してはいけません。
        例えば、タブ付きダイアログでパネルを隠すために hidden 属性を使用するのは不適切です。
        これはタブ付きインターフェイスが、単に内容がはみ出ていることを示す表現の一種であり、
        スクロールバーを使用してひとつの大きなページにすべての
        フォームコントロールを表示するのと同等であるためです。
        同様に、ある表現方法からコンテンツを隠すためにこの属性を使用するのも不適切です。
        何かを隠した場合は、例えばスクリーンリーダーを含むすべての表現方法から隠されます。
        隠された要素は、隠されていない要素からリンクしないようにしてください。
        また、隠された要素の子孫要素は依然アクティブです。
        これは script 要素が実行可能、またフォーム要素が送信可能であるということです。
        例えば、 href 属性を使用して hidden 属性が設定された部分にリンクを張るのは不適切です。
        コンテンツが利用できないか無関係ならば、リンクする理由がないからです。
        しかし、 ARIA の aria-describedby 属性を使って隠された要素の記述を参照することは良いことです。
        記述を隠すことは、それ自身では役に立たないことを意味しますが、
        記述された要素から参照される特定の文脈に限っては有用であるように記述することができます。
        同様に、 canvas 要素に hidden 属性をつけたものはオフスクリーンバッファーとして
        グラフィックエンジンを記述することができますし、
        フォーム制御では hidden のフォーム要素をフォーム属性を使用して参照することができます。

        この属性の値は不伝導性の文字列です。
        つまり、ウェブ作者は人間が理解するための情報を伝えるために この情報を使用してはいけません。
        id の値にホワイトスペース文字 (空白やタブなど) を含めてはいけません。
        ブラウザーはホワイトスペース文字を含む不適合な ID を、
        ホワイトスペース文字が ID の一部であるかのように扱います。
        空白区切りで並べた値を受け入れる class 属性とは対照的に、
        要素は ID の値をひとつだけ持つことができます。

        ASCII 英文字、数字、'_'、'-'、'.' 以外の文字は HTML 4 で許容されていなかったため、
        使用した場合に互換性の問題を引き起こす可能性があります。
        この制約は HTML5 で外されましたが、互換性のために ID はこれらの文字で始めるようにしましょう。

        itemprop グローバル属性は、アイテムにプロパティを追加するために使用します。
        すべての HTML 要素に itemprop 属性を設定することができ、
        itemprop は名前と値の組み合わせで構成されます。
        名前と値の組み合わせはプロパティと呼ばれ、
        1つまたは複数のプロパティでアイテムを構成します。
        プロパティ値は文字列又は URL のどちらかで、
        <audio>, <embed>, <iframe>, <img>, <link>, <object>, <source> , <track>, <video> など、
        広範にわたる要素と関連付けすることができます。

        lang グローバル属性は、要素の言語の定義に使われます。
        編集不可の要素では記述されている言語、
        また、編集可能な要素ではユーザーが書き込むべき言語です。
        属性には単一の「言語タグ」を Tags for Identifying Languages (BCP47)
        で定義された書式で持ちます。

        spellcheck
        要素でスペルミスのチェックを行うかを定義する列挙型属性です。
        以下の値を使用できます。

        true: 可能であればその要素でスペルチェックを行うことを示す
        false: その要素でスペルチェックを行わないことを示す
        この属性を設定しなかった場合の既定値は、要素の種類やブラウザーによって定義されます。
        既定値は継承、つまりもっとも近い祖先要素の spellcheck が true である場合にのみ、
        自身もスペルチェックを受けることがあります。

        この属性は列挙型であり、論理型ではありません。
        これは値 true または false のいずれかを明示的に使用することが必須であり、
        <label spellcheck>Example Label</label> といった省略形は認められないということです。
        正しい使用法は <label spellcheck="true">Example Label</label> です。

        この属性は単に、ブラウザーに対する助言です。
        ブラウザーがスペルチェックを有効にすることを求められてはいません。
        一般的に編集不可能な要素は、 spellcheck 属性を true に設定してブラウザーが
        スペルチェックに対応していても、スペルチェックされません。
        この属性の既定値は、ブラウザーおよび要素により異なります。

        style グローバル属性は、要素に適用する CSS スタイル宣言を包含します。
        なお、スタイルは別のファイルで定義することが推奨されます。
        この属性と <style> 要素の主な用途は、例えばテストのために、
        すばやくスタイルを適用できるようにすることです。

        tabindex グローバル属性は、要素が入力フォーカスを持てることと、
        キーボードの順次ナビゲーション (ふつうは名前の由来である Tab キーによる) に
        加わるかどうか、どの位置に加わるかを示します。

        値としては整数値を受け付け、値によって次のような様々な結果になります。

        負の数 (ふつう tabindex="-1") は、その要素がキーボードの順次ナビゲーションでは到達できませんが、
        JavaScript や視覚的にフォーカスを持つことができるという意味です。
        これは主に、 JavaScript で操作可能なウィジェットを作成するのに有用です。
        負の値はオフスクリーンのコンテンツで特定のイベントにより現れる場合に有用です。
        ユーザーは負の tabindex が付いた要素に、キーボードを使用して
        フォーカスを与えることはできませんが、スクリプトは focus() メソッドを呼び出すことで
        フォーカスを与えることはできます。

        tabindex="0" は、要素がキーボードの順次ナビゲーションでフォーカスを持つことが
        可能ですが、その順序は文書のソース内の順序で決定されることを表します。
        正の数は、要素がキーボードの順次ナビゲーションでフォーカスを持つことが可能であり、
        その順序は数値で定義されることを表します。
        つまり、 tabindex="4" は tabindex="5" よりも前にフォーカスが来ますが、
        tabindex="3" よりも後だということです。複数の要素に同じ正の数の tabindex が
        指定された場合は、文書のソース内の互いの位置に従った順序になります。
        tabindex の最大値は32767です。指定されなかった場合、既定値の0を取ります。
        tabindex の値に0よりも大きな値を使用することは避けてください。
        そうすると、支援技術に頼っている人がページコンテンツを移動したり操作したりすることが難しくなります。
        代わりに、論理的な順序で要素を並べて文書を書いてください。

        tabindex 属性を<div> に設定する場合は、子のコンテンツにも tabindex を
        設定しなければ、矢印キーを使用して子のコンテンツをスクロールできなくなります。
        tabindex のスクロール効果を理解するには、こちらの fiddle を確認してください。

        <iframe> 要素の支援技術のためのラベル付け
        プログラム的に関連付けれた<input> 要素のためのラベルを、実際の <label> の代替として提供
        データ表内のコントロールのラベル付け
        title 属性は <link>, <abbr>, <input>, <menuitem> の各要素において、
        追加の意味を持ちます。
        """
        ACCESSKEY = 'accesskey'
        AUTOCAPITALIZE = 'autocapitalize'
        CLASS = 'class'
        CONTENTEDITABLE = 'contenteditable'
        DRAGGABLE = 'draggable'
        HIDDEN = 'hidden'
        ID = 'id'
        ITEMPROP = 'itemprop'
        LANG = 'lang'
        SPELLCHECK = 'spellcheck'
        STYLE = 'style'
        TABINDEX = 'tabindex'
        TITLE = 'title'

    class AutoCapitalize(object):
        """AutoCapitalize

        AutoCapitalize is a object.
        Responsibility:
        """
        OFF = 'off'
        """自動大文字化機能をオフにします。"""
        NONE = 'none'
        """自動大文字化機能をオフにします。"""
        ON = 'on'
        """自動大文字化機能をオンにします。"""
        SENTENCES = 'sentences'
        """文章毎に自動大文字化機能をオンにします。"""
        WORDS = 'words'
        """単語毎に自動大文字化機能をオンにします。"""
        CHARACTERS = 'characters'
        """文字毎に自動大文字化機能をオンにします。"""

    class ContentEditable(object):
        """ContentEditable

        ContentEditable is a object.
        Responsibility:
        """
        TRUE = 'true'
        FALSE = 'false'

    class Draggable(object):
        """Draggable

        Draggable is a object.
        Responsibility:
        """
        TRUE = 'true'
        FALSE = 'false'

    class Spellcheck(object):
        """Spellcheck

        Spellcheck is a object.
        Responsibility:
        """
        TRUE = 'true'
        FALSE = 'false'

    def _set_one_attribute(self, name, value):
        """Set one attribute.

        _set_one_attribute(name, value)

        @Arguments:
        - `name`: attribute name
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        if name not in self.attrs:
            self.attrs[name] = OnlyOneAttrValue()
        if not isinstance(self.attrs[name], (OnlyOneAttrValue, )):
            self.attrs[name] = OnlyOneAttrValue()
        self.attrs[name].set(value)
        return self

    def get_accesskey(self, ):
        """Get accesskey attribute values.

        get_accesskey()

        @Return: attribute value.

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ACCESSKEY, None)

    def append_accesskey(self, key):
        """Append Accesskey.

        append_accesskey(key)

        @Arguments:
        - `key`: accesskey

        @Return: this instance.

        @Error:
        """
        self.append_attribute_value(self.AttributeNames.ACCESSKEY, key)
        return self

    def remove_accesskey(self, key):
        """Remove accesskey.

        remove_accesskey(key)

        @Arguments:
        - `key`: accesskey

        @Return: this instance.

        @Error:
        """
        self.remove_attribute_value(self.AttributeNames.ACCESSKEY, key)
        return self

    def clear_accesskeys(self, ):
        """Clear accesskeys.

        clear_accesskeys()

        @Return: this instance.

        @Error:
        """
        self.clear_attribute_value(self.AttributeNames.ACCESSKEY)
        return self

    def delete_accesskey(self, ):
        """Delete accesskeys from attribute.

        delete_accesskey()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.ACCESSKEY in self.attrs:
            del self.attrs[self.AttributeNames.ACCESSKEY]
        return self

    def contains_accesskey(self, key):
        """Contains accesskey.

        contains_accesskey(key)

        @Arguments:
        - `key`: accesskey

        @Return: Return True if exists. Else False.

        @Error:
        """
        return self.contains_attribute_value(self.AttributeNames.ACCESSKEY, key)

    def set_autocapitalize(self, value):
        """Set autocapitalize value.

        set_autocapitalize(value)

        @Arguments:
        - `value`: auto capitalize value.

        AutoCapitalize
          off:        自動大文字化機能をオフにします。
          none:       自動大文字化機能をオフにします。
          on:         自動大文字化機能をオンにします。
          sentences:  文章毎に自動大文字化機能をオンにします。
          words:      単語毎に自動大文字化機能をオンにします。
          characters: 文字毎に自動大文字化機能をオンにします。

        <input type="text" autocapitalize="off">

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.AUTOCAPITALIZE, value)

    def remove_autocapitalize(self, ):
        """remove autocapitalize.

        remove_autocapitalize()

        @Return: this instance.

        @Error:
        """
        if self.AttributeNames.AUTOCAPITALIZE in self.attrs:
            del self.attrs[self.AttributeNames.AUTOCAPITALIZE]
        return self

    def get_autocapitalize(self, ):
        """Get autocapitalize.

        get_autocapitalize()

        @Return:

        @Error:
        """
        if self.AttributeNames.AUTOCAPITALIZE not in self.attrs:
            return None
        return str(self.attrs[self.AttributeNames.AUTOCAPITALIZE])

    def get_classes(self, ):
        """Get class attribute values.

        get_classes()

        @Return:

        @Error:
        """
        return self.attrs.get(self.AttributeNames.CLASS, None)

    def append_class(self, klass):
        """Append class values.

        append_class(klass)

        @Arguments:
        - `klass`:

        @Return: this instance

        @Error:
        """
        self.attrs.append_value(self.AttributeNames.CLASS, klass)
        return self

    def remove_class(self, klass):
        """Remove class value.

        remove_class(klass)

        @Arguments:
        - `klass`: class

        @Return: this instance

        @Error:
        """
        self.attrs.remove_value(self.AttributeNames.CLASS, klass)
        return self

    def clear_classes(self, ):
        """Clear classes.

        clear_classes()

        @Return: this instance

        @Error:
        """
        self.clear_attribute_value(self.AttributeNames.CLASS)
        return self

    def delete_classes(self, ):
        """Delete classes.

        delete_classes()

        @Return: this instance

        @Error:
        """
        self.set_attribute_none(self.AttributeNames.CLASS)
        return self

    def set_contenteditable(self, value):
        """Set contenteditable value.

        set_contenteditable(value)

        @Arguments:
        - `value`: set contenteditable value. true or false

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.CONTENTEDITABLE, value)

    def enable_contenteditable(self, ):
        """set true contenteditable attribute value.

        enable_contenteditable()

        @Return: this instance.

        @Error:
        """
        self.set_contenteditable(self.ContentEditable.TRUE)
        return self

    def disable_contenteditable(self, ):
        """Set false contenteditable attribute value.

        disable_contenteditable()

        @Return: this instance.

        @Error:
        """
        self.set_contenteditable(self.ContentEditable.FALSE)
        return self

    def remove_contenteditable(self, ):
        """Remove contenteditable attribute.

        remove_contenteditable()

        @Return: this instance.

        @Error:
        """
        if self.AttributeNames.CONTENTEDITABLE in self.attrs:
            del self.attrs[self.AttributeNames.CONTENTEDITABLE]
        return self

    def get_contenteditable(self, ):
        """Get contenteditable value.

        get_contenteditable()

        @Return: this instance.

        @Error:
        """
        if self.AttributeNames.CONTENTEDITABLE not in self.attrs:
            return None
        return str(self.attrs[self.AttributeNames.CONTENTEDITABLE])

    def set_draggable(self, value):
        """Set draggable value.

        set_draggable(value)

        @Arguments:
        - `value`: set draggable value. true or false

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.DRAGGABLE, value)

    def enable_draggable(self, ):
        """set true draggable attribute value.

        enable_draggable()

        @Return: this instance.

        @Error:
        """
        self.set_draggable(self.Draggable.TRUE)
        return self

    def disable_draggable(self, ):
        """Set false draggable attribute value.

        disable_draggable()

        @Return: this instance.

        @Error:
        """
        self.set_draggable(self.ContentEditable.FALSE)
        return self

    def remove_draggable(self, ):
        """Remove draggable attribute.

        remove_draggable()

        @Return: this instance.

        @Error:
        """
        del self.attrs[self.AttributeNames.DRAGGABLE]
        return self

    def get_draggable(self, ):
        """Get draggable value.

        get_draggable()

        @Return: this instance.

        @Error:
        """
        if self.AttributeNames.DRAGGABLE not in self.attrs:
            return None
        return str(self.attrs[self.AttributeNames.DRAGGABLE])

    def set_hidden(self, ):
        """Set hidden attribute.

        set_hidden()

        @Return: this instance

        @Error:
        """
        self.attrs.set_none(self.AttributeNames.HIDDEN)
        return self

    def remove_hidden(self, ):
        """Remove hidden attribute.

        remove_hidden()

        @Return: this instance

        @Error:
        """
        self.attrs.remove_attribute(self.AttributeNames.HIDDEN)
        return self

    def has_hidden(self, ):
        """Check has hidden attribute.

        has_hidden()

        @Return: (bool) if exists hidden attribute

        @Error:
        """
        return self.AttributeNames.HIDDEN in self.attrs

    def set_id(self, value):
        """Set id attribute.

        set_id(value)

        @Arguments:
        - `value`: id value

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.ID, value)

    def remove_id(self, ):
        """Remove ID attribute.

        remove_id()

        @Return: this instance.

        @Error:
        """
        self.attrs.remove_attribute(self.AttributeNames.ID)
        return self

    def get_id(self, ):
        """Get id attribute.

        get_id()

        @Return: (str) id value if exists else None.

        @Error:
        """
        if self.AttributeNames.ID not in self.attrs:
            return None
        return str(self.attrs[self.AttributeNames.ID])

    def append_itemprop(self, value):
        """Append itemprop values.

        append_itemprop(value)

        @Arguments:
        - `value`: value of attribute

        @Return: this instance

        @Error:
        """
        self.attrs.append_value(self.AttributeNames.ITEMPROP, value)
        return self

    def delete_itemprop(self, ):
        """Delete itemprop.

        delete_classes()

        @Return: this instance

        @Error:
        """
        self.set_attribute_none(self.AttributeNames.ITEMPROP)
        return self

    def get_itemprop(self, ):
        """Get itemprop attribute.

        get_itemprop()

        @Return: Attribute Value

        @Error:
        """
        return self.attrs.get(self.AttributeNames.ITEMPROP, None)

    def set_lang(self, value):
        """Set Language.

        set_lang(value)

        @Arguments:
        - `value`: lang value.

        <p lang="en-GB">This paragraph is defined as British English.</p>

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.LANG, value)

    def remove_lang(self, ):
        """Remove lang.

        remove_lang()

        @Return: this instance.

        @Error:
        """
        if self.AttributeNames.LANG in self.attrs:
            del self.attrs[self.AttributeNames.LANG]
        return self

    def get_lang(self, ):
        """Get lang.

        get_lang()

        @Return: Language value

        @Error:
        """
        if self.AttributeNames.LANG not in self.attrs:
            return None
        return str(self.attrs[self.AttributeNames.LANG])

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

    def get_style(self, ):
        """Get style attribute value.

        get_style()

        @Return: attribute value or None

        @Error:
        """
        raise NotImplemented()
        return self.attrs.get(self.AttributeNames.STYLE, None)

    def append_style(self, value):
        """Append style values.

        append_style(value)

        @Arguments:
        - `value`: style attribute value.
        like this "margin: 15px;"

        @Return: this instance

        @Error:
        """
        raise NotImplemented()
        self.attrs.append_value(self.AttributeNames.STYLE, value)
        return self

    def remove_style(self, value):
        """Remove style value.

        remove_style(value)

        @Arguments:
        - `value`: style attribute value

        @Return: this instance

        @Error:
        """
        raise NotImplemented()
        self.attrs.remove_value(value)
        return self

    def clear_styles(self, ):
        """Clear styles.

        clear_styles()

        @Return: this instance

        @Error:
        """
        raise NotImplemented()
        self.clear_attribute_value(self.AttributeNames.STYLE)
        return self

    def delete_style(self, ):
        """Delete style attribute from tag.

        delete_style()

        @Return: this instance

        @Error:
        """
        raise NotImplemented()
        self.set_attribute_none(self.AttributeNames.STYLE)
        return self

    def set_tabindex(self, value):
        """Set tabindex attribute value.

        set_tabindex(value)

        @Arguments:
        - `value`: tabindex value.

        <input type="text" tabindex="1">

        @Return: this instance.

        @Error:
        ValueError: value must be int or blank string and lower than 32767.
        """
        if value == "":
            return self._set_one_attribute(self.AttributeNames.TABINDEX, value)
        value = int(value)
        if 32767 < value:
            raise ValueError('tabindex value must be lower than 32767')
        return self._set_one_attribute(self.AttributeNames.TABINDEX, str(value))

    def remove_tabindex(self, ):
        """Remove tabindex attribute.

        remove_tabindex()

        @Return: this instance.

        @Error:
        """
        if self.AttributeNames.TABINDEX in self.attrs:
            del self.attrs[self.AttributeNames.TABINDEX]
        return self

    def get_tabindex(self, ):
        """Get tabindex attribute value.

        get_tabindex()

        @Return:

        @Error:
        """
        if self.AttributeNames.TABINDEX not in self.attrs:
            return None
        return str(self.attrs[self.AttributeNames.TABINDEX])

    def set_title(self, value):
        """Set title attribute value.

        set_title(value)

        @Arguments:
        - `value`: title value.

        <input type="text" title="this is title">

        @Return: this instance.

        @Error:
        """
        return self._set_one_attribute(self.AttributeNames.TITLE, value)

    def remove_title(self, ):
        """Remove title attribute.

        remove_title()

        @Return: this instance.

        @Error:
        """
        if self.AttributeNames.TITLE in self.attrs:
            del self.attrs[self.AttributeNames.TITLE]
        return self

    def get_title(self, ):
        """Get title attribute value.

        get_title()

        @Return:

        @Error:
        """
        if self.AttributeNames.TITLE not in self.attrs:
            return None
        return str(self.attrs[self.AttributeNames.TITLE])



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# html_tag.py ends here
