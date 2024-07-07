class Citizen:
    def role_duties(self):
        return "Citizen duties"

class Politician(Citizen):
    def role_duties(self):
        return "Politician duties"

class PublicServant(Citizen):
    def role_duties(self):
        return "Public Servant duties"

class Mayor(Politician, PublicServant):
    def role_duties(self):
        return "Mayor duties"

class Voter(Citizen):
    def role_duties(self):
        return "Voter duties"

class ElectedOfficial(Voter, Candidate):
    def role_duties(self):
        return "Elected official duties"

class Activist(Citizen):
    def role_duties(self):
        return "Activist duties"

class ActivistPolitician(Activist, Politician):
    def role_duties(self):
        return "Activist Politician duties"

class Worker(Citizen):
    def role_duties(self):
        return "Worker duties"

class WorkingPolitician(Worker, Politician):
    def role_duties(self):
        return "Working Politician duties"

def mro_sequence(cls):
    return [c.__name__ for c in cls.mro()]


class_name = input()

cls = globals()[class_name]

print(mro_sequence(cls))




    
