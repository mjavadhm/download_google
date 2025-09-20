import gdown
import os
import sys

def create_directories():
    """ساختار پوشه‌ها را ایجاد می‌کند."""
    print(">>> (Step 1/3) Creating directory structure...")
    try:
        # مسیر پوشه داخلی را تعریف می‌کنیم
        nested_dir = '/app/product_db/d4a7390d-0a2e-4264-a144-c2d71ba823de'
        # دستور os.makedirs با exist_ok=True پوشه‌ها را می‌سازد و اگر از قبل وجود داشته باشند، خطا نمی‌دهد.
        os.makedirs(nested_dir, exist_ok=True)
        print("    Directory structure created successfully.")
    except Exception as e:
        print(f"    ❌ Error creating directories: {e}")
        sys.exit(1)

def download_main_file():
    """فایل اصلی را در پوشه product_db دانلود می‌کند."""
    print("\n>>> (Step 2/3) Downloading main file...")
    url = 'https://drive.google.com/file/d/1-4KmB4iUG3vtxxCmWA2_ql0u8RgCit5N/view?usp=drive_link'
    output_path = '/app/product_db/'
    try:
        # با تعیین output به عنوان یک پوشه، gdown نام اصلی فایل را حفظ می‌کند
        gdown.download(url=url, output=output_path, quiet=False)
        print("    Main file downloaded successfully.")
    except Exception as e:
        print(f"    ❌ Error downloading main file: {e}")
        sys.exit(1)

def download_nested_files():
    """۵ فایل دیگر را در پوشه داخلی دانلود می‌کند."""
    print("\n>>> (Step 3/3) Downloading nested files...")
    
    # لیستی از لینک‌ها برای خوانایی بهتر
    links = [
        'https://drive.google.com/file/d/1LT_tQOj4tf9JSBBo4rqmRdJlzeg_0r27/view?usp=drive_link',
        'https://drive.google.com/file/d/1bvlMBdZ9l1Dwiq74eKHc1ApCaihZnVEI/view?usp=drive_link',
        'https://drive.google.com/file/d/1HCGvbD1zbN6mEDXqPGNIunSCfyCd-esG/view?usp=drive_link',
        'https://drive.google.com/file/d/1Rj_ospgxOAX3E0Jkc59aFYjFiJ0g8p9/view?usp=drive_link',
        'https://drive.google.com/file/d/12Km_UMn8nhfpnz9aXB_AICuvESJEE7w_/view?usp=drive_link'
    ]
    
    output_path = '/app/product_db/d4a7390d-0a2e-4264-a144-c2d71ba823de/'
    
    # با یک حلقه for، تمام لینک‌ها را به ترتیب دانلود می‌کنیم
    for index, url in enumerate(links):
        print(f"    Downloading file {index + 1} of {len(links)}...")
        try:
            gdown.download(url=url, output=output_path, quiet=False)
        except Exception as e:
            print(f"    ❌ Error downloading file {index + 1}: {e}")
            # در صورت بروز خطا برای یک فایل، می‌توانیم تصمیم بگیریم که ادامه دهیم یا متوقف شویم
            # در اینجا ادامه می‌دهیم
            pass
    print("    All nested files have been processed.")


if __name__ == "__main__":
    create_directories()
    download_main_file()
    download_nested_files()
    print("\n✅ All tasks completed successfully! The container will now exit.")
