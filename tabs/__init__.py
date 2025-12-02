"""
SECURITY UTILITIES MODULE
"""

import re
import os
from typing import Tuple, Optional, List
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')


class SecurityValidator:
    SQL_PATTERNS = [
        re.compile(r"(\bDROP\b|\bDELETE\b|\bINSERT\b|\bUPDATE\b|\bSELECT\b|\bUNION\b|\bEXEC\b)", re.IGNORECASE),
        re.compile(r"[;']"),
        re.compile(r"(-{2}|/\*|\*/|xp_)", re.IGNORECASE),
    ]
    
    XSS_PATTERNS = [
        re.compile(r"<script[^>]*>.*?</script>", re.IGNORECASE | re.DOTALL),
        re.compile(r"javascript:", re.IGNORECASE),
        re.compile(r"on\w+\s*=", re.IGNORECASE),
    ]
    
    PATH_TRAVERSAL_PATTERNS = [
        re.compile(r"\.\./"),
        re.compile(r"\.\.\\"),
    ]
    
    @staticmethod
    def detect_sql_injection(input_str: str) -> Tuple[bool, Optional[str]]:
        if not input_str or not isinstance(input_str, str):
            return True, None
        for pattern in SecurityValidator.SQL_PATTERNS:
            if pattern.search(input_str):
                return False, f"SQL injection pattern detected"
        return True, None
    
    @staticmethod
    def detect_xss(input_str: str) -> Tuple[bool, Optional[str]]:
        if not input_str or not isinstance(input_str, str):
            return True, None
        for pattern in SecurityValidator.XSS_PATTERNS:
            if pattern.search(input_str):
                return False, f"XSS pattern detected"
        return True, None
    
    @staticmethod
    def validate_input(input_str: str, input_type: str = "general") -> Tuple[bool, Optional[str]]:
        if not input_str:
            return True, None
        checks = [
            SecurityValidator.detect_sql_injection(input_str),
            SecurityValidator.detect_xss(input_str),
        ]
        for is_safe, threat in checks:
            if not is_safe:
                return False, threat
        return True, None
    
    @staticmethod
    def sanitize_string(input_str: str, allow_alphanumeric_only: bool = False) -> str:
        if not input_str or not isinstance(input_str, str):
            return ""
        sanitized = input_str.replace('\x00', '')
        sanitized = ''.join(char for char in sanitized if ord(char) >= 32 or char in '\t\n\r')
        if allow_alphanumeric_only:
            sanitized = re.sub(r'[^a-zA-Z0-9\s\-_.]', '', sanitized)
        return sanitized.strip()


def quick_validate(input_str: str) -> bool:
    is_safe, _ = SecurityValidator.validate_input(input_str)
    return is_safe

def sanitize(input_str: str) -> str:
    return SecurityValidator.sanitize_string(input_str)
