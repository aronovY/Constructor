import re
from itertools import chain

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from constructor import models


@login_required
def start_constructor(request):
    setup = models.Setup.objects.create(user_id=request.user.id)
    if request.GET:
        return render(request, 'constructor_templates/first_component.html', context={'id': setup.id})
    return render(request, 'constructor_templates/start_constructor.html', context={'id': setup.id})


class FirstSelectLisView(LoginRequiredMixin, generic.ListView):
    model = models.Product
    template_name = 'constructor_templates/first_component.html'
    paginate_by = 10
    id_setup = int()
    components = str()

    def get_queryset(self):
        return models.Product.objects.filter(name__contains=self.components).all()

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['id'] = self.id_setup
        return context_data

    def get(self, request, *args, **kwargs):
        self.id_setup = kwargs['id']
        self.components = kwargs['manufacturer']
        return super().get(request, *args, **kwargs)


class SecondSelectLisView(LoginRequiredMixin, generic.ListView):
    query_sets = []
    model = models.Product
    template_name = 'constructor_templates/second_component_sel.html'
    paginate_by = 10
    id_setup = int()
    component = None

    def get_queryset(self):
        if 'Socket' in self.component.characteristics:
            socket = self.component.characteristics['Socket']
            self.query_sets.append(models.Product.objects.filter(category_id=2).filter(characteristics__Socket=socket))
            self.query_sets.append(models.Product.objects.filter(category_id=2).filter(characteristics__Сокет=socket))

        else:
            socket = self.component.characteristics['Сокет']
            self.query_sets.append(models.Product.objects.filter(category_id=2).filter(characteristics__Socket=socket))
            self.query_sets.append(models.Product.objects.filter(category_id=2).filter(characteristics__Сокет=socket))

        return list(chain(*self.query_sets))

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['id'] = self.id_setup
        return context_data

    def get(self, request, *args, **kwargs):
        self.id_setup = kwargs['id']
        self.component = models.Product.objects.get(id=kwargs['component'])
        setup = models.Setup.objects.get(id=self.id_setup)
        setup.cpu = self.component
        setup.save()
        return super().get(request, *args, **kwargs)


class ThirdSelectLisView(LoginRequiredMixin, generic.ListView):
    model = models.Product
    template_name = 'constructor_templates/third_component_sel.html'
    paginate_by = 10
    id_setup = int()
    query_sets = []
    component = None

    def get_queryset(self):
        if 'Память' in self.component.characteristics:
            if 'DDR3' in self.component.characteristics['Память']:
                return models.Product.objects\
                    .filter(category_id=4)\
                    .filter(name__contains='DDR3')
            elif 'DDR4' in self.component.characteristics['Память']:
                return models.Product.objects \
                    .filter(category_id=4) \
                    .filter(name__contains='DDR4')
        elif 'Тип памяти' in self.component.characteristics:
            if 'DDR3' in self.component.characteristics['Тип памяти']:
                return models.Product.objects \
                    .filter(category_id=4) \
                    .filter(name__contains='DDR3')
            elif 'DDR4' in self.component.characteristics['Тип памяти']:
                return models.Product.objects \
                    .filter(category_id=4) \
                    .filter(name__contains='DDR4')
        else:
            return models.Product.objects.filter(category_id=4)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['id'] = self.id_setup
        return context_data

    def get(self, request, *args, **kwargs):
        self.id_setup = kwargs['id']
        self.component = models.Product.objects.get(id=kwargs['component'])
        setup = models.Setup.objects.get(id=self.id_setup)
        setup.motherboard = self.component
        setup.save()
        return super().get(request, *args, **kwargs)


@login_required
def which_video_card(request, id, component):
    setup = models.Setup.objects.get(id=id)
    setup.ram = models.Product.objects.get(id=component)
    setup.save()
    return render(request, 'constructor_templates/which_video_card.html', context={'id': id, 'component': component})


class FourthSelectLisView(LoginRequiredMixin, generic.ListView):
    model = models.Product
    template_name = 'constructor_templates/fourth_component.html'
    paginate_by = 10
    id_setup = int()
    memory = str()
    card = str()

    def get_queryset(self):
        if self.memory == 'All':
            return models.Product.objects.filter(category_id=3).filter(name__contains=self.card)
        else:
            return models.Product.objects.filter(category_id=3).filter(name__contains=self.card).filter(name__contains=self.memory).all()

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['id'] = self.id_setup
        return context_data

    def get(self, request, *args, **kwargs):
        self.id_setup = kwargs['id']
        self.memory = kwargs['memory']
        self.card = kwargs['card']
        return super().get(request, *args, **kwargs)


class FifthSelectLisView(LoginRequiredMixin, generic.ListView):
    model = models.Product
    template_name = 'constructor_templates/fifth_component.html'
    paginate_by = 10
    id_setup = int()
    component = None

    def get_queryset(self):
        return models.Product.objects.filter(category_id=5).filter(name__contains='Кулер для процессора')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['id'] = self.id_setup
        return context_data

    def get(self, request, *args, **kwargs):
        self.id_setup = kwargs['id']
        self.component = models.Product.objects.get(id=kwargs['component'])
        setup = models.Setup.objects.get(id=self.id_setup)
        setup.video_card = self.component
        setup.save()
        return super().get(request, *args, **kwargs)


class SixthSelectLisView(LoginRequiredMixin, generic.ListView):
    model = models.Product
    template_name = 'constructor_templates/sixth_component.html'
    paginate_by = 10
    id_setup = int()
    component = None

    def get_queryset(self):
        return models.Product.objects.filter(category_id=6)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['id'] = self.id_setup
        return context_data

    def get(self, request, *args, **kwargs):
        self.id_setup = kwargs['id']
        self.component = models.Product.objects.get(id=kwargs['component'])
        setup = models.Setup.objects.get(id=self.id_setup)
        setup.cooler = self.component
        setup.save()
        return super().get(request, *args, **kwargs)


@login_required
def which_power(request, id, component):
    setup = models.Setup.objects.get(id=id)
    setup.hdd = models.Product.objects.get(id=component)
    setup.save()
    return render(request, 'constructor_templates/which_power.html', context={'id': id, 'component': component})


class SeventhSelectLisView(LoginRequiredMixin, generic.ListView):
    model = models.Product
    template_name = 'constructor_templates/seventh_component.html'
    paginate_by = 10
    id_setup = int()
    component = None

    def get_queryset(self):
        return models.Product.objects.filter(category_id=8).filter(name__contains='Блок питания')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['id'] = self.id_setup
        return context_data

    def get(self, request, *args, **kwargs):
        self.id_setup = kwargs['id']
        self.component = models.Product.objects.get(id=kwargs['component'])
        return super().get(request, *args, **kwargs)


class EighthSelectLisView(LoginRequiredMixin, generic.ListView):
    model = models.Product
    template_name = 'constructor_templates/eighth_component.html'
    paginate_by = 10
    id_setup = int()
    block = str()
    component = None

    def get_queryset(self):
        if self.block == 'False':
            return models.Product.objects\
                .filter(category_id=8)\
                .filter(name__contains='Корпус')\
                .filter(characteristics__Тип='с блоком питания')
        else:
            return models.Product.objects \
                .filter(category_id=8) \
                .filter(name__contains='Корпус') \
                .filter(characteristics__Тип='без блока питания')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['id'] = self.id_setup
        return context_data

    def get(self, request, *args, **kwargs):
        self.id_setup = kwargs['id']
        self.block = kwargs['block']
        self.component = models.Product.objects.get(id=kwargs['component'])
        if self.block == 'False':
            setup = models.Setup.objects.get(id=self.id_setup)
            setup.power = None
            setup.save()
            return super().get(request, *args, **kwargs)
        else:
            setup = models.Setup.objects.get(id=self.id_setup)
            setup.power = self.component
            setup.save()
            return super().get(request, *args, **kwargs)


@login_required
def choice_dvd(request, case_id, component):
    setup = models.Setup.objects.get(id=case_id)
    setup.case = models.Product.objects.get(id=component)
    setup.save()
    return render(request, 'constructor_templates/dvd_choice.html', context={'id': case_id, 'component': component})


class NinthSelectLisView(LoginRequiredMixin, generic.ListView):
    model = models.Product
    template_name = 'constructor_templates/ninth_component.html'
    paginate_by = 10
    choice = int()
    id_setup = int()

    def get_queryset(self):
        return models.Product.objects.filter(category_id=7)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['id'] = self.id_setup
        context_data['choice'] = self.choice
        return context_data

    def get(self, request, *args, **kwargs):
        self.id_setup = kwargs['id']
        self.choice = kwargs['choice']
        return super().get(request, *args, **kwargs)


class EndConstructorView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'constructor_templates/end_constructor.html'
    component = None
    id_setup = int()

    def get_context_data(self, **kwargs):
        setup = models.Setup.objects.get(id=self.id_setup)
        components = [
            'cpu', 'motherboard', 'video_card', 'ram', 'hdd', 'cooler', 'power',
            'case', 'dvd'
        ]
        components_for_template = [
            setup.cpu, setup.motherboard, setup.video_card, setup.ram, setup.hdd, setup.cooler,
            setup.power, setup.case, setup.dvd
        ]
        full_price = 0

        if re.search(r"\bIntel\b", setup.cpu.name):
            cpu = 'Intel'
        else:
            cpu = 'AMD'

        for component in components:
            full_price += getattr(getattr(setup, component, 0), 'price', 0)

        context_data = super().get_context_data(**kwargs)
        context_data['setup'] = setup
        context_data['components'] = components_for_template
        context_data['sum'] = round(full_price, 2)
        context_data['cpu'] = cpu
        return context_data

    def get(self, request, *args, **kwargs):
        self.id_setup = kwargs['id']
        self.component = models.Product.objects.get(id=kwargs['component'])
        if kwargs['choice'] == 'Yes':
            setup = models.Setup.objects.get(id=self.id_setup)
            setup.dvd = self.component
            setup.save()
            return super().get(request, *args, **kwargs)
        else:
            setup = models.Setup.objects.get(id=self.id_setup)
            setup.dvd = None
            setup.save()
            return super().get(request, *args, **kwargs)