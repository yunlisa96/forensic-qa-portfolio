import os
import pytest

SAMPLE_DIR = os.path.join(os.path.dirname(__file__), "../sample_data")

def get_file_metadata(filepath):
    """파일 메타데이터 추출"""
    stat = os.stat(filepath)
    return {
        "size": stat.st_size,
        "extension": os.path.splitext(filepath)[1],
        "filename": os.path.basename(filepath),
    }

def test_metadata_extracted_correctly():
    """파일 메타데이터가 정확히 추출되는지 검증"""
    filepath = os.path.join(SAMPLE_DIR, "test_file.txt")
    metadata = get_file_metadata(filepath)
    assert metadata["extension"] == ".txt"
    assert metadata["filename"] == "test_file.txt"
    assert metadata["size"] > 0

def test_raw_file_metadata():
    """raw 파일 메타데이터 검증"""
    filepath = os.path.join(SAMPLE_DIR, "test_image.raw")
    metadata = get_file_metadata(filepath)
    assert metadata["extension"] == ".raw"
    assert metadata["size"] == 1048576  # 1MB

def test_metadata_size_matches_real_size():
    """메타데이터의 파일 크기가 실제 크기와 일치하는지 검증"""
    filepath = os.path.join(SAMPLE_DIR, "test_file.txt")
    metadata = get_file_metadata(filepath)
    real_size = os.path.getsize(filepath)
    assert metadata["size"] == real_size