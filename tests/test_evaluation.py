from app.evaluation import evaluate_recall_at_one


def test_demo_retrieval_recall_at_one() -> None:
    assert evaluate_recall_at_one() == 1.0
