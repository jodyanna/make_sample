
import unittest
import maker


class TestHuman(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.default_human = maker.Human()
        cls.custom_human = maker.Human(first_name="Jane", last_name="Doe", telephone="630-123-1234")

    def setUp(self):
        pass

    def test_fullname(self):
        self.assertEqual(self.default_human.fullname(), "John Doe")
        self.assertEqual(self.custom_human.fullname(), "Jane Doe")

    def test_set_first_names(self):
        custom_first_names = ["Bobby", "Ben", "Joe"]
        maker.Human.set_first_names(custom_first_names)
        self.assertEqual(maker.Human.first_names, custom_first_names)

    def test_set_last_names(self):
        custom_last_names = ["Smith", "Mares", "Franklin"]
        maker.Human.set_first_names(custom_last_names)
        self.assertEqual(maker.Human.first_names, custom_last_names)

    def test_add_first_name(self):
        maker.Human.add_first_name("Makoto")
        self.assertIn("Makoto", maker.Human.first_names)

    def test_add_last_name(self):
        maker.Human.add_last_name("Mares")
        self.assertIn("Mares", maker.Human.last_names)

    def test_add_full_name(self):
        maker.Human.add_full_name("Jim Halpert")
        self.assertIn("Jim", maker.Human.first_names)
        self.assertIn("Halpert", maker.Human.last_names)


class TestMaker(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.random_human = maker.Maker.create_random_human()
        cls.many_random_humans = maker.Maker.create_multiple_random_humans(3)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_create_random_human(self):
        self.assertIsInstance(self.random_human, maker.Human)

    def test_create_multiple_humans(self):
        self.assertIsInstance(self.many_random_humans[1], maker.Human)
        self.assertEqual(len(self.many_random_humans), 3)


if __name__ == '__main__':
    unittest.main()
