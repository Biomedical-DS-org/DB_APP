from django.urls import path
from .import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'main'

urlpatterns = [
    path("", views.login_request, name="login"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("records/", views.records, name='records'),
    path("search/", views.search, name='search'),
    path("details/?<pk>\d+/$)", views.details, name='details'),
    path("filtered_records/", views.filtered_records, name='filtered_records'),
    path("filtered_details/", views.filtered_details, name='filtered_details'),
    path("fake_search/", views.fake_search, name='fake_search'),
    path("change_password/", views.change_password, name='change_password'),
    path("reset_password/", PasswordResetView.as_view(), name='reset_password'),
    path("reset_password/done", PasswordResetDoneView.as_view(), name='password_reset_done'),
    path("reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P/<token>.+/$)", PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path("reset_password/complete", PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path("export/", views.export, name='export')
]
