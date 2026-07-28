from django.contrib import admin
from .models import TeacherProfile, Attendance, LeaveRequest, OfficialDuty, DailyQR

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "staff_id", "position", "is_approver")
    search_fields = ("user__username", "user__first_name", "user__last_name", "staff_id")

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "check_in", "check_out", "status", "distance_in_m")
    list_filter = ("date", "status")
    search_fields = ("user__username", "user__first_name", "user__last_name")

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ("user", "leave_type", "start_date", "end_date", "status")
    list_filter = ("status", "leave_type")

@admin.register(OfficialDuty)
class OfficialDutyAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "location", "start_date", "end_date", "status")
    list_filter = ("status",)


@admin.register(DailyQR)
class DailyQRAdmin(admin.ModelAdmin):
    list_display = ("date", "token", "active", "created_at")
    list_filter = ("active", "date")
    readonly_fields = ("created_at",)
