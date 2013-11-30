from django.db import models


class GlassType(models.Model):
    """
    Model representing the Glass type
    """
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Beer(models.Model):
    """
    Beer model
    # ibu :  international bittering unit, range from 0 to 200 max
    # abv : Alcohol by volume represented in %
    # style : it can be refactored to its own model but for
     brevety it's a CharField.A beer style is a term used to differentiate and
     categorize beers by factors such as colour, flavour, strength, ingredients,
     production method, recipe, history, or origin.
    """
    name = models.CharField(max_length=200)
    ibu = models.PositiveSmallIntegerField()
    calories = models.PositiveSmallIntegerField()
    abv = models.PositiveSmallIntegerField()
    style = models.CharField(max_length=100)
    brewery_location = models.CharField(max_length=200)
    glass_type = models.ForeignKey(GlassType)

    def __unicode__(self):
        return '%s from %s' % (self.name, self.brewery_location)

    def save(self, *args, **kwargs):
        if self.abv > 100:
            raise ValueError('Invalid value : %s is not within  0 and 100' %
             self.abv)
        super(Beer, self).save(*args, **kwargs)

