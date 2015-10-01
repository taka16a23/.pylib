#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: test_note.py 349 2015-08-04 22:35:27Z t1 $
# $Revision: 349 $
# $Date: 2015-08-05 07:35:27 +0900 (Wed, 05 Aug 2015) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2015-08-05 07:35:27 +0900 (Wed, 05 Aug 2015) $

r"""Name: test_note.py

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
from datetime import datetime
from diary.note import DiaryNote


class TestDiaryNote(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.newyear = datetime(2000, 1, 1)
        cls.text = 'test text'

    def setUp(self):
        self.note = DiaryNote(self.newyear, self.text)
        self.mocker.replay()

    def test_get_date(self, ):
        self.assertEqual(self.newyear, self.note.get_date())

    def test_get_text(self, ):
        self.assertEqual(self.text, self.note.get_text())

    def test_as_dict(self, ):
        self.assertEqual({'date': self.newyear, 'text': self.text,},
                         self.note.as_dict())

    def test___gt__(self, ):
        self.assertTrue(self.note > DiaryNote(datetime(1999, 1, 1), self.text))
        self.assertFalse(self.note > DiaryNote(datetime(2001, 1, 1), self.text))
        self.assertTrue(self.note > datetime(1999, 1, 1))
        self.assertFalse(self.note > datetime(2001, 1, 1))

    def test___ge__(self, ):
        self.assertTrue(self.note >= DiaryNote(datetime(1999, 1, 1), self.text))
        self.assertFalse(self.note >= DiaryNote(datetime(2001, 1, 1), self.text))
        self.assertTrue(self.note >= self.note)
        self.assertTrue(self.note >= datetime(1999, 1, 1))
        self.assertFalse(self.note >= datetime(2001, 1, 1))

    def test___lt__(self, ):
        self.assertFalse(self.note < DiaryNote(datetime(1999, 1, 1), self.text))
        self.assertTrue(self.note < DiaryNote(datetime(2001, 1, 1), self.text))
        self.assertFalse(self.note < datetime(1999, 1, 1))
        self.assertTrue(self.note < datetime(2001, 1, 1))

    def test___le__(self, ):
        self.assertFalse(self.note <= DiaryNote(datetime(1999, 1, 1), self.text))
        self.assertTrue(self.note <= DiaryNote(datetime(2001, 1, 1), self.text))
        self.assertTrue(self.note <= self.note)
        self.assertFalse(self.note <= datetime(1999, 1, 1))
        self.assertTrue(self.note <= datetime(2001, 1, 1))

    def test___eq__(self, ):
        self.assertTrue(self.note == DiaryNote(datetime(2000, 1, 1), self.text))
        self.assertFalse(self.note == DiaryNote(datetime(2001, 1, 1), self.text))

    def test___ne__(self, ):
        self.assertFalse(self.note != DiaryNote(datetime(2000, 1, 1), self.text))
        self.assertTrue(self.note != DiaryNote(datetime(2001, 1, 1), self.text))

    def test___str__(self, ):
        self.assertEqual('2000-01-01 00:00:00\ntest text', str(self.note))

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass


# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_note.py ends here
