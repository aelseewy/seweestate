# Generated by Django 3.2 on 2021-05-19 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_auto_20210519_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='city',
            field=models.CharField(choices=[('الحي الاول', 'الحي الاول'), ('اكتوبر 6', '6 اكتوبر'), ('الحصري', 'الحصري'), ('الحي الثالث', 'الحي الثالث'), ('الحي التاني', 'الحي التاني'), ('الشيخ زايد', 'الشيخ زايد'), ('الحي الرابع', 'الحي الرابع'), ('الحي الحادي عشر', 'الحي الحادي عشر'), ('الحي اثني عشر', 'الحي اثني عشر'), ('مدينة نصر', 'مدينة نصر'), ('المتميز', 'المتميز')], max_length=70),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(choices=[('القاهرة الكبري', 'القاهرة الكبري'), ('الغردقة', 'الغردقة'), ('الساحل الشمالي', 'الساحل الشمالي'), ('الجيزة', 'الجيزة'), ('الفيوم', 'الفيوم'), ('الاسماعيلية', 'الاسماعيلية'), ('راس سدر', 'راس سدر'), ('اسكندرية', 'اسكندرية'), ('العين السخنة', 'العين السخنة')], max_length=100),
        ),
    ]