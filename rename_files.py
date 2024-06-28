import os
import sys

def rename_files(directory, prefix, ext, start_index=1, padding=2):
    if not os.path.exists(directory):
        print(f"Directory does not exist: {directory}")
        return

    files = [f for f in os.listdir(directory) if f.endswith(ext)]
    files.sort()
    
    for index, file in enumerate(files, start=start_index):
        new_name = f"{prefix}{str(index).zfill(padding)}.{ext}"
        os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
        print(f"Renamed {file} to {new_name}")

def main():
    base_path = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else os.path.abspath(__file__))
    print(f"Base path: {base_path}")

    paths = {
        "videos_classes": os.path.join(base_path, 'video-emulator', 'videos', 'classes'),
        "videos_techniques": os.path.join(base_path, 'video-emulator', 'videos', 'techniques'),
        "videos_concepts": os.path.join(base_path, 'video-emulator', 'videos', 'concepts'),
        "videos_people": os.path.join(base_path, 'video-emulator', 'videos', 'people'),
        "thumbnails_classes": os.path.join(base_path, 'video-emulator', 'thumbnails', 'classes'),
        "thumbnails_techniques": os.path.join(base_path, 'video-emulator', 'thumbnails', 'techniques'),
        "thumbnails_concepts": os.path.join(base_path, 'video-emulator', 'thumbnails', 'concepts'),
        "thumbnails_people": os.path.join(base_path, 'video-emulator', 'thumbnails', 'people')
    }

    for key, path in paths.items():
        print(f"{key} path: {path}")
        if not os.path.exists(path):
            print(f"Error: {path} does not exist.")
    
    # Rename video files
    rename_files(paths["videos_classes"], 'classes', 'mp4')
    rename_files(paths["videos_techniques"], 'techniques', 'mp4')
    rename_files(paths["videos_concepts"], 'concepts', 'mp4')
    rename_files(paths["videos_people"], 'people', 'mp4')
    
    # Rename thumbnail files
    rename_files(paths["thumbnails_classes"], 'classes_th', 'jpg')
    rename_files(paths["thumbnails_techniques"], 'techniques_th', 'jpg')
    rename_files(paths["thumbnails_concepts"], 'concepts_th', 'jpg')
    rename_files(paths["thumbnails_people"], 'people_th', 'jpg')

if __name__ == "__main__":
    main()
