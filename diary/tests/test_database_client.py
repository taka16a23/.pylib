#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Name: test_database_client.py

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
from diary import DiaryDatabaseClient
from diary.note import DiaryNote


class TestDiaryDatabaseClient(MockerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = DiaryDatabaseClient()

    def setUp(self):
        self.mocker.replay()

    def test_list_notes(self, ):
        notes = self.client.list_notes()
        for note in notes:
            self.assertTrue(isinstance(note, (DiaryNote, )))
            self.assertTrue(isinstance(note.date, (datetime, )))
            self.assertTrue(isinstance(note.text, (str, )))

    def test_list_by_date_year(self, ):
        expects = 2015
        notes = self.client.list_by_date(year=expects)
        for note in notes:
            self.assertTrue(isinstance(note, (DiaryNote, )))
            self.assertTrue(isinstance(note.date, (datetime, )))
            self.assertTrue(isinstance(note.text, (str, )))
            self.assertEqual(expects, note.date.year)

    def test_list_by_date_month(self, ):
        expects = 5
        notes = self.client.list_by_date(month=expects)
        for note in notes:
            self.assertTrue(isinstance(note, (DiaryNote, )))
            self.assertTrue(isinstance(note.date, (datetime, )))
            self.assertTrue(isinstance(note.text, (str, )))
            self.assertEqual(expects, note.date.month)

    def test_list_by_date_day(self, ):
        expects = 5
        notes = self.client.list_by_date(day=expects)
        for note in notes:
            self.assertTrue(isinstance(note, (DiaryNote, )))
            self.assertTrue(isinstance(note.date, (datetime, )))
            self.assertTrue(isinstance(note.text, (str, )))
            self.assertEqual(expects, note.date.day)

    def test_list_by_date_month_day(self, ):
        expect_month, expect_day = 5, 6
        notes = self.client.list_by_date(month=expect_month, day=expect_day)
        for note in notes:
            self.assertTrue(isinstance(note, (DiaryNote, )))
            self.assertTrue(isinstance(note.date, (datetime, )))
            self.assertTrue(isinstance(note.text, (str, )))
            self.assertEqual(expect_month, note.date.month)
            self.assertEqual(expect_day, note.date.day)

    def test_list_by_date_year_day(self, ):
        expect_year, expect_day = 2015, 5
        notes = self.client.list_by_date(year=expect_year, day=expect_day)
        for note in notes:
            self.assertTrue(isinstance(note, (DiaryNote, )))
            self.assertTrue(isinstance(note.date, (datetime, )))
            self.assertTrue(isinstance(note.text, (str, )))
            self.assertEqual(expect_year, note.date.year)
            self.assertEqual(expect_day, note.date.day)

    def test_list_by_date_year_month(self, ):
        expect_year, expect_month = 2015, 5
        notes = self.client.list_by_date(year=expect_year, month=expect_month)
        for note in notes:
            self.assertTrue(isinstance(note, (DiaryNote, )))
            self.assertTrue(isinstance(note.date, (datetime, )))
            self.assertTrue(isinstance(note.text, (str, )))
            self.assertEqual(expect_year, note.date.year)
            self.assertEqual(expect_month, note.date.month)

    def test_list_by_date_year_month_day(self, ):
        expecty, expectm, expectd = 2015, 5, 6
        notes = self.client.list_by_date(year=expecty, month=expectm, day=expectd)
        self.assertTrue(0 < len(notes))
        for note in notes:
            self.assertTrue(isinstance(note, (DiaryNote, )))
            self.assertTrue(isinstance(note.date, (datetime, )))
            self.assertTrue(isinstance(note.text, (str, )))
            self.assertEqual(expecty, note.date.year)
            self.assertEqual(expectm, note.date.month)
            self.assertEqual(expectd, note.date.day)

    def test_list_by_date_raise(self, ):
        with self.assertRaises(ValueError):
            self.client.list_by_date()

    def test_list_by_date_range(self, ):
        start = datetime(2015, 1, 1)
        end = datetime(2015, 3, 1)
        notes = self.client.list_by_date_range(start, end)
        for note in notes:
            self.assertTrue(isinstance(note, (DiaryNote, )))
            self.assertTrue(isinstance(note.date, (datetime, )))
            self.assertTrue(isinstance(note.text, (str, )))
            self.assertTrue(start <= note.date <= end)

    def test_list_by_search_text(self, ):
        expects = 'hkjdlskjfaohtoajlkjflkajsdifhaoijfjasdhfoia'
        notes = self.client.list_by_search_text(expects)
        for note in notes:
            self.assertTrue(isinstance(note, (DiaryNote, )))
            self.assertTrue(isinstance(note.date, (datetime, )))
            self.assertTrue(isinstance(note.text, (str, )))
            self.assertTrue(expects in note.text)

    def test_close(self, ):
        self.skipTest('Not Implemented')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls, ):
        pass



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# test_database_client.py ends here
