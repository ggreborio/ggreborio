"""
generate_data.py
Creates a fully SYNTHETIC daily behavior dataset for a fictional student ("Student A").
No real student, school, or district data is used. Patterns are invented to
mirror the kind of data an RBT might collect in a general education setting.

Run:  python generate_data.py
Out:  data/synthetic_daily_data.csv
"""

from pathlib import Path

import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=42)  # fixed seed = same data every run

# ---- 1. School days: ~10 weeks of weekdays, fictional start date ----
dates = pd.bdate_range(start="2025-09-02", periods=50)
df = pd.DataFrame({"date": dates})
df["day_of_week"] = df["date"].dt.day_name()
df["week"] = ((df["date"] - df["date"].min()).dt.days // 7) + 1

# ---- 2. Low demand day flag (about 1 in 5 days) ----
df["low_demand_day"] = rng.choice(["Yes", "No"], size=len(df), p=[0.2, 0.8])
low = (df["low_demand_day"] == "Yes").to_numpy()

# Behavior is a bit worse on Mondays and Fridays (a common pattern)
day_boost = df["day_of_week"].map(
    {"Monday": 1.2, "Tuesday": 1.0, "Wednesday": 1.0, "Thursday": 1.0, "Friday": 1.15}
).to_numpy()

# Low demand days reduce behavior; supports help slightly over time
demand_factor = np.where(low, 0.4, 1.0)
trend = 1 - 0.004 * np.arange(len(df))  # very slight improvement


def behavior_counts(base_rate):
    """Daily frequency counts drawn from a Poisson distribution."""
    return rng.poisson(base_rate * demand_factor * day_boost * trend)


# ---- 3. Daily frequency counts ----
df["off_task"] = behavior_counts(14)
df["demand_refusal"] = behavior_counts(7)
df["elopement"] = behavior_counts(3)
df["unsafe_physical"] = behavior_counts(2)

# ---- 4. Reinforcer points (earned out of a fixed daily maximum) ----
df["points_possible"] = 20
p_points = np.where(low, 0.65, 0.4)
df["points_earned"] = rng.binomial(df["points_possible"], p_points)

# ---- 5. IEP goal tracking: opportunities and correct responses ----
# Goal 10: chooses an appropriate accommodation (<=2 prompts) and returns in 2-3 min
# Goal 11: initiates a non-preferred task within 1 min with a visual support
# Goal 12: stays in assigned area / with staff (no elopement) during instruction + transitions
goal_settings = {
    "g10": {"opps": (3, 7), "p_normal": 0.35, "p_low": 0.60},
    "g11": {"opps": (4, 8), "p_normal": 0.30, "p_low": 0.55},
    "g12": {"opps": (4, 8), "p_normal": 0.50, "p_low": 0.75},
}

for goal, s in goal_settings.items():
    opps = rng.integers(s["opps"][0], s["opps"][1] + 1, size=len(df))
    p = np.where(low, s["p_low"], s["p_normal"]) + 0.003 * np.arange(len(df))
    df[f"{goal}_opps"] = opps
    df[f"{goal}_correct"] = rng.binomial(opps, np.clip(p, 0, 0.95))

# ---- 6. Short synthetic narrative notes ----
def make_note(row):
    if row["low_demand_day"] == "Yes":
        return rng.choice([
            "Low demand day. Mostly engaged in preferred activities; accepted breaks with few prompts.",
            "Modified schedule today. Needed one prompt to use choice board; returned to group.",
        ])
    if row["elopement"] >= 4:
        return rng.choice([
            "Left assigned area multiple times during transitions. Staff redirected back each time.",
            "Eloped during independent work; brought back with visual support and two prompts.",
        ])
    if row["unsafe_physical"] >= 3:
        return rng.choice([
            "Threw materials after a work request. Area cleared; student moved to calm corner.",
            "Unsafe physical behavior during a transition. Staff blocked and redirected safely.",
        ])
    if row["demand_refusal"] >= 8:
        return rng.choice([
            "Refused most non-preferred tasks. First/then board helped on a few attempts.",
            "Verbal refusal during math. Chose a movement break after the second prompt.",
        ])
    return rng.choice([
        "Typical day. Off-task behavior was frequent; responded to some choice board options.",
        "Earned part of her reinforcer points. Needed repeated prompts to start tasks.",
        "Participated briefly with the group before requesting a break.",
    ])


df["narrative_note"] = df.apply(make_note, axis=1)

# ---- 7. Save ----
out = Path("data")
out.mkdir(exist_ok=True)
df.to_csv(out / "synthetic_daily_data.csv", index=False)
print(f"Saved {len(df)} rows to {out / 'synthetic_daily_data.csv'}")
