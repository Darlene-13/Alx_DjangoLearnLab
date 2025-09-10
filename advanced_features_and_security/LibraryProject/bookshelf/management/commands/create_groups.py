# bookshelf/management/commands/create_groups.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book  # replace with your model

class Command(BaseCommand):
    help = "Create default groups and assign permissions"

    def handle(self, *args, **kwargs):
        # Define your groups and permissions
        groups_permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_edit", "can_create"],
            "Admins": ["can_view", "can_edit", "can_create", "can_delete"],
        }

        book_content_type = ContentType.objects.get_for_model(Book)

        for group_name, perms in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm_code in perms:
                try:
                    perm = Permission.objects.get(
                        codename=perm_code,
                        content_type=book_content_type
                    )
                    group.permissions.add(perm)
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.ERROR(
                        f"Permission {perm_code} not found."
                    ))
            self.stdout.write(self.style.SUCCESS(f"Group '{group_name}' updated."))

        self.stdout.write(self.style.SUCCESS("Groups and permissions created!"))
