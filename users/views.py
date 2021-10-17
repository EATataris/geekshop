from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, redirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileFrom
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin


from baskets.models import Basket, User
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
# Create your views here.


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'GeekShop - Авторизация'
        return context


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'GeekShop - Регистрация'
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save()
            if send_verify_link(user):
                messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect(self.success_url)
        return redirect(self.success_url)


class UserProfileView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserProfileFrom
    template_name = 'users/profile.html'
    success_message = 'Информация успешно обновлена!'
    error_message = 'Нельзя обновить инфу!'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(object_list=None, **kwargs)
    #     context['title'] = 'GeekShop - Личный кабинет'
    #     context['baskets'] = Basket.objects.filter(user=self.request.user)
    #     return context

    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'pk': self.object.pk})

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class Logout(LogoutView):
    template_name = 'products/index.html'

# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))


def send_verify_link(user):
    verify_link = reverse('users:verify', args=[user.email, user.activation_key])
    title = f'Подтверждение учетной записи {user.username}'
    message = f'Для подтверждения учетной записи {user.username} на портале {settings.DOMAIN_NAME} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.activation_key = ''
            user.activation_created = None
            user.is_active = True
            user.save()
            auth.login(request, user)
        return render(request, 'users/verification.html')
    except Exception as e:
        print(f'error activation user : {e.args}')
        return HttpResponseRedirect(reverse('index'))

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileFrom(instance=request.user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Информация успешно обновлена!')
#             return HttpResponseRedirect(reverse('users:profile'))
#     else:
#         form = UserProfileFrom(instance=request.user)
#     context = {
#         'title': 'GeekShop - Личный кабинет',
#         'form': form,
#         'baskets': Basket.objects.filter(user=request.user),
#     }
#     return render(request, 'users/profile.html', context)

# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user and user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = UserLoginForm()
#     context = {
#         'title': 'GeekShop - Авторизация',
#         'form': form,
#     }
#     return render(request, 'users/login.html', context)

# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Регистрация прошла успешно!')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm()
#
#     context = {
#         'title': 'GeekShop - Регистрация',
#         'form': form,
#     }
#     return render(request, 'users/registration.html', context)