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
