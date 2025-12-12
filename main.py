from Planner import bfs_planner
from controller import run_with_recomposition, run_with_repair
from executor import execute_plan
from travel_domain import build_travel_domain, TripRequest, UserProfile, PaymentInfo, Itinerary


def main():
    domain = build_travel_domain()
    initial_data = {
        TripRequest: {"destination": "Paris", "dates": "2024-09-01 to 2024-09-10"},
        UserProfile: {"name": "Alice", "preferences": {"seat": "window"}},
        PaymentInfo: {"card_number": "1234-5678-9012-3456", "expiry": "12/26"},
    }
    initial_state = {TripRequest, UserProfile, PaymentInfo}
    goal_type = Itinerary
    final_data = run_with_recomposition(initial_data, initial_state, domain, goal_type)
    # repair = run_with_repair(domain, initial_data, initial_state, goal_type)


if __name__ == "__main__":
    main()