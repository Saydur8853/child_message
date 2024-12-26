# Generated by Django 5.1.4 on 2024-12-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_childgeneralist_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childgeneralist',
            name='district',
            field=models.CharField(choices=[(1, 'কুমিল্লা'), (2, 'ফেনী'), (3, 'ব্রাহ্মণবাড়িয়া'), (4, 'রাঙ্গামাটি'), (5, 'নোয়াখালী'), (6, 'চাঁদপুর'), (7, 'লক্ষ্মীপুর'), (8, 'চট্টগ্রাম'), (9, 'কক্সবাজার'), (10, 'খাগড়াছড়ি'), (11, 'বান্দরবান'), (12, 'সিরাজগঞ্জ'), (13, 'পাবনা'), (14, 'বগুড়া'), (15, 'রাজশাহী'), (16, 'নাটোর'), (17, 'জয়পুরহাট'), (18, 'চাঁপাইনবাবগঞ্জ'), (19, 'নওগাঁ'), (20, 'যশোর'), (21, 'সাতক্ষীরা'), (22, 'মেহেরপুর'), (23, 'নড়াইল'), (24, 'চুয়াডাঙ্গা'), (25, 'কুষ্টিয়া'), (26, 'মাগুরা'), (27, 'খুলনা'), (28, 'বাগেরহাট'), (29, 'ঝিনাইদহ'), (30, 'ঝালকাঠি'), (31, 'পটুয়াখালী'), (32, 'পিরোজপুর'), (33, 'বরিশাল'), (34, 'ভোলা'), (35, 'বরগুনা'), (36, 'সিলেট'), (37, 'মৌলভীবাজার'), (38, 'হবিগঞ্জ'), (39, 'সুনামগঞ্জ'), (40, 'নরসিংদী'), (41, 'গাজীপুর'), (42, 'শরীয়তপুর'), (43, 'নারায়ণগঞ্জ'), (44, 'টাঙ্গাইল'), (45, 'কিশোরগঞ্জ'), (46, 'মানিকগঞ্জ'), (47, 'ঢাকা'), (48, 'মুন্সিগঞ্জ'), (49, 'রাজবাড়ী'), (50, 'মাদারীপুর'), (51, 'গোপালগঞ্জ'), (52, 'ফরিদপুর'), (53, 'পঞ্চগড়'), (54, 'দিনাজপুর'), (55, 'লালমনিরহাট'), (56, 'নীলফামারী'), (57, 'গাইবান্ধা'), (58, 'ঠাকুরগাঁও'), (59, 'রংপুর'), (60, 'কুড়িগ্রাম'), (61, 'শেরপুর'), (62, 'ময়মনসিংহ'), (63, 'জামালপুর'), (64, 'নেত্রকোণা')], max_length=50, verbose_name='District Name'),
        ),
    ]
