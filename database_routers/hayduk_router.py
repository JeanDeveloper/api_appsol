class HaydukRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'hayduk':
            return 'bd_hayduk'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'hayduk':
            return 'hayduk'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
                obj1._meta.app_label == 'hayduk' or
                obj2._meta.app_label == 'hayduk'
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'hayduk':
            return db == 'bd_hayduk'
        return None