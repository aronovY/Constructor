from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from constructor import models


@login_required
def home(request):
    template = 'home.html'
    return render(request, template)


@login_required
def parts_view(request):
    if request.GET:
        return render(request, 'product_list.html')
    return render(request, 'parts.html')


@login_required
def settings(request):
    return render(request, 'settings.html')


@login_required
def history(request):
    history_setup = models.Setup.objects.filter(user_id=request.user.id).all()
    for obj in history_setup:
        if obj.video_card == None or obj.case == None:
            obj.delete()
    return render(request, 'history.html', context={'history_setup': history_setup})


class ProdListView(LoginRequiredMixin, generic.ListView):
    model = models.Product
    template_name = 'product_list.html'
    paginate_by = 15
    category = int()

    def get_queryset(self):
        return models.Product.objects.filter(category_id=self.category)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['count'] = models.Product.objects.filter(category_id=self.category).count()
        return context_data

    def get(self, request, *args, **kwargs):
        self.category = kwargs['category']
        return super().get(request, *args, **kwargs)


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Product
    template_name = 'detail.html'


