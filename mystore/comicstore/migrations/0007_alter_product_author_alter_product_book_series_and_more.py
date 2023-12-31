# Generated by Django 4.2.3 on 2023-08-23 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comicstore', '0006_remove_product_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='comicstore.author'),
        ),
        migrations.AlterField(
            model_name='product',
            name='book_series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series', to='comicstore.book_series'),
        ),
        migrations.AlterField(
            model_name='product',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genres', to='comicstore.genre'),
        ),
        migrations.AlterField(
            model_name='product',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='laanguages', to='comicstore.language'),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_details',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='comicstore.product_details'),
        ),
        migrations.AlterField(
            model_name='product',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publishers', to='comicstore.publisher'),
        ),
    ]
