from src.simulation import run_simulation

def test_simulation_runs():
    """Просто проверка на то, что симуляция работает"""
    run_simulation(steps=10, seed=42)
    assert True