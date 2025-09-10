### LIBRARY PROJECT


# Permissions and Groups Setup Documentation

This document provides an overview of how user permissions, groups, and roles are structured and implemented in this project. The system uses Django’s built-in authentication and authorization framework, combined with a custom `CustomUser` model, to control access across different apps (`bookshelf` and `relationship_app`). Custom permissions such as `can_view`, `can_create`, `can_edit`, and `can_delete` are defined to manage access to key resources, while groups (`Viewers`, `Editors`, `Admins`) are configured to simplify permission assignment. Roles in the `CustomUser` model further enhance access control by allowing role-based checks in views. Together, this approach ensures a clear and maintainable security structure for managing users and their actions.


# Permissions and Groups Setup – Bookshelf App

This document outlines how **custom permissions** and **groups** are configured in the `bookshelf` app.

---

## 🔐 Custom Permissions
Defined in `bookshelf/models.py` under the `Book` model:

- `can_view` – Allows a user to view books.
- `can_create` – Allows a user to add books.
- `can_edit` – Allows a user to edit books.
- `can_delete` – Allows a user to delete books.

These permissions are assigned to groups as follows:

| Permission    | Viewers | Editors | Admins |
|---------------|---------|---------|--------|
| `can_view`    | ✅      | ✅      | ✅     |
| `can_create`  | ❌      | ✅      | ✅     |
| `can_edit`    | ❌      | ✅      | ✅     |
| `can_delete`  | ❌      | ❌      | ✅     |

---

## 👥 Groups Setup
Groups are created manually in the Django admin or programmatically:

```python
from django.contrib.auth.models import Group

viewers_group, _ = Group.objects.get_or_create(name='Viewers')
editors_group, _ = Group.objects.get_or_create(name='Editors')
admins_group, _ = Group.objects.get_or_create(name='Admins')
