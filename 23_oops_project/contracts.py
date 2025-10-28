# Contracts for entities like Student, Trainer, Admin etc

from abc import ABC, abstractmethod

class Personable(ABC):
    # set personal details like Student, Trainer, Admin etc
    @abstractmethod
    def set_personal_details(self,id,name,age,email,mobile):
        pass

    # display personal details like Student, Trainer, Admin etc
    @abstractmethod
    def person_complete_info(self):
        pass

# In future make payments as mandatory for every entity
class Payable(ABC):
    @abstractmethod
    def person_payment_info(self):
        pass