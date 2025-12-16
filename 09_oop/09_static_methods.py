class ChaiUtils:
    @staticmethod
    def clean_ingerdients(text):
       return [item.strip() for item in text.split(",")]
    
    
raw = "water , milk , ginger , honey "

obj = ChaiUtils()
cleaned  = ChaiUtils.clean_ingerdients(raw)
print(cleaned)