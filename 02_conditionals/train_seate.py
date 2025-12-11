seat_type = input("Enter seat type(sleeper/AC/luxury/General):").lower()

match seat_type:
    case "sleeper":
        print(f"sleeper - No AC, beds available")
    case "ac":
        print(f"AC - Air Condition , comfy ride")
    case "luxury":
        print(f"luxury - Premium seat with meals")
    case "general":
        print(f"general - Cheapest option, no reservation")
    case _:
        print(f"Invalid seat type")