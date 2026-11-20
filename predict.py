THRESHOLD = 0.5


def predict(scores):
    """Nhãn có điểm cao nhất trong dict {nhãn: điểm}.

    Trả về "unknown" nếu điểm cao nhất nhỏ hơn THRESHOLD.
    """
    label = max(scores, key=scores.get)
    if scores[label] < THRESHOLD:
        return "unknown"
    return label
