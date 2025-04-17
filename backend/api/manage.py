import os
import sys

def main():
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_project.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError("Couldn't import Django.")
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()