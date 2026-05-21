import hashlib
import os
import pytest

SAMPLE_DIR = os.path.join(os.path.dirname(__file__), "../sample_data")

def get_hash(filepath, algorithm="sha256"):
    """파일의 해시값 계산"""
    h = hashlib.new(algorithm)
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def test_hash_consistency():
    """같은 파일을 두 번 해시했을 때 동일한 값이 나오는지 검증 (무결성 핵심)"""
    filepath = os.path.join(SAMPLE_DIR, "test_file.txt")
    assert get_hash(filepath) == get_hash(filepath)

def test_hash_changes_when_file_modified(tmp_path):
    """파일 내용이 바뀌면 해시값도 달라지는지 검증"""
    f = tmp_path / "test.txt"
    f.write_text("original content")
    original_hash = get_hash(str(f))

    f.write_text("modified content")
    modified_hash = get_hash(str(f))

    assert original_hash != modified_hash

def test_corrupted_file_has_different_hash():
    """손상된 파일과 정상 파일의 해시값이 다른지 검증"""
    normal = os.path.join(SAMPLE_DIR, "test_file.txt")
    corrupted = os.path.join(SAMPLE_DIR, "corrupted_file.raw")
    assert get_hash(normal) != get_hash(corrupted)