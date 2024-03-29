from typing import Any

from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages

from .forms import RegisterForm


class RegisterView(View):
    template_name = "users/signup.html"
    form_class = RegisterForm

    def dispatch(self, request, *args: Any, **kwargs: Any):
        if request.user.is_authenticated:
            return redirect("quotes:root")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request,
                             message=f"Congratulations, {username}. Your account has been successfully created.")
            return redirect(reverse_lazy("users:login"))
        return render(request, self.template_name, {"form": form})


def logout_view(request):
    messages.info(request, 'You have logged out. Thank you for using our website!')
    logout(request)
    return redirect('/')
