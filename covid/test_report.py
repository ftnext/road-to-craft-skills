from unittest import TestCase

from report import NewCasesReporter


class NewCasesReporterTest(TestCase):
    _DELTA = 0.0001

    def setUp(self):
        self.reporter = NewCasesReporter()

    def test_county_report(self):
        report = self.reporter.make_report(
            ""
            + "c1, s1, 1, 1, 1, 1, 1, 1, 1, 7\n"
            + "c2, s2, 2, 2, 2, 2, 2, 2, 2, 7"
        )
        self.assertEqual(
            ""
            + "County     State     Avg New Cases\n"
            + "======     =====     =============\n"
            + "c1         s1        1.86\n"
            + "c2         s2        2.71\n\n"
            + "s1 cases: 14\n"
            + "s2 cases: 21\n"
            + "Total Cases: 35\n",
            report,
        )

    def test_state_with_two_counties(self):
        report = self.reporter.make_report(
            ""
            + "c1, s1, 1, 1, 1, 1, 1, 1, 1, 7\n"
            + "c2, s1, 2, 2, 2, 2, 2, 2, 2, 7"
        )
        self.assertEqual(
            ""
            + "County     State     Avg New Cases\n"
            + "======     =====     =============\n"
            + "c1         s1        1.86\n"
            + "c2         s1        2.71\n\n"
            + "s1 cases: 35\n"
            + "Total Cases: 35\n",
            report,
        )

    def test_states_with_short_lines(self):
        report = self.reporter.make_report(
            "" + "c1, s1, 1, 1, 1, 1, 7\n" + "c2, s2, 7"
        )
        self.assertEqual(
            ""
            + "County     State     Avg New Cases\n"
            + "======     =====     =============\n"
            + "c1         s1        2.20\n"
            + "c2         s2        7.00\n\n"
            + "s1 cases: 11\n"
            + "s2 cases: 7\n"
            + "Total Cases: 18\n",
            report,
        )
