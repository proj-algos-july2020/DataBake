from django.db import models
import re
from datetime import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):

        errors = {}

        if len(postData['first_name'])<2:
            errors['first_name'] = "First name must be at least 2 characters"

        if len(postData['last_name'])<2:
            errors['last_name'] = "Last name must be at least 2 characters"

        if len(postData['email'])<1:
            errors['email'] = "Email cannot be blank"
        elif not EMAIL_REGEX.match(postData['email']):               
            errors['email'] = "Invalid email address"
        elif User.objects.filter(email=postData['email']).exists():
            errors['emailunique'] = "Email already registered, please login."

        if len(postData['password'])<8:
            errors['password'] = "Password must be at least 8 characters"

        if postData['password'] != postData['confirm']:
            errors['passwords'] = "Passwords must match"

        if len(postData['user_name'])<4:
            errors['user_name'] = "Your user name must have 4 or more characters"
        elif User.objects.filter(user_name=postData['user_name']).exists():
            errors['username_unique'] = "Email already registered, please login."

        if len(postData['city'])<2:
            errors['city'] = "please enter a city "
        if len(postData['state'])<2:
            errors['state'] = "please add a state"
        if len(postData['zipcode'])<5:
            errors['zipcode'] = "please enter a zipcode"

        if len(postData['bio'])<10:
            errors['bio'] = "Bio cannot be blank"   

        if len(postData['title'])<1:
            errors['title'] = "Title cannot be blank"      
        return errors


    def login_validator(self, postData):
        errors = {}
        if not User.objects.filter(user_name=postData['user_name']).exists():
            errors['username_unique'] = "User not found"
        if len(postData['password_input']) < 5:
             errors['password'] = 'Please enter an email that contains 5 or more character'
        return errors

    def update_validator(self, postData):
        errors = {}
        if len(postData['title'])<1:
            errors['title'] = "Title cannot be blank"
        if len(postData['city'])<2:
            errors['city'] = "please enter a city "
        if len(postData['state'])<2:
            errors['state'] = "please add a state"
        if len(postData['zipcode'])<5:
            errors['zipcode'] = "please enter a zipcode"
        if len(postData['bio'])<10:
            errors['bio'] = "Bio cannot be blank" 
        return errors 



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    zipcode= models.IntegerField()
    state=models.CharField(max_length=2)
    city=models.CharField(max_length=75)
    email = models.CharField(max_length=255)
    user_name=models.CharField(max_length=150)
    password = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    bio = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()


class RecipeManager(models.Manager):

    def recipe_validator(self, postData):

        errors = {}

        if len(postData['recipe_title'])<2:
            errors['recipe_title'] = "Title must be at least 2 characters" 

        if len(postData["recipe_directions"]) <10:
            errors["recipe_directions"] = "Directions must be at least 10 characters"

        if len(postData['prep_time']) < 1:
            errors['prep_time'] = "Prep time cannot be left blank"

        if len(postData['cook_time'])<1:
            errors['cook_time'] = "Cook time cannot be left blank"

        return errors

class Recipe(models.Model):
    recipe_title = models.CharField(max_length=255)
    recipe_directions = models.TextField()
    prep_time = models.CharField(max_length = 20)
    cook_time = models.CharField(max_length = 20)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    uploaded_by = models.ForeignKey(User, related_name="recipes_uploaded", on_delete = models.CASCADE)
    added_by = models.ManyToManyField(User, related_name="added_recipes")

    objects = RecipeManager()


class Image(models.Model):
    recipe_image = models.ImageField(upload_to='images/')

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    images = models.ForeignKey(Recipe, related_name="for_recipe", on_delete = models.CASCADE)

class CategoryManager(models.Manager):

    def category_validator(self, postData):

        errors = {}

        if len(postData['category_name'])<1:
            errors['category_name'] = "Category name cannot be blank" 

        return errors

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    categories = models.ForeignKey(Recipe, related_name="recipe_categories", on_delete = models.CASCADE, null=True)

    objects = CategoryManager()


class IngredientManager(models.Manager):

    def ingredient_validator(self, postData):

        errors = {}

        if len(postData['ingredient_name'])<1:
            errors['ingredient_name'] = "Ingredients cannot be blank" 

        if len(postData['ingredient_quantity'])<1:
            errors['ingredient_quantity'] = "Quantity cannot be blank" 

        if len(postData['ingredient_measurement'])<1:
            errors['ingredient_measurement'] = "Quantities cannot be blank"   

        return errors


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=255)
    ingredient_quantity = models.FloatField(null=True)
    ingredient_measurement = models.CharField(max_length=15, null=True)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    ingredients_for = models.ForeignKey(Recipe, related_name="recipe_ingredients",on_delete=models.CASCADE)

    objects = IngredientManager()



# class Tag(models.Model):
#     tag_name = models.CharField(max_length=255)

#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

#     tags = models.ManyToManyField(Recipe, related_name="recipe_tags")


class Survey(models.Model):
    overall = models.IntegerField()
    flavor = models.IntegerField()
    difficulty = models.IntegerField()
    accessibility = models.IntegerField()
    survey_text = models.TextField()

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    surveys = models.ForeignKey(Recipe, related_name="recipe_surveys", on_delete=models.CASCADE)

# messages links to recipe
class Messages(models.Model):
    messages = models.CharField(max_length=255)
    recipe_message = models.ForeignKey(Recipe, related_name="recipe_message", on_delete = models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

#comments links to messages
class Comments(models.Model):
    comment = models.CharField(max_length=255)
    mess_comment = models.ForeignKey(Messages, related_name="recipe_comment", on_delete = models.CASCADE, null=True )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    



# class ProfileManager(models.Manager):
#     def profile_validator(self, postData):

#         errors = {}

#         if len(postData['title'])<1:
#             errors['title'] = "Title cannot be blank" 

#         if len(postData['location'])<1:
#             errors['location'] = "Location cannot be blank" 

#         if len(postData['bio'])<10:
#             errors['bio'] = "Bio cannot be blank"   

#         return errors

# class Profile(models.Model):
#     title = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)
#     bio = models.TextField()

#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)

#     users = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE)

#     objects = ProfileManager()
