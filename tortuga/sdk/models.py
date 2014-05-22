from django.db import models

# Create your models here.

class Indexes(models.Model):
    hash=models.CharField(max_length=300)
    version = models.DecimalField(max_digits=10, decimal_places=1)
    model_id = models.IntegerField()
    description = models.CharField(max_length=300)
    implementationLevel =models.CharField(max_length=300) 
    name=models.CharField(max_length=300)
    author=models.CharField(max_length=300)
    organization=models.CharField(max_length=300)
    preprocessorVersion=models.CharField(max_length=300)
    originatingSystem=models.CharField(max_length=300)
    authorization=models.CharField(max_length=300)
    schemaIdentifiers=models.CharField(max_length=300)

    def __unicode__(self):
        return '%s,%r,%.1f'%(self.hash,self.model_id,self.version)


class SRL(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField(null = True,blank=True)
    file=models.FileField(upload_to='rules',null=True,blank=True)

    def __unicode__(self):
        return '%s'%(self.name)


