chai_type = "Ginger chai"
customer_name = "Priya"

print(f" Order for {customer_name} : {chai_type} Please !")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[0:8]}")
print(f"Last word: {chai_description[12:]}")
print(f"Last word: {chai_description[::-1]} ")

label_text = "Résumé"
encoded_text = label_text.encode()
print(f"Non Encoded label: {encoded_text}")
decoded_label = encoded_text.decode()
print(f"Encoded label: {decoded_label}")