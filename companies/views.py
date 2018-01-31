from django.shortcuts import render
from .kontur import get_company_inn
from .models import Company
from datetime import date, timedelta
from django.utils import timezone

from django.conf import settings

def find_company(request):
    search = request.GET.get('search')
    error = False
    company = False
    company_list = []

    if search:
        company, error = get_company_by_inn(search)
      
        company_list = Company.objects.filter(short_legal_name__contains=search).all()

    return render(request, 'mainproject.html', {'search': search, 'error': error, 'company': company, 'company_list': company_list})


def is_inn(inn):
    if not len(inn) == 10:
        return False
    try:
        inn = int(inn)
        return True
    except(ValueError):
        return False

def list_of_companies(request):

    search = request.GET.get('search')
    companies = []
    errors = []

    if search:
        list_of_companies = list(set(search.splitlines()))

        for inn in list_of_companies:
            company, error = get_company_by_inn(inn)
            if company:
                companies.append(company)
            elif error:
                error = "{} {}".format(error, inn)
                errors.append(error)
            else:
                print("Ошибка")
        search = '\n'.join(list_of_companies)


    return render(request, 'multipalcompanies.html', {'search': search, 'errors': errors, 'company_list': companies })


def get_company_by_inn(search):
    company = None
    error = None
    if is_inn(search):
        if Company.objects.filter(inn=search).exists():
            company = Company.objects.filter(inn=search).first()
            td = timedelta(days=settings.KONTUR_CHECK_DELAY)
            if (date.today() - td) < company.modified:
                return (company, error)
        else:
            company = Company()
        


        company_data = get_company_inn(search)
        if not company_data:
            error = "По Вашему запросу возникла ошибка"
        else:
            street = "{} {}".format(
                company_data["UL"]["legalAddress"]["parsedAddressRF"]["street"]["topoFullName"],
                company_data["UL"]["legalAddress"]["parsedAddressRF"]["street"]["topoValue"]
            )
            house = "{} {}".format(
                company_data["UL"]["legalAddress"]["parsedAddressRF"]["house"]["topoFullName"],
                company_data["UL"]["legalAddress"]["parsedAddressRF"]["house"]["topoValue"]
            )
            company.short_legal_name=company_data["UL"]["legalName"]["short"]
            company.zip_code = company_data["UL"]["legalAddress"]["parsedAddressRF"]["zipCode"]
            company.city = company_data["UL"]["legalAddress"]["parsedAddressRF"]["city"]["topoValue"]
            company.street = street
            company.house = house
            company.registration_date = company_data["UL"]["legalName"]["date"]
            company.status = company_data["UL"]["status"]["statusString"]
            company.ceo = company_data["UL"]["heads"][0]["fio"]
            company.inn = company_data["inn"]
            company.ogrn = company_data["ogrn"]
            company.okpo = company_data["UL"]["okpo"]
            company.kpp = company_data["UL"]["kpp"]
            company.modified = timezone.now()
            
            company.save()
    else:
        error = "Некорректный ИНН"
    return (company, error)


