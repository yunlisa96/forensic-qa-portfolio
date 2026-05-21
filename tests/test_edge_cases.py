import hashlib
import os
import pytest

SAMPLE_DIR = os.path.join(os.path.dirname(__file__), "../sample_data")

def get_hash(filepath, algorithm="sha256"):
    h = hashlib.new(algorithm)
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def test_empty_file_handling(tmp_path):
    """빈 파일도 해시값이 나오는지 검증"""
    f = tmp_path / "empty.txt"
    f.write_text("")
    result = get_hash(str(f))
    assert result is not None
    assert len(result) == 64  # SHA-256은 항상 64자리

def test_nonexistent_file_raises_error():
    """존재하지 않는 파일 접근 시 에러가 발생하는지 검증"""
    with pytest.raises(FileNotFoundError):
        get_hash("nonexistent_file.txt")

def test_corrupted_file_still_readable():
    """손상된 파일도 읽을 수 있는지 검증"""
    filepath = os.path.join(SAMPLE_DIR, "corrupted_file.raw")
    result = get_hash(filepath)
    assert result is not None

def test_large_file_hash_performance(tmp_path):
    """대용량 파일도 해시 계산이 완료되는지 검증"""
    f = tmp_path / "large.raw"
    f.write_bytes(b"0" * 1024 * 1024)  # 1MB
    result = get_hash(str(f))
    assert result is not None