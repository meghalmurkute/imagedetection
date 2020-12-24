from django.db import models

# Create your models here.
class miss(models.Model):
    Male = 'M'
    Female = 'F'
    
    Churchgate='Chu'
    MarineLine='MarL'
    CharniRoad='ChaR'
    GrantRoad='GraR'
    MumbaiCentral='MumC'
    Mahalaxmi='Mah'
    Lowerparel='LowP'
    ElphinstoneRoad='ElpR'
    Dadar='Dad'
    MatungaRoad='MatR'
    MahimJunction='MahJ'
    Bandra='Ban'
    KharRoad='KhaR'
    Santacruz='San'
    VileParle='VilP'
    Andheri='And'
    Jogeshwari='Jog'
    RamMandir='RamM'
    Goregaon='Gor'
    Malad='Mal'
    Kandivali='Kan'
    Borivali='Bor'
    Dahisar='Dah'
    MumbaiCST='MCST'
    Masjidbunder='Mbun'
    SandhurstRoad='SanR'
    Byculla='By'
    Chinchpokli='Chi'
    CurreyRoad='Cur'
    Parel='Prl'
    Matunga='Mat'
    Sion='Si'
    Kurla='Ku'
    Vidyavihar='Vid'
    Ghatkopar='Gha'
    Vikroli='Vik'
    Kanjurmarg='Kan'
    Bhandup='Bha'
    Nahur='Nah'
    Mulund='Mul'
    Thane='Tha'
    Location_choices=[
        (Churchgate, 'Churchgate'),
        (MarineLine, 'Marine Line'),
        (CharniRoad, 'Charni Road'),
        (GrantRoad, 'Grant Road'),
        (MumbaiCentral, 'Mumbai Central'),
        (Mahalaxmi, 'Mahalaxmi'),
        (Lowerparel, 'Lowerparel'),
        (ElphinstoneRoad, 'Elphinstone Road'),
        (Dadar, 'Dadar'),
        (MatungaRoad, 'Matunga Road'),
        (MahimJunction, 'Mahim Junction'),
        (Bandra, 'Bandra'),
        (KharRoad, 'Khar Road'),
        (Santacruz, 'Santacruz'),
        (VileParle, 'Vile Parle'),
        (Andheri, 'Andheri'),
        (Jogeshwari, 'Jogeshwari'),
        (RamMandir, 'Ram Mandir'),
        (Goregaon, 'Goregaon'),
        (Malad, 'Malad'),
        (Kandivali, 'Kandivali'),
        (Borivali, 'Borivali'),
        (Dahisar, 'Dahisar'),
        (MumbaiCST, 'Mumbai CST'),
        (Masjidbunder,'Masjid bunder'),
        (SandhurstRoad,'Sandhurst Road'),
        (Byculla,'Byculla'),
        (Chinchpokli,'Chinchpokli'),
        (CurreyRoad,'CurreyRoad'),
        (Parel, 'Parel'),
        (Matunga, 'Matunga'),
        (Sion, 'Sion'),
        (Kurla, 'Kurla'),
        (Vidyavihar, 'Vidyavihar'),
        (Ghatkopar, 'Ghatkopar'),
        (Vikroli, 'Vikroli'),
        (Kanjurmarg, 'Kanjurmarg'),
        (Bhandup, 'Bhandup'),
        (Nahur, 'Nahur'),
        (Mulund, 'Mulund'),
        (Thane, 'Thane')
        ]
    Gender_choices = [
        (Male, 'Male'),
        (Female, 'Female')
        ]
    
    name=models.CharField(max_length=50)
    gender = models.CharField(max_length=2, choices=Gender_choices, default=Male)
    age=models.IntegerField()
    height=models.DecimalField(decimal_places=2, max_digits=3)
    address=models.TextField()
    missing_location=models.CharField(max_length=4 , choices=Location_choices, default=Churchgate)
    contact_number=models.IntegerField(max_length=10)
    email_id=models.EmailField()
    photo=models.ImageField(upload_to = 'missing_pic_folder/', default = 'missing_pic_folder/None/no-img.jpg')