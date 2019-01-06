from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateField()

    def __str__(self):
        return(self.name, self.birthdate)


class TestType(models.Model):
    type = models.CharField(max_length=200)


class PatientsTest(models.Model):
    date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    testType = models.ForeignKey(TestType, on_delete=models.CASCADE)


class BloodCountTest(models.Model):
    hb = models.FloatField()
    rbc = models.FloatField()
    hct = models.FloatField()
    wbc = models.FloatField()
    patientsTest = models.ForeignKey(PatientsTest, on_delete=models.CASCADE)



