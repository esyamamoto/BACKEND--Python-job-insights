from src.pre_built.counter import count_ocurrences


def test_counter():
    # arquivo data>jobs.csv , ver quantas vezes a palavra aparece
    assert count_ocurrences("data/jobs.csv", "Python") == 1639
    assert count_ocurrences("data/jobs.csv", "Javascript") == 122
