from src.models import Finding
from src.service import Service

def test_statistics():
    result = Service.stats([Finding("ioc", "1.1.1.1", "test", "high")])
    assert result["total"] == 1
    assert result["by_category"]["ioc"] == 1
