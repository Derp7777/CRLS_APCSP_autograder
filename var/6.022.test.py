import random
import unittest
import io
from contextlib import redirect_stdout
import re


class testAutograde(unittest.TestCase):
    def test_1(self):
        lam_list = ['Sprints', 'Sprints', 'Sprints', 'Sprints', 'Sprints']
        self.assertEqual(dr_lam_workout_counter(lam_list), {'Sprints': 5},
                         "Test for dr_lam_workout_counter, "
                         "['Sprints', 'Sprints', 'Sprints', 'Sprints', 'Sprints'], expect back"
                         "{'Sprints': 5}' <br>")

    def test_2(self):
        lam_list = ['Sprints', 'Sprints', 'biceps', 'Bench', 'Bench', 'squats', 'Sprints']
        self.assertEqual(dr_lam_workout_counter(lam_list),
                         {'Sprints': 3, 'biceps': 1, 'Bench': 2, 'squats': 1},
                         "Test for dr_lam_workout_counter, "
                         "['Sprints', 'Sprints', 'biceps', 'Bench', 'Bench', 'squats', 'Sprints'], expect back" 
                         "{'Sprints': 3, 'biceps': 1, 'Bench':2, 'squats':1}' <br>"
                         )


if __name__ == '__main__':
    unittest.main()
