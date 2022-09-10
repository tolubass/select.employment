class Students:
    def __init__(self,School, Location, Class, Age, Uniform, Idcard, Textbooks ):
        self.Schoolname = School
        self. Location = Location
        self.Age = Age
        self.MyClass = Class
        self.Uniforms = Uniform
        self.schoolIdcard = Idcard
        self.schoolTextbook = Textbooks
    def output(self):
        return " My name is Ojo Praise , i am from " + self.Schoolname + ", located at " + self.Location + ", i am in " + self.MyClass + " with different " + self.schoolTextbook

class Child(Students):
    def __init__(self,School, Location, Class, Age, Uniform, Idcard, Textbooks,name, hobby,sex):
        super(Child, self).__init__(School, Location, Class, Age, Uniform, Idcard, Textbooks)
        self.name = name
        self.hobby = hobby
        self.sex = sex
    def speak(self, lang):
        s = self.output() + ".My name is " + self.name + ", I am a " + self.sex + " and I am very fluent in speaking " + lang
        return s
class SecondaryPupil(Child):
    def __init__(self,School, Location, Class, Age, Uniform, Idcard, Textbooks,name, hobby,sex,ssce,jamb,post):
        super(SecondaryPupil, self).__init__(School, Location, Class, Age, Uniform, Idcard,Textbooks,name, hobby,sex )
        self.ssce = ssce
        self.jamb = jamb
        self.post = post
    def results(self):
        a = self.name + ", " + self.post + " of " + self.Schoolname + " who is in  " + self.MyClass + " scored " + self.jamb + " in JAMB"
        return a
    def add_numbers(num1,num2):
        return num1 + num2