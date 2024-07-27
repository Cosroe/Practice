import json
import os

import numpy as np


HERE = os.path.dirname(__file__)


def random_params(n_machines, n_jobs, t_span, seed=None):
    np.random.seed(seed)
    M = [m for m in range(n_machines)]
    J = [j for j in range(n_jobs)]
    tech = [
        np.random.permutation(M).astype(int).tolist()
        for j in J
    ]
    processing = [
        {
            "machine": m,
            "job": j,
            "time": int(np.random.choice(range(t_span[0], t_span[1] + 1)))
        }
        for m in M
        for j in J
    ]
    return {"technology": tech, "processing": processing}


if __name__ == "__main__":
    for pair in [(3, 4), (5, 6), (6, 8), (8, 8), (8, 10), (10, 10)]:
        data = random_params(pair[0], pair[1], (5, 20), 12)
        with open(os.path.join(HERE, f"random_{pair[0]}_{pair[1]}.json"), mode="w") as file:
            json.dump(data, file, default=str, indent=4)
