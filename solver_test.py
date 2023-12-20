import solver


def is_solved():
    assert not solver.solver(10)


def test_solver():
    assert solver.solver(2e6) == 142913828922
