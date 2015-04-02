import unittest
from mock import patch, MagicMock, call


class TestSingleTower(unittest.TestCase):

   def setUp(self):
      self.dbscode_minecraft_mock = MagicMock()
      self.minecraft_mock = MagicMock()
      self.autocastle_mock = MagicMock()
      
      modules = {
         'dbscode_minecraft': self.dbscode_minecraft_mock,
         'minecraft': self.minecraft_mock,
         'autocastle': self.autocastle_mock
      }
      self.module_patcher = patch.dict('sys.modules', modules)
      self.module_patcher.start()
      from castlemap import draw_castle_map
      self.draw_castle_map = draw_castle_map

   def tearDown(self):
      self.module_patcher.stop()

   def test_single_tower(self):
      self.autocastle_mock.reset_mock()
      height = 10
      spacing = 10
      self.draw_castle_map("O", height, spacing)
      self.autocastle_mock.tower.assert_called_with((0,0,0),height)

   def test_three_towers(self):
      self.autocastle_mock.reset_mock()
      height = 10
      spacing = 10
      self.draw_castle_map("O O O", height, spacing)
      expected_calls = [call((0,0,0), height), 
                        call((20,0,0), height),
                        call((40,0,0), height)]
      self.autocastle_mock.tower.assert_has_calls(expected_calls)

if __name__ == '__main__':
   unittest.main()
