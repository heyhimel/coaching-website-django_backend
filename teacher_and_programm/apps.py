from django.apps import AppConfig


class TeacherAndProgrammConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'teacher_and_programm'

    def ready(self):
        import teacher_and_programm.signals