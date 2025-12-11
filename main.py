from Planner import bfs_planner
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
    plan = bfs_planner(domain, initial_state, goal_type)
    print([a.name for a in plan] if plan else "No plan found")
    executed = execute_plan(plan, initial_data)



if __name__ == "__main__":
    main()