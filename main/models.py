from django.db import models
import django_filters
import datetime

# Create your models here.


class Record(models.Model):
    SEX_OPTIONS = (('F', 'F'), ('M', 'M'), ('NI', 'No Information'))
    AMD_OPTIONS = (('No', 'No'), ('Early', 'Early'), ('Borderline', 'Borderline'), ('Late', 'Late'), ('Wet', 'Wet'), ('Unknown', 'Unknown'), ('Not Clincial', 'Not Clincial'), ('Non Control', 'Non Control'))
    TISSUE_OPTIONS = (('Yes', 'Yes'), ('No', 'No'))
    MED_OPTIONS = (('Yes', 'Yes'), ('No', 'No'), ('NI', 'No Information'))
    COD_OPTIONS = (('Known', 'Known'), ('Unknown', 'Unknown'))
    GENO_OPTIONS = (('No Risk', 'No Risk'), ('Heterozygous Risk', 'Heterozygous Risk'), ('Homozygous Risk', 'Homozygous Risk'), ('Not Complete', 'Not Complete'))

    ETR_id = models.CharField(max_length=200, primary_key=True)
    SEX = models.CharField(max_length=14, choices=SEX_OPTIONS, blank=True)
    AGE = models.IntegerField(blank=True)
    date_processed = models.DateField(blank=True)
    pm_time = models.IntegerField(blank=True)
    AMD = models.CharField(max_length=15, choices=AMD_OPTIONS)
    AMD_comments = models.TextField(blank=True)
    image_file = models.CharField(max_length=100, blank=True)
    ICB_R = models.CharField(max_length=3, choices=TISSUE_OPTIONS, blank=False)
    ICB_L = models.CharField(max_length=3, choices=TISSUE_OPTIONS, blank=False)
    LENS_R = models.CharField(max_length=3, choices=TISSUE_OPTIONS, blank=False)
    LENS_L = models.CharField(max_length=3, choices=TISSUE_OPTIONS, blank=False)
    mac_BM = models.CharField(max_length=3, choices=TISSUE_OPTIONS, blank=False)
    mac_biopsy = models.CharField(max_length=3, choices=TISSUE_OPTIONS, blank=False)
    NSR_R = models.CharField(max_length=3, choices=TISSUE_OPTIONS, blank=False)
    NSR_L = models.CharField(max_length=3, choices=TISSUE_OPTIONS, blank=False)
    RET_BM_R = models.CharField(max_length=3, choices=TISSUE_OPTIONS, blank=False)
    RET_BM_L = models.CharField(max_length=3, choices=TISSUE_OPTIONS, blank=False)
    ret_biopsy = models.CharField(max_length=3, choices=TISSUE_OPTIONS, blank=False)
    SCLERA_R = models.CharField(max_length=3, choices=TISSUE_OPTIONS, blank=False)
    SCLERA_L = models.CharField(max_length=3, choices=TISSUE_OPTIONS, blank=False)
    VITREOUS_R = models.CharField(max_length=3, choices=TISSUE_OPTIONS, blank=False)
    VITREOUS_L = models.CharField(max_length=3, choices=TISSUE_OPTIONS, blank=False)
    optic_nerve = models.CharField(max_length=3, choices=TISSUE_OPTIONS, blank=False)
    DNA_Banked = models.CharField(max_length=3, choices=TISSUE_OPTIONS, blank=False)
    ICB_Genotyped = models.CharField(max_length=3, choices=TISSUE_OPTIONS, blank=False)
    Paul_Bisop = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    other = models.TextField(blank=True)
    smoking = models.CharField(max_length=3, choices=MED_OPTIONS)
    smoking_comments = models.TextField(blank=True)
    diabetes = models.CharField(max_length=3, choices=MED_OPTIONS)
    diabetes_comments = models.TextField(blank=True)
    ocular_disease = models.CharField(max_length=3, choices=MED_OPTIONS)
    ocular_disease_comments = models.TextField(blank=True)
    COD = models.CharField(max_length=9, choices=COD_OPTIONS)
    COD_comments = models.TextField(blank=True)
    medication = models.TextField(blank=True)
    ethnicity = models.TextField(blank=True)
    additional_notes = models.TextField(blank=True)
    ARMS2 = models.CharField(max_length=3, blank=True)
    HTRA1 = models.CharField(max_length=3, blank=True)
    Risk = models.CharField(max_length=100, choices=GENO_OPTIONS, blank=True)
    haplotype_1 = models.CharField(max_length=200, blank=True)
    haplotype_2 = models.CharField(max_length=200, blank=True)
    probability = models.CharField(max_length=200, blank=True)
    Most_likely_haplotype = models.CharField(max_length=3, choices=TISSUE_OPTIONS, blank=True)
    Macular_Biopsy = models.CharField(max_length=400, blank=True)
    Macular_Slides = models.CharField(max_length=400, blank=True)
    Retinal_Biopsy = models.CharField(max_length=400, blank=True)
    Retinal_Slides = models.CharField(max_length=400, blank=True)
    Macular_Biopsy_Location = models.CharField(max_length=400, blank=True)
    Macular_Slides_Location = models.CharField(max_length=400, blank=True)
    Retinal_Biopsy_Location = models.CharField(max_length=400, blank=True)
    Retinal_Slides_Location = models.CharField(max_length=400, blank=True)
    RNA_Seq = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Records'
    """docstring for haplorypes"""

    def __str__(self):
        return self.ETR_id
