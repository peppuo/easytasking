from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


urlpatterns = [
    path('',
         PasswordResetView.as_view(),
         #{'post_reset_redirect': reverse_lazy('password_reset_done')},
         name='password_reset'
         ),
    path('done/',
         PasswordResetDoneView.as_view(),
         name='password_reset_done'
         ),
    path('reset/<uidb64>/<token>/',  # token generated for each user
         PasswordResetConfirmView.as_view(),
        # {'post_reset_redirect': reverse_lazy('password_reset_complete')},
         name='password_reset_confirm'
         ),
    path('reset/done/',
         PasswordResetCompleteView.as_view(),
         name='password_reset_complete'
         ),
]
