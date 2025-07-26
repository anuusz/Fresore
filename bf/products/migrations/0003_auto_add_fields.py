from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('products', '0002_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='original_price',
            field=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='review_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sold',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
