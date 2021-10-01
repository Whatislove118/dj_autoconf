from django.urls import path

from account.views import UserViewSet

register_user = UserViewSet.as_view({
    'post': 'create'
})
retrieve_user = UserViewSet.as_view({
    'get': 'retrieve'
})
login_user = UserViewSet.as_view({
    'post': 'login'
})
urlpatterns = [
    path('account/', register_user, name='register'),
    path('account/<int:id>/', retrieve_user, name='retrieve'),
    path('account/login/', login_user, name='login'),

]