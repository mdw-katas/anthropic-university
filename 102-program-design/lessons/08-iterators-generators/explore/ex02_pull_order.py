"""Exploration: generators run interleaved with their consumer — pull, not push.

Both stages drop breadcrumbs as they work. Does the producer finish
before the consumer starts (push), or do they alternate (pull)? Predict
the exact trail for consuming TWO items.

Fill the PREDICT_* constants, run this file, then:
uni grade 102/explore-08
"""

PREDICT_TRAIL = None  # e.g. ["produce 1", "produce 2", "consume 1", ...]
PREDICT_PRODUCED_COUNT = None  # how many values were produced in total?


def scenario():
    trail = []

    def produce():
        for n in [10, 20, 30, 40]:
            trail.append(f"produce {n}")
            yield n

    stream = produce()
    for value in stream:
        trail.append(f"consume {value}")
        if value >= 20:
            break
    return trail


if __name__ == "__main__":
    trail = scenario()
    for crumb in trail:
        print(crumb)
    produced = len([c for c in trail if c.startswith("produce")])
    print(f"(produced {produced} of 4 available values)")
