#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""tr -- tr tag

"""
from .html_tag import HtmlTag


class tr(HtmlTag):
    """tr

    tr is a HtmlTag.
    Responsibility:

    HTML の <tr> 要素は、表内でセルの行を定義します。
    行のセルは <td> (データセル) および <th> (見出しセル)
    要素をを混在させることができます。

    HTML の <tr> 要素は、表のひとつの行で構成される <tr>
    ブロックを内部に持つマークアップを明示します。
    行の内部で <th> 要素および <td> 要素が、
    それぞれ見出しやデータのセルを生成します。
    それぞれの列は、自身の列に配置されます。
    ユーザーエージェントは、それぞれの行のセルを別のセルの
    行セルとともにどのように列へ配置するかを決める、固有の規則に従います。

    セルをどのように列に収める (または列にまたがる) かを制御できるようにするため、
    <th> および <td> で colspan 属性をサポートします。
    これはセルの幅をいくつの列にするかを指定でき、既定値は 1 です。
    同様に、セルが複数の行にまたがることを示す rowspan 属性も使用できます。

    表を作成するとき、正しい表にするために少し経験が必要かもしれません。
    以下にいくつか例がありますが、さらに多くの例や詳しいチュートリアルは、
    ウェブ開発を学ぶエリアの HTML tables シリーズをご覧ください。
    表形式のデータを正しいレイアウトに整形するため、
    table 要素やその属性の使い方を学ぶことができます。

    属性
    この要素にはグローバル属性があります。
    使用を避けるべき非推奨の属性もいくつかありますが、
    古いコードを読む際は知っている必要があるでしょう。

    非推奨の属性
    以下の属性は依然としてブラウザーが実装していますが、
    すでに HTML 仕様に含まれていませんのでまったく動作しない、
    あるいは期待どおりに動作しない可能性があります。使用は避けるべきです。

    left
    各セルの中身を左側に揃えます。

    center
    中身をセルの左端と右端の間で中央揃えにします。

    right
    各セルの中身を右側に揃えます。

    justify
    テキストが各セルの幅全体を満たす (両端揃え) ように、
    テキスト内のホワイトスペースを広げます。

    char
    行内の各セルを、特定の文字に対して揃えます
    (この方法で設定された列内の各行は、その文字に対して揃えます)。
    これは char および charoff を使用して、揃える文字
    (数値データを揃える際の "." や "," が一般的です)
    および揃える文字に続く文字の数を指定します。
    この配置方法は、広くは対応されていませんでした。
    align の値が明示的に設定されていない場合は、親ノードの値を継承します。

    行内のセルで配置方法を指定するには、廃止された align
    属性の代わりに CSS の text-align プロパティで
    left, center, right, justify を指定してください。
    文字ベースの配置方法を適用するには、
    CSS の text-align プロパティに揃える文字 ("." や "," など) を
    設定してください。

    baseline
    テキストを可能な限りセルの下端に近づけますが、
    下端ではなく文字で使用するフォントの baseline に揃えます。
    文字がサイズ全体に渡る場合は、bottom と同じ効果になります。

    bottom
    テキストを可能な限りセルの下端に近づけて配置します。

    middle
    テキストをセルの中央部に置きます。

    top
    テキストを可能な限りセルの上端に近づけて配置します。
    valign 属性は廃止されたため、使用しないでください。代わりに
    CSS の vertical-align プロパティを使用してください。

    例
    <tr> 要素の使用例については、 <table> を参照してください。

    基本的な例
    これは、人名とクラブまたはサービスのさまざまな会員情報を載せる
    表を表示する簡単な例です。

    HTML
    この HTML は、表のもっとも基本的な構造を示します。
    グループ、複数の行や列にまたがるセル、タイトルはなく、
    明確にに似ているもののために表の構成要素の周りに線を生成する、
    もっとも基本的なスタイルだけがあります。

    表には4列（1列の見出しを含む）があるの行が4行（1行の見出しを含む）があります。
    表セクション要素は使用していません。
    代わりに、ブラウザーはそれらを自動的に定義できます。
    この次の例では <thead>, <tbody>, <tfoot> を追加します。
    """
    class AttributeNames(HtmlTag.AttributeNames):
        LEFT = 'left'
        CENTER = 'center'
        RIGHT = 'right'
        JUSTIFY = 'justify'
        CHAR = 'char'
        BASELINE = 'baseline'
        BOTTOM = 'bottom'
        MIDDLE = 'middle'
        TOP = 'top'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='tr', tags=[], attrs=None, **kwargs)

    def set_left(self, value):
        """Set left attibutes value.

        set_left(value)

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

    def set_center(self, value):
        """Set center attibutes value.

        set_center(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.CENTER, value)
        return self

    def get_center(self, ):
        """Get center attribute value.

        get_center()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.CENTER, None)

    def remove_center(self, ):
        """Remove center attribute value.

        remove_center()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.CENTER in self.attrs:
            del self.attrs[self.AttributeNames.CENTER]
        return self

    def set_right(self, value):
        """Set right attibutes value.

        set_right(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.RIGHT, value)
        return self

    def get_right(self, ):
        """Get right attribute value.

        get_right()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.RIGHT, None)

    def remove_right(self, ):
        """Remove right attribute value.

        remove_center()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.RIGHT in self.attrs:
            del self.attrs[self.AttributeNames.RIGHT]
        return self

    def set_justify(self, value):
        """Set justify attibutes value.

        set_justify(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.JUSTIFY, value)
        return self

    def get_justify(self, ):
        """Get justify attribute value.

        get_justify()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.JUSTIFY, None)

    def remove_justify(self, ):
        """Remove justify attribute value.

        remove_justify()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.JUSTIFY in self.attrs:
            del self.attrs[self.AttributeNames.JUSTIFY]
        return self

    def set_char(self, value):
        """Set char attibutes value.

        set_char(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.CHAR, value)
        return self

    def get_char(self, ):
        """Get char attribute value.

        get_char()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.CHAR, None)

    def remove_char(self, ):
        """Remove char attribute value.

        remove_char()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.CHAR in self.attrs:
            del self.attrs[self.AttributeNames.CHAR]
        return self

    def set_baseline(self, value):
        """Set baseline attibutes value.

        set_baseline(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.BASELINE, value)
        return self

    def get_baseline(self, ):
        """Get baseline attribute value.

        get_baseline()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.BASELINE, None)

    def remove_baseline(self, ):
        """Remove baseline attribute value.

        remove_baseline()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.BASELINE in self.attrs:
            del self.attrs[self.AttributeNames.BASELINE]
        return self

    def set_bottom(self, value):
        """Set bottom attibutes value.

        set_bottom(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.BOTTOM, value)
        return self

    def get_bottom(self, ):
        """Get bottom attribute value.

        get_bottom()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.BOTTOM, None)

    def remove_bottom(self, ):
        """Remove bottom attribute value.

        remove_bottom()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.BOTTOM in self.attrs:
            del self.attrs[self.AttributeNames.BOTTOM]
        return self

    def set_middle(self, value):
        """Set middle attibutes value.

        set_middle(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.MIDDLE, value)
        return self

    def get_middle(self, ):
        """Get middle attribute value.

        get_middle()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.MIDDLE, None)

    def remove_middle(self, ):
        """Remove middle attribute value.

        remove_middle()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.MIDDLE in self.attrs:
            del self.attrs[self.AttributeNames.MIDDLE]
        return self

    def set_top(self, value):
        """Set top attibutes value.

        set_top(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.TOP, value)
        return self

    def get_top(self, ):
        """Get top attribute value.

        get_top()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.TOP, None)

    def remove_top(self, ):
        """Remove top attribute value.

        remove_top()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.TOP in self.attrs:
            del self.attrs[self.AttributeNames.TOP]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# tr.py ends here
