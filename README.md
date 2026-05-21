# Forensic QA Automation Portfolio

## 프로젝트 개요
디지털 포렌식 툴의 핵심 기능인 **파일 무결성 검증**과 **메타데이터 파싱 정확도**를 자동화 테스트로 구현한 프로젝트입니다.

실제 포렌식 수사 환경에서는 증거 파일의 무결성이 법적 효력과 직결됩니다.
본 프로젝트는 GMDSOFT MD-RED와 같은 모바일 포렌식 툴이 수행하는
데이터 검증 프로세스를 QA 자동화 관점에서 구현했습니다.

## 기술 스택
- Python 3.9
- pytest / pytest-html
- The Sleuth Kit (TSK)
- GitHub Actions (CI/CD)

## 테스트 구성

### 1. 해시 무결성 검증 (`test_hash.py`)
포렌식 증거의 핵심인 파일 무결성을 SHA-256 해시로 자동 검증합니다.
- 동일 파일 반복 해시 일관성 검증
- 파일 변조 시 해시값 변경 검증
- 손상 파일과 정상 파일의 해시값 차이 검증

### 2. 메타데이터 파싱 정확도 (`test_parser.py`)
포렌식 툴이 파일에서 메타데이터를 정확히 추출하는지 검증합니다.
- 파일명, 확장자, 크기 정확도 검증
- RAW 이미지 파일 메타데이터 검증
- 실제 파일 크기와 메타데이터 일치 여부 검증

### 3. 엣지케이스 처리 (`test_edge_cases.py`)
실제 수사 현장의 예외 상황을 시뮬레이션합니다.
- 빈 파일 처리 검증
- 존재하지 않는 파일 접근 시 에러 처리 검증
- 손상된 파일 가독성 검증
- 대용량 파일 성능 검증

## 실행 방법
```bash
# 가상환경 활성화
source venv/bin/activate

# 테스트 실행
pytest tests/ -v

# HTML 리포트 생성
pytest tests/ -v --html=reports/report.html --self-contained-html
```

## CI/CD
main 브랜치에 push할 때마다 GitHub Actions에서 자동으로 테스트가 실행됩니다.
테스트 결과는 Actions 탭 Artifacts에서 HTML 리포트로 확인할 수 있습니다.
