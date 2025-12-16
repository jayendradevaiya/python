def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError ("We don't know that flavor")
    except ValueError as e :
        print("Error: ",e)
    else:
        print(f"{flavor} chai is sreved")

    finally:
        print("Next customer plase")

serve_chai("masala")
serve_chai("unknown")
