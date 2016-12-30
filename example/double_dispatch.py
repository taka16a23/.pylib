#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""double_dispatch -- DESCRIPTION

# From Wiki
たとえば、以下のような状況でダブルディスパッチを活用することができる。
二項演算子 ベクトル×行列、スカラ×ベクトル、など、ダブルディスパッチを活用する余地は大きい。
適応的衝突判定アルゴリズム では、通例物体により異なる方法で衝突を判定する必要がある。典型的な例では、ゲーム開発環境で、宇宙船と小惑星の衝突と、宇宙船と宇宙ステーションの衝突とは異なる方法で計算される。
塗りつぶしアルゴリズム 重なる可能性のある 2次元スプライトの描画の際には、スプライトの重なり部分を異なった方法で描画する必要がある。
人事管理 システムでは、様々な種類の仕事を様々な種類の作業者に割り当てる。たとえば、経理担当者の型を持つオブジェクトが技術の型を持つ仕事に割り当てられた場合、schedule アルゴリズムは割り当てを拒絶する。
イベント処理 では、イベントの型とイベントを受け付けるオブジェトの種類に応じて適切な処理ルーチンを呼び出す必要がある。



Double Dispatch をじゃんけんで

>>> goo=Goo()
>>> choki=Choki()
>>> paa=Paa()
>>> goo.fight(choki)
<JankenResult.Win: 1>
>>> goo.fight(paa)
<JankenResult.Lose: 2>

"""
from abc import ABCMeta, abstractmethod
from enum import Enum


JANKENRESULT = Enum('JankenResult', 'Win Lose Draw')


class Hand(object):
    """Hand

    Hand is a object.
    Responsibility:
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def fight(self, hand):
        """SUMMARY

        fight(hand)

        @Arguments:
        - `hand`:

        @Return:

        @Error:
        """

    @abstractmethod
    def from_goo(self, oponent):
        """SUMMARY

        from_goo(oponent)

        @Arguments:
        - `oponent`:

        @Return:

        @Error:
        """

    @abstractmethod
    def from_choki(self, oponent):
        """SUMMARY

        from_choki(oponent)

        @Arguments:
        - `oponent`:

        @Return:

        @Error:
        """

    @abstractmethod
    def from_paa(self, oponent):
        """SUMMARY

        from_paa(oponent)

        @Arguments:
        - `oponent`:

        @Return:

        @Error:
        """


class Goo(Hand):
    """Goo

    Goo is a Hand.
    Responsibility:
    """
    def fight(self, hand):
        """SUMMARY

        fight(hand)

        @Arguments:
        - `hand`:

        @Return:

        @Error:
        """
        return hand.from_goo(self)

    def from_goo(self, oponent):
        """SUMMARY

        from_goo(oponent)

        @Arguments:
        - `oponent`:

        @Return:

        @Error:
        """
        return JANKENRESULT.Draw

    def from_choki(self, oponent):
        """SUMMARY

        from_choki(oponent)

        @Arguments:
        - `oponent`:

        @Return:

        @Error:
        """
        return JANKENRESULT.Lose

    def from_paa(self, oponent):
        """SUMMARY

        from_paa(oponent)

        @Arguments:
        - `oponent`:

        @Return:

        @Error:
        """
        return JANKENRESULT.Win


class Choki(Hand):
    """Choki

    Choki is a Hand.
    Responsibility:
    """
    def fight(self, hand):
        """SUMMARY

        fight(hand)

        @Arguments:
        - `hand`:

        @Return:

        @Error:
        """
        return hand.from_choki(self)

    def from_goo(self, oponent):
        """SUMMARY

        from_goo(oponent)

        @Arguments:
        - `oponent`:

        @Return:

        @Error:
        """
        return JANKENRESULT.Win

    def from_choki(self, oponent):
        """SUMMARY

        from_choki(oponent)

        @Arguments:
        - `oponent`:

        @Return:

        @Error:
        """
        return JANKENRESULT.Draw

    def from_paa(self, oponent):
        """SUMMARY

        from_paa(oponent)

        @Arguments:
        - `oponent`:

        @Return:

        @Error:
        """
        return JANKENRESULT.Lose


class Paa(Hand):
    """Paa

    Paa is a Hand.
    Responsibility:
    """
    def fight(self, hand):
        """SUMMARY

        fight(hand)

        @Arguments:
        - `hand`:

        @Return:

        @Error:
        """
        return hand.from_paa(self)

    def from_goo(self, oponent):
        """SUMMARY

        from_goo(oponent)

        @Arguments:
        - `oponent`:

        @Return:

        @Error:
        """
        return JANKENRESULT.Lose

    def from_choki(self, oponent):
        """SUMMARY

        from_choki(oponent)

        @Arguments:
        - `oponent`:

        @Return:

        @Error:
        """
        return JANKENRESULT.Win

    def from_paa(self, oponent):
        """SUMMARY

        from_paa(oponent)

        @Arguments:
        - `oponent`:

        @Return:

        @Error:
        """
        return JANKENRESULT.Draw



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# double_dispatch.py ends here
