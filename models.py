from django.db import models
from django.contrib.auth.models import User

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.CharField("No. staf", max_length=30, blank=True)
    position = models.CharField("Jawatan", max_length=100, blank=True)
    phone = models.CharField("No. telefon", max_length=30, blank=True)
    is_approver = models.BooleanField("Pelulus", default=False)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Attendance(models.Model):
    STATUS_CHOICES = [
        ("HADIR", "Hadir"),
        ("LEWAT", "Lewat"),
        ("CUTI", "Cuti"),
        ("TUGAS_RASMI", "Tugas Rasmi"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField("Tarikh")
    check_in = models.DateTimeField("Masa masuk", null=True, blank=True)
    check_out = models.DateTimeField("Masa keluar", null=True, blank=True)
    check_in_lat = models.FloatField(null=True, blank=True)
    check_in_lng = models.FloatField(null=True, blank=True)
    check_out_lat = models.FloatField(null=True, blank=True)
    check_out_lng = models.FloatField(null=True, blank=True)
    distance_in_m = models.FloatField(null=True, blank=True)
    distance_out_m = models.FloatField(null=True, blank=True)
    selfie_in = models.ImageField(upload_to="selfies/", null=True, blank=True)
    selfie_out = models.ImageField(upload_to="selfies/", null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="HADIR")
    notes = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ("user", "date")
        ordering = ["-date", "user__first_name"]

    def __str__(self):
        return f"{self.user} - {self.date}"

class LeaveRequest(models.Model):
    TYPE_CHOICES = [
        ("CUTI_REHAT", "Cuti Rehat"),
        ("CUTI_SAKIT", "Cuti Sakit"),
        ("CUTI_KHAS", "Cuti Khas"),
        ("LAIN", "Lain-lain"),
    ]
    STATUS_CHOICES = [
        ("MENUNGGU", "Menunggu"),
        ("DILULUSKAN", "Diluluskan"),
        ("DITOLAK", "Ditolak"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    attachment = models.FileField(upload_to="leave/", null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="MENUNGGU")
    admin_note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

class OfficialDuty(models.Model):
    STATUS_CHOICES = [
        ("MENUNGGU", "Menunggu"),
        ("DILULUSKAN", "Diluluskan"),
        ("DITOLAK", "Ditolak"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True)
    attachment = models.FileField(upload_to="official_duty/", null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="MENUNGGU")
    admin_note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]


class DailyQR(models.Model):
    date = models.DateField(unique=True)
    token = models.CharField(max_length=64, unique=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"QR {self.date}"
