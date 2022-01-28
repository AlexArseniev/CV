class CV:
    next_id = 0

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id

    def __init__(self, first_name=None, last_name=None, age=None, date_of_birth=None,
                 contact_no=None, sex=None, nationality=None, address=None, education=None, exp=None,
                 technologies=[]):


        self.technologies = technologies
        self.exp = exp
        self.education = education
        self.address = address
        self.nationality = nationality
        self.sex = sex
        self.contact_no = contact_no
        self.date_of_birth = date_of_birth
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def display(self):
        print(f"CV ID:{self.next_id}")
        print(f"NAME :{self.first_name}")
        print(f"LAST NAME :{self.last_name}")
        print(f"AGE :{self.age}")
        print(f"SEX :{self.sex}")
        print(f"NATIONALITY :{self.nationality}")
        print(f"DATE OF BIRTH:  {self.date_of_birth}")
        print(f"ADDRESS : {self.address}")
        print(f"CONTACT NO: {self.contact_no}")
        print("EDUCATION :", self.education)
        print("EXPERIENCE :", self.exp)
        print("TECHNOLOGIES :", self.technologies)

