import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import unittest
from datetime import datetime
from sla_calc import due, breached
class T(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(due("2026-10-25 09:00", "P1"), datetime(2026, 10, 25, 13, 0))
    def test_breach(self):
        self.assertTrue(breached("2026-10-25 09:00", "P1", datetime(2026, 10, 25, 14, 0)))
        self.assertFalse(breached("2026-10-25 09:00", "P1", datetime(2026, 10, 25, 12, 0)))
if __name__ == "__main__": unittest.main()
