
import os;
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django;
django.setup()

import random;
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ["Social", "Search", "News", "Games", "Blogs", "Marketplace"]

def add_topic():
    print(Topic.objects.get_or_create(top_name=random.choice(topics)))
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #Get topic for the entry
        top = add_topic()

        #creating fake data
        fake_name = fakegen.company()  #fake company name
        fake_url = fakegen.url()
        fake_date = fakegen.date()

        #creating new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, name= fake_name, url=fake_url)[0]
    
        #creating new accessrecord entry
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == "__main__":
    print("populating")
    populate(20)
    print("population completed")



#Note that we are passing an entire topic object in webpage as it is the foreign key and similarly we are pssing the entire the webpage object in the name of accessrecord.
#read again about this name == main thing.

#So many things became clear
#
