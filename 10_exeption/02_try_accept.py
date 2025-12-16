chai_menu = {"masala" :30, "ginger":40}

try:
    chai_menu["elaichi"]
except KeyError:
    print("Key that you are access does not exists")

