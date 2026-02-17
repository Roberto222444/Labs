is_admin = False        # Чи є користувач адміністратором
has_key = True          # Чи є електронний ключ
knows_password = True   # Чи знає пароль
access_granted = is_admin or (has_key and knows_password)
print("Доступ дозволено:", access_granted)