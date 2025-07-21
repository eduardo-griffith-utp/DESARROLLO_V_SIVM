import os
import sys

# Configuración de paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)  # Añade /backend/api al path

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_project.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Instala Django: pip install django") from exc
    
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()