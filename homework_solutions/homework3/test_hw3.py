import unittest
import random
import json

from kbest import KBestCounter
from earthquakes import Earthquake
import lights_out

class PointsTestResult(unittest.TextTestResult):
    """
    A unittest result that awards points per-test and prints a total.

    Usage:
      - Inherit from PointsTestCase and set POINTS on each test method
        using the @points decorator (below) or by setting method.POINTS.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.earned = 0
        self.possible = 0

    def addSuccess(self, test):
        super().addSuccess(test)
        self.possible += getattr(test, "_points", 0) 
        self.earned += getattr(test, "_points", 0)

    def addFailure(self, test, err): 
        super().addFailure(test, err)
        self.possible += getattr(test, "_points", 0) 

    def addSkip(self, test, reason):
        super().addSkip(test, reason)


class PointsTestRunner(unittest.TextTestRunner):
    resultclass = PointsTestResult

    def run(self, test):
        result = super().run(test)
        # Print totals after the normal unittest summary
        self.stream.writeln(f"\nPOINTS: {result.earned}/{result.possible}")
        return result


def points(n):
    """Decorator to assign point value to a test method."""
    def deco(fn):
        fn.POINTS = n
        return fn
    return deco


class PointsTestCase(unittest.TestCase):
    """
    Base class that copies method-level POINTS onto the test instance,
    so the Result object can read it.
    """
    def setUp(self):
        super().setUp()
        method = getattr(self, self._testMethodName)
        self._points = getattr(method, "POINTS", 0)


class TestKBestCounter(PointsTestCase):

    @points(1)
    def test_empty_stream_returns_empty_list(self):
        kb = KBestCounter(k=5)
        self.assertEqual(kb.kbest(), [])

    @points(1)
    def test_stream_shorter_than_k(self):
        kb = KBestCounter(k=5)
        data = [3, 1, 2]
        for x in data:
            kb.count(x)

        result = kb.kbest()
        self.assertEqual(len(result), 3)
        self.assertEqual(set(result), set(data))

    @points(1)
    def test_exactly_k_elements(self):
        kb = KBestCounter(k=5)
        data = [5, 1, 3, 2, 4]
        for x in data:
            kb.count(x)

        result = kb.kbest()
        self.assertEqual(len(result), 5)
        self.assertEqual(set(result), set(data))

    @points(4)
    def test_more_than_k_elements_distinct(self):
        kb = KBestCounter(k=3)
        data = [10, 1, 7, 3, 9, 2]
        for x in data:
            kb.count(x)

        result = kb.kbest()
        self.assertEqual(len(result), 3)
        self.assertEqual(set(result), {10, 9, 7})

    @points(4)
    def test_handles_duplicates(self):
        kb = KBestCounter(k=4)
        data = [5, 1, 5, 2, 5, 3, 4]
        for x in data:
            kb.count(x)

        result = kb.kbest()
        # Top 4 with multiplicity: 5, 5, 5, 4
        self.assertEqual(len(result), 4)
        self.assertEqual(sorted(result), [4, 5, 5, 5])

    @points(4)
    def test_randomized_against_reference(self):
        random.seed(0)
        k = 5
        kb = KBestCounter(k=k)

        seen = []
        for i in range(100):
            x = random.randint(-1000, 1000)
            kb.count(x)
            seen.append(x)

            if (i + 1) % 10 == 0:
                expected = sorted(seen, reverse=True)[:k]
                got = kb.kbest()
                self.assertEqual(
                    sorted(got, reverse=True),
                    sorted(expected, reverse=True),
                    msg=f"Mismatch at i={i+1}",
                )

class TestEarthquakes(PointsTestCase):

  def setUp(self):
    super().setUp()
    self.eq_test_json = {'type': 'Feature', 'properties': {'mag': 0.77, 'place': '3 km S of Cobb, CA', 'time': 1778357012510, 'updated': 1778358141530, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/nc75357856', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nc75357856.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'automatic', 'tsunami': 0, 'sig': 9, 'net': 'nc', 'code': '75357856', 'ids': ',nc75357856,', 'sources': ',nc,', 'types': ',nearby-cities,origin,phase-data,scitech-link,', 'nst': 9, 'dmin': 0.01526, 'rms': 0.02, 'gap': 103, 'magType': 'md', 'type': 'earthquake', 'title': 'M 0.8 - 3 km S of Cobb, CA'}, 'geometry': {'type': 'Point', 'coordinates': [-122.723999023438, 38.7948341369629, 1.92999994754791]}, 'id': 'nc75357856'}
    self.eq2_test_json = {'type': 'Feature', 'properties': {'mag': 3.1, 'place': '3 km S of Cobb, CA', 'time': 1778357012510, 'updated': 1778358141530, 'tz': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/nc75357856', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nc75357856.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'automatic', 'tsunami': 0, 'sig': 9, 'net': 'nc', 'code': '75357856', 'ids': ',nc75357856,', 'sources': ',nc,', 'types': ',nearby-cities,origin,phase-data,scitech-link,', 'nst': 9, 'dmin': 0.01526, 'rms': 0.02, 'gap': 103, 'magType': 'md', 'type': 'earthquake', 'title': 'M 0.8 - 3 km S of Cobb, CA'}, 'geometry': {'type': 'Point', 'coordinates': [-122.723999023438, 38.7948341369629, 1.92999994754791]}, 'id': 'nc75357857'}

  @points(3)
  def test_eq(self): 
    earthquake1 = Earthquake(self.eq_test_json)
    earthquake2 = Earthquake(self.eq_test_json)
    self.assertEqual(earthquake1, earthquake2, msg = "__eq__ not implemented correctly")

  @points(2)
  def test_neq(self): 
    earthquake1 = Earthquake(self.eq_test_json)
    earthquake2 = Earthquake(self.eq2_test_json)
    self.assertNotEqual(earthquake1, earthquake2, msg = "__eq__ not implemented correctly. Different earthquakes evaluating as equal")

  @points(3)
  def test_hash_equal(self): 
    earthquake1 = Earthquake(self.eq_test_json)
    earthquake2 = Earthquake(self.eq_test_json)
    self.assertEqual(hash(earthquake1), hash(earthquake2), msg = "__hash__ not implemented correctly")

  @points(2)
  def test_hash_nequal(self): 
    earthquake1 = Earthquake(self.eq_test_json)
    earthquake2 = Earthquake(self.eq2_test_json)
    self.assertNotEqual(hash(earthquake1), hash(earthquake2), msg = "__hash__ not implemented correctly. Same hashcode for different earthquakes")

  @points(5)
  def test_gt(self): 
    earthquake1 = Earthquake(self.eq_test_json)
    earthquake2 = Earthquake(self.eq2_test_json)
    self.assertTrue(earthquake2 > earthquake1, msg = "__gt__ not implemented correctly.")
    
  @points(5)
  def test_lt(self): 
    earthquake1 = Earthquake(self.eq_test_json)
    earthquake2 = Earthquake(self.eq2_test_json)
    self.assertTrue(earthquake1 < earthquake2, msg = "__lt__ not implemented correctly.")


class TestLightsOut(PointsTestCase):

  @points(5)
  def test_solver_num_steps(self):
    start = (
        (0, 1, 0, 0),
        (1, 0, 1, 0),
        (0, 1, 0, 1),
        (0, 0, 1, 0))

    solution_path = lights_out.solve(start)
    self.assertEqual(len(solution_path), 6, msg = f"solve returned incorrect path length {len(solution_path)}")

  @points(5)
  def test_solver_solution(self):
    start = (
        (0, 1, 0, 0),
        (1, 0, 1, 0),
        (0, 1, 0, 1),
        (0, 0, 1, 0))

    correct = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 2), (2, 2)]
    solution_path = lights_out.solve(start)
    self.assertEqual(solution_path, correct, msg = "incorrect solution path returned by solver")

  @points(5)
  def test_solver_solution_easy(self):
    start = (
        (0, 1, 0, 0),
        (1, 1, 1, 0),
        (0, 1, 0, 0),
        (0, 0, 0, 0))

    correct = [(1, 1)]
    solution_path = lights_out.solve(start)
    print(solution_path)
    self.assertEqual(solution_path, correct, msg = "incorrect solution path returned by solver")

  @points(5)
  def test_solver_solution_goal(self):
    start = (
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0),
        (0, 0, 0, 0))

    correct = []
    solution_path = lights_out.solve(start)
    self.assertEqual(solution_path, correct, msg = "solver didn't return empty list when starting at goal")

if __name__ == "__main__":
    unittest.main(testRunner=PointsTestRunner(verbosity=2))
