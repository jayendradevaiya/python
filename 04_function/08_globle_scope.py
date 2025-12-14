chai_type = "Plain"

def front_desk():
    chai_type = "Elaichi " 
    def kitchen():
        global chai_type
        chai_type = "Irani"
    kitchen()
front_desk()
print("final globle chai:", chai_type)