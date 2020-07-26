#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""time -- time tag

"""
from .html_tag import HtmlTag


class Time(HtmlTag):
    """Time

    Time is a HtmlTag.
    Responsibility:

    HTML の <time> 要素は、特定の時の区間を表します。
    datetime 属性を使用して、機械可読な形式の日付を記述することができ、
    検索エンジンの結果を改善したりリマインダーなどの独自機能に
    使用したりすることができます。

    次のうちの一つを表します。

    24時間制の時刻
    グレゴリオ暦の正確な日付 (時刻やタイムゾーンを伴うことも可能)
    妥当な期間

    コンテンツカテゴリ	フローコンテンツ, 記述コンテンツ, 知覚可能コンテンツ。
    許可されている内容	記述コンテンツ
    タグの省略	不可。開始と終了タグの両方が必要。
    許可されている親要素	記述コンテンツを受け入れるすべての要素
    許可されている ARIA ロール	すべて
    DOM インターフェイス	HTMLTimeElement

    属性
    他のすべての HTML 要素と同様に、この要素はグローバル属性に対応しています。

    datetime
    この属性は要素の日付や時刻を表し、下記に示す書式のうちの一つでなければなりません。
    使用上のメモ
    この要素は、機械可読な形式で日付や時刻を表現するためのものです。
    例えばユーザーエージェントが、ユーザーのカレンダーにイベントの
    予定情報を提供することに役立てることができます。

    この要素はグレゴリオ暦導入前の日付に対して使用するべきではありません
    (日付の計算で混乱するため)。

    datetime 値 (機械可読な日時の値) は要素の datetime 属性の値であり、
    正しい書式 (下記参照) でなければなりません。
    要素に datetime 属性がない場合、子孫要素を持ってはならず、
    datetime 値が要素のテキストの内容になります。

    妥当な年の文字列
    2011
    妥当な月の文字列
    2011-11
    妥当な日付の文字列
    2011-11-18
    年のない妥当な日付の文字列
    11-18
    妥当な週の文字列
    2011-W47
    妥当な時刻の文字列
    14:54
    14:54:39
    14:54:39.929
    妥当なローカル日時の文字列
    2011-11-18T14:54:39.929
    2011-11-18 14:54:39.929
    妥当なグローバル日時の文字列
    2011-11-18T14:54:39.929Z
    2011-11-18T14:54:39.929-0400
    2011-11-18T14:54:39.929-04:00
    2011-11-18 14:54:39.929Z
    2011-11-18 14:54:39.929-0400
    2011-11-18 14:54:39.929-04:00
    妥当な期間の文字列
    PT4H18M3S
    """
    class AttributeNames(HtmlTag.AttributeNames):
        DATETIME = 'datetime'

    def __init__(self, tags=[], attrs=None, **kwargs):
        super(HtmlTag, self).__init__(name='time', tags=[], attrs=None, **kwargs)

    def set_datetime(self, value):
        """Set datetime attibutes value.

        set_datetime(value)

        @Arguments:
        - `value`: attribute value

        @Return: this instance

        @Error:
        """
        self._set_one_attribute(self.AttributeNames.DATETIME, value)
        return self

    def get_datetime(self, ):
        """Get datetime attribute value.

        get_datetime()

        @Return: this instance

        @Error:
        """
        return self.attrs.get(self.AttributeNames.DATETIME, None)

    def remove_datetime(self, ):
        """Remove datetime attribute value.

        remove_datetime()

        @Return: this instance

        @Error:
        """
        if self.AttributeNames.DATETIME in self.attrs:
            del self.attrs[self.AttributeNames.DATETIME]
        return self



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# time.py ends here
