from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f"{self.name} 전문의"
    
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, through='Reservation')  ###### Manytomany
    name = models.TextField()
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk}번 환자 {self.name}"

# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)     # FK
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)   # FK

#     def __str__(self):
#         return f"{self.doctor_id}번 의사의 {self.patient_id}번 환자"
    
#     # 각각은 독립적인 형태를 유지하고, 관계를 기억해주는 테이블을 만들어 관계를 위임하면
#     # M : N 관계를 구성했다고 할 수 있다.
#     # 하지만 django는 이마저도 대신 해줌

#### Many-to-many Field through 와 같은 내용

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)     # FK
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)   # FK
    symptom = models.TextField()
    reservation_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.doctor.pk}번 의사의 {self.patient.pk}번 환자"
    
