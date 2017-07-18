"""
This is Python script file showing usage of the application code
outside of the Django app (e.g. running the whole application server).
"""

# ----
# START
# Needed to bootstrap the Django app
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crumpa.settings")
django.setup()
# END
# ----



# https://docs.djangoproject.com/en/1.11/topics/db/queries/#retrieving-objects
# https://docs.djangoproject.com/en/1.11/ref/models/querysets/#when-querysets-are-evaluated

# Specific test/usage code
from profiles.models import Profile


# Add new Profile record - two steps -create and save
newProfile = Profile(name="rumen")
newProfile.save()

#  Add new record in on one step
newProfile2 = Profile.objects.create(name="rumen2")

# Retrieve all records by usgin all()
profilesAll = Profile.objects.all()
for profile in profilesAll:
    print(profile.name)

# Retrieve specific record by its ID using get(ID)
profileSpecific = Profile.objects.get(pk=1)  # get the first
print(profileSpecific)

# Update a record
profileSpecific.name = 'New ' + profileSpecific.name
profileSpecific.save()



