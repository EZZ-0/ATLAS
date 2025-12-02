"""
Config package for Atlas Financial Intelligence
"""

# Simple version - no imports that might fail
APP_NAME = "ATLAS FINANCIAL INTELLIGENCE"
APP_NAME_SHORT = "Atlas Engine"
APP_TAGLINE = "Professional-Grade Financial Analysis & Valuation Engine"
APP_VERSION = "2.0.0"

FEATURES = {
    'ai_chat': True,
    'live_dcf': True,
    'pdf_export': True,
    'investment_summary': True,
    'validation_engine': True,
    'quant_analysis': True,
    'forensic_accounting': True,
    'advanced_options': True,
}

def is_feature_enabled(feature_name: str) -> bool:
    return FEATURES.get(feature_name, False)

def get_app_title() -> str:
    return f"⚡ {APP_NAME}"

def get_app_header() -> str:
    return f"<div class='main-header'><h1>⚡ {APP_NAME}</h1><p>{APP_TAGLINE}</p></div>"

def get_footer() -> str:
    return f"<div class='footer'><p>{APP_NAME} v{APP_VERSION}</p></div>"

__all__ = [
    'APP_NAME', 'APP_NAME_SHORT', 'APP_TAGLINE', 'APP_VERSION',
    'FEATURES', 'is_feature_enabled',
    'get_app_title', 'get_app_header', 'get_footer'
]
