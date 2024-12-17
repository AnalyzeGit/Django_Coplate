from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import User, Review, Comment, Like


class CommentInLine(admin.StackedInline):
    model = Comment

class LikeInLine(GenericStackedInline):
    model = Like

class UserInLine(admin.StackedInline):
    model = User.following.through
    fk_name = 'to_user'
    verbose_name = 'Follower'
    verbose_name_plural = 'Followers'
    
UserAdmin.fieldsets += ('Custom fields', {'fields': ('nickname', 'profile_pic', 'intro','following',)}),
UserAdmin.inlines = (UserInLine,)


class ReviewAdmin(admin.ModelAdmin):
    inlines = (
        CommentInLine,
        LikeInLine,
    )

admin.site.register(User, UserAdmin)

admin.site.register(Review, ReviewAdmin)

admin.site.register(Comment)

admin.site.register(Like)