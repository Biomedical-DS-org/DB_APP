import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Record
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm)
from django.contrib.auth import (login, logout, authenticate, update_session_auth_hash)
from django.contrib import messages
from .filters import recordsfilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def homepage(request):
  return render(request=request, template_name="main/home.html", context={"med_rec": medical_record.objects.all})


def login_request(request):
  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        # request.session.set_expiry(60*30)
        messages.success(request, f"You are now logged in as {username}")
        return redirect("main:login")
      else:
        messages.error(request, f"Invalid username or password")
    else:
      messages.error(request, f"Invalid username or password")

  form = AuthenticationForm()
  return render(request,
                "main/login.html",
                {"form": form})


def logout_request(request):
  logout(request)
  messages.info(request, f"You have been logged out!")
  return redirect("main:login")


def search(request):
  return render(request, 'main/search.html')


def search_the_record(request):
  etr = request.GET.get("ETRID", default="")
  etr_ = etr.upper()
  PK = etr.upper()
  if PK.startswith('ETR'):
    PK = PK[3:]
  PK2 = 'ETR' + PK
  sex = request.GET.get("SEX", default="")
  # age = request.GET.get("AGE", default="")
  amd = request.GET.get("AMD", default="")
  icbr = request.GET.get("ICBR", default="")
  icbl = request.GET.get("ICBL", default="")
  lensr = request.GET.get("LENSR", default="")
  lensl = request.GET.get("LENSL", default="")
  macbm = request.GET.get("MACBM", default="")
  macbio = request.GET.get("MACBIO", default="")
  nsrr = request.GET.get("NSRR", default="")
  nsrl = request.GET.get("NSRL", default="")
  retbmr = request.GET.get("RETBMR", default="")
  retbml = request.GET.get("RETBML", default="")
  retbio = request.GET.get("RETBIO", default="")
  sclerar = request.GET.get("SCLERAR", default="")
  scleral = request.GET.get("SCLERAL", default="")
  vitreousr = request.GET.get("VITREOUSR", default="")
  vitreousl = request.GET.get("VITREOUSL", default="")
  opticnerve = request.GET.get("OPTICNERVE", default="")
  dna_banked = request.GET.get("DNABANKED", default="")
  icbgenotyped = request.GET.get("ICB_GEN", default="")
  smoking = request.GET.get("smoking", default="")
  diabetes = request.GET.get("Diabetes", default="")
  ocular = request.GET.get("OCULAR", default="")
  medication = request.GET.get("MEDICATION", default="")
  RNA_Seq = request.GET.get("RNA_Seq", default="")
  haplotype1 = request.GET.get("HAPLO1", default="")
  haplotype2 = request.GET.get("HAPLO2", default="")
  arms2 = request.GET.get("ARMS2", default="")
  htra1 = request.GET.get("HTRA1", default="")
  min_age_ = request.GET.get("MIN")
  max_age_ = request.GET.get("MAX")
  tissue = request.GET.get("tissue", default="")
  tissue2 = tissue
  # risk = request.GET["RISK"]
  if min_age_ != '':
    min_age = int((min_age_))
  else:
    min_age = 0

  if max_age_ != '':
    max_age = int((max_age_))
  else:
    max_age = 150

  trial = (Record.objects.filter(ETR_id__icontains=PK2,
                                 AMD__icontains=amd,
                                 ICB_R__icontains=icbr,
                                 ICB_L__icontains=icbl,
                                 LENS_R__icontains=lensr,
                                 LENS_L__icontains=lensl,
                                 mac_BM__icontains=macbm,
                                 mac_biopsy__icontains=macbio,
                                 NSR_R__icontains=nsrr,
                                 NSR_L__icontains=nsrl,
                                 RET_BM_R__icontains=retbmr,
                                 RET_BM_L__icontains=retbml,
                                 ret_biopsy__icontains=retbio,
                                 SCLERA_R__icontains=sclerar,
                                 SCLERA_L__icontains=scleral,
                                 VITREOUS_R__icontains=vitreousr,
                                 VITREOUS_L__icontains=vitreousl,
                                 optic_nerve__icontains=opticnerve,
                                 DNA_Banked__icontains=dna_banked,
                                 ICB_Genotyped__icontains=icbgenotyped,
                                 smoking__icontains=smoking,
                                 diabetes__icontains=diabetes,
                                 ocular_disease__icontains=ocular,
                                 medication__icontains=medication,
                                 RNA_Seq__icontains=RNA_Seq,
                                 haplotype_1__icontains=haplotype1,
                                 haplotype_2__icontains=haplotype2,
                                 ARMS2__icontains=arms2,
                                 HTRA1__icontains=htra1,
                                 # Risk__icontains=risk,
                                 SEX__icontains=sex,
                                 AGE__range=(min_age, max_age),
                                 # Macular_Biopsy__icontains=tissue,
                                 # Macular_Slides__icontains=tissue2,
                                 Retinal_Biopsy__icontains=tissue2,
                                 # Retinal_Slides__icontains=tissue,
                                 # AGE__icontains=age
                                 ))

  return trial


def filtered_records(request):
  template = 'main/records2.html'
  trial = search_the_record(request)
  search_filter = recordsfilter(request.GET, queryset=trial)
  paginator = Paginator(search_filter.qs, 25)
  page = request.GET.get('page')
  records = paginator.get_page(page)
  count = search_filter.qs.count()
  context = {'records': records, 'count': count}
  return render(request, template, context)


def records(request):
  search_list = Record.objects.all()
  search_filter = recordsfilter(request.GET, queryset=search_list)
  paginator = Paginator(search_filter.qs, 25)
  page = request.GET.get('page')
  try:
    items = paginator.page(page)
  except PageNotAnInteger:
    items = paginator.page(1)
  except EmptyPage:
    items = paginator.page(paginator.num_pages)

  index = items.number - 1
  max_index = len(paginator.page_range)
  start_index = index - 5 if index >= 5 else 0
  end_index = index + 5 if index <= max_index - 5 else max_index
  page_range = paginator.page_range[start_index:end_index]

  count = search_list.count()
  # page = request.GET.get('page')
  # records = paginator.get_page(page)
  context = {'filter': search_filter, 'records': items, 'page_range': page_range, 'count': count}
  return render(request, 'main/records.html', context)


def details(request, pk):
  template = 'main/details.html'
  post = Record.objects.filter(pk=pk).values()

  context = {'post': post}
  return render(request, template, context)


def filtered_details(request):
  template = 'main/details.html'
  etr = request.GET["ETRID"]
  PK = etr.upper()
  if PK.startswith('ETR'):
    PK = etr[3:]
    PK2 = 'ETR' + PK
  else:
    PK2 = 'ETR' + etr
  # PK2 = 'ETR' + PK
  post = Record.objects.filter(pk=PK2).values()
  if post:
    messages.success(request, f"This is: {PK2}")
    context = {'post': post}
    return render(request, template, context)
  else:
    messages.error(request, f"The ETR ID was invalid or it does not exist!")

  context = {'post': post}
  return render(request, 'main/fake_search.html')


def fake_search(request):
  return render(request, "main/fake_search.html")


def change_password(request):
  if request.method == 'POST':
    form = PasswordChangeForm(data=request.POST, user=request.user)

    if form.is_valid():
      form.save()
      update_session_auth_hash(request, form.user)
      messages.success(request, f"Your Password has been changed")
      return redirect("main:login")
    else:
      messages.error(request, f"Invalid Form. Try Again")
      return redirect("main:change_password")
  else:
    form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'main/change_password.html', context)


def export(request):
  items = search_the_record(request)
  print(items)

  response = HttpResponse(content_type='text.csv')
  response['Content-Disposition'] = 'attachment; filename=AMD_filtered_records.csv'
  writer = csv.writer(response, delimiter=',')
  writer.writerow(['ETR ID', 'SEX', 'AGE', 'AMD', 'AMD Comments', 'Haplotype 1', 'Haplotype 2', 'ARMS2', 'HTRA',
                   'ICB Right', 'ICB Left', 'LENS Right', 'LENS Left', 'MAC BM', 'MAC Biopsy', 'NSR Right', 'NSR Left', 'RET BM Right', 'RET BM Left', 'RET Biopsy',
                   'SCLERA Right', 'SCLERA Left', 'VITREOUS Right', 'VITREOUS Left', 'Optic Nerve', 'DNA Banked', 'ICB Genotyped', 'Paul Bisop'])

  for obj in items:
    writer.writerow([obj.ETR_id, obj.SEX, obj.AGE, obj.AMD, obj.AMD_comments, obj.haplotype_1, obj.haplotype_2, obj.ARMS2, obj.HTRA1,
                     obj.ICB_R, obj.ICB_L, obj.LENS_R, obj.LENS_L, obj.mac_BM, obj.mac_biopsy, obj.NSR_R, obj.NSR_L,
                     obj.RET_BM_R, obj.RET_BM_L, obj.ret_biopsy, obj.SCLERA_R, obj.SCLERA_L, obj.VITREOUS_R, obj.VITREOUS_L, obj.optic_nerve, obj.DNA_Banked,
                     obj.ICB_Genotyped, obj.Paul_Bisop])

  return response
