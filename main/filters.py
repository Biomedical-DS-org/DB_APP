import django_filters
from .models import Record


class recordsfilter(django_filters.FilterSet):
    ETR_id = django_filters.CharFilter(lookup_expr='iexact')
    smoking = django_filters.CharFilter(lookup_expr='iexact')
    SEX = django_filters.CharFilter(lookup_expr='iexact')
    AGE = django_filters.CharFilter(lookup_expr='iexact')
    ocular_disease = django_filters.CharFilter(lookup_expr='iexact')
    diabetes = django_filters.CharFilter(lookup_expr='iexact')
    AMD = django_filters.CharFilter(lookup_expr='icontains')
    COD = django_filters.CharFilter(lookup_expr='iexact')
    medication = django_filters.CharFilter(lookup_expr='icontains')
    Macular_Biopsy = django_filters.CharFilter(lookup_expr='icontains')
    Macular_Slides = django_filters.CharFilter(lookup_expr='icontains')
    Retinal_Slides = django_filters.CharFilter(lookup_expr='icontains')
    Retinal_Biopsy = django_filters.CharFilter(lookup_expr='icontains')
    RNA_Seq = django_filters.CharFilter(lookup_expr='icontains')
    ARMS2 = django_filters.CharFilter(lookup_expr='iexact')
    HTRA1 = django_filters.CharFilter(lookup_expr='iexact')
    Risk = django_filters.CharFilter(lookup_expr='icontains')
    haplotype_1 = django_filters.CharFilter(lookup_expr='iexact')
    haplotype_2 = django_filters.CharFilter(lookup_expr='iexact')
    ICB_R = django_filters.CharFilter(lookup_expr='iexact')
    ICB_L = django_filters.CharFilter(lookup_expr='iexact')
    LENS_R = django_filters.CharFilter(lookup_expr='iexact')
    LENS_L = django_filters.CharFilter(lookup_expr='iexact')
    mac_BM = django_filters.CharFilter(lookup_expr='iexact')
    mac_biopsy = django_filters.CharFilter(lookup_expr='iexact')
    NSR_R = django_filters.CharFilter(lookup_expr='iexact')
    NSR_L = django_filters.CharFilter(lookup_expr='iexact')
    RET_BM_R = django_filters.CharFilter(lookup_expr='iexact')
    RET_BM_L = django_filters.CharFilter(lookup_expr='iexact')
    ret_biopsy = django_filters.CharFilter(lookup_expr='iexact')
    SCLERA_R = django_filters.CharFilter(lookup_expr='iexact')
    SCLERA_L = django_filters.CharFilter(lookup_expr='iexact')
    VITREOUS_R = django_filters.CharFilter(lookup_expr='iexact')
    VITREOUS_L = django_filters.CharFilter(lookup_expr='iexact')
    optic_nerve = django_filters.CharFilter(lookup_expr='iexact')
    DNA_Banked = django_filters.CharFilter(lookup_expr='iexact')
    ICB_Genotyped = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Record
        fields = ['ETR_id', 'SEX', 'AGE', 'smoking','Retinal_Biopsy','Retinal_Slides','Macular_Slides','Macular_Biopsy' ,'RNA_Seq', 'ARMS2', 'RET_BM_R', 'VITREOUS_R', 'VITREOUS_L', 'optic_nerve', 'DNA_Banked', 'ICB_Genotyped', 'RET_BM_L', 'ret_biopsy', 'SCLERA_R', 'SCLERA_L', 'ICB_R', 'ICB_L', 'LENS_R', 'LENS_L', 'mac_biopsy', 'mac_BM', 'NSR_R', 'NSR_L', 'HTRA1', 'Risk', 'haplotype_1', 'haplotype_2', 'ocular_disease', 'diabetes', 'smoking_comments', 'AMD', 'COD', 'medication']
