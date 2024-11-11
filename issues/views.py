from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.urls import reverse_lazy
from .models import Issue, Status
from accounts.models import CustomUser, Role, Team

class IssueListView(LoginRequiredMixin, ListView):
    template_name = "posts/list.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        role = Role.objects.get(name="product owner")
        team_po = (
            CustomUser.objects
            .filter(team=user.team)
            .filter(role=role)
        )
        to_do = Status.objects.get(name="to do")
        context["to_do_list"] = (
            Issue.objects
            .filter(status=to_do)
            .filter(reporter=team_po[0])
            .order_by("created_on").reverse()
        )
        in_progress = Status.objects.get(name="in progress")
        context["in_progress_list"] = (
            Issue.objects
            .filter(status=in_progress)
            .filter(reporter=team_po[0])
            .order_by("created_on").reverse()
        )
        done = Status.objects.get(name="done")
        context["done_list"] = (
            Issue.objects
            .filter(status=done)
            .filter(reporter=team_po[0])
            .order_by("created_on").reverse()
        )

        return context


class IssueDetailView(LoginRequiredMixin, DetailView):
    template_name = "issues/detail.html"
    model = Issue

class IssueCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = "issues/new.html"
    model = Issue
    fields = [
        "summary", "description", "assignee",
        "priority", "status"
    ]

    def test_func(self):
        role = Role.objects.get(name="product owner")
        return self.request.user.role == role

    def form_valid(self, form):
        form.instance.reporter = self.requester.user
        return super().form_valid(form)
    
class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "issues/update.html"
    model = Issue
    fields = [
        "summary", "description", "assignee",
        "priority", "status"
    ]

    def test_func(self):
        po_role = Role.objects.get(name="product owner") 
        product_owner= (
            CustomUser.objects
            .filter(role=po_role)
            .filter(team=self.request.user.team)
        )
        if product_owner:
            issue = self.get_object()
            return issue.reporter == product_owner[0]
        return False

class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "issues/delete.html"
    model = Issue
    success_url = reverse_lazy("list")

    def test_func(self):
        po_role = Role.objects.get(name="product owner") 
        product_owner= (
            CustomUser.objects
            .filter(role=po_role)
            .filter(team=self.request.user.team)
        )
        if product_owner:
            issue = self.get_object()
            return issue.reporter == product_owner[0]
        return False

