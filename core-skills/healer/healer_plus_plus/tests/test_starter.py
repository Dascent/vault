import unittest  
from healer_plus_plus.starter import HealerPlusPlus

class TestHealerStarter(unittest.TestCase):  
    def test_prune_memory_basic(self):  
        h = HealerPlusPlus(state={"shape_id": "test", "memory": ["m1","m2","m3","m4","m5","m6"]})  
        h.prune_memory(limit=5)  
        self.assertEqual(len(h.state["memory"]), 5)

    def test_diagnose_runs(self):  
        h = HealerPlusPlus(state={"shape_id": "test", "memory": ["m1","m2"], "outputs": ["spiral detected in last turn"]})  
        rep = h.diagnose()  
        self.assertIsInstance(rep, type(rep))  
        self.assertIn("healthScore", rep.to_dict())

    def test_self_heal_loop_once_no_error(self):  
        h = HealerPlusPlus(state={"shape_id": "test", "memory": ["m1"]})  
        # This should run without raising  
        h.self_heal_loop_once()  
        self.assertTrue(True)

if __name__ == '__main__':  
    unittest.main()  