favourite_chais = [
    "Masala Chai","Green Chai","Masala Chai",
    "Lemon Chai","Green Chai","Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chais}
print(unique_chai)

recipes = {
    "Masala Chai" :["ginger", "cardamom","clove"],
    "Elaichi Chai" :["cardamom","milk"],
    "Spicy Chai" :["ginger","black pepper","clove"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}