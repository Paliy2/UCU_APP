from django.db import models


class DayMenu(models.Model):
    class Meta:
        pass


class FoodItem(models.Model):
    TRAPEZNA_CHOICE = (
        ('Kozelnytska 2A', 'BFS'),
        ('Sventsitskoho', 'Sventsa'),
        ('FBF', 'FBF'),
    )

    building = models.CharField(choices=TRAPEZNA_CHOICE, max_length=255, default=TRAPEZNA_CHOICE[0])
    item_name = models.CharField(max_length=255, null=False)
    item_type = models.CharField(max_length=255)
    portion_size = models.CharField(max_length=20)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    available = models.BooleanField()

    class Meta:
        db_table = 'trapezna-menu'


'''
parse excel and create a corresponding DB

|Trapezna type|item-name|item-Type|portion-size|Price grn float|Available|
|Kozelnytska  |potato   | food    |200g        |15.00          |True     |
|Sventsitskogo|milk     | drink   |100ml       |12.00          |False    |

'''
