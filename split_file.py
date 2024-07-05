import os

def split_file(file_path, chunk_size=50 * 1024 * 1024):
    file_size = os.path.getsize(file_path)
    with open(file_path, 'rb') as f:
        chunk_number = 0
        while chunk_size * chunk_number < file_size:
            chunk_file_path = f"{file_path}_part_{chunk_number}"
            with open(chunk_file_path, 'wb') as chunk_file:
                chunk_file.write(f.read(chunk_size))
            chunk_number += 1

if __name__ == "__main__":
    split_file("similarity.pkl")
