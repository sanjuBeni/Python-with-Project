
class StaticMethodClass:

    @staticmethod
    def km_to_meter(km):
        return km * 1000
    
    @staticmethod
    def is_valid_age(age):
        return age >= 18

    @staticmethod
    def capitalize_text(text):
        return text.capitalize()
    
    