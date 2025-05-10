import subprocess
import os

# Fungsi untuk menjalankan perintah Git
def run_git_command(command, repo_path):
    try:
        # Mengubah direktori ke repositori yang ditentukan
        os.chdir(repo_path)

        # Menjalankan perintah git dan menangkap output
        result = subprocess.run(command, check=True, shell=True, capture_output=True, text=True)
        print(result.stdout)  # Print the output of the command
    except subprocess.CalledProcessError as e:
        print(f"Error saat menjalankan perintah {command} di {repo_path}: {e.stderr}")

# Meminta input pesan commit dari pengguna
commit_msg = input("Masukkan pesan commit untuk repositori: ").strip()

# Memastikan pesan commit tidak kosong
if not commit_msg:
    print("Pesan commit tidak boleh kosong.")
    exit(1)

# Path repositori yang akan digunakan
repo_path = r"G:\Project\Crypto\AirdropBOT\TelegramBOT\AQuery"

# Menjalankan perintah git untuk repositori tersebut
print(f"Mengupload repo dengan pesan: {commit_msg}")
run_git_command("git add .", repo_path)
run_git_command(f"git commit -m \"{commit_msg}\"", repo_path)
run_git_command("git push origin main", repo_path)

print(f"Selesai mengupload repo dengan pesan: {commit_msg}!")
