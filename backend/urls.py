from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Home view for the root URL
def home_view(request):
    return HttpResponse("Welcome to the Invoice Management System!")

# URL patterns
urlpatterns = [
    path('', home_view, name='home'),  # Root URL
    path('admin/', admin.site.urls),  # Admin panel
    path('api/', include('invoices.urls')),  # Include URLs from the invoices app
]