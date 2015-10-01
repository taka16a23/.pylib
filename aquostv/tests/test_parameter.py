#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_parameter.py

['skipTest', ]

['assertAlmostEqual', 'assertAlmostEquals', 'assertApproximates',
 'assertDictContainsSubset', 'assertDictEqual', 'assertEndsWith', 'assertEqual',
 'assertEquals', 'assertFalse', 'assertGreater', 'assertGreaterEqual',
 'assertIdentical', 'assertIn', 'assertIs', 'assertIsInstance', 'assertIsNone',
 'assertIsNot', 'assertIsNotInstance', 'assertIsNotNone', 'assertItemsEqual',
 'assertLess', 'assertLessEqual', 'assertListEqual', 'assertMethodsMatch',
 'assertMultiLineEqual', 'assertNotAlmostEqual', 'assertNotAlmostEquals',
 'assertNotApproximates', 'assertNotEndsWith', 'assertNotEqual',
 'assertNotEquals', 'assertNotIdentical', 'assertNotIn', 'assertNotIsInstance',
 'assertNotRegexpMatches', 'assertNotStartsWith', 'assertRaises',
 'assertRaisesRegexp', 'assertRegexpMatches', 'assertSequenceEqual',
 'assertSetEqual', 'assertStartsWith', 'assertTrue', 'assertTupleEqual', ]

['failIf', 'failIfAlmostEqual', 'failIfApproximates', 'failIfEndsWith',
 'failIfEqual', 'failIfIdentical', 'failIfIn', 'failIfIs', 'failIfIsInstance',
 'failIfStartsWith', 'failUnless', 'failUnlessAlmostEqual',
 'failUnlessApproximates', 'failUnlessEndsWith', 'failUnlessEqual',
 'failUnlessIdentical', 'failUnlessIn', 'failUnlessIs', 'failUnlessIsInstance',
 'failUnlessMethodsMatch', 'failUnlessRaises', 'failUnlessRaisesRegexp',
 'failUnlessStartsWith', 'failureException', ]

"""
from mocker import *
from .. import command


class TestParameter(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.param = command.Parameter('')
        self.mocker.replay()

    def test__get_trimed(self, ):
        self.param.set(1)
        expect = '1'
        got = self.param._get_trimed()
        self.assertEqual(
            expect, got,
            msg='Failed: Parameter._get_trimed expect: \{}, got: \{}'
            .format(expect, got))

    def test_get(self, ):
        expect = '    '
        got = self.param.get()
        self.assertEqual(
            expect, got, msg='Failed: Parameter.get expect: \{}, got: \{}'
            .format(expect, got))

    def test_set(self, ):
        lis = ['?', ' ', '', 1, '1', -1, '-1', '0001', '????']
        expects = ['?   ', '    ', '    ', '1   ', '1   ',
                   '-1  ', '-1  ', '0001', '????']
        for val, expect in zip(lis, expects):
            self.param.set(val)
            got = self.param.get()
            self.assertEqual(expect, got,
                             msg='Failed: Parameter.set expect: \{}, got: \{}'
                             .format(expect, got))
        with self.assertRaises(command.ParameterLengthError):
            self.param.set('11111')

    def test___int__(self, ):
        self.param.set(1)
        got = int(self.param)
        self.assertIsInstance(got, int)
        self.param.set('?')
        with self.assertRaises(ValueError) as _err:
            int(self.param)

    def test___long__(self, ):
        self.param.set(1)
        got = long(self.param)
        self.assertIsInstance(got, long)
        self.param.set('?')
        with self.assertRaises(ValueError) as _err:
            long(self.param)

    def test___add__(self, ):
        self.param.set(1)
        # int 1
        got = self.param + 1
        self.assertEqual('2   ', got,
                         msg='Failed: Parameter.__add__ expect: \{}, got: \{}'
                         .format('2   ', got))
        # string '1'
        got = self.param + '1'
        self.assertEqual('2   ', got,
                         msg='Failed: Parameter.__add__ expect: \{}, got: \{}'
                         .format('2   ', got))
        # '-1'
        got = self.param + '-1'
        self.assertEqual('0   ', got,
                         msg='Failed: Parameter.__add__ expect: \{}, got: \{}'
                         .format('0   ', got))
        # Parameter object
        got = self.param + command.Parameter(1)
        self.assertEqual('2   ', got,
                         msg='Failed: Parameter.__add__ expect: \{}, got: \{}'
                         .format('2   ', got))
        with self.assertRaises(ValueError) as _err:
            self.param + '?'

    def test___sub__(self, ):
        self.param.set(2)
        # int 1
        got = self.param - 1
        self.assertEqual('1   ', got,
                         msg='Failed: Parameter.__sub__ expect: \{}, got: \{}'
                         .format('1   ', got))
        # string '1'
        got = self.param - '1'
        self.assertEqual('1   ', got,
                         msg='Failed: Parameter.__sub__ expect: \{}, got: \{}'
                         .format('1   ', got))
        # '-1'
        got = self.param - '-1'
        self.assertEqual('3   ', got,
                         msg='Failed: Parameter.__sub__ expect: \{}, got: \{}'
                         .format('3   ', got))
        # Parameter object
        got = self.param - command.Parameter(1)
        self.assertEqual('1   ', got,
                         msg='Failed: Parameter.__sub__ expect: \{}, got: \{}'
                         .format('1   ', got))
        with self.assertRaises(ValueError) as _err:
            self.param - '?'

    def test___str__(self, ):
        self.param.set(1)
        expect = '1   '
        got = str(self.param)
        self.assertEqual(expect, got,
                         msg='Failed: Parameter.__str__ expect: \{}, got: \{}'
                         .format(expect, got))

    def test___cmp__(self, ):
        self.param.set(1)
        expect = 0
        got = cmp(self.param, command.Parameter(1))
        self.assertEqual(expect, got,
                         msg='Failed: Parameter.__cmp__ expect: \{}, got: \{}'
                         .format(expect, got))
        got = cmp(self.param, '1   ')
        self.assertEqual(expect, got,
                         msg='Failed: Parameter.__cmp__ expect: \{}, got: \{}'
                         .format(expect, got))

        expect = 0
        got = cmp(self.param, 1)
        self.assertNotEqual(expect, got,
                         msg='Failed: Parameter.__cmp__ expect: \{}, got: \{}'
                         .format(expect, got))

    def test___div__(self, ):
        self.param.set(2)
        expect = '1   '
        param = self.param / 2
        got = str(param)
        self.assertEqual(expect, got,
                         msg='Failed: Parameter.__div__ expect: \{}, got: \{}'
                         .format(expect, got))

    def test___hash__(self, ):
        self.param.set(1)
        expect = hash('1   ')
        got = hash(self.param)
        self.assertEqual(expect, got,
                         msg='Failed: Parameter.__hash__ expect: \{}, got: \{}'
                         .format(expect, got))

    def test___repr__(self, ):
        self.param.set(1)
        expect = 'Parameter("1   ")'
        got = repr(self.param)
        self.assertEqual(expect, got,
                         msg='Failed: Parameter.__repr__ expect: \{}, got: \{}'
                         .format(expect, got))

    def test___getitem__(self, ):
        self.param.set(1)
        lis = ['1', ' ',  ' ',  ' ']
        for i, expect in enumerate(lis, start=0):
            got = self.param[i]
            self.assertEqual(expect, got,
                msg='Failed: Parameter.__getitem__ expect: \{}, got: \{}'
                .format(expect, got))

    def test___setitem__(self, ):
        self.param.set(1)
        expect = '2   '
        self.param[0] = '2'
        got = str(self.param)
        self.assertEqual(
            expect, got,
            msg='Failed: Parameter.__setitem__ expect: \{}, got: \{}'
            .format(expect, got))
        with self.assertRaises(ValueError):
            self.param[1] = '2 '

    def test___eq__(self, ):
        self.param.set(1)
        self.assertTrue(self.param == '1   ')
        self.assertFalse(self.param == '1')

    def test___ne__(self, ):
        self.param.set(1)
        self.assertTrue(self.param != '?   ')
        self.assertFalse(self.param != '1   ')

    def test___lt__(self, ):
        self.param.set(1)
        self.assertTrue(self.param < 2)

    def test___le__(self, ):
        self.param.set(1)
        self.assertTrue(self.param <= 1)

    def test___gt__(self, ):
        self.param.set(1)
        self.assertTrue(self.param > 0)

    def test___ge__(self, ):
        self.param.set(1)
        self.assertTrue(self.param >= 1)

    def test___pos__(self, ):
        self.param.set(-1)
        param = +self.param
        self.assertTrue(param == "1   ")

    def test___neg__(self, ):
        self.param.set(1)
        param = -self.param
        self.assertTrue(param == "-1  ")

    def test___iadd__(self, ):
        self.param.set(1)
        # int 1
        self.param += 1
        got = str(self.param)
        self.assertEqual('2   ', got,
                         msg='Failed: Parameter.__iadd__ expect: \{}, got: \{}'
                         .format('2   ', got))
        # string '1'
        self.param.set(1)
        self.param += '1'
        got = str(self.param)
        self.assertEqual('2   ', got,
                         msg='Failed: Parameter.__iadd__ expect: \{}, got: \{}'
                         .format('2   ', got))
        # '-1'
        self.param.set(1)
        self.param += '-1'
        got = str(self.param)
        self.assertEqual('0   ', got,
                         msg='Failed: Parameter.__iadd__ expect: \{}, got: \{}'
                         .format('0   ', got))
        # Parameter object
        self.param.set(1)
        self.param += command.Parameter(1)
        got = str(self.param)
        self.assertEqual('2   ', got,
                         msg='Failed: Parameter.__iadd__ expect: \{}, got: \{}'
                         .format('2   ', got))
        with self.assertRaises(ValueError) as _err:
            self.param += '?'


    def test___isub__(self, ):
        self.param.set(2)
        # int 1
        self.param.set(2)
        self.param -= 1
        got = str(self.param)
        self.assertEqual('1   ', got,
                         msg='Failed: Parameter.__isub__ expect: \{}, got: \{}'
                         .format('1   ', got))
        # string '1'
        self.param.set(2)
        self.param -= '1'
        got = str(self.param)
        self.assertEqual('1   ', got,
                         msg='Failed: Parameter.__isub__ expect: \{}, got: \{}'
                         .format('1   ', got))
        # '-1'
        self.param.set(2)
        self.param -= '-1'
        got = str(self.param)
        self.assertEqual('3   ', got,
                         msg='Failed: Parameter.__isub__ expect: \{}, got: \{}'
                         .format('3   ', got))
        # Parameter object
        self.param.set(2)
        self.param -= command.Parameter(1)
        got = str(self.param)
        self.assertEqual('1   ', got,
                         msg='Failed: Parameter.__isub__ expect: \{}, got: \{}'
                         .format('1   ', got))
        with self.assertRaises(ValueError) as _err:
            self.param -= '?'

    def test___delitem__(self, ):
        self.param.set(1)
        del self.param[0]
        expect = '    '
        got = str(self.param)
        self.assertEqual(
            expect, got,
            msg='Failed: Parameter.__delitem__ expect: \{}, got: \{}'
            .format(expect, got))

    def test___iter__(self, ):
        self.param.set(1)
        expects = ['1', ' ', ' ', ' ']
        for expect, got in zip(expects, self.param):
            self.assertEqual(
                expect, got,
                msg='Failed: Parameter.__iter__ expect: \{}, got: \{}'
                .format(expect, got))

    def test___setslice__(self, ):
        self.param.set(1)
        self.param[0:2] = ['1', '2']
        expect = '12  '
        got = str(self.param)
        self.assertEqual(
            expect, got,
            msg='Failed: Parameter.__setslice__ expect: \{}, got: \{}'
            .format(expect, got))
        with self.assertRaises(command.ParameterLengthError):
            self.param[0:1] = ['1', '2']


    def test___getslice__(self, ):
        self.param.set(1)
        expect = '1 '
        got = self.param[0:2]
        self.assertEqual(
            expect, got,
            msg='Failed: Parameter.__getslice__ expect: \{}, got: \{}'
            .format(expect, got))

    def test___len__(self, ):
        expect = 4
        got = len(self.param)
        self.assertEqual(
            expect, got,
            msg='Failed: Parameter.__len__ expect: \{}, got: \{}'
            .format(expect, got))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_parameter.py ends here
