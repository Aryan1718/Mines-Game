import unittest
from mines import setup_game, reset_game, grid, revealed, num_mines, MIN_MINES, MAX_MINES
import pygame
class TestMinesGame(unittest.TestCase):

    def setUp(self):
        # Call reset_game to initialize the game state before each test
        reset_game()

    def test_setup_game_places_correct_number_of_mines(self):
        global num_mines
        num_mines = 5  # Set number of mines for testing
        setup_game()
        print("num mines from test" , num_mines)
        # Count the number of mines placed in the grid
        mine_count = sum(row.count(-1) for row in grid)
        self.assertEqual(mine_count, num_mines, f"Expected {num_mines} mines, but found {mine_count}")

    def test_mines_are_not_in_revealed_cells(self):
        global num_mines
        num_mines = 5  # Set number of mines for testing
        setup_game()

        # Reveal some cells
        for i in range(2):
            for j in range(2):
                revealed[i][j] = True

        # Check revealed cells for mines
        for i in range(len(grid)):
            for j in range(len(grid)):
                if revealed[i][j]:
                    self.assertNotEqual(grid[i][j], -1, "Revealed cell should not contain a mine.")

    def test_mine_selection_limits(self):
        global num_mines

        # Check the initial state
        num_mines = 0
        self.assertEqual(num_mines, MIN_MINES, f"Number of mines should be at least {MIN_MINES}")

        # Test increasing the mine count
        num_mines = MAX_MINES
        self.assertEqual(num_mines, MAX_MINES, f"Number of mines should not exceed {MAX_MINES}")

        # Attempt to set beyond maximum
        num_mines += 1
        self.assertEqual(num_mines, MAX_MINES, "Number of mines should not exceed maximum limit.")

        # Test decreasing the mine count
        num_mines = MIN_MINES
        self.assertEqual(num_mines, MIN_MINES, f"Number of mines should not go below {MIN_MINES}")

        # Attempt to set below minimum
        num_mines -= 1
        self.assertEqual(num_mines, MIN_MINES, "Number of mines should not go below minimum limit.")

if __name__ == '__main__':
    # Make sure the game is not initialized when running tests
    pygame.quit()  # Ensure Pygame is cleanly exited
    unittest.main()
