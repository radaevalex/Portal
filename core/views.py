from .models import Office, Dynamic, Indicator
from django.shortcuts import render, get_list_or_404, redirect
from django.db.models import Q
from datetime import datetime
from django.db.models import Sum


# Create your views here.
def departs(request):
    depart_list = Office.objects.values('department', 'slug').distinct().order_by()
    context = {'departs': depart_list}
    return render(request, 'core/departments.html', context=context)


def depart_values(request, office_slug):
    fields_name = ('month', 'office__department',
                   'office__city', 'office__id',
                   'indicator__group', 'indicator__name',
                   'value',)

    offices = get_list_or_404(Office, slug=office_slug)
    values = Dynamic.objects.filter(office__in=offices)
    name_depart = offices[0].department
    direct = ''
    req_sort_field = request.GET.get('sort')

    if req_sort_field is None:
        req_sort_field = 'month'
    elif req_sort_field[0] == '-':
        direct = '-'
        req_sort_field = req_sort_field[1:]

    if req_sort_field in fields_name:
        if direct == '-':
            values = values.order_by(direct + req_sort_field)
            direct = ''
        else:
            values = values.order_by(req_sort_field)
            direct = '-'

    q = request.GET.get('q')
    if q is not None:
        print(q)
        values = values.filter(Q(month__icontains=q)
                               | Q(office__city__icontains=q)
                               | Q(office__city__icontains=q)
                               | Q(office__id__icontains=q)
                               | Q(indicator__group__icontains=q)
                               | Q(indicator__name__icontains=q)
                               | Q(value__icontains=q))

    month_list = Dynamic.objects.values_list('month', flat=True).distinct()
    sort_link = {'direct': direct,
                 'field': req_sort_field}

    context = {'department': name_depart,
               'values': values,
               'sort_link': sort_link,
               'month_list': month_list}

    return render(request, 'core/departvalues.html', context=context)


def results(request, office_slug):
    offices = get_list_or_404(Office, slug=office_slug)
    values = Dynamic.objects.filter(office__in=offices)
    name_depart = offices[0].department
    s1 = request.GET.get('s1')
    s2 = request.GET.get('s2')

    if s1 is None or s2 is None:
        return redirect('core:depart_values', office_slug)

    d1 = datetime.strptime(s1, '%d.%m.%Y')
    d2 = datetime.strptime(s2, '%d.%m.%Y')

    if d1 > d2:
        return redirect('core:depart_values', office_slug)

    d1 = d1.strftime('%Y-%m-%d')
    d2 = d2.strftime('%Y-%m-%d')

    indicators = Indicator.objects.all()
    groups = dict()
    res = dict()
    for indic in indicators:
        v1 = values.filter(Q(month=d1) & Q(indicator__name=indic.name)).aggregate(ag_value=Sum('value'))
        v2 = values.filter(Q(month=d2) & Q(indicator__name=indic.name)).aggregate(ag_value=Sum('value'))
        v = round((float(v2['ag_value']) / float(v1['ag_value'])) * 100)
        if groups.get(indic.group):
            groups[indic.group] += 1
        else:
            groups[indic.group] = 1
        res[indic.name] = v

    context = {
        'groups': groups,
        'indicators': indicators,
        'slug': office_slug,
        'department': name_depart,
        'res': res,
    }

    return render(request, 'core/results.html', context=context)
