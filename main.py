import json

def load_drones():
    with open("drones.json") as f:
        return json.load(f)

def score_drone(drone):
    # Custom scoring formula based on mission
    base_score = (
        drone["battery"] * 0.5
        - drone["distance"] * 0.3
        - drone["obstacles"] * 15
        + drone["payload"] * 10
    )

    if drone["mission"] == "rescue":
        base_score += 20  # rescue priority boost
    elif drone["mission"] == "delivery":
        base_score += 10

    return base_score

def select_best_drone(drones):
    scored = [(d, score_drone(d)) for d in drones]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[0], scored

if __name__ == "__main__":
    fleet = load_drones()
    best, all_scores = select_best_drone(fleet)

    print("🚀 Best Drone Selected:")
    print(f"ID: {best[0]['id']}, Score: {best[1]:.2f}")
    print("Details:", best[0])
