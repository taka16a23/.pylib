#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""cls -- DESCRIPTION

"""
from bitflag.abstract import BitFlagAbstract
from bitflag.flagenum import FlagEnum
from bitflag.error import BitLengthError, BitFlagValueError


class BitFlag8(BitFlagAbstract):
    r"""SUMMARY
    """
    _max = 9

    def __init__(self, flags=0):
        r"""SUMMARY

        __init__(flag=0)

        @Arguments:
        - `flag`:

        @Return:
        """
        BitFlagAbstract.__init__(self, flags=flags)
        self.__lengthcheck()

    def __lengthcheck(self, ):
        r"""SUMMARY

        __lengthcheck()

        @Return:
        """
        if self.flags < 0:
            raise BitFlagValueError('must "0 <=" given {0.flags}'.format(self))
        if self._max < len(str(self)):
            raise BitLengthError('unsupported {0.flags} bit length {1}, "{2}"'
                                 .format(self, len(str(self)), str(self)))

    def clear(self, ):
        r"""Clear flags.

        clear()

        '10111' => '00000'

        @Return:
        None
        """
        self.flags = int(FlagEnum.flag0)

    def set1(self, ):
        r"""Set bit flag '0' => '1'.

        set1()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag1

    def reset1(self, ):
        r"""Reset bit flag '1' => '0'.

        reset1()

        @Return:
        None
        """
        if self.isflaged1():
            self.flags ^= FlagEnum.flag1

    def isflaged1(self, ):
        r"""Check flaged 1th bit.

        isflaged1()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag1)

    def set2(self, ):
        r"""Set bit flag '00' => '10'.

        set2()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag2

    def reset2(self, ):
        r"""Reset bit flag '10' => '00'.

        reset2()

        @Return:
        None
        """
        if self.isflaged2():
            self.flags ^= FlagEnum.flag2

    def isflaged2(self, ):
        r"""Check flaged 2th bit.

        isflaged2()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag2)

    def set3(self, ):
        r"""Set bit flag '000' => '100'.

        set3()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag3

    def reset3(self, ):
        r"""Reset bit flag '100' => '000'.

        reset3()

        @Return:
        None
        """
        if self.isflaged3():
            self.flags ^= FlagEnum.flag3

    def isflaged3(self, ):
        r"""Check flaged 3th bit.

        isflaged3()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag3)

    def set4(self, ):
        r"""Set bit flag '0000' => '1000'.

        set4()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag4

    def reset4(self, ):
        r"""Reset bit flag '1000' => '0000'.

        reset4()

        @Return:
        None
        """
        if self.isflaged4():
            self.flags ^= FlagEnum.flag4

    def isflaged4(self, ):
        r"""Check flaged 4th bit.

        isflaged4()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag4)

    def set5(self, ):
        r"""Set bit flag '00000' => '10000'.

        set5()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag5

    def reset5(self, ):
        r"""Reset bit flag '10000' => '00000'.

        reset5()

        @Return:
        None
        """
        if self.isflaged5():
            self.flags ^= FlagEnum.flag5

    def isflaged5(self, ):
        r"""Check flaged 5th bit.

        isflaged5()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag5)

    def set6(self, ):
        r"""Set bit flag '000000' => '100000'.

        set6()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag6

    def reset6(self, ):
        r"""Reset bit flag '100000' => '000000'.

        reset6()

        @Return:
        None
        """
        if self.isflaged6():
            self.flags ^= FlagEnum.flag6

    def isflaged6(self, ):
        r"""Check flaged 6th bit.

        isflaged6()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag6)

    def set7(self, ):
        r"""Set bit flag '0000000' => '1000000'.

        set7()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag7

    def reset7(self, ):
        r"""Reset bit flag '1000000' => '0000000'.

        reset7()

        @Return:
        None
        """
        if self.isflaged7():
            self.flags ^= FlagEnum.flag7

    def isflaged7(self, ):
        r"""Check flaged 7th bit.

        isflaged7()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag7)

    def set8(self, ):
        r"""Set bit flag '00000000' => '10000000'.

        set8()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag8

    def reset8(self, ):
        r"""Reset bit flag '10000000' => '00000000'.

        reset8()

        @Return:
        None
        """
        if self.isflaged8():
            self.flags ^= FlagEnum.flag8

    def isflaged8(self, ):
        r"""Check flaged 8th bit.

        isflaged8()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag8)


class BitFlag16(BitFlag8):
    r"""SUMMARY
    """
    _max = 17

    def __init__(self, flags=0):
        r"""SUMMARY

        __init__(flag=0)

        @Arguments:
        - `flag`:

        @Return:
        None
        """
        BitFlag8.__init__(self, flags=flags)

    def set9(self, ):
        r"""Set bit flag '000000000' => '100000000'.

        set9()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag9

    def reset9(self, ):
        r"""Reset bit flag '100000000' => '000000000'.

        reset9()

        @Return:
        None
        """
        if self.isflaged9():
            self.flags ^= FlagEnum.flag9

    def isflaged9(self, ):
        r"""Check flaged 9th bit.

        isflaged9()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag9)

    def set10(self, ):
        r"""Set bit flag '0000000000' => '1000000000'.

        set10()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag10

    def reset10(self, ):
        r"""Reset bit flag '1000000000' => '0000000000'.

        reset10()

        @Return:
        None
        """
        if self.isflaged10():
            self.flags ^= FlagEnum.flag10

    def isflaged10(self, ):
        r"""Check flaged 10th bit.

        isflaged10()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag10)

    def set11(self, ):
        r"""Set bit flag '00000000000' => '10000000000'.

        set11()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag11

    def reset11(self, ):
        r"""Reset bit flag '10000000000' => '00000000000'.

        reset11()

        @Return:
        None
        """
        if self.isflaged11():
            self.flags ^= FlagEnum.flag11

    def isflaged11(self, ):
        r"""Check flaged 11th bit.

        isflaged11()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag11)

    def set12(self, ):
        r"""Set bit flag '000000000000' => '100000000000'.

        set12()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag12

    def reset12(self, ):
        r"""Reset bit flag '100000000000' => '000000000000'.

        reset12()

        @Return:
        None
        """
        if self.isflaged12():
            self.flags ^= FlagEnum.flag12

    def isflaged12(self, ):
        r"""Check flaged 12th bit.

        isflaged12()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag12)

    def set13(self, ):
        r"""Set bit flag '0000000000000' => '1000000000000'.

        set13()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag13

    def reset13(self, ):
        r"""Reset bit flag '1000000000000' => '0000000000000'.

        reset13()

        @Return:
        None
        """
        if self.isflaged13():
            self.flags ^= FlagEnum.flag13

    def isflaged13(self, ):
        r"""Check flaged 13th bit.

        isflaged13()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag13)

    def set14(self, ):
        r"""Set bit flag '00000000000000' => '10000000000000'.

        set14()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag14

    def reset14(self, ):
        r"""Reset bit flag '10000000000000' => '00000000000000'.

        reset14()

        @Return:
        None
        """
        if self.isflaged14():
            self.flags ^= FlagEnum.flag14

    def isflaged14(self, ):
        r"""Check flaged 14th bit.

        isflaged14()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag14)

    def set15(self, ):
        r"""Set bit flag '000000000000000' => '100000000000000'.

        set15()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag15

    def reset15(self, ):
        r"""Reset bit flag '100000000000000' => '000000000000000'.

        reset15()

        @Return:
        None
        """
        if self.isflaged15():
            self.flags ^= FlagEnum.flag15

    def isflaged15(self, ):
        r"""Check flaged 15th bit.

        isflaged15()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag15)

    def set16(self, ):
        r"""Set bit flag '0000000000000000' => '1000000000000000'.

        set16()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag16

    def reset16(self, ):
        r"""Reset bit flag '1000000000000000' => '0000000000000000'.

        reset16()

        @Return:
        None
        """
        if self.isflaged16():
            self.flags ^= FlagEnum.flag16

    def isflaged16(self, ):
        r"""Check flaged 16th bit.

        isflaged16()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag16)


class BitFlag32(BitFlag16):
    r"""SUMMARY
    """
    # FIXME: (Atami) [2014/04/12]
    # cannot 32 limited by enum
    _max = 30

    def __init__(self, flags=0):
        r"""SUMMARY

        __init__(flag=0)

        @Arguments:
        - `flag`:

        @Return:
        None
        """
        BitFlag16.__init__(self, flags=flags)

    def set17(self, ):
        r"""Set bit flag '00000000000000000' => '10000000000000000'.

        set17()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag17

    def reset17(self, ):
        r"""Reset bit flag '10000000000000000' => '00000000000000000'.

        reset17()

        @Return:
        None
        """
        if self.isflaged17():
            self.flags ^= FlagEnum.flag17

    def isflaged17(self, ):
        r"""Check flaged17th bit.

        isflaged17()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag17)

    def set18(self, ):
        r"""Set bit flag '000000000000000000' => '100000000000000000'.

        set18()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag18

    def reset18(self, ):
        r"""Reset bit flag '100000000000000000' => '000000000000000000'.

        reset18()

        @Return:
        None
        """
        if self.isflaged18():
            self.flags ^= FlagEnum.flag18

    def isflaged18(self, ):
        r"""Check flaged 18th bit.

        isflaged18()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag18)

    def set19(self, ):
        r"""Set bit flag '0000000000000000000' => '1000000000000000000'.

        set19()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag19

    def reset19(self, ):
        r"""Reset bit flag '1000000000000000000' => '0000000000000000000'.

        reset19()

        @Return:
        None
        """
        if self.isflaged19():
            self.flags ^= FlagEnum.flag19

    def isflaged19(self, ):
        r"""Check flaged 19th bit.

        isflaged19()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag19)

    def set20(self, ):
        r"""Set bit flag '00000000000000000000' => '10000000000000000000'.

        set20()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag20

    def reset20(self, ):
        r"""Reset bit flag '10000000000000000000' => '00000000000000000000'.

        reset20()

        @Return:
        None
        """
        if self.isflaged20():
            self.flags ^= FlagEnum.flag20

    def isflaged20(self, ):
        r"""Check flaged 20th bit.

        isflaged20()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag20)

    def set21(self, ):
        r"""Set bit flag '000000000000000000000' => '100000000000000000000'.

        set21()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag21

    def reset21(self, ):
        r"""Reset bit flag '100000000000000000000' => '000000000000000000000'.

        reset21()

        @Return:
        None
        """
        if self.isflaged21():
            self.flags ^= FlagEnum.flag21

    def isflaged21(self, ):
        r"""Check flaged 21th bit.

        isflaged21()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag21)

    def set22(self, ):
        r"""Set bit flag '0000000000000000000000' => '1000000000000000000000'.

        set22()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag22

    def reset22(self, ):
        r"""Reset bit flag '1000000000000000000000' => '0000000000000000000000'.

        reset22()

        @Return:
        None
        """
        if self.isflaged22():
            self.flags ^= FlagEnum.flag22

    def isflaged22(self, ):
        r"""Check flaged 22th bit.

        isflaged22()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag22)

    def set23(self, ):
        r"""Set bit flag.
        '00000000000000000000000' => '10000000000000000000000'.

        set23()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag23

    def reset23(self, ):
        r"""Reset bit flag.
        '10000000000000000000000' => '00000000000000000000000'.

        reset23()

        @Return:
        None
        """
        if self.isflaged23():
            self.flags ^= FlagEnum.flag23

    def isflaged23(self, ):
        r"""Check flaged 23th bit.

        isflaged23()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag23)

    def set24(self, ):
        r"""Set bit flag.
        '000000000000000000000000' => '100000000000000000000000'.

        set24()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag24

    def reset24(self, ):
        r"""Reset bit flag.
        '100000000000000000000000' => '000000000000000000000000'.

        reset24()

        @Return:
        None
        """
        if self.isflaged24():
            self.flags ^= FlagEnum.flag24

    def isflaged24(self, ):
        r"""Check flaged 24th bit.

        isflaged24()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag24)

    def set25(self, ):
        r"""Set bit flag.
        '0000000000000000000000000' => '1000000000000000000000000'.

        set25()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag25

    def reset25(self, ):
        r"""Reset bit flag.
        '1000000000000000000000000' => '0000000000000000000000000'.

        reset25()

        @Return:
        None
        """
        if self.isflaged25():
            self.flags ^= FlagEnum.flag25

    def isflaged25(self, ):
        r"""Check flaged 25th bit.

        isflaged25()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag25)

    def set26(self, ):
        r"""Set bit flag.
        '00000000000000000000000000' => '10000000000000000000000000'.

        set26()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag26

    def reset26(self, ):
        r"""Reset bit flag.
        '10000000000000000000000000' => '00000000000000000000000000'.

        reset26()

        @Return:
        None
        """
        if self.isflaged26():
            self.flags ^= FlagEnum.flag26

    def isflaged26(self, ):
        r"""Check flaged 26th bit.

        isflaged26()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag26)

    def set27(self, ):
        r"""Set bit flag.
        '000000000000000000000000000' => '100000000000000000000000000'.

        set27()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag27

    def reset27(self, ):
        r"""Reset bit flag.
        '100000000000000000000000000' => '000000000000000000000000000'.

        reset27()

        @Return:
        None
        """
        if self.isflaged27():
            self.flags ^= FlagEnum.flag27

    def isflaged27(self, ):
        r"""Check flaged 27th bit.

        isflaged27()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag27)

    def set28(self, ):
        r"""Set bit flag.
        '0000000000000000000000000000' => '1000000000000000000000000000'.

        set28()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag28

    def reset28(self, ):
        r"""Reset bit flag.
        '1000000000000000000000000000' => '0000000000000000000000000000'.

        reset28()

        @Return:
        None
        """
        if self.isflaged28():
            self.flags ^= FlagEnum.flag28

    def isflaged28(self, ):
        r"""Check flaged 28th bit.

        isflaged28()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag28)

    def set29(self, ):
        r"""Set bit flag.
        '00000000000000000000000000000' => '10000000000000000000000000000'.

        set29()

        @Return:
        None
        """
        self.flags |= FlagEnum.flag29

    def reset29(self, ):
        r"""Reset bit flag.
        '10000000000000000000000000000' => '00000000000000000000000000000'.

        reset29()

        @Return:
        None
        """
        if self.isflaged29():
            self.flags ^= FlagEnum.flag29

    def isflaged29(self, ):
        r"""Check flaged 29th bit.

        isflaged29()

        @Return:
        (bool)
        """
        return bool(self & FlagEnum.flag29)

    # def set30(self, ):
    #     r"""Set bit flag '0000000000000014' => '1000000000000000'.

    #     set30()

    #     @Return:
    #     None
    #     """
    #     self.flags |= FlagEnum.flag30

    # def reset30(self, ):
    #     r"""Reset bit flag '1000000000000014' => '0000000000000000'.

    #     reset30()

    #     @Return:
    #     None
    #     """
    #     if self.isflaged30():
    #         self.flags ^= FlagEnum.flag30

    # def isflaged30(self, ):
    #     r"""Check flaged 30th bit.

    #     isflaged30()

    #     @Return:
    #     (bool)
    #     """
    #     return bool(self & FlagEnum.flag30)


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# cls.py ends here
