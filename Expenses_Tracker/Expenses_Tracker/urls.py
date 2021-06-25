from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Expenses_tracker.expenses.urls')),
    path('profile/', include('Expenses_tracker.profiles.urls')),
]
