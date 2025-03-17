GENDER_CHOICES = [
    ('', '-- Select Gender --'),
    ('M', 'Male'),
    ('F', 'Female'),
]

BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
    ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')
]

USER_TYPE_CHOICES = [
    ('AD', 'Admin'),
    ('TE', 'Teacher'),
    ('ST', 'Student'),
]

EMPLOYEE_DEPARTMENT_CHOICES = [
    ('ADM', 'Admission'),
    ('RCP', 'Receptionist'),
    ('ACT', 'Accountant')
]

COURSE_LEVEL_CHOICES = [
    ('DP', 'Diploma'), ('UG', 'Undergraduate'), ('PG', 'Postgraduate')
]

COURSE_SYSTEM_CHOICES = [
    ('SEM', 'Semester'),
    ('ANL', 'Anual')
]

ADDRESS_TYPE_CHOICES = [
    ('PR', 'Permanent'), ('PS', 'Present')
]

STATE_CHOICES = [
    ('AN', 'Andaman and Nicobar Islands'), ('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'),
    ('AS', 'Assam'), ('BR', 'Bihar'), ('CH', 'Chandigarh'), ('CG', 'Chhattisgarh'), ('DD', 'Dadra and Nagar Haveli'),
    ('DL', 'Delhi'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'),
    ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('LD', 'Lakshadweep'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'),
    ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Odisha'), ('PY', 'Puducherry'), ('WB', 'West Bengal'),
]

RELATION_CHOICES = [
    ('F', 'Father'), ('M', 'Mother'), ('B', 'Brother'), ('S', 'Sister'), ('O', 'Other')
]

LATEST_QUALIFICATION_CHOICES = [
    ('10', '10th'), ('12', '12th'), ('UG', 'Undergraduate'), ('PG', 'Postgraduate')
]

SEMESTER_CHOICE = [
    (1, 'Semester 1'),
    (2, 'Semester 2'),
    (3, 'Semester 3'),
    (4, 'Semester 4'),
    (5, 'Semester 5'),
    (6, 'Semester 6'),
    (7, 'Semester 7'),
    (8, 'Semester 8'),
]

GRADE_NAME_CHOICES = [
    ('SEM', 'Semester')
]

FEE_TYPE_CHOICES = [
    ('CRS', 'Course Fee'),
    ('ADM', 'Admission Fee'),
    ('EXM', 'Exam Fee')
]

DAY_CHOICES = [
    ('MON', 'Monday'),
    ('TUE', 'Tuesday'),
    ('WED', 'Wednesday'),
    ('THU', 'Thursday'),
    ('FRI', 'Friday'),
    ('SAT', 'Saturday')
]