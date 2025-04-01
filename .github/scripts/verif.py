import os
import sys

# Extensions autorisées
ALLOWED_EXTENSIONS = {
    "site": [".html", ".php"],
    "site/img": [".png", ".jpg"],
    "site/css": [".css"],
    "site/js": [".js"],
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_DIR = os.path.join(BASE_DIR, "site")

def verify_files():
    errors = []

    if not os.path.exists(SITE_DIR):
        errors.append("Le dossier 'site' est manquant.")
        return errors

    for root, _, files in os.walk(SITE_DIR):
        relative_folder = os.path.relpath(root, BASE_DIR).replace("\\", "/")

        for file in files:
            file_ext = os.path.splitext(file)[-1]

            for folder, allowed_exts in ALLOWED_EXTENSIONS.items():
                if relative_folder.startswith(folder) and file_ext not in allowed_exts:
                    errors.append(f"Mauvaise extension : {file} dans {relative_folder} (autorisé: {allowed_exts})")

    return errors

if __name__ == "__main__":
    errors = verify_files()
    if errors:
        for error in errors:
            print(error)
        sys.exit(1)
    else:
        print("Bonne extension")
