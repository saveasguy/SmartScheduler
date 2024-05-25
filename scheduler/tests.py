import unittest

from scheduler import controllers, models


class FindByTitleTests(unittest.TestCase):
    def test_projects_default_behavior(self):
        N_PROJECTS = 10
        projects = []
        for i in range(N_PROJECTS):
            prj = models.Project()
            prj.id = str(i)
            prj.title = f"prj{i}"
            projects.append(prj)

        for i in range(N_PROJECTS):
            prj_title = f"prj{i}"
            prj = controllers.find_by_title(projects, prj_title)
            self.assertEqual(prj.id, str(i))
            self.assertEqual(prj.title, prj_title)

    def test_boards_default_behavior(self):
        N_BOARDS = 10
        boards = []
        for i in range(N_BOARDS):
            board = models.Board()
            board.id = str(i)
            board.title = f"board{i}"
            boards.append(board)

        for i in range(N_BOARDS):
            board_title = f"board{i}"
            board = controllers.find_by_title(boards, board_title)
            self.assertEqual(board.id, str(i))
            self.assertEqual(board.title, board_title)

    def test_projects_exception(self):
        prj1 = models.Project()
        prj1.id = "1"
        prj1.title = "prj1"
        projects = [prj1, prj1]
        multiple_projects_detected = False
        try:
            controllers.find_by_title(projects, "prj1")
        except Exception:
            multiple_projects_detected = True
        self.assertTrue(multiple_projects_detected)
        no_projects_detected = False
        try:
            controllers.find_by_title(projects, "prj1")
        except Exception:
            no_projects_detected = True
        self.assertTrue(no_projects_detected)

    def test_boards_exception(self):
        board1 = models.Board()
        board1.id = "1"
        board1.title = "board1"
        boards = [board1, board1]
        multiple_boards_detected = False
        try:
            controllers.find_by_title(boards, "board1")
        except Exception:
            multiple_boards_detected = True
        self.assertTrue(multiple_boards_detected)
        no_boards_detected = False
        try:
            controllers.find_by_title(boards, "board1")
        except Exception:
            no_boards_detected = True
        self.assertTrue(no_boards_detected)
